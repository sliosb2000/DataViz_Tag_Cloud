from email import message
import os

from os import path
from typing import TextIO

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'input.txt'), encoding='utf-8').read()
#text = open(path.join(d, 'pridpred.txt')).read()

# generates the word cloud with arguments
wordcloud = WordCloud(
    background_color='Rosybrown', max_font_size=64, min_word_length=3, width=400, height=400, colormap="Pastel1",
).generate(text)

# Creates SVG file
wordcloud_svg = wordcloud.to_svg(embed_font=True)
# this line below is actually used to write the SVG info into the HTML DOC
info = wordcloud_svg

# creates an actual SVG file
# f = open("cloud.svg","w+")
# f.write(wordcloud_svg)
# f.close()


# Here we Generate the HTML File we write the nessesary text to generate
# the file to our liking.
f = open('index.html', 'w')

Top = """
<html>
    <head>
    <meta charset="UTF-8">
    <style>
    text:focus,text:hover {
        font-weight: bold;
    }
    </style>
    </head>
    <body>
"""
Bottom = """
    </body>
</html>
"""
f.write(Top + info + Bottom)
f.close
