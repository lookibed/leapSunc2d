from stt import rec_wav, get_wav_duration
from leapSync_visem import text_to_phonemes_visemes
from leapSync2_show import load_viseme_images, create_viseme_animation, add_visemes_pauses
from mix import mix_audio_video
import json

# Rec
print("Recognition..")
model_path = r"G:\PythonProjects\leapSunc2d\vosk-model-small-ru-0.22"
input_file = r"G:\PythonProjects\leapSunc2d\input.wav"
text_data = rec_wav(model_path, input_file)
# print(json.dumps(text_data, indent=2, ensure_ascii=False))

print("Visemes..")
visemes_data = text_to_phonemes_visemes(text_data)
# print(json.dumps(visemes_data, indent=2, ensure_ascii=False))

print("Connect visemes and wav..")
duration = get_wav_duration(input_file)
end_vis = visemes_data["visemes"][-1]["end"]
close_end = {
    "viseme": "close",
    "start": end_vis,
    "end": duration
}
# print(json.dumps(close_end, indent=2, ensure_ascii=False))
visemes_data["visemes"].append(close_end)

print("Visemes data with pauses..")
visemes_data_with_pauses = add_visemes_pauses(visemes_data)
print(json.dumps(visemes_data_with_pauses['visemes'], indent=2, ensure_ascii=False))

print("Load viseme images..")
visemes_dir = r"G:\PythonProjects\leapSunc2d\visemes"
output_video = r"G:\PythonProjects\leapSunc2d\visemes_animation.mp4"
target_size = (124, 132)
viseme_images = load_viseme_images(visemes_dir, target_size, visemes_data_with_pauses)
print("Create viseme animation..")
create_viseme_animation(visemes_data_with_pauses, viseme_images, output_video, 24)

result_video = r"G:\PythonProjects\leapSunc2d\output.mp4"
print("Join mp4 and wav for one Video..")
mix_audio_video(output_video, input_file, result_video)

print("All Comlite!")