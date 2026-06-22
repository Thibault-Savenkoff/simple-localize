# © 2026 Thibault Savenkoff

import locale
import json
import os
import threading

_translations = {}
_default_lang = 'EN'
_translations_file = None
_lock = threading.Lock()
_thread_local = threading.local()  # per-thread current language

def _detect_system_language():
    try:
        for env_var in ['LANG', 'LC_ALL', 'LC_MESSAGES', 'LANGUAGE']:
            lang_value = os.environ.get(env_var, '')
            if lang_value and '_' in lang_value:
                return lang_value.split('_')[0].upper()
            elif len(lang_value) >= 2:
                return lang_value[:2].upper()

        # ponytail: no setlocale() — it has process-wide side effects
        system_locale = locale.getlocale()[0]
        if system_locale:
            return system_locale[:2].upper()
    except Exception:
        pass
    return _default_lang

def _load_translations(translations_file):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        translations_path = os.path.join(script_dir, translations_file)
        with open(translations_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Translations file '{translations_file}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{translations_file}'.")
        return {}

def _get_current_lang():
    return getattr(_thread_local, 'lang', _default_lang)

def init_localizer(translations_file=None, default_lang='EN'):
    if not translations_file:
        raise ValueError("You must specify a translations file. Example: init_localizer('my_translations.json')")

    global _translations, _default_lang, _translations_file
    _translations_file = translations_file
    _default_lang = default_lang.upper()
    _thread_local.lang = _detect_system_language()
    _translations = _load_translations(translations_file)
    return True

def get_text(key, lang=None, **kwargs):
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")

    lang = (lang or _get_current_lang()).upper()

    if key not in _translations:
        print(f"Warning: Translation key '{key}' not found. \nAvailable keys: {list(_translations.keys())}")
        return key

    translations_for_key = _translations[key]
    text = (
        translations_for_key.get(lang)
        or translations_for_key.get(_default_lang)
        or next(iter(translations_for_key.values()), None)
    )
    if text is None:
        return key

    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text

    return text

def set_language(lang):
    """Change language for the current thread only."""
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    _thread_local.lang = lang.upper()

def get_current_language():
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    return _get_current_lang()

def add_translations(key, translations_dict):
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    with _lock:
        _translations[key] = translations_dict

def get_available_languages():
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    all_languages = set()
    for translations_for_key in _translations.values():
        all_languages.update(translations_for_key.keys())
    return sorted(all_languages)
