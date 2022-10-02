import math

#Stores the frequency, amount of docuements a word appears in, and the weight of some word in a corpus of documents.
class FrequenciesAndScores:
    def __init__(self):
        self.frequency = 1
        self.doc_frequency = 1
        self.weight = 0

    def increment_frequency(self):
        self.frequency += 1

    def increment_doc_frequency(self):
        self.doc_frequency += 1

    # weight = frequency * log(1 + (total_documents/doc_frequency))
    def update_weight(self, total_documents):
        self.weight = self.frequency * math.log(1 + (total_documents/self.doc_frequency))

    def __str__(self):
        return "Frequency: " + str(self.frequency) + " | Docs: " + str(self.doc_frequency) \
               + " | Weight " + str(self.weight)