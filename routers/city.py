from fastapi import APIRouter, HTTPException, status, Depends
from utils import getId

import traceback
import logging
logger = logging.getLogger(__name__)


from exceptions import user_exceptions 

from service.city import CityService
from dependency import create_city_service

from models.requests.city.create_city import CreateCityRequest

from models.domain.city.city import City

from models.response.city.create_city import CreateCityResponse

def createCityRouter():
    router = APIRouter()

    @router.post("/createCity")
    async def create_city(new_city_body:CreateCityRequest, cityService:CityService = Depends(create_city_service)):

        new_city = City(id = None,
                        added_by=new_city_body.user_id,
                        name=new_city_body.name)

        try:
            created_city = cityService.createCity(new_city)
            created_city_response = CreateCityResponse.model_validate(created_city)
            return {"Created City" : created_city_response}

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



