# Simple Localize

A simple and efficient Python module to easily add localization (multilingual support) to your projects.

## Installation

```bash
pip install simple-localize
```

## Quick Start

```python
import simple_localize

simple_localize.init_localizer('your_translations.json')
print(simple_localize.get_text('your_text_key'))  # Auto-detects your language
```

## Features

- 🌍 **Auto-detects** your system language
- 📁 **JSON-based** translations (easy to edit)
- 🔄 **Switch languages** on the fly (per-thread safe)
- 🎯 **Text formatting** with variables
- ⚠️ **Missing key warnings** with helpful suggestions
- ⚡ **Zero dependencies** - uses only Python standard library
- 🔒 **Thread-safe** - safe to use in multi-threaded apps (Flask, FastAPI…)

## Basic Examples

```python
# Get text in your system language
message = simple_localize.get_text('welcome_message')

# Get text in specific language
french_msg = simple_localize.get_text('welcome_message', 'fr')

# Change current language
simple_localize.set_language('es')

# Use variables in text
greeting = simple_localize.get_text('greeting', name="Alice")
```

## API Reference

| Function | Description | Example |
|----------|-------------|---------|
| `init_localizer(file, lang)` | Initialize with JSON file | `init_localizer('my_translations.json')` |
| `get_text(key, lang, **kwargs)` | Get translated text | `get_text('hello', name="John")` |
| `set_language(lang)` | Change language for the current thread | `set_language('fr')` |
| `get_current_language()` | Get current thread's language code | Returns `'en'` |
| `get_available_languages()` | List all available languages | Returns `['en', 'fr', 'es']` |
| `add_translations(key, dict)` | Add/update a key at runtime (thread-safe) | `add_translations('hello', {'en': 'Hi'})` |

## Create Your Translation File

Create a JSON file with any name you like (`my_texts.json`, `lang.json`, `app_translations.json`, etc.):

```json
{
  "app_title": {
    "en": "My Application",
    "fr": "Mon Application",
    "es": "Mi Aplicación"
  },
  "login_button": {
    "en": "Login",
    "fr": "Connexion",
    "es": "Iniciar sesión"
  },
  "welcome_user": {
    "en": "Welcome {username}!",
    "fr": "Bienvenue {username} !",
    "es": "¡Bienvenido {username}!"
  }
}
```

Then use it in your code:

```python
import simple_localize

simple_localize.init_localizer('my_app_texts.json')
print(simple_localize.get_text('app_title'))
print(simple_localize.get_text('welcome_user', username="John"))
```

## Thread Safety

`set_language()` applies **per thread** — each thread can have its own active language without affecting others. This makes it safe to use in web servers where each request runs in its own thread:

```python
# Thread A (e.g. a French user's request)
simple_localize.set_language('fr')
simple_localize.get_text('welcome')  # → French
simple_localize.get_text('goodbye')  # → French too

# Thread B (e.g. a Spanish user's request), simultaneously
simple_localize.set_language('es')
simple_localize.get_text('welcome')  # → Spanish, unaffected by Thread A
```

`add_translations()` is also thread-safe for concurrent writes.

## Supported Languages

Add any languages you need! Use standard ISO 639-1 codes (`en`, `fr`, `pt`…) or regional variants (`pt_br`, `pt_pt`, `en_us`…).

The fallback chain for a `pt_br` user:
1. `pt_br` — exact match
2. `pt` — language fallback
3. default language (usually `en`)

```json
{
  "hello": {
    "pt_br": "Olá (Brasil)",
    "pt_pt": "Olá (Portugal)",
    "pt": "Olá",
    "en": "Hello"
  }
}
```
