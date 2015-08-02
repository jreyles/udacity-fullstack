import media
import fresh_tomatoes

# Create instances of the Movie class that lists movie trailers

harold_kumar = media.Movie("Harold and Kumar",
                           "A story of two Asian stoners trying to get to White Castle.",
                           "http://www.gstatic.com/tv/thumb/movieposters/34664/p34664_p_v7_aa.jpg",
                           "https://www.youtube.com/watch?v=cwP5E15VzRM")

hitch_hikers = media.Movie("Hitchhiker's Guide to the Galaxy",
                           "A 2005 British-American comic science fiction film",
                           "http://www.gstatic.com/tv/thumb/dvdboxart/35755/p35755_d_v7_aa.jpg",
                           "https://www.youtube.com/watch?v=MbGNcoB2Y4I")

iron_man = media.Movie("Iron Man",
                       "An engineer that saves the world with a suit of armor",
                       "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v7_ah.jpg",
                       "www.youtube.com/watch?v=8hYlB38asDY")

the_dragon = media.Movie("Enter the Dragon",
                         "Bruce Lee avenging the death of his sister and the Shaolin family.",
                         "http://www.dvdsreleasedates.com/covers/"
                         "enter-the-dragon-40th-anniversary-blu-ray-cover-93.jpg",
                         "www.youtube.com/watch?v=tB-QGOChuQc")

matrix = media.Movie("Matrix",
                     "Reality of life as it is.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Add the instances to a list
movies = [
    harold_kumar,
    hitch_hikers,
    iron_man,
    the_dragon,
    matrix
]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
