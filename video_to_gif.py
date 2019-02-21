import os
import glob
import random

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

time = input('분 초: ')
try:
    time = time.split(' ')
    min, sec = int(time[0]), int(time[1])
    start_play_time = (min*60) + (sec)
    end_play_time = start_play_time + 1
except Exception as e:
    print(str(e))
    start_play_time = 0
    end_play_time = round(clip.duration - 2)

for i in range(5):
    start_t = random.randrange(start_play_time, end_play_time)
    end_t = start_t + 2

    file_path = f'{GIFS_DIR}{filename}{start_t}.gif'

    if os.path.exists(file_path):
        continue
    snapshot = clip.subclip(start_t, end_t).resize(0.3)
    snapshot.write_gif(file_path)
