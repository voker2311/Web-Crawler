# Web-Crawler
Spider-bot for accessing hidden contents of a website

This is a simple web crawler which I created using python.What exactly is web crawler - So this crawler goes through the entire website and gives us all the links related to that website 
i.e in scope of that website.It is similar to the spider that we use in Burp Suite for accessing hidden directories and files.

There are two types - First the crawler will check for the hidden directories and paths using a wordlist which should be provided by us like subdomains.txt or common.txt.
It will go through each and every file in the wordlist and will give us a specific response.

The second one i.e spider.py will give all the urls which we can manually check for more info.

We can also check for domains by modifying the code.

I used a module named requests for getting the response from the website and also used regular expression to filter out unnecessary data.
