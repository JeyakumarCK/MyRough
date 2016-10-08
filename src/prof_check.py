def read_txt():
    quotefile = open("C:\JK\Udacity\Python\movie_quotes.txt")
    quotetext = quotefile.read()
    print quotetext
    quotefile.close()
    #End of Function
    
read_txt()