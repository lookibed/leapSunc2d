import imageio
import os
from PIL import Image
import numpy as np
import copy

def add_visemes_pauses(visemes_data):
  visemes_data_with_pauses = copy.deepcopy(visemes_data)

  visemes = visemes_data_with_pauses["visemes"]
  visemes_with_pauses = []

  for i in range(len(visemes)):
      visemes_with_pauses.append(visemes[i])
      if i < len(visemes) - 1: # Если это не последняя визема
          current_end = visemes[i]["end"]
          next_start = visemes[i+1]["start"]
          if next_start > current_end: #Если есть промежуток
              pause_duration = next_start - current_end
              visemes_with_pauses.append({
                  "viseme": "close",
                  "start": current_end,
                  "end": next_start
              })
  visemes_data_with_pauses["visemes"] = visemes_with_pauses
  return visemes_data_with_pauses

def load_viseme_images(visemes_dir, target_size=(100, 100), visemes_data={}):
  viseme_images = {}
  for viseme_data in visemes_data['visemes']:
    viseme_name = viseme_data['viseme']
    image_path = os.path.join(visemes_dir, f"{viseme_name}.png")
    print(image_path)
    try:
      image = Image.open(image_path)
      image = image.resize(target_size)
      image = image.convert('RGB')
      viseme_images[viseme_name] = image
    except FileNotFoundError:
        print(f"Предупреждение: Изображение для виземы '{viseme_name}' не найдено.")
  return viseme_images


def create_viseme_animation(visemes_data, viseme_images, output_file, fps=30):
    duration = visemes_data["visemes"][-1]["end"]  # Последняя точка окончания
    num_frames = int(duration * fps)
    frames = []

    for frame_number in range(num_frames):
        time = frame_number / fps  # Текущее время кадра
        current_viseme = None
        for viseme_info in visemes_data["visemes"]:
            if viseme_info["start"] <= time < viseme_info["end"]:
                current_viseme = viseme_info["viseme"]
                break
        
        if current_viseme and current_viseme in viseme_images:
          frame = np.array(viseme_images[current_viseme])
          frames.append(frame)

    if frames:
      imageio.mimwrite(output_file, frames, fps=fps, codec="libx264")
      print(f"Видео успешно создано: {output_file}")
    else:
      print("Ошибка: Не создано ни одного кадра. Возможно, отсутствуют необходимые изображения визем")

