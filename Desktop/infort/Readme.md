# Assignment 1
## Information
Name: Jeet Mehta

UIN: 668581235

## Functionality of each program

There are five main functions here in my code. 
1. file_open()
2. punctuations()
3. text_cleaning
4. portStemmer()
5. find_stats()
Except for this we have also imported stopwords that is extracted from the nltk.corpus package which will help us get rid of the 
words that I won't want to use to describe the summary of my content/ words. 
### 1. file_open()

Here, I have just implemented the file read method basically where the entire citeseer directory is passed. This function,
not only helps in reading the file but also helps in preparing the `words_list` & `words_dict`. These vars account for
total words in collection and vocab size(unique terms) respectively.

### 2. punctuations()

This function helps in getting rid of the white space by matching every non word character and replace them with `''`.

### 3. text_cleaning()

The input to this is received from the `file_open()` function. What this does is basically tokenize each and every
word. This function works in conjunction with punctuations. 

### 4. port_stemmer()

This function is the third part of the assignment where we had to implement stemming(i.e. reduce the word to stem word)
and hence the name port_stemmer. To avoid overstemming and understemming care has to be taken.
To make it as good as possible, we have another `stem_dict` var which takes care that we don't run into the mainstream error
of stemming. 
`PorterStemmer()` module, comes from the NLTK library. 

### 5. find_stats()

This method here helps in answering the questions to answer the top 20 words in ranking, in these top 20 help us recognise
the stop words & the minimum number of unique words that are 15% of the total words we have in collection. 
The 15% is basically the 15% of the the words list that we have computed.

## Instructions to run the code.

My environment:

OS: Windows 10
IDE: VSCode
Language: Python
Prereq:
Have python installed on your system. 
Make sure you have the citeseer directory and the python code both in the same folder.
My structure:
        Desktop
        |
        --folder
                |
                -- citeseer folder
                -- infortr.py
                -- Readme.md
Run using:

        `python infortr.py`

## Answers/ Results:

2(a) Total words in the collection:  476198
2(b) Total vocab. size:  19886
2(c) Top 20 words by ranking:
('the', 25662)
('of', 18638)
('and', 14131)
('a', 13345)
('to', 11536)
('in', 10067)
('for', 7379)
('is', 6577)
('we', 5138)
('that', 4820)
('this', 4446)
('are', 3737)
('on', 3656)
('an', 3281)
('with', 3200)
('as', 3057)
('by', 2765)
('data', 2691)
('be', 2500)
('information', 2322)
Stop words from the Top 20 words are:
('the', 25662)
('of', 18638)
('and', 14131)
('a', 13345)
('to', 11536)
('in', 10067)
('for', 7379)
('is', 6577)
('we', 5138)
('that', 4820)
('this', 4446)
('are', 3737)
('on', 3656)
('an', 3281)
('with', 3200)
('as', 3057)
('by', 2765)
('be', 2500)
Words that account for 15% or more of the total number of words:  4
<---------------------------------------------------------------------------------------------------------------------------------------->
Part 3: Integrate a stemmer and stopword
3(a) Total words in the collection:  294256
3(b) Total vocab. size:  13778
3(c) Top 20 words by ranking:
('system', 3741)
('use', 3740)
('data', 2691)
('agent', 2688)
('inform', 2398)
('model', 2315)
('paper', 2246)
('queri', 1905)
('user', 1756)
('learn', 1740)
('algorithm', 1584)
('1', 1552)
('approach', 1544)
('problem', 1543)
('applic', 1522)
('present', 1507)
('base', 1486)
('web', 1439)
('databas', 1424)
('comput', 1411)
Stop words from the Top 20 words are:
Not in top 20. Hence, 0 stopwords
Words that account for 15% or more of the total number of words:  24