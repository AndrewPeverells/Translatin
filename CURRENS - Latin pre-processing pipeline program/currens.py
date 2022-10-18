import re
import nltk
from nltk.tokenize.punkt import PunktLanguageVars
from replacer import replacerfunction
from ArchaismsHandler import ArchaismsHandler
from removeStopwords import removeStopwords
from EncliticsHandler import EncliticsHandler

with open('corpus/truculentus.txt', 'r') as file:
    text = file.read()

# Scelte
archaismschoice = None
stopwordschoice = None

var = input("Would you like to remove Stopwords? Please type yes or no: ")
if (var == "yes"):
    stopwordschoice = True

var = input("Would you like to handle Archaisms? Please type yes or no: ")
if (var == "yes"):
    archaismschoice = True

# Tokenizer

p = PunktLanguageVars()
tokens = p.word_tokenize(text)

text = ""

for element in tokens:
        text += element+" "

# General cleaning

text = replacerfunction(text)
text = text.lower()
textlist = list(text.split(" "))

# Stopwords

if (stopwordschoice == True):
    textlist = removeStopwords(textlist)

# Archaisms handler

if (archaismschoice == True):
    textlist = ArchaismsHandler(textlist)

# Enclitics handler

textlist = EncliticsHandler(textlist)

text = ""

for element in textlist:
        text += element+" "

with open('./temp.txt', 'w') as f:
    f.write(text)



""""
latin_replacements = [
        (r"\bmecum\b", "cum me"),
        (r"\btecum\b", "cum te"),
        (r"\bsecum\b", "cum se"),
        (r"\bnobiscum\b", "cum nobis"),
        (r"\bvobiscum\b", "cum vobis"),
        (r"\buobiscum\b", "cum uobis"),
        (r"\bquocum\b", "cum quo"),
        (r"\bquacum\b", "cum qua"),
        (r"\bquicum\b", "cum qui"),
        (r"\bquibuscum\b", "cum quibus"),
        (r"\bsodes\b", "si audes"),
        (r"\bsatin\b", "satis ne"),
        (r"\bscin\b", "scis ne"),
        (r"\bsultis\b", "si vultis"),
        (r"\bsimilist\b", "similis est"),
        (r"\bqualist\b", "qualis est"),
    ]"""

