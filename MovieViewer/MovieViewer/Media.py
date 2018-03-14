import webbrowser

class Media():
    """description of class"""
    def __init__(self, movieTitle=None, movieStory=None, posterImage=None, trailer=None):
        self.title = movieTitle
        self.story = movieStory
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer
        #print self.title, self.story

    def showTrailer(self):
        webbrowser.open(self.trailerUrl)
