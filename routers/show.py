from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import UUID4
from utils.getId import getRandomId

import logging
logger = logging.getLogger(__name__)

from exceptions import user_exceptions
from exceptions import show_exceptions
from exceptions import movie_exceptions

from service.show import ShowService
from dependency import create_show_service

from models.requests.shows.create_show import CreateShowRequest
from models.domain.shows.show import Show
from models.response.shows.create_show import CreateShowResponse

def createShowRouter():
    router = APIRouter()

    @router.post("/createShow")
    async def create_show(new_show_body:CreateShowRequest, showService:ShowService = Depends(create_show_service)): 
        new_show = Show(id = getRandomId(),
                            added_by= new_show_body.user_id,
                            audi_id = new_show_body.audi_id,
                            movie_id=new_show_body.movie_id,
                            start_time= new_show_body.start_time,
                            price= new_show_body.price
                            )

        try:
            created_show = showService.createShow(new_show)
            created_show_response =  CreateShowResponse.model_validate(created_show)
            return created_show_response

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

        except show_exceptions.ShowIntegrityException as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(e)
            )

        except movie_exceptions.MovieNotFoundException(new_show.movie_id) as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
        
        except Exception as e:
            logger.exception("Unexpected error while creating show")
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
                 
        
    return router