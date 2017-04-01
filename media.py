import webbrowser

#Defines movie class and attributes
class Movie():
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,review_rotten_tomatoes):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rotten_tomatoes_url = review_rotten_tomatoes

#opens youtube video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

#opens rotten tomatoes reviews
    def show_reviews(self):
        webbrowser.open(self.rotten_tomatoes_url)
