import utils.getId as getId
from models.response.movies.create_movie import CreateMovieResponse

class Movie:

    def __init__(self, id, name, added_by, poster, runtime_in_sec, release_date, details):

        self.id = id
        self.name = name
        self.added_by = added_by
        self.poster = poster
        self.runtime_in_sec = runtime_in_sec
        self.release_date = release_date
        self.details = details


    def __str__(self):
        return f"{self.id} : {self.name}"

    def to_create_movie_response(self):
        return CreateMovieResponse(id = self.id, name = self.name)