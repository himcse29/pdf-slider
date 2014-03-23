#!/usr/bin/python



import os
import re
from distutils.core import setup

data_files=[('share/pdfslider', ['data/pdfslider.ui']),
            ('share/applications', ['data/pdfslider.desktop']),
            ('share/man/man1', ['doc/pdfslider.1']),
            ('share/pixmaps', ['data/pdfslider.png']),
            ('share/pdfslider/icons/hicolor/scalable',
                ['data/pdfslider.svg']) ]


# Freshly generate .mo from .po, add to data_files:
if os.path.isdir('mo/'):
    os.system ('rm -r mo/')
for name in os.listdir('po'):
    m = re.match(r'(.+)\.po$', name)
    if m != None:
        lang = m.group(1)
        out_dir = 'mo/%s/LC_MESSAGES' % lang
        out_name = os.path.join(out_dir, 'pdfslider.mo')
        install_dir = 'share/locale/%s/LC_MESSAGES/' % lang
        os.makedirs(out_dir)
        os.system('msgfmt -o %s po/%s' % (out_name, name))
        data_files.append((install_dir, [out_name]))

setup(name='pdfslider',
      version='0.6.0',
      author='Konstantinos Poulios',
      author_email='logari81 at gmail dot com',
      description='A simple application for PDF Merging, Rearranging, and Splitting',
      url = 'https://sourceforge.net/projects/pdfslider',
      license='GNU GPL-3',
      scripts=['bin/pdfslider'],
      packages=['pdfslider'],
      data_files=data_files
     )

# Clean up temporary files
if os.path.isdir('mo/'):
    os.system ('rm -r mo/')
if os.path.isdir('build/'):
    os.system ('rm -r build/')

