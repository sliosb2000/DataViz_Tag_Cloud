from email import message
import os

import frequenciesAndScores
from frequenciesAndScores import FrequenciesAndScores
from basicWordProcessor import BasicWordProcessor

from os import path
from typing import TextIO

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Gets a dictionary of words and important values from an unstructured text document.
# inputText: An unstructured text file.
# tokenProcessor: Used to process a token into an acceptable format.
# return: A dictionary(word, frequenciesAndScores).
# TODO: Hopefully get this to work with multiple documents, merging the dictionaries that pop out and updating
#  their counts.
def get_word_counts(directory, tokenProcessor):
    totalDocs = 0
    wordsAndFrequencies = {}

    for filename in os.listdir(directory):
        inputText = os.path.join(directory, filename)
        #Check if file
        if os.path.isfile(inputText):
            discoveredWords = []
            totalDocs += 1
            print("Scanning document: " + filename)
            text = open(path.join(directory, filename), encoding='utf-8').read()
            words = text.split()

            for word in words:
                processed = tokenProcessor.process_token(word)
                if(wordsAndFrequencies.__contains__(processed)):
                    wordsAndFrequencies.get(processed).increment_frequency()
                    if not(discoveredWords.__contains__(processed)):
                        wordsAndFrequencies.get(processed).increment_doc_frequency()
                        discoveredWords.append(processed)
                else:
                    wordsAndFrequencies[processed] = frequenciesAndScores.FrequenciesAndScores()
                    discoveredWords.append(processed)

    #Once all the docs have been processed, we can go through and update each word's weight.
    for key in wordsAndFrequencies:
        wordsAndFrequencies[key].update_weight(totalDocs)

    #Debug printing
    for key in wordsAndFrequencies:
        print(key)
        print(wordsAndFrequencies.get(key))

    return wordsAndFrequencies

def get_words_and_frequencies_dictionary_above_weight(wordsAndWeights, targetWeight):
    wordsAndCounts = { }
    for word in wordsAndWeights:
        if(wordsAndWeights.get(word).weight >= targetWeight):
            wordsAndCounts[word] = wordsAndWeights.get(word).frequency

    return wordsAndCounts


processor = BasicWordProcessor()
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
#text = open(path.join(d, 'Documents/input.txt'), encoding='utf-8').read()
#text = open(path.join(d, 'pridpred.txt')).read()

counts = get_word_counts('Documents', processor)
filteredWords = get_words_and_frequencies_dictionary_above_weight(counts, 0.0)


# generates the word cloud with arguments
wordcloud = WordCloud(
    background_color='Rosybrown', max_font_size=64, min_word_length=3, width=400, height=400, colormap="Pastel1",
).generate_from_frequencies(filteredWords)


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
