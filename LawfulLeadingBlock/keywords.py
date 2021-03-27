from transcript  import trans
from nltk import tokenize
from operator import itemgetter
import math
#remove stopwords from transcipt to prevent error
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

#READ: Nltk stopwords not working. it doesnt prevent the word "the" and a few other words. Idk why
from gensim.parsing.preprocessing import remove_stopwords


doc = remove_stopwords(trans)
print(doc)

total_words = doc.split()
total_word_length = len(total_words)
#print(total_word_length)

#number of sentences
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
#print(total_sent_len)

#calculates the term frequency score
tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

# Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
#print(tf_score)

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))


idf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word] = 1

# Performing a log and divide
idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

#print(idf_score)


tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
#print(tf_idf_score)

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result


#Gets top 5 most important words
top_5_words = get_top_n(tf_idf_score, 5)




#Google search code
from googlesearch import search

keys =  top_5_words.keys()

list = []
for key in keys:
  list.append(key)

print(list)

#youtube vid search
import urllib.request
import re
import ssl

def searchVideoForKeyword(searchKeyword):
    allvideos = []
    allEmbedLinks = []
    if len(searchKeyword.split(" ")) > 1:
        searchKeyword = searchKeyword.replace(" ", "+")

    searchKeyword = searchKeyword.replace("!web ", "")
    url = "https://www.youtube.com/results?search_query=" + searchKeyword
    gcontext = ssl.SSLContext()
    html = urllib.request.urlopen(url, context=gcontext)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    allvideos.append("https://www.youtube.com/embed/" + video_ids[0])

    return allvideos



#prints top 5 most relevant links for every word in list
# for j in list:
#   for i in search(j,tld= "com", num = 3, stop = 3, pause = 0.5):
#     linked_list = [i]
#     print(linked_list)


# #gives the youtube video link(embed)
# for word in list:
#   youtube_list = [searchVideoForKeyword(word)]
#   print(youtube_list)

# def key_word():
#   for i in range(linked_list,youtube_list):
#     final_dict = {youtube_list[i]: [linked_list[i],linked_list[i],linked_list[i]]}

#{key:[link, link, link], key:[link, link, link]}


def get_keyword():
  dict = {}
  linked_list = []
  for x in list:
    yt = searchVideoForKeyword(x)
    dict[x] = yt 
    
  return dict

