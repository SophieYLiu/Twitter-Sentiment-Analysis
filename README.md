Twitter Sentiment Analysis Report
=====================
Get twitter stream (samples not status) at 11:29 AM - 11:34 AM on 2/28/2016

Programming environment
----------------
- Operating System: Linux ubuntu 14/04
- Libraries: tweepy - get twitter stream samples
- Tools: collections

Q & A 
----------------

<p>Q1: How large is the file?</p>
<p>A1: The file is saved as “ouput.txt”. The size is 177.1 MB</p>

<p>Q2: How many objects are in the file?</p>
<p>A2: There are 123,240 objects in total. Run CountObj.py</p>

<p>Q3: How many are tweets?</p>
<p>A3: There are 39,279 are tweets. Run CountObj.py
     By parsing a single tweet, I find 68 items in a tweet. See details in the 3rd item (What is in One Piece) in README.txt</p>

<p>Q4: How many of the tweets have hashtags?</p>
<p>A4: 8363. See details in Parse_n_Filter.py</p>

<p>Q5: What are the 10 most popular hashtags?</p>
<p>A5: See details in top 10.txt</p>
-  KCA 725
-  USAWeaponsKillsYemenis 447
-  iHeartAwards 161
-  VoteShawnMendes 152
-  BestFanArmy 150
-  VoteArianaGrande 148
-  Oscars 113
-  CapitalOneCupFinal 99
-  5SOSFam 96
-  mcfc  74

<p>Q6: How does your list compare with the trending hashtags shown on Twitter?</p>
<p>A6: I have 2 hashtags are the same with the Trend on twitter. See twittertrend from 2016-02-28 11:28:01.png</p>
-  Trend	My Analysis
-  Oscars	KCA
-  CapitalOneCupFinal	USAWeaponsKillsYemenis
-  RIPKeith	iHeartAwards
-  SundayFunday	VoteShawnMendes
-  David Duke	BestFanArmy
-  Jihadi	VoteArianaGrande
-  Arsenal	Oscars
-  Eric Staal	CapitalOneCupFinal
-  Liverpool	5SOSFam
-  Coutinho	mcfc


<p>Q7: What is the average sentiment for each hashtag?</p>
<p>A7: See details in scores.txt</p>
-  0.17: ('"KCA"\n', 725)
-  -0.04: ('"USAWeaponsKillsYemenis"\n', 447)
-  -0.17: ('"iHeartAwards"\n', 161)
-  0.44: ('"VoteShawnMendes"\n', 152)
-  0.40: ('"BestFanArmy"\n', 150)
-  0.41: ('"VoteArianaGrande"\n', 148)
-  0.79: ('"Oscars"\n', 113)
-  1.47: ('"CapitalOneCupFinal"\n', 99)
-  1.43: ('"5SOSFam"\n', 96)
-  2.14: ('"mcfc"\n', 74)

<p>Q8: What are the most positive and most negative of the popular hashtags?</p>
<p>A8: From the above list, we can see the most positive hashag is “mcfc” and the most negative is “iHeartAwards”</p>

