from typing import List, Dict
from user.models import User


class UserService:
    def get_objects(self) -> List[User]:
        """Returns a queryset of all User records in the database"""
        return User.objects.all()
    
    def get_object_by_id(self, id: int) -> User:
        """Returns a single User record by id"""
        return User.objects.get(id=id)
    
    def update_object(self, id: int, **data: Dict) -> User:
        """Updates an existing User record in the database"""
        object = User.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object
