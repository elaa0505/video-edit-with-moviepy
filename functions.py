import os
import glob
import subprocess
import random
import string
from PIL import Image


def same_scale_resize_width(width, image):
    x, y = image.size[0], image.size[1]

    if width > x:
        diff_scale = x/(width - x)
        y = y + (y/diff_scale)

    elif width < x:
        diff_scale = x/(x - width)
        y = y - (y/diff_scale)

    else:
        pass

    x = width
    y = round(y)

    image = image.resize((x, y))
    return image


def same_scale_resize_height(height, image):
    x, y = image.size[0], image.size[1]

    if height > y:
        diff_scale = y/(height - y)
        x = x + (x/diff_scale)

    elif height < y:
        diff_scale = y/(y - height)
        x = x - (x/diff_scale)

    else:
        pass

    x = round(x)
    y = height

    image = image.resize((x, y))
    return image


def iter_frames(image):
    try:
        i= 0
        while 1:
            image.seek(i)
            imframe = image.copy()
            # if i == 0:
            #     palette = imframe.getpalette()
            # else:
            #     imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


def create_file_name():
    val = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return val


def get_min_len_and_random_list(files_1, files_2):
    len_1 = len(files_1)
    len_2 = len(files_2)

    min_len = min([len_1, len_2])

    random_1 = [i for i in range(len_1)]
    random.shuffle(random_1)
    random_1 = random_1[:min_len]

    random_2 = [i for i in range(len_2)]
    random.shuffle(random_2)
    random_2 = random_2[:min_len]

    return min_len, random_1, random_2


def image_merge_to_width_center(image_1, image_2, margin):
    x_1, y_1 = image_1.size[0], image_1.size[1]
    x_2, y_2 = image_2.size[0], image_2.size[1]

    total_width = x_1 + x_2 + margin
    total_height = max([y_1, y_2])

    new_image = Image.new('RGB', (total_width, total_height), (256, 256, 256))

    between_y_value = abs(y_1 - y_2)
    start_y = round(between_y_value/2)

    if y_1 > y_2:
        area_1 = (
            0,   # x start
            0,   # y start
            x_1, # x end
            y_1  # y end
        )
        area_2 = (
            x_1 + margin,
            start_y,
            x_1 + x_2 + margin,
            start_y + y_2
        )
    else:
        area_1 = (
            0,
            start_y,
            x_1,
            start_y + y_1
        )
        area_2 = (
            x_1 + margin,
            0,
            x_1 + x_2 + margin,
            y_2
        )

    new_image.paste(image_1, area_1)
    new_image.paste(image_2, area_2)

    return new_image


def image_merge_to_height_center(image_1, image_2, margin):
    x_1, y_1 = image_1.size[0], image_1.size[1]
    x_2, y_2 = image_2.size[0], image_2.size[1]

    total_width = max([x_1, x_2])
    total_height = y_1 + y_2 + margin

    new_image = Image.new('RGB', (total_width, total_height), (256, 256, 256))

    between_x_value = abs(x_1 - x_2)
    start_x = round(between_x_value/2)

    if x_1 > x_2:
        area_1 = (
            0,   # x start
            0,   # y start
            x_1, # x end
            y_1  # y end
        )
        area_2 = (
            start_x,
            y_1 + margin,
            start_x + x_2,
            y_1 + y_2 + margin
        )
    else:
        area_1 = (
            start_x,
            0,
            start_x + x_1,
            y_1
        )
        area_2 = (
            0,
            y_1 + margin,
            x_2,
            y_1 + y_2 + margin
        )

    new_image.paste(image_1, area_1)
    new_image.paste(image_2, area_2)

    return new_image


def get_avg_fps(filename):
    PIL_Image_object = Image.open(filename)
    PIL_Image_object.seek(0)
    frames = duration = 0
    while True:
        try:
            frames += 1
            duration += PIL_Image_object.info['duration']
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
        except EOFError:
            return frames / duration * 1000
    return None


def get_all_dir_files(path, all_files=[]):
    files = glob.glob(path + '*.*')
    all_files += files

    child_folders = glob.glob(path + '*/')
    for child_folder in child_folders:
        get_all_dir_files(child_folder, all_files)

    return all_files
