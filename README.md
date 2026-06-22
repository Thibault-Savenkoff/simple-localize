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
french_msg = simple_localize.get_text('welcome_message', 'FR')

# Change current language
simple_localize.set_language('ES')

# Use variables in text
greeting = simple_localize.get_text('greeting', name="Alice")
```

## API Reference

| Function | Description | Example |
|----------|-------------|---------|
| `init_localizer(file, lang)` | Initialize with JSON file | `init_localizer('my_translations.json')` |
| `get_text(key, lang, **kwargs)` | Get translated text | `get_text('hello', name="John")` |
| `set_language(lang)` | Change language for the current thread | `set_language('FR')` |
| `get_current_language()` | Get current thread's language code | Returns `'EN'` |
| `get_available_languages()` | List all available languages | Returns `['EN', 'FR', 'ES']` |
| `add_translations(key, dict)` | Add/update a key at runtime (thread-safe) | `add_translations('hello', {'EN': 'Hi'})` |

## Create Your Translation File

Create a JSON file with any name you like (`my_texts.json`, `lang.json`, `app_translations.json`, etc.):

```json
{
  "app_title": {
    "EN": "My Application",
    "FR": "Mon Application",
    "ES": "Mi Aplicación"
  },
  "login_button": {
    "EN": "Login",
    "FR": "Connexion",
    "ES": "Iniciar sesión"
  },
  "welcome_user": {
    "EN": "Welcome {username}!",
    "FR": "Bienvenue {username} !",
    "ES": "¡Bienvenido {username}!"
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
simple_localize.set_language('FR')
simple_localize.get_text('welcome')  # → French
simple_localize.get_text('goodbye')  # → French too

# Thread B (e.g. a Spanish user's request), simultaneously
simple_localize.set_language('ES')
simple_localize.get_text('welcome')  # → Spanish, unaffected by Thread A
```

`add_translations()` is also thread-safe for concurrent writes.

## Supported Languages

Add any languages you need! Just use standard language codes like: EN, FR, ES, DE, IT, etc.
