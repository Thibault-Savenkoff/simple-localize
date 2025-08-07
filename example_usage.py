# Example usage of Simple Localize
# This script shows you how to use the localizer module step by step

import localizer

def main():
    print("🌍 SIMPLE LOCALIZE - STEP BY STEP GUIDE")
    print("=" * 50)
    print()
    
    # STEP 1: Initialize the module
    print("📋 STEP 1: Initialize the localizer")
    print("Code: localizer.init_localizer('translations.json')")
    loc = localizer.init_localizer('translations.json')
    print("✅ Module initialized successfully!")
    print()
    
    # STEP 2: Check what language was detected
    print("🔍 STEP 2: Check detected system language")
    current_lang = localizer.get_current_language()
    available_langs = localizer.get_available_languages()
    print(f"Code: localizer.get_current_language()")
    print(f"Result: Your system language is '{current_lang}'")
    print(f"Available languages: {available_langs}")
    print()
    
    # STEP 3: Get text in current language
    print("📝 STEP 3: Get translated text (automatic language)")
    print("Code: localizer.get_text('welcome_message')")
    welcome = localizer.get_text('welcome_message')
    print(f"Result: '{welcome}'")
    print("💡 The text is automatically shown in your system language!")
    print()
    
    # STEP 4: Get text in specific language
    print("🌐 STEP 4: Get text in specific language")
    print("Code: localizer.get_text('welcome_message', 'FR')")
    welcome_fr = localizer.get_text('welcome_message', 'FR')
    print(f"Result: '{welcome_fr}'")
    print("💡 You can specify any language code!")
    print()
    
    # STEP 5: Change the current language
    print("🔄 STEP 5: Change current language")
    print("Code: localizer.set_language('ES')")
    localizer.set_language('ES')
    new_lang = localizer.get_current_language()
    welcome_new = localizer.get_text('welcome_message')
    print(f"New language: {new_lang}")
    print(f"Same message now: '{welcome_new}'")
    print("💡 After changing language, all texts use the new language!")
    print()
    
    # STEP 6: Using text formatting with parameters
    print("🎯 STEP 6: Text formatting with parameters")
    # For demo purposes, we'll add a translation directly to the global dict
    localizer._translations['user_greeting'] = {
        'EN': 'Hello {username}, you have {count} messages!',
        'FR': 'Bonjour {username}, vous avez {count} messages !',
        'ES': '¡Hola {username}, tienes {count} mensajes!'
    }
    print("Code: localizer.get_text('user_greeting', username='John', count=5)")
    personalized = localizer.get_text('user_greeting', username='John', count=5)
    print(f"Result: '{personalized}'")
    print("💡 Use {parameter} in your translations for dynamic content!")
    print()
    
    # STEP 7: What happens with missing keys
    print("⚠️  STEP 7: What happens with non-existent keys")
    print("Code: localizer.get_text('this_key_does_not_exist')")
    missing = localizer.get_text('this_key_does_not_exist')
    print(f"Result: '{missing}'")
    print("💡 Non-existent keys return the key name and show a warning!")
    print()
    
    # SUMMARY
    print("🎓 SUMMARY - How to use in your project:")
    print("-" * 50)
    print("1. Copy localizer.py to your project")
    print("2. Create your own JSON file with translations")
    print("3. Import: import localizer")
    print("4. Initialize: localizer.init_localizer('your_file.json')")
    print("5. Use: localizer.get_text('your_key')")
    print("6. Change language: localizer.set_language('FR')")
    print("7. Add parameters: localizer.get_text('key', param='value')")
    print()
    print("🔧 To create your translations file:")
    print("Create a JSON file (any name) with your keys like:")
    print('{"your_key": {"EN": "English text", "FR": "Texte français"}}')
    print()
    print("📝 Note: The 'translations.json' in this demo is just an example!")
    print("Create your own file with your specific texts and any name you want.")
    print()
    print("✅ That's it! You now know how to use the localizer!")

if __name__ == "__main__":
    main()