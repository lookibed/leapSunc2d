import phonetics

def russian_to_phonetic(word):
    # Используем библиотеку phonetics для фонемной транскрипции
    phonetic = phonetics.metaphone(word)
    print(phonetic)
    # Ручная корректировка для русского языка, если нужно
    # (например, чтобы добавить ударения)
    # Пример реализации: заменить "v" на "в", "k" на "к", и т. д.
    phonetic = phonetic.replace('v', 'в').replace('k', 'к')  # простая подстановка
    return phonetic

# Пример
word = "Автор"
print(f"Транскрипция слова: {russian_to_phonetic(word)}")
