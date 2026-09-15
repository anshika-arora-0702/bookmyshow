from fastapi import APIRouter, HTTPException, status, Depends

from exceptions import audi_exceptions

from models.requests.audis.create_audi import CreateAudiRequest
from models.requests.audis.delete_audi import DeleteAudiRequest
from models.requests.audis.fetch_audi import FetchAudiRequest
from models.requests.audis.update_audi import UpdateAudiRequest

from models.domain.audis.audi import Audi

from models.response.audis.create_audi import CreateAudiResponse
from models.response.audis.delete_audi import DeleteAudiResponse
from models.response.audis.fetch_audi import FetchAudiResponse
from models.response.audis.update_audi import UpdateAudiResponse


import utils 

from service.audi import AudiService
from dependency import create_audi_service

def createAudiRouter():
    router = APIRouter()

    @router.post("/createAudi")
    async def create_audi(new_audi_body:CreateAudiRequest, audiService:AudiService = Depends(create_audi_service)):

        new_audi = Audi(id = utils.getRandomId(), 
                        added_by= new_audi_body.user_id, 
                        cinema_id=new_audi_body.cinema_id, 
                        screen_num= new_audi_body.screen_num, 
                        row_count=new_audi_body.row_count, 
                        column_count=new_audi_body.column_count,
                        type=new_audi_body.type
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


    return router

        

