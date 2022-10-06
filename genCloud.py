import frequenciesAndScores
import os
from os import path
from wordcloud import WordCloud
from basicWordProcessor import BasicWordProcessor


# Gets a dictionary of words and important values from an unstructured text document.
# inputText: An unstructured text file.
# tokenProcessor: Used to process a token into an acceptable format.
# return: A dictionary(word, frequenciesAndScores).
# TODO: Hopefully get this to work with multiple documents, merging the dictionaries that pop out and updating
#  their counts.
def wordcloud_gen(folder):  # This is the Head function of the whole project
    counts = get_word_counts(folder, processor)  # gets the words from the documents within the folder
    filteredWords = get_words_and_frequencies_dictionary_above_weight(counts, 1.0)  # finds freq of said words
    info = wordcloud_svg_gen(filteredWords)  # creates the SVG of the word cloud
    aaa = svg_edit(info,counts)
    return aaa
    # html_name = folder + ".html"  # gives html file output name
    # html_file = open(html_name, 'w')  # opens a new/exiting html doc and allows writing
    # html_builder(html_file, aaa, counts)  # enters html info into opened file
    # html_file.close()


def get_word_counts(directory, tokenProcessor):
    totalDocs = 0
    wordsAndFrequencies = {}

    for filename in os.listdir(directory):
        inputText = os.path.join(directory, filename)
        # Check if file
        if os.path.isfile(inputText):
            discoveredWords = []
            totalDocs += 1
            print("Scanning document: " + filename)
            text = open(path.join(directory, filename), encoding='utf-8').read()
            words = text.split()

            for word in words:
                processed = tokenProcessor.process_token(word)
                if (wordsAndFrequencies.__contains__(processed)):
                    wordsAndFrequencies.get(processed).increment_frequency()
                    if not (discoveredWords.__contains__(processed)):
                        wordsAndFrequencies.get(processed).increment_doc_frequency()
                        discoveredWords.append(processed)
                else:
                    wordsAndFrequencies[processed] = frequenciesAndScores.FrequenciesAndScores()
                    discoveredWords.append(processed)

    # Once all the docs have been processed, we can go through and update each word's weight.
    for key in wordsAndFrequencies:
        wordsAndFrequencies[key].update_weight(totalDocs)

    # Debug printing
    for key in wordsAndFrequencies:
        print(key + '\t')
        print(wordsAndFrequencies.get(key))

    return wordsAndFrequencies


def get_words_and_frequencies_dictionary_above_weight(wordsAndWeights, targetWeight):
    wordsAndCounts = {}
    for word in wordsAndWeights:
        if (wordsAndWeights.get(word).weight >= targetWeight):
            wordsAndCounts[word] = wordsAndWeights.get(word).frequency

    return wordsAndCounts


def wordcloud_svg_gen(text):
    # generates the word cloud with arguments
    wordcloud = WordCloud(
        background_color='white', max_font_size=64, min_word_length=3, width=400, height=400, colormap="flag",
    ).generate_from_frequencies(text)
    # Creates SVG file
    wordcloud_svg = wordcloud.to_svg(embed_font=True)
    # this line below is actually used to write the SVG info into the HTML DOC
    info = wordcloud_svg
    return info

def svg_edit(svg_file, wordData):
    open("temp_svg.svg","w").write(svg_file) #there probably is a be a better idea, smoother
    read = open("temp_svg.svg","r")
    write_svg = ""

    for line in read:
        word =line.split(">")[1].split("<")[0]
        if len(word)>1 and len(word)<72:      #to ignore the first three lines and empty ones
            s = word+"<title> Word: "+word+"\nOccurrences: "+str(wordData[word].frequency)+"\nWeight: "\
                +str(round(wordData[word].weight, 3))+"</title>"
            li = line.replace(word,s)
            write_svg+=li
        else:
            write_svg += line
    
    return write_svg

def html_builder(file, eis, ken, nix):
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
        <select id="choose" onchange="myFunction(this.options[this.selectedIndex].value);"> 
            <option value="triangle">Eisenhower</option>
            <option value="square">Kennedy</option>
            <option value="circle">Nixon</option>
        </select>
        <div class="triangle" id="triangle">
    """
    # Eisen content here
    mid1 = """
    </div>


        <div class="square" id="square">
        """
    # Ken content here
    mid2="""
    </div>

<div class="circle" id="circle">
    """
    # Nix content here
    Bottom = """
</div>

<script>
    document.getElementById("triangle").style.display = "block";
    document.getElementById("circle").style.display = "none";
    document.getElementById("square").style.display = "none";
    //document.getElementById("square").style.display = "none";
  
    function myFunction(c) 
    {
    document.getElementById("triangle").style.display = "none";
    document.getElementById("circle").style.display = "none";
    document.getElementById("square").style.display = "none";
    document.getElementById(c).style.display = "block";
    }
</script>
</body>
</html>
    """
    # aaa = svg_file
    # aaa = svg_edit(svg_file, wordData)
    # open("temp_svg.svg","w").write(svg_file) #there probably is a be a better idea, smoother
    
    # read = open("temp_svg.svg","r")
    # write_svg = ""
    # for line in read:
    #     word =line.split(">")[1].split("<")[0]
    #     if len(word)>1 and len(word)<72:      #to ignore the first three lines and empty ones
    #         s = word+"<title> Word: "+word+"\nOccurrences: "+str(wordData[word].frequency)+"\nWeight: "\
    #             +str(round(wordData[word].weight, 3))+"</title>"
    #         li = line.replace(word,s)
    #         write_svg+=li
    #     else:
    #         write_svg += line
    
    file.write(Top + eis + mid1 + ken + mid2 + nix + Bottom)


processor = BasicWordProcessor()
nixon=wordcloud_gen('nixon')
esien=wordcloud_gen('eisenhower')
kenne=wordcloud_gen('speeches')
html_file = open("index.html", 'w')
html_builder(html_file, esien,kenne,nixon)