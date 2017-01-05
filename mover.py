#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-01-05 21:23:18
# ---------------------------------------


import os
import re
import filecmp
import shutil
from glob import glob

from extensions import allowed_file


class FileMover(object):

    def move(self, src, dst, allowed_types=('image', 'video')):
        """ 将源目录下的所有符合条件的文件移动到新的目录

        :param src: 源目录
        :param dst: 目标目录
        :param allowed_types: tuple, set or list
        :return:
        """
        if not os.path.exists(dst):
            os.mkdir(dst)
        for dir_path, dir_names, file_names in os.walk(src):
            for filename in file_names:
                src_path = os.path.join(os.path.abspath(dir_path), filename)
                dst_path = os.path.join(dst, filename)
                if allowed_file(filename, allowed_types):
                    print(filename)
                    self.move_file(src_path, dst_path)
                else:
                    print('dd', filename)

    def move_file(self, src, dst):
        """ 将指定路径文件移动到目标路径, 如果文件名已经存在, 则根据文件名创建新的路径

        """
        if os.path.exists(dst):
            if not filecmp.cmp(src, dst):
                new_dst = self.name_conflict(dst)
                print('Moving File:', src, dst)
                shutil.move(src, new_dst)
        else:
            print('Moving File:', src, dst)
            shutil.move(src, dst)

    def name_conflict(self, path):
        """ 根据给定的文件路径查看是否有文件存在,如果存在就创建新的路径并返回,不存在返回原路径

        """
        if not os.path.exists(path):
            return path

        dir_name, filename = os.path.split(path)
        name, extension = os.path.splitext(filename)

        numbers = []
        for path in glob(os.path.join(dir_name, '{}-(*){}'.format(name, extension))):
            match = re.search(r'-\((P?\d+)\)', path)
            if match:
                number = int(match.group(1))
                numbers.append(number)

        if not numbers:
            new_filename = '{}-(1){}'.format(name, extension)
        else:
            new_filename = '{0}-({1}){2}'.format(name, max(numbers) + 1, extension)

        return os.path.join(dir_name, new_filename)
