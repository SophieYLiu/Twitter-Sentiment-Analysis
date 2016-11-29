# Twitter Sentiment Analysis Report

<b>1. Programming environment: </b>
Hardware: 
● Operating System: Linux ubuntu 14/04 LTU
Software:
● Libraries:  tweepy - get twitter stream samples
● Tools: collections 

<b>2. Q and A </b>
<t>Q1: How large is the file?</t>
<t>A1: The file is saved as “ouput.txt”. The size is 177.1 MB</t>

<t>Q2: How many objects are in the file?</t>
<t>A2: There are 123,240 objects in total. Run CountObj.py</t>

<t>Q3: How many are tweets?</t>
<t>A3: There are 39,279 are tweets. Run CountObj.py</t>
   <t>By parsing a single tweet, I find 68 items in a tweet. See details in the 3rd item (What is in One Piece) in README.txt</t>

<t>Q4: How many of the tweets have hashtags?</t>
<t>A4: 8363. See details in Parse_n_Filter.py</t>

<t>Q5: What are the 10 most popular hashtags?</t>
<t>A5: See details in top 10.txt</t>
<tab>● KCA 725</tab>
<t>● USAWeaponsKillsYemenis 447</t>
<t>● iHeartAwards 161</t>
<t>● VoteShawnMendes 152</t>
<t>● BestFanArmy 150</t>
<t>● VoteArianaGrande 148</t>
<t>● Oscars 113</t>
<t>● CapitalOneCupFinal 99</t>
<t>● 5SOSFam 96</t>
<t>● mcfc  74</t>

<t>Q6: How does your list compare with the trending hashtags shown on Twitter?</t>
<t>A6:  I have 2 hashtags are the same with the Trend on twitter. See twittertrend from 2016-02-28 11:28:01.png</t>
<t>Trend	My Analysis</t>
<t>Oscars	KCA</t>
<t>CapitalOneCupFinal	USAWeaponsKillsYemenis</t>
<t>RIPKeith	iHeartAwards</t>
<t>SundayFunday	VoteShawnMendes</t>
<t>David Duke	BestFanArmy</t>
<t>Jihadi	VoteArianaGrande</t>
<t>Arsenal	Oscars</t>
<t>Eric Staal	CapitalOneCupFinal</t>
<t>Liverpool	5SOSFam</t>
<t>Coutinho	mcfc</t>


<t>Q7: What is the average sentiment for each hashtag?
<t>A7: See details in scores.txt
<t>●  0.17: ('"KCA"\n', 725)
<t>● -0.04: ('"USAWeaponsKillsYemenis"\n', 447)
<t>● -0.17: ('"iHeartAwards"\n', 161)
<t>●  0.44: ('"VoteShawnMendes"\n', 152)
<t>●  0.40: ('"BestFanArmy"\n', 150)
<t>●  0.41: ('"VoteArianaGrande"\n', 148)
<t>●  0.79: ('"Oscars"\n', 113)
<t>●  1.47: ('"CapitalOneCupFinal"\n', 99)
<t>●  1.43: ('"5SOSFam"\n', 96)
<t>●  2.14: ('"mcfc"\n', 74)


<t>Q8: What are the most positive and most negative of the popular hashtags?
<t>A8: From the above list, we can see the most positive hashag is “mcfc” and the most negative is “iHeartAwards”

