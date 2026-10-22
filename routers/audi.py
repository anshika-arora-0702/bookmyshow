from fastapi import APIRouter, HTTPException, status, Depends

import logging
logger = logging.getLogger(__name__)

from exceptions import audi_exceptions
from exceptions import user_exceptions

from models.requests.audis.create_audi import CreateAudiRequest
from models.requests.seats.create_seat import CreateSeatRequest

from models.requests.audis.delete_audi import DeleteAudiRequest
from models.requests.audis.fetch_audi import FetchAudiRequest
from models.requests.audis.update_audi import UpdateAudiRequest

from models.domain.audis.audi import Audi
from models.domain.seats.seat import Seat

from models.response.audis.create_audi import CreateAudiResponse
from models.response.seats.create_seat import CreateSeatResponse

from models.response.audis.delete_audi import DeleteAudiResponse
from models.response.audis.fetch_audi import FetchAudiResponse
from models.response.audis.update_audi import UpdateAudiResponse


import utils.getId as getId 

from service.audi import AudiService
from dependency import create_audi_service

def createAudiRouter():
    router = APIRouter()

    @router.post("/createAudi")
    async def create_audi(new_audi_body:CreateAudiRequest, audiService:AudiService = Depends(create_audi_service)):

        new_audi = Audi(id = getId.getRandomId(), 
                        user_id = new_audi_body.user_id, 
                        cinema_id=new_audi_body.cinema_id, 
                        screen_num= new_audi_body.screen_num, 
                        row_count=new_audi_body.row_count, 
                        column_count=new_audi_body.column_count,
                        type=new_audi_body.type,
                        )

        try:
            created_audi = audiService.createAudi(new_audi)
            created_audi_response = CreateAudiResponse.model_validate(created_audi)
            return {"Created Audi" : created_audi_response}

        except audi_exceptions.AudiAlreadyExists as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=str(e)
            )

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
            logger.exception("Unexpected error while updating audi")
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    @router.post("/createSeat")
    async def create_seat(new_seat_body:CreateSeatRequest, audiService:AudiService = Depends(create_audi_service)):

        new_seat = Seat(id = getId.getRandomId(),
            audi_id = new_seat_body.audi_id,
            column_num = new_seat_body.column_num,
            row_char = new_seat_body.row_char,
            type = new_seat_body.type
            )

        user_id = new_seat_body.user_id

        # try:
        created_seat = audiService.createSeat(new_seat, user_id)
        created_seat_response = CreateSeatResponse.model_validate(created_seat)
        return {"Created Seat" : created_seat_response}

        # except audi_exceptions.AudiAlreadyExists as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_409_CONFLICT, 
        #         detail=str(e)
        #     )

        # except user_exceptions.UserDoesnotExistException as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND, 
        #         detail=str(e)
        #     )

        # except user_exceptions.UnauthorizedException as e:
        #     raise HTTPException(
        #         status_code= status.HTTP_403_FORBIDDEN,
        #         detail=str(e)
        #     )

        # except Exception as e:
        #     logger.exception("Unexpected error while updating audi")
        #     raise HTTPException(
        #         status_code= status.HTTP_400_BAD_REQUEST,
        #         detail=str(e)
        #     )
         
    return router

    @router.post("/fetchAudi")
    async def fetch_audi(audi_to_fetch_body:FetchAudiRequest, audiService:AudiService = Depends(create_audi_service)):
        try:
             
            fetched_audi = audiService.fetchAudi(audi_to_fetch_body)
            fetched_audi_response = FetchAudiResponse.model_validate(fetched_audi)
            return {"Fetched Audi" : fetched_audi_response}

        except audi_exceptions.AudiNotFoundException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )

    @router.delete("/deleteAudi")
    async def delete_audi(audi_to_delete_body:DeleteAudiRequest, audiService:AudiService = Depends(create_audi_service)):

            try:
                deleted_audi = audiService.deleteAudi(audi_to_delete_body)
                deleted_audi_response = DeleteAudiResponse.model_validate(deleted_audi)
                return {"Deleted Audi" : deleted_audi_response}
        
            except audi_exceptions.AudiNotFoundException as e:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail=str(e)
                )

    @router.put("/updateAudi")
    async def update_audi(audi_to_update_body:UpdateAudiRequest, audiService:AudiService = Depends(create_audi_service)):

            try:
                updated_audi = audiService.updateAudi(audi_to_update_body)
                updated_audi_response = UpdateAudiResponse.model_validate(updated_audi)
                return {"Updated Audi" : updated_audi_response}
        
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail=str(e)
                )




        

