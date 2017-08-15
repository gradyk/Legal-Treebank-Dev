# Use this on extracted fact, issue, analysis, etc text.
# This text converts the extracted text to a SENTENCE tokenized file.

import nltk, numpy, os, re, codecs

washSent = os.path.join(os.getcwd(),'Documents/GitHub/LegalTreebankDev/Case XML', 'cleaned.txt')
case_type_sent = os.path.join(os.getcwd(), 'Documents/GitHub/LegalTreebankDev/Case Processing', 'clean_type_sent.txt')

def splitSent(file):
    
    raw_text = open(file,'r')
    raw_text_string = raw_text.read()
    text_string = nltk.sent_tokenize(raw_text_string)

    # Write contents to file.
    hold_sent = open(case_type_sent, 'w')
    hold_sent.write(str(text_string))
    hold_sent.close()
    
splitSent(washSent)