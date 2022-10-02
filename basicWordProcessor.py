#import regular expressions
import re


class BasicWordProcessor:

    #Removes all non-alphanumeric characters from a token.
    def process_token(self, token):
        processed_token = re.sub('[\W\d]+', '', token)
        #print("Token: " + token + ", Processed " + processed_token)
        return processed_token.lower()