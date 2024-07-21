#   Brainrot limnal spaces generator
#             by kolino
#
#   P.S this script is for my friend kadziug adhd ;)

#Importujemy biblioteki!
import datetime
import os
import time
import praw
import requests
import random
from moviepy.editor import *
from PIL import Image
import shutil


#Funkcja rozpoczyjaca inne
def START():
    log("Tworze Nowy brainrot!")
    reddit()
    resize_and_crop_image('downloaded_images', 'cropped_images', 1920, 1080)
    cooking()

#Logi | log.txt
def log(info):
    now = datetime.datetime.now()
    log_message = f"[LOG] [{now}] >> {info}"
    print(now)
    print(log_message)

    # Zapisz log_message do pliku log.txt
    with open("log.txt", "a") as log_file:
        log_file.write(log_message + "\n")

#funkcja szukajca brainrot
def reddit():
    # Ustawienia Reddit API
    reddit = praw.Reddit(
        client_id='client_id',
        client_secret='client_secret',
        user_agent='user_agent'
    )

    # Funkcja do pobierania losowych zdjęć z określonych subredditow
    def download_random_images(subreddits, num_images, download_folder):
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        all_images = []

        for subreddit in subreddits:
            subreddit_instance = reddit.subreddit(subreddit)
            for submission in subreddit_instance.hot(limit=100):  # Pobieramy top 100 postów z danego subreddit
                if submission.url.endswith(('.jpg', '.jpeg', '.png')):
                    all_images.append(submission.url)

        if len(all_images) < num_images:
            log(f"Found only {len(all_images)} images.")
            num_images = len(all_images)

        random.shuffle(all_images)  # Losowe przemieszanie listy obrazów

        downloaded_count = 0
        idx = 1

        while downloaded_count < num_images and all_images:
            image_url = all_images.pop()
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image_path = os.path.join(download_folder, f"{idx}.png")
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                log(f"Downloaded {image_url} as {image_path}")
                downloaded_count += 1
                idx += 1
            except Exception as e:
                log(f"Failed to download {image_url}: {e}")

    subreddits = ['LiminalSpace', 'Homes', 'EarthPorn']  # subreddity
    num_images = 5  # Liczba obrazów do pobrania
    download_folder = 'downloaded_images'  # Folder docelowy

    download_random_images(subreddits, num_images, download_folder)
    log("pobieranie zakonczone")

#funkcja która zmienia wielkosć zdjec z reddita
def resize_and_crop_image(input_folder, output_folder, target_width, target_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:

                scale = target_height / img.height
                new_width = int(img.width * scale)
                new_height = target_height


                resized_img = img.resize((new_width, new_height), Image.LANCZOS)


                left = (new_width - target_width) / 2
                right = left + target_width
                top = 0
                bottom = target_height

                # Przytnij obraz
                cropped_img = resized_img.crop((left, top, right, bottom))

                # Zapisz przycięty obraz w folderze docelowym
                output_path = os.path.join(output_folder, filename)
                cropped_img.save(output_path)
                log(f'Zmieniono rozmiar i przycieto: {filename}')

#Tutaj gotujemy czyli montaż
def cooking():
    log("Rozpoczynanie tworzenia filmu...")

    # Ścieżki do zasobów
    resources_folder = "resources"
    cropped_images_folder = "cropped_images"
    startscreen_path = os.path.join(resources_folder, "startscreen.png")
    audio_path = os.path.join(resources_folder, "letgo.mp3")
    output_folder = "cooked"

    # Parametry filmu
    total_duration = 15  # całkowity czas trwania filmu w sekundach
    startscreen_duration = 3  # czas trwania ekranu startowego
    slide_duration = 2.4  # czas trwania każdego slajdu

    # Tworzenie startscreen
    startscreen_clip = ImageClip(startscreen_path, duration=startscreen_duration)

    # Tworzenie klipów ze slajdów
    image_files = sorted([os.path.join(cropped_images_folder, img) for img in os.listdir(cropped_images_folder)])
    slides_clips = [ImageClip(img).set_duration(slide_duration) for img in image_files]

    # Połączenie klipów w jeden film
    final_clips = [startscreen_clip] + slides_clips
    video = concatenate_videoclips(final_clips)

    # Dodanie letgo.mp3
    audio = AudioFileClip(audio_path).subclip(0, total_duration)
    video = video.set_audio(audio)

    # Nazwa pliku wyjściowego
    output_filename = "brainrot-data.mp4"
    output_path = os.path.join(output_folder, output_filename)

    # Tworzenie folderu docelowego, jeśli nie istnieje
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Zapisanie finalnego filmu
    video.write_videofile(output_path, codec="libx264", fps=24)

    log(f"Film zostal pomyslnie stworzony i zapisany jako '{output_filename}' w folderze '{output_folder}'")

#jeżeli chcesz aby workspace sie czyscił dodaj clean() do funkcji START()
def clean():
    def clear_folder(folder_path):
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    pass

    folders_to_clear = ["cooked", "cropped_images", "downloaded_images"]
    for folder in folders_to_clear:
        clear_folder(folder)
    log("Zawartosc wyczyszona lsni i blyszczy")

#startujemy
START()
