from typing import List, Dict
from main.models import Post, Comment, Report


class PostService:
    def get_objects(self) -> List[Post]:
        """Returns a queryset of all Post records in the database"""
        return Post.objects.all()
    
    def filter_objects(self, author_id: int) -> List[Post]:
        """Returns a queryset of filtered Post records in the database"""
        return Post.objects.filter(author_id=author_id)
    
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


class CommentService:
    def get_objects(self) -> List[Comment]:
        """Returns a queryset of all Comment records in the database"""
        return Comment.objects.all()
    
    def filter_objects(self, **data: Dict) -> List[Comment]:
        """Returns a queryset of filtered Comment records in the database"""
        return Comment.objects.filter(**data)

    def get_object_by_id(self, id: int) -> Comment:
        """Returns a single Comment record by id"""
        return Comment.objects.get(id=id)
    
    def create_object(self, **data: Dict) -> Comment:
        """Creates a new Comment record in the database"""
        return Comment.objects.create(**data)
    
    def update_object(self, id: int, **data: Dict) -> Comment:
        """Updates an existing Comment record in the database"""
        object = Comment.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object

    def delete_object(self, id: int) -> None:
        """Deletes an existing Comment record in the database"""
        object = Comment.objects.get(id=id)
        object.delete()


class ReportService:
    def get_objects(self) -> List[Report]:
        """Returns a queryset of all Report records in the database"""
        return Report.objects.all()
    
    def filter_objects(self, **data: Dict) -> List[Report]:
        """Returns a queryset of filtered Report records in the database"""
        return Report.objects.filter(**data)

    def get_object_by_id(self, id: int) -> Report:
        """Returns a single Report record by id"""
        return Report.objects.get(id=id)
    
    def create_object(self, **data: Dict) -> Report:
        """Creates a new Report record in the database"""
        return Report.objects.create(**data)
    
    def update_object(self, id: int, **data: Dict) -> Report:
        """Updates an existing Report record in the database"""
        object = Report.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object

    def delete_object(self, id: int) -> None:
        """Deletes an existing Report record in the database"""
        object = Report.objects.get(id=id)
        object.delete()
