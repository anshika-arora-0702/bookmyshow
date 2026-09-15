from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
import utils

from service.movie import MovieService
from dependency import create_movie_service

from models.requests.movies.create_movie import CreateMovieRequest
from models.domain.movies.movie import Movie



def createMovieRouter():
    router = APIRouter()

    @router.post("/")
    async def create_movie(movie: CreateMovieRequest, movieService:MovieService = Depends(create_movie_service())):
        new_movie = Movie(id = utils.getRandomId(), name = movie.name, added_by= movie.added_by, poster = movie.poster, runtime_in_sec=movie.runtime_in_sec, release_date=movie.release_date, details=movie.details)
        created_movie = movieService.createMovie(new_movie)
        return created_movie.to_create_movie_response()

