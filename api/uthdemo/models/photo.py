
from django.db import models 

import uuid 


class Photo(models.Model): 

    uuid = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False 
    ) 
    image = models.ImageField( 
        upload_to="uploads/", 
        blank=True, 
        null=True, 
    ) 
    name = models.CharField( 
        max_length=128, 
        blank=True, 
        null=True, 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
    ) 

