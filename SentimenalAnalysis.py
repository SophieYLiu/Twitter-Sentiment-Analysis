import math
import re
import sys
reload(sys)
from collections import Counter
sys.setdefaultencoding('utf-8')

# create 2 empty lists for hashtag and text that contains that hashtag
H = [] 
T = []

#a list of 10 lists because we need top 10 popular hashtags, each contains all the texts that contain the hashtag
HashtagText = [None]*10 
for i in range(10):
   HashtagText[i] = []

#open and read files contain all the hashtags and texts from the twitter stream we caputred
with open("Harray.txt") as f:
    for line in f.readlines():
        H.append(line) 

f.close()

with open("Tarray.txt") as f:
    for line in f.readlines():
        T.append(line)

f.close()
#get TOP 10 popular hashtags
c = Counter(H)
tops = c.most_common(10)
print "======================================== TOP 10 HASHTAGS ============================================"
print tops

#find all the texts for each top 10 hashtags, store in HashtagText array whose size was declared as 10
for i in range(10):
   for k in range(len(H)):
       if H[k] == tops[i][0]:
          HashtagText[i].append(T[k])


########################################## SENTIMENTAL SCORING ON TOP 10 HASHTAGS ########################################################

# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = 'AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))

# Word splitter pattern
pattern_split = re.compile(r"\W+")

def sentiment(text):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        
    else:
        sentiment = 0
    return sentiment

print "=========================================== SCORES BREAKDOWN =========================================="
score = 0
if __name__ == '__main__':
    
    for i in range(10):
        for text in HashtagText[i]:
          score += sentiment(text)
          
        print("%6.2f: %s" %(score/len(HashtagText[i]), tops[i]))
