import json

def text_to_phonemes_visemes(text_data):
    """
    Преобразует текст с таймингами в фонемы и виземы для русского языка.

    Args:
        text_data (dict): Словарь с текстом и таймингами слов.

    Returns:
        dict: Словарь с фонемами и виземами.
    """
    
    # Упрощенная модель, т.к. точное фонетическое разбиение это сложная задача.
    # Идеально, тут должен быть полноценный G2P преобразователь (graph to phoneme).
    # Мы будем использовать упрощенные правила.
    # Словарь соответствия фонем и визем.
    phoneme_to_viseme = {
      'а': 'а_я',
      'о': 'о_ё',
      'я': 'а_я',
      'э': 'э_е',
      'е': 'э_е',
      'у': 'у_ю',
      'ю': 'у_ю',
      'и': 'и',
      'ы': 'ы',
      'б': 'б_п',
      'п': 'б_п',
      'м': 'м',
      'в': 'ф_в',
      'ф': 'ф_в',
      'г': 'г_к',
      'к': 'г_к',
      'х': 'х',
      'д': 'д_т_н',
      'т': 'д_т_н',
      'н': 'д_т_н',
      'ж': 'ж_ш',
      'ш': 'ж_ш',
      'ч': 'ч_щ',
      'щ': 'ч_щ',
      'з': 'з_с_ц',
      'с': 'з_с_ц',
      'ц': 'з_с_ц',
      'л': 'л',
      'р': 'р',
      'й': 'й'
    }

    phonemes = []
    visemes = []
    
    i_g = -1
    for word_data in text_data['timing']:
        i_g += 1
        word = word_data['word'].lower()
        start_time = word_data['start']
        end_time = word_data['end']
        word_duration = end_time - start_time

        # Упрощенное разбиение на фонемы (на основе символов).
        # В реальности тут должна быть более сложная логика.
        
        num_chars = len(word)
        
        if num_chars > 0: #check empty words
            
            duration_per_char = word_duration / num_chars
        
            for i, char in enumerate(word):
                phoneme = char
                char_start = start_time + i * duration_per_char
                char_end = char_start + duration_per_char
                
                if char in phoneme_to_viseme:
                    viseme = phoneme_to_viseme[char]
                else:
                   viseme = 'close' # default case
                if i_g == 0:
                    visemes.append({"viseme": "close", "start": 0.0, "end": char_start})
                phonemes.append({"phoneme": phoneme, "start": char_start, "end": char_end})
                visemes.append({"viseme": viseme, "start": char_start, "end": char_end})

    return {"phonemes": phonemes, "visemes": visemes}

# # Пример использования
# text_data = {
#   "text": "Привет, как дела?",
#   "timing": [
#     {"word": "Привет", "start": 0.0, "end": 0.8},
#     {"word": "как", "start": 0.9, "end": 1.2},
#     {"word": "дела", "start": 1.3, "end": 1.9}
#   ]
# }

# result = text_to_phonemes_visemes(text_data)
# print(json.dumps(result, indent=2))