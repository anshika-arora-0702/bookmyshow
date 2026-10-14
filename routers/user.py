from fastapi import APIRouter, HTTPException, status, Depends

from exceptions import user_exceptions

from models.requests.users.create_user import CreateUserRequest
from models.requests.users.create_admin import CreateAdminRequest
from models.requests.users.create_super_admin import CreateSuperAdminRequest
from models.requests.users.delete_user import DeleteUserRequest
from models.requests.users.fetch_user import FetchUserRequest

from models.domain.users.user import User
from models.database.users.user_role import UserRole

from models.response.users.create_user import CreateUserResponse
from models.response.users.delete_user import DeleteUserResponse

import utils 

from service.user import UserService
from dependency import create_user_service

import traceback


def createUserRouter():
    router = APIRouter()

    @router.post("/createUser")
    async def create_user(new_user_body:CreateUserRequest, userService:UserService = Depends(create_user_service)):

        new_user = User(id = utils.getRandomId(),
                        first_name= new_user_body.first_name,
                        last_name= new_user_body.last_name,
                        role = UserRole.USER,
                        phone = new_user_body.phone,
                        email= new_user_body.email,
                        dob= new_user_body.dob
                        )

        try:
            created_user = userService.createUser(new_user)
            created_user_response = CreateUserResponse.model_validate(created_user)
            return {"Created User" : created_user_response}

        except Exception as e:
            # print(f"error while creating user: {e}")
            # traceback.print_exc()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=str(e)
            )

    @router.post("/createAdmin")
    async def create_admin(new_admin_body:CreateAdminRequest, userService:UserService = Depends(create_user_service)):

        new_user = User(id = utils.getRandomId(),
                        first_name= new_admin_body.first_name,
                        last_name= new_admin_body.last_name,
                        role = UserRole.ADMIN,
                        phone = new_admin_body.phone,
                        email= new_admin_body.email,
                        dob= new_admin_body.dob
                        )

        try:
            created_admin = userService.createAdmin(new_user, new_admin_body.created_by)
            created_admin_response = CreateUserResponse.model_validate(created_admin)
            return {"Created Admin" : created_admin_response}

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=str(e)
            )

    @router.post("/createSuperAdmin")
    async def create_super_admin(new_super_admin_body:CreateSuperAdminRequest, userService:UserService = Depends(create_user_service)):

        new_user = User(id = utils.getRandomId(),
                        first_name= new_super_admin_body.first_name,
                        last_name= new_super_admin_body.last_name,
                        role = UserRole.SUPER_ADMIN,
                        phone = new_super_admin_body.phone,
                        email= new_super_admin_body.email,
                        dob= new_super_admin_body.dob
                        )

        try:
            created_super_admin = userService.createSuperAdmin(new_user, new_super_admin_body.created_by)
            created_super_admin_response = CreateUserResponse.model_validate(created_super_admin)
            return {"Created Super Admin" : created_super_admin_response}

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=str(e)
            )

    @router.post("/fetchUser")
    async def fetch_user(user_to_fetch_body:FetchUserRequest, userService:UserService = Depends(create_user_service)):
        pass
    return router

        

