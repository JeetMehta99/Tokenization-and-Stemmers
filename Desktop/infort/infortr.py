# Jeet Mehta
# UIN: 668581235
from nltk import PorterStemmer 
from nltk.corpus import stopwords
import re, os, string
directory = "citeseer"

def file_open():
    for filename in os.listdir(directory):
        file = directory+'/'+filename
        f = open(file, 'r')
        words = f.read()
        words = words.translate(str.maketrans('', '', string.punctuation))
        tokens = text_cleaning(words)
        for tk in tokens:
            words_list.append(tk)
            if tk in words_dict:
                words_dict[tk] += 1
            else:
                words_dict[tk] = 1

def punctuations(w):
    z = re.sub('\W+', '', w)
   # getting the white space from CRLF prolly not sure
   # z = z.replace(" ", "")
    # z = z.translate(str.maketrans('', '', string.punctuation))
    return z

def text_cleaning(words):
    words = words.lower()
    words = words.split()
    word_token = [punctuations(w) for w in words]
    return word_token

def portStemmer():
    portstem = PorterStemmer()
    for word in words_list:
        if word not in stopwords:
            stem_list.append(portstem.stem(word))
            if portstem.stem(word) in stem_dict:
                stem_dict[portstem.stem(word)] += 1
            else:
                stem_dict[portstem.stem(word)] = 1

def find_stats(val_word_list, count_unique_words_achieved):
    top_20 = []
    unique_count = 0
    counter = 20
    unique_words_achieved = 0
    for w in range(counter):
        print(val_word_list[w])
        if val_word_list[w][0] in stopwords:
            top_20.append(val_word_list[w])

    for w in range(len(val_word_list)):
        if count_unique_words_achieved > unique_words_achieved:
            unique_words_achieved += val_word_list[w][1]
            unique_count += 1
    print("Stop words from the Top 20 words are:")
    
    if top_20:
        for x in top_20:
            print(x)
    else:
        print("Not in top 20. Hence, 0 stopwords")
    print("Words that account for 15% or more of the total number of words: ", unique_count)

stopwords = set(stopwords.words('english'))
words_list = []
words_dict = {}
stem_list = []
stem_dict = {}
file_open()
print("2(a) Total words in the collection: ", len(words_list))
print("2(b) Total vocab. size: ", len(words_dict))

print("2(c) Top 20 words by ranking:")
val_global = sorted(words_dict.items(), key = lambda x:(x[1]), reverse = True)
count_unique_words_achieved = 0.15 * len(words_list)

find_stats(val_global, count_unique_words_achieved)
print("<---------------------------------------------------------------------------------------------------------------------------------------->")
print("Part 3: Integrate a stemmer and stopword")

portStemmer()
print("3(a) Total words in the collection: ", len(stem_list))
print("3(b) Total vocab. size: ", len(stem_dict))
print("3(c) Top 20 words by ranking:")
stem_val_list = sorted(stem_dict.items(), key = lambda x:(x[1]), reverse = True)
count_unique_words_achieved = 0.15*len(stem_list)
find_stats(stem_val_list, count_unique_words_achieved)