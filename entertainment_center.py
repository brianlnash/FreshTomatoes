import media
import fresh_tomatoes

#Individual movie data (Name, Storyline, Poster, Trailer, Rotten_Tomatoes_Reviews)
ant_man = media.Movie("Ant-Man", "An unlikely superhero",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
                      "https://www.youtube.com/watch?v=pWdKf3MneyI",
                      "https://www.rottentomatoes.com/m/antman/")
lego_batman = media.Movie("The Lego Batman Movie",
                          "Batman takes on his greatest challenge",
                          "https://upload.wikimedia.org/wikipedia/en/6/61/The_Lego_Batman_Movie_PromotionalPoster.jpg",
                          "https://www.youtube.com/watch?v=aBJyp2LFHgk",
                          "https://www.rottentomatoes.com/m/the_lego_batman_movie")
sausage_party = media.Movie("Sausage Party",
                            "Food comes to life",
                            "https://upload.wikimedia.org/wikipedia/en/e/e4/Sausage_Party.png",
                            "https://www.youtube.com/watch?v=c7fP9q_LyDc",
                            "https://www.rottentomatoes.com/m/sausage_party")
transformers = media.Movie("Transformers - The Movie",
                           "Robots In Disguise",
                           "https://upload.wikimedia.org/wikipedia/en/9/91/Transformers-movieposter-west.jpg",
                           "https://www.youtube.com/watch?v=JAzdgNLByjw",
                           "https://www.rottentomatoes.com/m/transformers_the_the_movie")

#List of movies to render
movies = [ant_man, lego_batman, sausage_party, transformers]

#Opens HTML page
fresh_tomatoes.open_movies_page(movies)


