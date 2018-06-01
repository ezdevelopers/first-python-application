import webbrowser

#create the class for movies with __init__ function to accept values when the class
#is instatiated and a show_trailer function to load the trailer of the movie

class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
