#!/usr/bin/env python3

import os
from pyperclip import paste
from zipfile import ZipFile

def main():
    clipboard = paste()
    zipName = clipboard.replace('*', 'PORT PKG')

    for file in os.listdir():
        os.rename(file, clipboard.replace('*', file))

    with ZipFile(zipName, 'w') as zipFile:
        for file in os.listdir():
            zipFile.write(file)


if __name__ == '__main__':
    main()
