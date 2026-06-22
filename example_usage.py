# Example usage of Simple Localize
# This script shows you how to use the localizer module step by step

import threading
import simple_localize as localizer

def pause():
    input("\nAppuie sur Entrée pour continuer...\n")

def main():
    print("🌍 SIMPLE LOCALIZE - STEP BY STEP GUIDE")
    print("=" * 50)

    # STEP 0: Create the JSON file
    print("\n📁 STEP 0: Create your translations JSON file")
    print('  {')
    print('    "welcome": {"en": "Welcome!", "fr": "Bienvenue!", "es": "¡Bienvenido!"},')
    print('    "greeting": {"en": "Hello {name}!", "fr": "Bonjour {name} !", "es": "¡Hola {name}!"}')
    print('  }')
    print("💡 Use any filename you want (e.g. 'my_texts.json', 'lang.json'…)")
    pause()

    # STEP 1: Import and initialize
    print("📋 STEP 1: Import and initialize the localizer")
    print(">>> import simple_localize")
    print(">>> simple_localize.init_localizer('translations.json')")
    localizer.init_localizer('translations.json')
    print("✅ Module initialized successfully!")
    pause()

    # STEP 2: Check what language was detected
    print("🔍 STEP 2: Check detected system language")
    print(">>> simple_localize.get_current_language()")
    current_lang = localizer.get_current_language()
    print(f"'{current_lang}'")
    print(">>> simple_localize.get_available_languages()")
    available_langs = localizer.get_available_languages()
    print(f"{available_langs}")
    pause()

    # STEP 3: Get text in current language
    print("📝 STEP 3: Get translated text (automatic language)")
    print(">>> simple_localize.get_text('welcome_message')")
    welcome = localizer.get_text('welcome_message')
    print(f"'{welcome}'")
    print("💡 The text is automatically shown in your system language!")
    pause()

    # STEP 4: Get text in specific language
    print("🌐 STEP 4: Get text in a specific language")
    print(">>> simple_localize.get_text('welcome_message', 'fr')")
    welcome_fr = localizer.get_text('welcome_message', 'fr')
    print(f"'{welcome_fr}'")
    pause()

    # STEP 5: Change the current language
    print("🔄 STEP 5: Change current language")
    print(">>> simple_localize.set_language('es')")
    localizer.set_language('es')
    print(">>> simple_localize.get_text('welcome_message')")
    welcome_es = localizer.get_text('welcome_message')
    print(f"'{welcome_es}'")
    pause()

    # STEP 6: Add translations at runtime
    print("➕ STEP 6: Add translations at runtime")
    print(">>> simple_localize.add_translations('user_greeting', {")
    print("...     'en': 'Hello {username}, you have {count} messages!',")
    print("...     'fr': 'Bonjour {username}, vous avez {count} messages !',")
    print("...     'es': '¡Hola {username}, tienes {count} mensajes!'")
    print("... })")
    localizer.add_translations('user_greeting', {
        'en': 'Hello {username}, you have {count} messages!',
        'fr': 'Bonjour {username}, vous avez {count} messages !',
        'es': '¡Hola {username}, tienes {count} mensajes!'
    })
    pause()

    # STEP 7: Text formatting with parameters
    print("🎯 STEP 7: Text formatting with parameters")
    print(">>> simple_localize.get_text('user_greeting', username='John', count=5)")
    personalized = localizer.get_text('user_greeting', username='John', count=5)
    print(f"'{personalized}'")
    print("💡 Use {parameter} in your translations for dynamic content!")
    pause()

    # STEP 8: What happens with missing keys
    print("⚠️  STEP 8: What happens with non-existent keys")
    print(">>> simple_localize.get_text('this_key_does_not_exist')")
    missing = localizer.get_text('this_key_does_not_exist')
    print(f"'{missing}'")
    print("💡 Non-existent keys return the key name and show a warning!")
    pause()

    # STEP 9: Thread safety — each thread has its own language
    print("🔒 STEP 9: Thread safety")
    print("💡 set_language() applies per thread — each thread has its own language.")
    print()
    print(">>> # In each thread, set_language() persists for all get_text() calls:")
    print(">>> simple_localize.set_language('fr')")
    print(">>> simple_localize.get_text('welcome_message')  # → French")
    print(">>> simple_localize.get_text('goodbye_message')  # → French too")
    print()
    print(f"Main thread language before: '{localizer.get_current_language()}'")
    results = {}

    def request(lang):
        localizer.set_language(lang)
        results[lang] = [
            localizer.get_text('welcome_message'),
            localizer.get_text('goodbye_message'),
        ]

    threads = [
        threading.Thread(target=request, args=('en',)),
        threading.Thread(target=request, args=('fr',)),
        threading.Thread(target=request, args=('es',)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    for lang, texts in results.items():
        print(f"  [{lang}] {texts[0]} / {texts[1]}")
    print(f"Main thread language after:  '{localizer.get_current_language()}'")
    print("💡 set_language() persists for all calls in the thread, and doesn't affect other threads!")

    print("\n✅ That's it! You now know how to use the localizer!")

if __name__ == "__main__":
    main()
