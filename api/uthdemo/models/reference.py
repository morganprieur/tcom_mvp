from django.db import models 
from .organism import Organism 
import uuid 
from uthdemo.utils.choices import REFERENCE_TYPE 


class Reference(models.Model): 
    """ References Organism """ 
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
    type = models.CharField( 
        max_length=2, 
        choices=REFERENCE_TYPE 
    ) 
    manufacturer = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='reference_manufacturer', 
        db_index=True, 
        blank=True, 
        null=True 
    ) 
    model = models.CharField( 
        max_length=254, 
        db_index=True, 
    ) 
    comment = models.TextField( 
        blank=True, 
        null=True 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
    ) 
    updated_at = models.DateField( 
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
        if not self.manufacturer: 
            manufacturer = ''
        else: 
            manufacturer = self.manufacturer 
        return f'''{self.racine}{self.id}, 
            Type : {self.type}, 
            Modèle : {self.model}, 
            Fabricant : {manufacturer} ''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

