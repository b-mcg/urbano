#!/usr/bin/env python2

# Imports
from distutils.core import setup
from os import remove
from os.path import abspath
from os.path import join as path_join
from os import getcwd
from shutil import copyfile, rmtree
import glob

import urbano

pathname                =               getcwd()

VERSION                 =               '0.0.1-1'

copyfile("urbano.py", "urbano/urbano")

packages                =               ['urbano']

setup(name              =               'urbano',
      version           =               VERSION,
      description       =               'Python program for getting word definitions from urban dictionary.',
      author            =               'b-mcg',
      author_email      =               'b-mcg@gmail.com',
      url               =               'https://github.com/b-mcg/urbano',
      packages          =               packages,
      package_dir       =               {'urbano' : abspath(path_join(pathname, 'urbano/'))},
      scripts           =               ['urbano/urbano'],
      data_files        =               [('share/urbano', ['README.md', 'LICENSE'])],

        )

prev_eggs   =       glob.iglob('/usr/lib/python2.7/site-packages/urbano-0.0.*')

# Remove moved main file
try:
    remove(abspath(path_join(pathname, 'urbano/urbano')))

except:
    pass

# Delete any previous egg files
for i in prev_eggs:
    try:
        temp        =       i.split('/')[-1].split('-')
        
        if temp[1] < VERSION.replace('-', '_'):
            remove(i)

    except:
        pass

# Delete build directory since it's no longer necessary
try:
    rmtree(abspath(path_join(pathname, 'build/')))

except:
    pass
