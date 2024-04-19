from django.db import models 
from uthdemo.models import Address 
import uuid 
from uthdemo.utils.choices import SUF_TYPE 

class Suf(models.Model): 
    """ references Address table """ 

    uuid = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False 
    ) 
    racine = models.CharField( 
        max_length=2, 
        db_index=True, 
        blank=True, 
        null=True 
    ) 
    id = models.CharField( 
        max_length=11, 
        db_index=True, 
        blank=True, 
        null=True 
    ) 
    # code = models.CharField( 
    #     max_length=254, 
    #     db_index=True, 
    # ) 
    address = models.ForeignKey( 
        Address, 
        on_delete=models.CASCADE, 
        related_name='suf_address', 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    equipment = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    type = models.CharField( 
        max_length=13, 
        choices=SUF_TYPE, 
        blank=True, 
        null=True, 
    ) 
    comment = models.TextField( 
        blank=True, 
        null=True, 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
    ) 
    updated_at = models.DateField( 
        auto_now_add=True,  
        blank=True, 
        null=True 
    )  
    archived_at = models.DateField( 
        blank=True, 
        null=True 
    ) 
    archive_reason = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) 

    def __str__(self) -> str: 
        return f'''{self.racine}{self.id}, 
        Type : {self.type} 
        Adresse : {self.address}''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 


