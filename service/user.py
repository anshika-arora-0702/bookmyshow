from utils.password import hash_password

class UserService():

    def __init__(self, userRepo):
        self.userRepo = userRepo

    def createUser(self, new_user):

        if new_user.id == None:
            raise ValueError("Error in creating user id")
        
        if new_user.first_name == None:
            raise ValueError("User First Name required")
        
        if new_user.phone == None:
            raise ValueError("User phone number required")
        
        if new_user.password == None:
            raise ValueError("User password required")

        hashed_password = hash_password(new_user.password)
        new_user.password = hashed_password

        created_user = self.userRepo.createUser(new_user)
        return created_user

    def fetchUser(self, user_to_fetch):

        if user_to_fetch.id == None:
            raise ValueError("User id required")

        if user_to_fetch.fetched_by == None:
            raise ValueError("Fetched by id required")

        fetched_user = self.userRepo.fetchUser(user_to_fetch)

        return fetched_user

    def deleteUser(self, user_to_delete):

        if user_to_delete.id == None:
            raise ValueError("Id required")
        
        if user_to_delete.deleted_by == None:
            raise ValueError("Deleted by id is required")

        deleted_user = self.userRepo.deleteUser(user_to_delete)

        return deleted_user

    def updateUser(self, user_id, updated_by, changes):

        if not changes:
            raise ValueError("No field to update")

        if user_id == None:
            raise ValueError("Id required")

        if updated_by == None:
            raise ValueError("Updated by id is required")

        updated_user = self.userRepo.updateUser(user_id, updated_by, changes)

        return updated_user
    
    def updateRole(self, user_to_update_body, new_role):

        if not new_role:
            raise ValueError("No role provided")

        if user_to_update_body.id == None:
            raise ValueError("Id required")

        if user_to_update_body.updated_by == None:
            raise ValueError("Updated by id is required")
    

        updated_user = self.userRepo.updateRole(user_to_update_body.id, user_to_update_body.updated_by, new_role)

        return updated_user
