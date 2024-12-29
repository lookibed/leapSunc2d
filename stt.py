import os
import sys
import wave
import json
import time
from vosk import Model, KaldiRecognizer

def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        # Получаем количество фреймов
        n_frames = wav_file.getnframes()
        # Получаем частоту дискретизации
        frame_rate = wav_file.getframerate()
        # Рассчитываем длительность в секундах
        duration = n_frames / float(frame_rate)
    return duration

def rec_wav(model_path, input_file):
    model = Model(model_path)
    # Open the audio file (ensure it's in WAV format with appropriate settings)
    wf = wave.open(input_file, "rb")
    # Initialize recognizer with the specified sample rate
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    n_frames = wf.getnframes()
    # Получаем частоту дискретизации
    frame_rate = wf.getframerate()
    # Рассчитываем длительность в секундах
    duration = n_frames / float(frame_rate)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            results.append(res)
        else:
            # print(rec.PartialResult())
            pass

    # Get final result
    final_res = json.loads(rec.FinalResult())
    results.append(final_res)

    # print(json.dumps(results, indent=2, ensure_ascii=False))
    # Print results with start and end times
    text_data = {
        "text": "",
        "timing": []
    }
    timing = []
    for result in results:
        if 'result' in result:
            for word_info in result['result']:
                timing.append(word_info)
                # print(f"Word: {word_info['word']}, Start: {word_info['start']}, End: {word_info['end']}")
            text_data["timing"] = timing
        elif 'text' in result:
            text_data["text"] = result['text']
    # print(json.dumps(text_data, indent=2, ensure_ascii=False))
    return text_data