#with open("hashtags.txt") as f0: #get the number of tweets
with open("output.txt") as f0: #get the number of all objects
    count=0
    for line in f0.readlines():
        count = count+1
    print count
