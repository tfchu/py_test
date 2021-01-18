# result
#  file: S_IFREG (regular)
#  dir: S_IFDIR (directory)
#  device (/dev/sda, /dev/sda1): S_IFBLK, S_IFCHR, S_IFDIR

import os
from stat import S_IFSOCK, S_IFREG, S_IFBLK, S_IFDIR, S_IFCHR, S_IFIFO

def get_file_type(path):
    """Retrieve the file type of the path

    :param path: The path to get the file type for
    :return: The file type as a string or None on error
    """
    f_types = {
        'socket':           S_IFSOCK,
        'regular':          S_IFREG,
        'block':            S_IFBLK,
        'directory':        S_IFDIR,
        'character_device': S_IFCHR,
        'fifo':             S_IFIFO,
    }
    if not path or not os.path.exists(path):
        return None

    obj = os.stat(path).st_mode
    for key, val in f_types.items():
        if obj & val == val:
            print(key)

def main():
    path = r'C:\\'
    get_file_type(path)

if __name__ == '__main__':
    main()
