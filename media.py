import webbrowser


class Movie():
    """Creates a Movie object with basic movie information

    Requires:
        webbrowser

    Attributes:
        title: A string with the movie title
        storyline: A string of the short synopsis of the movie
        poster_image_url: A string with the url of the movie's poster image
        trailer_youtube_url: A string with the url of the movie's trailer
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """The Movie contructor"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Performs a webbrowser.open of the object's trailer_youtube_url"""
        webbrowser.open(self.trailer_youtube_url)
