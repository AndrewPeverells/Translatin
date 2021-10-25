*- Translatin project: https://translatin.nl* \
*- Head of the project: Jan Bloemendal - https://www.huygens.knaw.nl/medewerkers/jan-bloemendal/* \
*- Author: Andrea Peverelli (Github/AndrewPeverells), Huygens ING, KNAW Humanities Cluster, DHLab - https://www.huygens.knaw.nl/medewerkers/andrea.peverelli* \
*- Supervisor: Marieke van Erp, KNAW Humanities Cluster, DHLab - https://mariekevanerp.com/* \
*- DHLab site: https://dhlab.nl/*

----------------------------------------------------------------------------------------------------------

> # CORPUS PREPARATION
<br />

> ### 0) ASSEMBLING THE CORPUS (Translatin Repository)

Texts:

Translatin_repo
1. crocus 1535
2. mhecastus 1539
3. mjoseph 1544
4. bidermann 1615
5. schonaeus 1592
6. diether 1543
7. libenus_ven 1634
8. libenus_agn 1639

---

Terentius
9. adelphoe
10. phormio
11. hecyra
12. eunuchus
13. heautontimoroumenos
14. andria

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

> ### 4) Calculating Cosine Similarities (see file)
