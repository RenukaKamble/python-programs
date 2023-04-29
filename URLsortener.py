import pyshorteners 

url=input("Enter the URL:") 

def shortURL(url):
    s=pyshorteners.Shortener()
    print("The short URL:\n",s.tinyurl.short(url)) 
    
shortURL(url) 



