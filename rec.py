import pyaudio
import wave
import threading
import tkinter as tk

# Параметры записи
FORMAT = pyaudio.paInt16  # Формат 16 бит
CHANNELS = 1               # Моно
RATE = 16000                # Частота дискретизации 16 кГц
CHUNK = 1024                # Размер блока данных
WAVE_OUTPUT_FILENAME = "input.wav"  # Имя выходного файла

# Флаг для управления записью
is_recording = False

def record_audio():
    global is_recording
    is_recording = True
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    frames = []

    print("Запись началась...")
    while is_recording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Запись завершена.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Сохранение записанных данных в файл WAV
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def start_recording():
    threading.Thread(target=record_audio).start()

def stop_recording():
    global is_recording
    is_recording = False

# Создание графического интерфейса
root = tk.Tk()
root.title("Запись аудио")

start_button = tk.Button(root, text="Начать запись", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Остановить запись", command=stop_recording)
stop_button.pack(pady=10)

root.mainloop()
