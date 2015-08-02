

class Movie():
    '''
    Movie() Class
    Description
        title: The title of the movie
        description: A short description of what the movie is about
        poster_image_url: The URL address of the movie poster
        trailer_youtube_url: A link to a YouTube page

    '''

    def __init__(self, movie_title, description, poster_image, 
    	         trailer_youtube_id):
        '''Method initiates movie constructor'''
        self.title = movie_title
        self.description = description
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_id
