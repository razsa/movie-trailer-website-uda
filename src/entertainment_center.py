import fresh_tomatoes
import media

# This opens the fresh tomatoes application and displays these movies

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/T4dPBt",
                        "https://www.youtube.com/watch?v=CxwTLktovTU")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://goo.gl/HRZL6G",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

the_matrix = media.Movie("The Matrix",
                         "A hacker saves humanity from AI machines.",
                         "https://goo.gl/g2RdoL",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

movies = [toy_story, avatar, the_matrix]

# This function call opens a page of movies generated from the input, an list
# of movie instances.
fresh_tomatoes.open_movies_page(movies)
