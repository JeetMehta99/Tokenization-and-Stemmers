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
5. find_stats() <br />
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
and hence the name port_stemmer. To avoid overstemming and understemming care has to be taken. <br />
To make it as good as possible, we have another `stem_dict` var which takes care that we don't run into the mainstream error
of stemming. <br />
`PorterStemmer()` module, comes from the NLTK library. 

### 5. find_stats()

This method here helps in answering the questions to answer the top 20 words in ranking, in these top 20 help us recognise
the stop words & the minimum number of unique words that are 15% of the total words we have in collection. 
The 15% is basically the 15% of the the words list that we have computed.

## Instructions to run the code.

My environment:

OS: Windows 10 <br />
IDE: VSCode <br />
Language: Python <br />
Prereq: <br />
Have python installed on your system. <br />
Make sure you have the citeseer directory and the python code both in the same folder.

My structure: <br />
        Desktop <br />
        |       <br />
        --folder <br />
&nbsp; &nbsp; &nbsp; &nbsp;         | <br />
&nbsp; &nbsp; &nbsp; &nbsp;                -- citeseer folder <br />
&nbsp; &nbsp; &nbsp; &nbsp;                -- infortr.py <br />
&nbsp; &nbsp; &nbsp; &nbsp;                -- Readme.md <br />

Clone the project on your local machine. <br />
Run using:

        `python infortr.py`

## Answers/ Results:

2(a) Total words in the collection:  476198 <br /><br />
2(b) Total vocab. size:  19886 <br /><br />
2(c) Top 20 words by ranking: <br /><br />
0 ('the', 25662) <br />
1 ('of', 18638) <br />
2 ('and', 14131) <br />
3 ('a', 13345) <br />
4 ('to', 11536) <br />
5 ('in', 10067) <br />
6 ('for', 7379) <br />
7 ('is', 6577)<br />
8 ('we', 5138)<br />
9 ('that', 4820)<br />
10 ('this', 4446)<br />
11 ('are', 3737)<br />
12 ('on', 3656)<br />
13 ('an', 3281)<br />
14 ('with', 3200)<br />
15 ('as', 3057)<br />
16 ('by', 2765)<br />
17 ('data', 2691)<br />
18 ('be', 2500)<br />
19 ('information', 2322)<br />
Stop words from the Top 20 words are:<br /><br />
0 ('the', 25662)<br />
1 ('of', 18638)<br />
2 ('and', 14131)<br />
3 ('a', 13345)<br />
4 ('to', 11536)<br />
5 ('in', 10067)<br />
6 ('for', 7379)<br />
7 ('is', 6577)<br />
8 ('we', 5138)<br />
9 ('that', 4820)<br />
10 ('this', 4446)<br />
11 ('are', 3737)<br />
12 ('on', 3656)<br />
13 ('an', 3281)<br />
14 ('with', 3200)<br />
15 ('as', 3057)<br />
16 ('by', 2765)<br />
17 ('be', 2500)<br />
Words that account for 15% or more of the total number of words:  4<br /><br />
<----------------------------------------------------------------------------------------------------------------------------------------><br /><br />
Part 3: Integrate a stemmer and stopword<br />
3(a) Total words in the collection:  294256<br /><br />
3(b) Total vocab. size:  13778<br /><br />
3(c) Top 20 words by ranking:<br />
0 ('system', 3741)<br />
1 ('use', 3740)<br />
2 ('data', 2691)<br />
3 ('agent', 2688)<br />
4 ('inform', 2398)<br />
5 ('model', 2315)<br />
6 ('paper', 2246)<br />
7 ('queri', 1905)<br />
8 ('user', 1756)<br />
9 ('learn', 1740)<br />
10 ('algorithm', 1584)<br />
11('1', 1552)<br />
12 ('approach', 1544)<br />
13 ('problem', 1543)<br />
14 ('applic', 1522)<br />
15 ('present', 1507)<br />
16 ('base', 1486)<br />
17 ('web', 1439)<br />
18 ('databas', 1424)<br />
19 ('comput', 1411)<br /><br />
Stop words from the Top 20 words are:<br />
Not in top 20. Hence, 0 stopwords<br />
Words that account for 15% or more of the total number of words:  24<br />