import webbrowser
class Video():
    """
    This class is a parent of the class Movie, and 
    will be a parent of some more classes once created in the future.
    This time, it is just for my own practice.
    """

    def __init__(self, movie_title, director_name):
        self.title = movie_title
        self.director = director_name

class Movie(Video):
    """
    This class is inherited by the class Video, and 
    provides a way to store movie related information
    """
    
    def __init__(self, movie_title, director_name, movie_storyline, poster_image,
        trailer_youtube):
        """This function defines instance variables"""

        Video.__init__(self, movie_title, director_name)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function defines instance methods"""

        webbrowser.open(self.trailer_youtube_url)

