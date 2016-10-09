from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story", "A story of a boy and his toys comes to life", 
                  "http://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742", 
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar", "A marine in an alien planet", 
                  "https://www.movieposter.com/posters/archive/main/105/MPW-52799", 
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

kaashmora = Movie("Kaashmora", "A supernatural historical thriller in tamil", 
                  "http://g.ahan.in/tamil/Kaashmora161006/Kaashmora-(2).jpg", 
                  "https://youtu.be/AJpED8zJlzo")

force2 = Movie("Force 2", "Indian action thriller movie", 
                  "http://1.bp.blogspot.com/-_S25W5lRsLo/VaI-TO-2poI/AAAAAAAADds/n3Vdr8liwI8/s1600/force-2-2016-movie-poster.jpg", 
                  "https://www.youtube.com/watch?v=r4O4Xec60_k")

movies = [toy_story, avatar, kaashmora, force2]
#fresh_tomatoes.open_movies_page(movies)
force2.print_variables()