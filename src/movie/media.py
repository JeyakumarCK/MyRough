import webbrowser
class Movie():
    
    """This is a document in Movie class """
    
    valid_ratings = ["A", "U", "U/A"]
    
    def __init__(self, movie_title, movie_storyline, poster_link, trailer_link):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_link
        self.trailer_youtube_url = trailer_link
    
    def play_trailer(self):
        if self.trailer_youtube_url is None:
            print "No Trailer You Tube Link available"
        else:
            webbrowser.open(self.trailer_url)
        
    def print_variables(self):
        print "Doc", __doc__
        print "Name", __name__
        if self.__module__ is None: 
            print "Module is none" 
        else:
            print "Module", self.__module__
        #print "Base", self.__base__