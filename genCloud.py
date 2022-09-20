import os

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'input.txt')).read()


wordcloud = WordCloud(background_color = 'white', max_font_size=40).generate(text)

wordcloud_svg = wordcloud.to_svg(embed_font=True)
f = open("cloud.svg","w+")
f.write(wordcloud_svg )
f.close()

