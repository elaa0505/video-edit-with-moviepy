import os
import sys
import glob

from moviepy.editor import VideoFileClip

VIDEO_DIR = '../video/movie/'
SOUND_DIR = '../video/sound/'


def __get_time(value):
    try:
        time = value.split(' ')
        min, sec = int(time[0]), int(time[1])
        return (min*60) + sec
    except:
        print('시간오류')
        sys.exit()

filename = input('생성 파일이름: ')
if not filename:
    print('미입력')
    sys.exit()

start_t = input('시작 분 초: ')
end_t = input('끝 분 초: ')

start_t = __get_time(start_t)
end_t = __get_time(end_t)

if start_t >= end_t:
    print('시간오류')
    sys.exit()

if not os.path.exists(VIDEO_DIR):
    os.makedirs(VIDEO_DIR)

if not os.path.exists(SOUND_DIR):
    os.makedirs(SOUND_DIR)

video_list = glob.glob(f'{VIDEO_DIR}*.*')
video = video_list[0]

clip = VideoFileClip(video)
file_path = f'{SOUND_DIR}{filename}.mp3'
snapshot = clip.subclip(start_t, end_t)
snapshot.audio.write_audiofile(file_path)
