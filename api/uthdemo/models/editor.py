from django.db import models 
import uuid 


class Editor(models.Model): 
    """ A user who can send GEt, POST, UPDATE and PUT requests """ 
    uuid = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False 
    ) 
    name = models.CharField( 
        max_length=50, 
        unique=True, 
        blank=True, 
        null=True 
    ) 
    password = models.CharField( 
        max_length=100, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
        blank=True, 
        null=True, 
    ) 
    updated_at = models.DateField( 
        blank=True, 
        null=True, 
    ) 
    archived_at = models.DateField( 
        blank=True, 
        null=True, 
    ) 
    archive_reason = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 

    def __str__(self) -> str: 
        return f'{self.uuid} name : {self.name}' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

