README.txt

Elizabeth Chabot

INSTRUCTIONS FOR APPLICATION
_____________________________________________________________________________________________________

1) Set up a Twitter application:  https://apps.twitter.com/. 
	-Click on Create New App in the top righthand corner of the page 
	-Fill in all required information for Create an application  
	-Create Access Token
	-Make note of your Consumer Key, Consumer Secret, Access Token and Access Token Secret

2) Spin up AWS EC2 Instance (c3.large tested) with image ami-d4dd4ec3

3) Login to the instance via ssh 

4) git clone Ex2

5) Edit and add twitter credentials to tweets.py
	- HINT($ vi tweets.py, then i to edit text)

6) psql -U postrgres (if no database or table made)

7) CREATE DATABASE tcount;

8) \c tcount (to enter database)

9) CREATE TABLE tweetwordcount (word TEXT NOT NULL, count INT NOT NULL);

10) \dt (to check that table made)

11) cd Ex2

12) sparse run 
		- will run application
13) To exit Ctrl-C

14) Check that data stored - psql -U postrgres, \c tcount, SELECT * FROM tweetwordcount LIMIT 10;

15) cd Ex2/serve

16) python finalres.py <word of interest>

17) python finalresults.py (to see all wordcounts)

18) python hist.py 3,6 (must enter in two numbers)

19) If Error = [Thread-20-tweet-spout] INFO  backtype.storm.spout.ShellSpout - ShellLog pid:5839, name:tweet-spout Empty queue exception , Run this to fix it: kill -9 `ps -ef | grep streamparse | grep -v grep | awk '{print $2}'`
