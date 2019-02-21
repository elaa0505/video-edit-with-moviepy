import os
import sys
import glob
import random

from moviepy.editor import VideoFileClip
from functions import create_file_name, get_all_dir_files

# input_dir = input('경로입력: ')
#
# input_dir = f'../{input_dir}'
# if not input_dir.endswith('/'):
#     input_dir = f'{input_dir}/'
# VIDEO_DIR = input_dir

VIDEO_DIR = '../video/movie/'
GIFS_DIR = '../video/gif/'


if not os.path.exists(VIDEO_DIR):
    print('경로없음')
    print(VIDEO_DIR)
    sys.exit()

if not os.path.exists(GIFS_DIR):
    os.makedirs(GIFS_DIR)

video_list = get_all_dir_files(VIDEO_DIR)

print(f'total count: {len(video_list)}')
for video in video_list:
    print(video)
for i, video in enumerate(video_list):
    try:
        filename = create_file_name()
        clip = VideoFileClip(video)

        start_play_time = 0
        end_play_time = round(clip.duration - 2)

        start_t = random.randrange(start_play_time, end_play_time)
        end_t = start_t + 2

        file_path = f'{GIFS_DIR}{filename}.gif'

        snapshot = clip.subclip(start_t, end_t).resize(0.3)
        snapshot.write_gif(file_path)

        clip.reader.close()
        clip.audio.reader.close_proc()

        print(i)
    except Exception as e:
        print(str(e))
        continue
