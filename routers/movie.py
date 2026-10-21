from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
import utils.getId as getId

import logging
logger = logging.getLogger(__name__)

from service.movie import MovieService
from dependency import create_movie_service

from models.requests.movies.create_movie import CreateMovieRequest
from models.domain.movies.movie import Movie
from models.response.movies.create_movie import CreateMovieResponse

from exceptions import user_exceptions
from exceptions import movie_exceptions


def createMovieRouter():
    router = APIRouter()

    @router.post("/movie")
    async def create_movie(new_movie_body: CreateMovieRequest, movieService:MovieService = Depends(create_movie_service)):
        new_movie = Movie(id = getId.getRandomId(), 
                          name = new_movie_body.name, 
                          added_by = new_movie_body.user_id,
                          poster= new_movie_body.poster,
                          runtime_in_sec= new_movie_body.runtime_in_sec,
                          release_date= new_movie_body.release_date,
                          details= new_movie_body.details
                          )
        try:
            created_movie = movieService.createMovie(new_movie)
            created_movie_response = CreateMovieResponse.model_validate(created_movie)
            return created_movie_response

        except user_exceptions.UserDoesnotExistException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )

        except user_exceptions.UnauthorizedException as e:
            raise HTTPException(
                status_code= status.HTTP_403_FORBIDDEN,
                detail=str(e)
            )
        
        except Exception as e:
            logger.exception("Unexpected error while updating user")
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    return router


