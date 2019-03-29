import os
import glob

from moviepy.editor import VideoFileClip
from functions import create_file_name

VIDEO_DIR = '../video/movie/'
GIFS_DIR = '../video/gif/'


if not os.path.exists(VIDEO_DIR):
    os.makedirs(VIDEO_DIR)

if not os.path.exists(GIFS_DIR):
    os.makedirs(GIFS_DIR)

video_list = glob.glob(VIDEO_DIR + '*.*')
video = video_list[0]

filename = os.path.splitext(os.path.basename(video))[0]
clip = VideoFileClip(video)

file_path = f'{GIFS_DIR}{filename}.gif'
clip.write_gif(file_path)
