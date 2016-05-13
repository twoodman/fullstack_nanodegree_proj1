import webbrowser #importing webbrowser module from python standard library

#creating Movie class
class Movie():
    #defining the 'init' function that runs when we use the Movie class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #assigning parameter values to 'self' variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #defining the 'show_trailer' function, which opens the default browser to the youtube link specified
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
