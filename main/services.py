from typing import List, Dict
from main.models import Post


class PostService:
    def get_objects(self) -> List[Post]:
        """Returns a queryset of all Post records in the database"""
        return Post.objects.all()
    
    def get_object_by_id(self, id: int) -> Post:
        """Returns a single Post record by id"""
        return Post.objects.get(id=id)
    
    def create_object(self, **data: Dict) -> Post:
        """Creates a new Post record in the database"""
        return Post.objects.create(**data)
    
    def update_object(self, id: int, **data: Dict) -> Post:
        """Updates an existing Post record in the database"""
        object = Post.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object

    def delete_object(self, id: int) -> None:
        """Deletes an existing Post record in the database"""
        object = Post.objects.get(id=id)
        object.delete()
