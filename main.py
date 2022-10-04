import os

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'Documents/input.txt')).read()


wordcloud = WordCloud(background_color = 'white', max_font_size=40).generate(text)

wordcloud_svg = wordcloud.to_svg(embed_font=True)
f = open("cloud.svg","w+")
f.write(wordcloud_svg )
f.close()

# We need to make an HTML Generator in python
# the idea is to use a HTML page to format the interaction with the SVG
# so by importing the SVG into the HTML document and by making the CSS for all <text> items
# All the words will react in the same way (depending on what we choose them to do)
html: open('index.html','w')

contents = """
<html>
    <head>
    <style>
    text:focus,text:hover {
        font-weight: bold;
    }
    </style>
    </head>
    <body>
    <text>text</text>
    </body>
</html>
"""
html.write(contents)
html.close

