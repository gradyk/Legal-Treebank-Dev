# Use this on extracted fact, issue, analysis, etc text.
# This text converts the extracted text to a WORD tokenized file.

import nltk, numpy, os, re, codecs, sys

washWord = os.path.join(os.getcwd(),'Documents/GitHub/LegalTreebankDev/Case XML', 'cleaned.txt')
clean_type_word = os.path.join(os.getcwd(), 'Documents/GitHub/LegalTreebankDev/Case Processing', 'clean_type_word.txt')

def splitWord(file):
    
    raw_text = open(file, 'r')
    raw_text_string = raw_text.read()
    processed_text = nltk.word_tokenize(raw_text_string)

    # Write contents to file.
    hold_word = open(clean_type_word, 'w')
    hold_word.write(str(processed_text))
    hold_word.close()

splitWord(washWord)