from django.db import models 
from .address import Address 
from .organism import Organism 
import uuid 
# Choices # chercher comment importer des choices pour plusieurs fichier ### 
from uthdemo.utils.choices import ( 
    PROPERTY_TYPE, 
    SITE_LOGICAL_TYPE, 
    SITE_PHYSICAL_TYPE, 
    STATE_TYPE, 
    STATUS 
) 


class Tech_site(models.Model): 
    """ References Organism and Address """ 
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
    ext_code = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) 
    name = models.CharField( 
        max_length=254, 
        db_index=True, 
    ) 
    owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='tech_site_owner', 
    ) 
    manager = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='tech_site_manager', 
    ) 
    user = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='tech_site_user', 
        blank=True, 
        null=True 
    ) 
    property_type = models.CharField( 
        max_length=3, 
        choices=PROPERTY_TYPE, 
        blank=True, 
        null=True, 
    ) 
    status = models.CharField( 
        max_length=3, 
        choices=STATUS, 
        blank=True, 
        null=True, 
    ) 
    state = models.CharField( 
        max_length=3, 
        choices=STATE_TYPE, 
        blank=True, 
        null=True, 
    ) 
    physical_type = models.CharField( 
        max_length=3, 
        choices=SITE_PHYSICAL_TYPE, 
        blank=True, 
        null=True, 
    ) 
    logical_type = models.CharField( 
        max_length=10, 
        choices=SITE_LOGICAL_TYPE, 
        blank=True, 
        null=True, 
    ) 
    address = models.ForeignKey( 
        Address, 
        on_delete=models.CASCADE, 
        related_name='tech_site_address', 
        db_index=True, 
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
        return f'{self.racine}{self.id}, {self.address} {self.name} {self.property_type}, {self.manager}' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 




