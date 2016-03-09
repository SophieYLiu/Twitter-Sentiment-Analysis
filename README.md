# Twitter Sentiment Analysis Report
1.	Programming environment: 
●	Hardware: 
●	Operating System: Linux ubuntu 14/04 LTU
      2. 
●	Libraries:  tweepy - get twitter stream samples
●	Tools: collections 
      3. Q and A
Q1: How large is the file?
A1: The file is saved as “ouput.txt”. The size is 177.1 MB

Q2: How many objects are in the file?
A2: There are 123,240 objects in total. Run CountObj.py

Q3: How many are tweets?
A3: There are 39,279 are tweets. Run CountObj.py
       By parsing a single tweet, I find 68 items in a tweet. See details in the 3rd item (What is in One Piece) in README.txt

Q4: How many of the tweets have hashtags?
A4: 8363. See details in Parse_n_Filter.py

Q5: What are the 10 most popular hashtags?
A5: See details in top 10.txt
●	KCA 725
●	USAWeaponsKillsYemenis 447
●	iHeartAwards 161
●	VoteShawnMendes 152
●	BestFanArmy 150
●	VoteArianaGrande 148
●	Oscars 113
●	CapitalOneCupFinal 99
●	5SOSFam 96
●	mcfc  74

Q6: How does your list compare with the trending hashtags shown on Twitter?
A6:  I have 2 hashtags are the same with the Trend on twitter. See twittertrend from 2016-02-28 11:28:01.png
Trend	My Analysis
Oscars	KCA
CapitalOneCupFinal	USAWeaponsKillsYemenis
RIPKeith	iHeartAwards
SundayFunday	VoteShawnMendes
David Duke	BestFanArmy
Jihadi	VoteArianaGrande
Arsenal	Oscars
Eric Staal	CapitalOneCupFinal
Liverpool	5SOSFam
Coutinho	mcfc


Q7: What is the average sentiment for each hashtag?
A7: See details in scores.txt
●	  0.17: ('"KCA"\n', 725)
●	 -0.04: ('"USAWeaponsKillsYemenis"\n', 447)
●	 -0.17: ('"iHeartAwards"\n', 161)
●	  0.44: ('"VoteShawnMendes"\n', 152)
●	  0.40: ('"BestFanArmy"\n', 150)
●	  0.41: ('"VoteArianaGrande"\n', 148)
●	  0.79: ('"Oscars"\n', 113)
●	  1.47: ('"CapitalOneCupFinal"\n', 99)
●	  1.43: ('"5SOSFam"\n', 96)
●	  2.14: ('"mcfc"\n', 74)


Q8: What are the most positive and most negative of the popular hashtags?
A8: From the above list, we can see the most positive hashag is “mcfc” and the most negative is “iHeartAwards”

