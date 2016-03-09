import json                                                        

f1 = open("Harray.txt", "w")
f2 = open("Tarray.txt", "w")

counth = 0 #counter to see how many tweets has hashtags    
with open("hashtags.txt") as f0:
    for line in f0.readlines():
        hdict = json.loads(line) #get a dict
        
        h = hdict['entities']['hashtags'] # this is for all the hashtags, a type of list of dict
        t = json.dumps(hdict['text']) # this is for all the texts, a type of string
        

       # we do this to make hashtag and text are having the same index in their arrays 
        if h: #if a is not empty
           counth = counth+1
           for i in range(len(h)):  #some of the list of a has more than 1 hashtags. so we do a loop here
              htext = json.dumps(h[i]['text'])  #h[i] is a type of dict
              #write hashtag texts in file
              f1.write(htext)
              f1.write('\n')
              
              #write 
              f2.write(t)
              f2.write('\n')
print counth

f0.close()
f1.close()
f2.close()
