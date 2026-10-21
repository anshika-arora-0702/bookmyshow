from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import UUID4
from models.database.users.user_role import UserRole

import logging
logger = logging.getLogger(__name__)

from exceptions import user_exceptions

from models.requests.users.create_user import CreateUserRequest
from models.requests.users.update_role import UpdateRoleRequest
from models.requests.users.delete_user import DeleteUserRequest
from models.requests.users.fetch_user import FetchUserRequest
from models.requests.users.update_user import UpdateUserRequest

from models.domain.users.user import User
from models.database.users.user_role import UserRole

from models.response.users.create_user import CreateUserResponse
from models.response.users.delete_user import DeleteUserResponse
from models.response.users.fetch_user import FetchUserResponse
from models.response.users.update_user import UpdateUserResponse

import utils.getId as getId 

from service.user import UserService
from dependency import create_user_service

import traceback


def createUserRouter():
    router = APIRouter()

    @router.post("/createUser")
    async def create_user(new_user_body:CreateUserRequest, userService:UserService = Depends(create_user_service)):

        new_user = User(id = getId.getRandomId(),
                        first_name= new_user_body.first_name,
                        last_name= new_user_body.last_name,
                        phone = new_user_body.phone,
                        email= new_user_body.email,
                        dob= new_user_body.dob,
                        password = new_user_body.password,
                        role = UserRole.USER
                        )

        try:
            created_user = userService.createUser(new_user)
            created_user_response = CreateUserResponse.model_validate(created_user)
            return {"Created User" : created_user_response}

        except Exception as e:
            traceback.print_exc()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=str(e)
            )

    @router.patch("/updateRole")
    async def update_role(update_role_body:UpdateRoleRequest, new_role : UserRole, userService:UserService = Depends(create_user_service)):


        if new_role is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = "No role defined"
            )

        try:
            updated_user = userService.updateRole(update_role_body, new_role)
            updated_user_response = UpdateUserResponse.model_validate(updated_user)
            return {"Updated User" : updated_user_response}

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

        except Exception :
            logger.exception("Unexpected error while updating user")
            raise

    @router.post("/fetchUser")
    async def fetch_user(user_to_fetch_body:FetchUserRequest, userService:UserService = Depends(create_user_service)):
        try:
             
            fetched_user = userService.fetchUser(user_to_fetch_body)
            fetched_user_response = FetchUserResponse.model_validate(fetched_user)
            return {"Fetched User" : fetched_user_response}

        except user_exceptions.UserDoesnotExistException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )

    @router.delete("/deleteUser")
    async def delete_user(user_to_delete_body:DeleteUserRequest, userService:UserService = Depends(create_user_service)):
        try:
             
            deleted_user = userService.deleteUser(user_to_delete_body)
            deleted_user_response = DeleteUserResponse.model_validate(deleted_user)
            return {"Deleted User" : deleted_user_response}

        except user_exceptions.UserDoesnotExistException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )

    @router.patch("/updateUser")
    async def update_user(user_to_update_body:UpdateUserRequest, updated_by:UUID4, userService:UserService = Depends(create_user_service)):
        changes = user_to_update_body.model_dump(exclude_unset=True, exclude={"id"})

        if not changes:
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail= "No field to update"
            )

        non_nullable_fields = {"first_name", "phone"}

        for field, value in changes.items():
            if field in non_nullable_fields and value is None:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                    detail=f"{field} cannot be null"
                )

        try:
            updated_user = userService.updateUser(user_to_update_body.id,updated_by, changes)
            updated_user_response = UpdateUserResponse.model_validate(updated_user)
            return {"Updated User" : updated_user_response}

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

        except Exception :
            logger.exception("Unexpected error while updating user")
            raise
        
    return router

        

