import nltk, numpy, os, re

washLoad = os.path.join(os.getcwd(),'Documents/GitHub/LegalTreebankDev/Case Processing', 'origcase.txt')
prewashFirst = os.path.join(os.getcwd(),'Documents/GitHub/LegalTreebankDev/Case Processing', 'preclean1.txt')
prewashSec = os.path.join(os.getcwd(),'Documents/GitHub/LegalTreebankDev/Case Processing', 'prewashSec.txt')
washed = os.path.join(os.getcwd(),'Documents/GitHub/LegalTreebankDev/Case Processing', 'cleaned.txt')

blank = ''
pretag = '<s>'
backtag = '</s>'


caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co|Ins|Cos)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
digits = "([0-9])"
months = '([Jan|Feb|Mar|Apr|Aug|Sept|Oct|Nov|Dec])'
abbr = '([No|v|n|cl])'
states = '([Ala|Am Sam|Ark|Cal|CZ|Colo|Conn|Del|DC|Fla|Ga|Haw|Ill|Ind|Kan|Ky|La|Me|Md|Mass|Mich|Minn|Miss|Mo|Mont|Neb|Nev|NH|NJ|NM|NY|NC|ND|N Mar I|Okla|Or|Pa|PR|RI|SC|SD|Tenn|Tex|Vt|VI|Va|Wash|W Va|Wis|Wyo])'
reporters = '([S.Ct|F.Cas|F|F 2d|F 3d|F Supp|F Supp 2d|F Supp 3d|FRD|BR|Fed Appx|A|A 2d|A 3d|NE|NW|NW 2d|SE|SE 2d|So|So 2d|So 3d|SW|SW 2d|SW 3d|P|P 2d|P 3d])'

def replace(file):
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    text = file_handle.read()
    file_handle.close()
    
    # Character cleanup
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace("’", "'").replace( "‘", "'") # Note: This replaces the apostrophe and open/close single quotation.
    text = text.replace( "&", "&amp;")
    text = text.replace( "¶¶", "paras.").replace( "¶", "para.")
    text = text.replace( "§§", "secs.").replace("§", "sec.")
    text = text.replace( "|", "")
    
    # Remove Westlaw numbers
    text = re.sub(r'(\*\d{1,4}.)', blank , text, flags=0)
           
    # Write contents to file.
    file_handle = open(prewashFirst, 'w')
    file_handle.write(text)
    file_handle.close()

def split_into_sentences(text):
    file_handle = open(text, 'r')
    text = file_handle.read()
    file_handle.close()
    
    # https://stackoverflow.com/questions/4576077/python-split-text-on-sentences
    # Add a blank space before and after text in file. Why?
    text = " " + text + "  "
    # Replace each linefeed with a blank space.
    text = text.replace("\n", " ")
    # Replace prefixes (above) with "\\1<prd>".
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    # These regex deal with period break issues that come up in case law.
    text = re.sub(caps + "[.]", "\\1<prd>", text) # testing
    text = re.sub(months + "[.]",'\\1<prd>',text) # testing
    text = re.sub(abbr + "[.]" + " ",' \\1<prd>',text) # testing
    text = re.sub(states + "[.]" + caps, '\\1<prd>\\2',text) # testing
    text = re.sub(states + "[.]" + digits, '\\1<prd>\\2',text) # testing
    text = re.sub(reporters + "[.]" + digits, '\\1<prd>\\2',text) # testing 
    # Fix eg and ie.
    text = text.replace("e.g.","e<prd>g<prd>") 
    text = text.replace("i.e.","i<prd>e<prd>")
    # The next four replacements move quotes at sentence end following the punctuation, inside the punctuation.
    if "\"" in text: text = text.replace(".\"","\".")
    if "'" in text: text = text.replace(".'","'.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    # The next four replacments add <stop> after puncutation at the end of a sentence.
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    # This is where the <prd> is replace with actual periods.
    text = text.replace("<prd>",".")
    # This is where the sentence split occurs - at each <stop> which is considered the separator (and dropped).
    sentences = text.split("<stop>")
    # This trims a space at the end of sentences.
    sentences = sentences[:-1]
    # This trims leading and trailing whitespace.
    sentences = [s.strip() for s in sentences]
    # This is a list comprehension. It adds <s></s> tags to the beginning and end of each string (sentence) in the list.
    tagsent = [pretag + s + backtag for s in sentences]
    
    # tagsent now is the primary file.
    # This uses a genexp (not list comprehension) so it prints one line at a time to the file, not using so much memory.
    file_handle = open(prewashSec, 'w')
    for item in tagsent:
        file_handle.write("%s\n" % item)

replace(washLoad)
split_into_sentences(prewashFirst)