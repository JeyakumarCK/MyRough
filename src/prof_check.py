import urllib

def read_txt():
    quotefile = open("C:\JK\Udacity\Python\movie_quotes.txt")
    quotetext = quotefile.read()
    print quotetext
    quotefile.close()
    check_profanity(quotetext)
    #End of Function
    
def check_profanity(test_text):
    conn = urllib.urlopen('http://www.wdylike.appspot.com/?q='+test_text)
    res = conn.read()
    print res
    if "true" in res:
        print "Profanity Alert: There is a curse word"
    else:
        print "You are all good"
    conn.close()
    #End of function
    
read_txt()