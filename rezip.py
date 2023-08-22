#!/usr/bin/env python3

import os
from optparse import OptionParser
from pyperclip import paste, copy
from zipfile import ZipFile
from pathlib import Path

def main():
    clipboard = paste()
    zipName = clipboard.replace('*', 'PORT PKG.zip')

    for file in os.listdir():
        os.rename(file, clipboard.replace('*', file))

    with ZipFile(zipName, 'w') as zipFile:
        for file in os.listdir():
            if file == zipName:
                continue
            zipFile.write(file)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-t', '--test', dest='test', action='store_true',
                      help="""
                      Run a test to make sure this works [default: %default]
                      """)
    parser.set_defaults(test=False)
    opts, args = parser.parse_args()
    if opts.test:
        Path('ALLOCATIONS.xlsx').touch()
        Path('ISP PV Form Jira.docx').touch()
        Path('Preterm-Fiber-Port Validation.docx').touch()
        Path('TIE POINT.pdf').touch()
        Path('TRACE.xlsx').touch()
        copy("F_123456_MY AWESOM COMPANY - *")
    main()
