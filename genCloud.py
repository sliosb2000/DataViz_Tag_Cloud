from email import message
import os

from os import path
from typing import TextIO

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'input.txt')).read()

# generates the word cloud with arguments
wordcloud = WordCloud(background_color = 'white', max_font_size=40).generate(text)

wordcloud_svg = wordcloud.to_svg(embed_font=True)
f = open("cloud.svg","w+")
f.write(wordcloud_svg)
info = wordcloud_svg
f.close()

with open('cloud.svg', 'r') as file:
    pass

# We need to make an HTML Generator in python
# the idea is to use a HTML page to format the interaction with the SVG
# so by importing the SVG into the HTML document and by making the CSS for all <text> items
# All the words will react in the same way (depending on what we choose them to do)
f = open('index.html','w')

Top = """
<html>
    <head>
    <style>
    text:focus,text:hover {
        font-weight: bold;
    }
    </style>
    </head>
    <body>
"""
Bottom ="""
    </body>
</html>
"""
f.write(Top + info + Bottom)
f.close