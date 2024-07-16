# Brainrot Liminal Spaces Generator
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

A script to generate mesmerizing videos using images from Reddit's top posts in specified subreddits.

## About
This project automates the creation of a video montage ("brainrot") using images sourced from Reddit. It downloads, resizes, crops, and compiles these images into a video with accompanying audio.

## Purpose
Primarily created for the adhd of my friend, designed to provide a relaxing visual experience.

## Features
- **Reddit Image Download**: Fetches top images from specified subreddits like `LiminalSpace`, `Homes`, `EarthPorn`.
- **Image Processing**: Resizes and crops images to a specified aspect ratio (1920x1080).
- **Video Compilation**: Combines images into a video with customizable parameters like slide duration and total video length.
- **Audio Integration**: Includes background audio (`letgo.mp3`) to accompany the visual montage.
- **Cleaning Functionality**: Optional function to clean up workspace directories after execution.

##  Video


https://github.com/user-attachments/assets/629f4570-bff9-48e9-a254-618597c56da2


## Requirements
- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`):
  - praw
  - requests
  - moviepy
  - Pillow (PIL)

## Usage
1. Ensure Python and required packages are installed.
2. Configure Reddit API credentials (`client_id`, `client_secret`, `user_agent`) in the script.
3. Customize subreddit preferences (`subreddits`) and number of images (`num_images`) to download.
4. Run the script `python main.py`.

## Notes
- The script generates a log (`log.txt`) detailing its activities.
- Adjust parameters (`total_duration`, `slide_duration`) to customize the output video.

## Clean Workspace
To automatically clean generated files (`cooked`, `cropped_images`, `downloaded_images`), add `clean()` to the `START()` function.

## Example Output
A sample output video (`brainrot-data.mp4`) is created in the `cooked` directory.

## Credits
- Developed by **kolino**.
- Subreddits r/Liminalspace r/Homes r/EarthPorn
