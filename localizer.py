# © 2025 Thibault Savenkoff

import locale
import json
import os

# Global variables
_translations = {}
_current_lang = 'EN'
_default_lang = 'EN'
_translations_file = None

def _detect_system_language():
    """Detect system language in a cross-platform way"""
    try:
        # Method 1: Environment variables
        for env_var in ['LANG', 'LC_ALL', 'LC_MESSAGES', 'LANGUAGE']:
            if env_var in os.environ:
                lang_value = os.environ[env_var]
                if lang_value and '_' in lang_value:
                    return lang_value.split('_')[0].upper()
                elif lang_value and len(lang_value) >= 2:
                    return lang_value[:2].upper()
        
        # Method 2: locale module
        locale.setlocale(locale.LC_ALL, '')
        system_locale = locale.getlocale()[0]
        if system_locale:
            return system_locale[:2].upper()
        else:
            return _default_lang
    except:
        return _default_lang

def _load_translations(translations_file):
    """Load translations from JSON file"""
    try:
        # Look for file in the same directory as this script
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

def init_localizer(translations_file=None, default_lang='EN'):
    """Initialize the localization module"""
    if translations_file is None:
        raise ValueError("You must specify a translations file. Example: init_localizer('my_translations.json')")
    
    if not translations_file:
        raise ValueError("You must specify a translations file. Example: init_localizer('my_translations.json')")
    
    global _translations, _current_lang, _default_lang, _translations_file
    _translations_file = translations_file
    _default_lang = default_lang.upper()
    _current_lang = _detect_system_language()
    _translations = _load_translations(translations_file)
    return True

def get_text(key, lang=None, **kwargs):
    """Get translated text with formatting support"""
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    
    if lang is None:
        lang = _current_lang
    
    lang = lang.upper()
    
    if key in _translations:
        translations_for_key = _translations[key]
        
        # Try requested language
        if lang in translations_for_key:
            text = translations_for_key[lang]
        # Fallback to default language
        elif _default_lang in translations_for_key:
            text = translations_for_key[_default_lang]
        # Last chance: take first available translation
        elif translations_for_key:
            text = list(translations_for_key.values())[0]
        else:
            return key
        
        # Apply formatting if parameters are provided
        if kwargs:
            try:
                return text.format(**kwargs)
            except (KeyError, ValueError):
                return text
        
        return text
    
    # Key not found - show warning
    print(f"Warning: Translation key '{key}' not found. \nAvailable keys: {list(_translations.keys())}")
    return key

def set_language(lang):
    """Change current language"""
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    
    global _current_lang
    _current_lang = lang.upper()

def get_current_language():
    """Return current language"""
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    
    return _current_lang

def get_available_languages():
    """Return list of available languages"""
    if not _translations_file:
        raise ValueError("Localizer not initialized. Call init_localizer('your_file.json') first.")
    
    if not _translations:
        return []
    
    # Collect all available languages
    all_languages = set()
    for translations_for_key in _translations.values():
        all_languages.update(translations_for_key.keys())
    
    return sorted(list(all_languages))