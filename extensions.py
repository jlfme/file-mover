#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-01-03 20:02:18
# ---------------------------------------


import os
import itertools


MAX_CONTENT_LENGTH = 16 * 1024 * 1024


# image types
IMAGE_EXTENSIONS = tuple('jpg jpe jpeg png gif svg bmp'.split())

# archive and compression formats
ARCHIVE_EXTENSIONS = tuple('gz bz2 zip rar tar tgz txz 7z'.split())

# audio file types
AUDIO_EXTENSIONS = tuple('wav mp3 aac ogg oga flac'.split())

# video file types
VIDEO_EXTENSIONS = tuple('avi mp4 wmv mov rmvb m4v mkv mpg mts mts flv'.split())

# structured data files
DATA_EXTENSIONS = tuple('csv ini json plist xml yaml yml'.split())

# This just contains plain text files
TEXT_EXTENSIONS = tuple('txt'.split())

# This contains various office document formats
DOCUMENT_EXTENSIONS = tuple('rtf odf ods gnumeric abw doc docx xls xlsx'.split())

# This contains various types of scripts
SCRIPT_EXTENSIONS = tuple('js php pl py rb sh'.split())

# This contains shared libraries and executable files
EXECUTABLE_EXTENSIONS = tuple('so exe dll'.split())

# The default allowed extensions - `TEXT`, `DOCUMENTS`, and `IMAGES`.
DEFAULT_EXTENSIONS = IMAGE_EXTENSIONS + TEXT_EXTENSIONS + DOCUMENT_EXTENSIONS


extensions_map = {
    'image': IMAGE_EXTENSIONS,
    'archive': ARCHIVE_EXTENSIONS,
    'audio': AUDIO_EXTENSIONS,
    'video': VIDEO_EXTENSIONS,
    'data': DATA_EXTENSIONS,
    'text': TEXT_EXTENSIONS,
    'doc': DOCUMENT_EXTENSIONS,
    'script': SCRIPT_EXTENSIONS,
    'exe': EXECUTABLE_EXTENSIONS,
    'default': DEFAULT_EXTENSIONS
}


def tuple_from(*iters):
    return tuple(itertools.chain(*iters))


def allowed_file(filename, allowed_extensions=('image', )):
    """
    :param filename: filename
    :param allowed_extensions: list tuple or set , ('image', 'video')
    :return:
    """
    extensions = tuple()
    for key in allowed_extensions:
        extensions = extensions_map[key] + extensions

    name, extension = os.path.splitext(filename)

    if '.' in extension:
        return extension.lower().split('.')[-1] in extensions
    return False
