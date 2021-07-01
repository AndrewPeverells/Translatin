*- Translatin project: https://translatin.nl* \
*- Head of the project: Jan Bloemendal - https://www.huygens.knaw.nl/medewerkers/jan-bloemendal/* \
*- Author: Andrea Peverelli (Github/AndrewPeverells), Huygens ING, KNAW Humanities Cluster, DHLab - https://www.huygens.knaw.nl/medewerkers/andrea.peverelli* \
*- Supervisor: Marieke van Erp, KNAW Humanities Cluster, DHLab - https://mariekevanerp.com/* \
*- DHLab site: https://dhlab.nl/*

----------------------------------------------------------------------------------------------------------

> # CORPUS PREPARATION
<br />

> ### 0) ASSEMBLING THE CORPUS (Translatin Repository)

3 texts:
- Crocus Ioseph
- Macropedius Hecastus
- Macropedius Ioseph

*2 from the same author / 2 with same topic*
<br />
<br />
> ### 1) CLEANING THE TEXTS


**Replacing punctuation**

1. `text = '[text]'`

2. `x = text.replace(",", " ").replace(".", " ").replace(":", " ").replace(";", " ").replace("!", " ").replace("?", " ").replace("’", " ").replace("-,", " ").replace("*", " ")`\
`print(x)`

<br />

**Changing everything to lower case**

1. `tokens = ['tokens', 'list']`

2. `tokens = [each_string.lower() for each_string in tokens]`\
  `print(tokens)`
  
***
<br />

> # TASKS (through CLTK: http://cltk.org/)

<br />

> ### 2) TOKENIZATION:

`import nltk`\
`from cltk.tokenize.word import WordTokenizer`\
`word_tokenizer = WordTokenizer('latin')`\
`word_tokenizer.tokenize(x)`

<br />

> ### 3) LEMMATIZATION:

`from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer`\
`lemmatizer = BackoffLatinLemmatizer()`\
`tokens = ['tokens', 'list']`\
`lemmatizer.lemmatize(tokens)`

*(cltk lemmatizer recognizes archaisms too!)*