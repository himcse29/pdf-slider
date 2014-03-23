#!/bin/sh



# Update translation files
find ./po -type f -iname "*.po" -exec msgmerge -U {} po/pdfslider.pot \;
