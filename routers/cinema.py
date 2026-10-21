from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import UUID4
from utils import getId

import traceback
import logging
logger = logging.getLogger(__name__)


from exceptions import user_exceptions
import utils.getId as getId 

from service.cinema import CinemaService
from dependency import create_cinema_service

from models.requests.city.create_city import CreateCityRequest
from models.requests.city.update_city import UpdateCityRequest

from models.requests.cinemas.create_cinema import CreateCinemaRequest

from models.domain.city.city import City
from models.domain.cinemas.cinema import Cinema

from models.response.city.create_city import CreateCityResponse
from models.response.cinemas.create_cinema import CreateCinemaResponse



def createCinemaRouter():
    router = APIRouter()

    @router.post("/createCinema")
    async def create_cinema(new_cinema_body:CreateCinemaRequest, cinemaService:CinemaService = Depends(create_cinema_service)): 
        new_cinema = Cinema(id = getId.getRandomId(),
                            added_by= new_cinema_body.user_id,
                            name = new_cinema_body.name,
                            address=new_cinema_body.address,
                            city = new_cinema_body.city)

        try:
            created_cinema = cinemaService.createCinema(new_cinema)
            created_cinema_response =  CreateCinemaResponse.model_validate(created_cinema)
            return created_cinema_response



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



