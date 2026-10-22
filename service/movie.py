from models.domain.movies.movie import Movie
class MovieService():

    def __init__(self, movieRepo):
        self.movieRepo = movieRepo

    def createMovie(self, new_movie:Movie):

        if new_movie.id == None:
            raise ValueError("Error in creating movie id")
        
        if new_movie.added_by == None:
            raise ValueError("User id required")
        
        if new_movie.name == None:
            raise ValueError("Movie name required")

        created_movie = self.movieRepo.createMovie(new_movie)
        return created_movie

    def fetchMovie(self, movieId):

        if movieId == None:
            raise ValueError("Movie id required")

        fetched_movie = self.movieRepo.fetchMovie(movieId)

        return fetched_movie

    def deleteMovie(self, movie_to_delete):

        if movie_to_delete.id == None:
            raise ValueError("Movie id required")
        
        if movie_to_delete.user_id == None:
            raise ValueError("User id required")

        deleted_movie = self.movieRepo.deleteMovie(movie_to_delete)

        return deleted_movie

    def updateMovie(self, movie_to_update):

        if movie_to_update.id == None:
            raise ValueError("Movie id required")

        if movie_to_update.user_id == None:
            raise ValueError("User id required")

        updated_movie = self.movieRepo.updateMovie(movie_to_update)

        return updated_movie
