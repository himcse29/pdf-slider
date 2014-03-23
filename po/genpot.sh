#!/bin/sh

#
# PdfSlider 0.6.0 - GTK+ based utility for splitting, rearrangement and
# modification of PDF documents.
#

# Make translation files
intltool-extract --type=gettext/glade data/pdfslider.ui
xgettext --language=Python --keyword=_ --keyword=N_ --output=po/pdflider.pot pdfslider/*.py data/pdfslider.ui.h
