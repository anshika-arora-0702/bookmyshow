from models.database.users.user_role import UserRole
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

        created_user = self.userRepo.createUser(new_user)
        return created_user
    
    def createAdmin(self, new_admin, created_by):

        if new_admin.id == None:
            raise ValueError("Error in creating user id")
        
        if new_admin.first_name == None:
            raise ValueError("User First Name required")
        
        if new_admin.phone == None:
            raise ValueError("User phone number required")
        
        if created_by == None:
            raise ValueError("Created by id required")

        created_user = self.userRepo.createAdmin(new_admin  , created_by)
        return created_user
    
    def createSuperAdmin(self, new_super_admin, created_by):

        if new_super_admin.id == None:
            raise ValueError("Error in creating user id")
        
        if new_super_admin.first_name == None:
            raise ValueError("User First Name required")
        
        if new_super_admin.phone == None:
            raise ValueError("User phone number required")
        
        if created_by == None:
            raise ValueError("Created by id required")

        created_user = self.userRepo.createAdmin(new_super_admin  , created_by)
        return created_user

    def fetchUser(self, user_to_be_fetched):

        if user_to_be_fetched.id == None:
            raise ValueError("User id required")

        if user_to_be_fetched.fetched_by_id == None:
            raise ValueError("Fetched by id required")

        fetched_user = self.userRepo.fetchUser(user_to_be_fetched)

        return fetched_user

    def delete(self, user_to_delete):

        if user_to_delete.id == None:
            raise ValueError("Id required")
        
        if user_to_delete.deleted_by_id == None:
            raise ValueError("Deleted by id is required")

        deleted_user = self.userRepo.deleteUser(user_to_delete)

        return deleted_user

    def updateUser(self, user_to_update):

        if user_to_update.id == None:
            raise ValueError("Id required")

        if user_to_update.updated_by_id == None:
            raise ValueError("Updated by id is required")

        updated_user = self.userRepo.updateUser(user_to_update)

        return updated_user
