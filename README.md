# Simple Localize

A simple and efficient Python module to easily add localization (multilingual support) to your projects.

## Quick Start

```python
import localizer

localizer.init_localizer('your_translations.json')  # Use your own JSON file
print(localizer.get_text('your_text_key'))  # Auto-detects your language
```

## Features

- 🌍 **Auto-detects** your system language
- 📁 **JSON-based** translations (easy to edit)
- 🔄 **Switch languages** on the fly
- 🎯 **Text formatting** with variables
- ⚠️ **Missing key warnings** with helpful suggestions
- ⚡ **Zero dependencies** - uses only Python standard library

## Installation

1. Copy `localizer.py` to your project
2. Create your own JSON file with your translations (any name you want)
3. That's it! No pip install needed.

## Basic Examples

```python
# Get text in your system language
message = localizer.get_text('welcome_message')

# Get text in specific language
french_msg = localizer.get_text('welcome_message', 'FR')

# Change current language
localizer.set_language('ES')

# Use variables in text
greeting = localizer.get_text('greeting', name="Alice")
```

## API Reference

| Function | Description | Example |
|----------|-------------|---------|
| `init_localizer(file, lang)` | Initialize with JSON file | `init_localizer('my_translations.json')` |
| `get_text(key, lang, **kwargs)` | Get translated text | `get_text('hello', name="John")` |
| `set_language(lang)` | Change current language | `set_language('FR')` |
| `get_current_language()` | Get current language code | Returns `'EN'` |
| `get_available_languages()` | List all available languages | Returns `['EN', 'FR', 'ES']` |

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
import localizer

localizer.init_localizer('my_app_texts.json')  # Use any filename you want
print(localizer.get_text('app_title'))
print(localizer.get_text('welcome_user', username="John"))
```

## Interactive Tutorial

Want to see it in action? The included example shows all features:

```bash
python example_usage.py
```

**Note:** The `translations.json` file included with this module is only for the demo. Create your own JSON file with any name and your specific texts!

## Supported Languages

Add any languages you need! Just use standard language codes like: EN, FR, ES, DE, IT, etc.
