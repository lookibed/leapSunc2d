from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip


# # Пути к файлам
# video_file = 'visemes_animation.mp4'  # Входной видеофайл
# audio_file = 'you_gay.wav'  # Входной аудиофайл
# output_file = 'output.mp4'  # Итоговый файл
def mix_audio_video(video_file, audio_file, output_file):
    # Загрузка видео и аудио
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)

    # Добавление аудио к видео
    video_with_audio = video.with_audio(audio)

    # Сохранение итогового файла
    video_with_audio.write_videofile(output_file, codec="libx264", audio_codec="aac")

    print(f"Файл успешно создан: {output_file}")
