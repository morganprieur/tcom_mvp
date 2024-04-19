from django.db import models 
from uthdemo.models import ( 
    Address, 
    Organism, 
) 
import uuid 
from uthdemo.utils.choices import ( 
    OCCUPATION_TYPE, 
    PROPERTY_TYPE, 
    STATE_TYPE, 
    STATUS, 
    TECH_POINT_LOGICAL_TYPE, 
    TECH_POINT_NATURE, 
    TECH_POINT_PHYSICAL_TYPE, 
) 


class Tech_point(models.Model): 
    """ References Address and Organisme """ 
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
    label = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 	
    address = models.ForeignKey( 
        Address, 
        on_delete=models.CASCADE, 
        related_name='tech_point_address', 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    dom_manager = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='tech_point_dom_manager', 
        blank=True, 
        null=True 
    ) 
    dom_owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='tech_point_dom_owner', 
        blank=True, 
        null=True 
    ) 
    owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='tech_point_owner', 
        blank=True, 
        null=True 
    ) 
    manager = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='tech_point_manager', 
        blank=True, 
        null=True 
    ) 
    user = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='tech_point_user', 
        blank=True, 
        null=True 
    ) 
    property_type = models.CharField( 
        max_length=3, 
        choices=PROPERTY_TYPE, 
        blank=True, 
        null=True 
    ) 
    status = models.CharField( 
        max_length=3, 
        choices=STATUS, 
        blank=True, 
        null=True 
    ) 
    state = models.CharField( 
        max_length=3, 
        choices=STATE_TYPE, 
        blank=True, 
        null=True 
    ) 
    physical_type = models.CharField( 
        max_length=1, 
        choices=TECH_POINT_PHYSICAL_TYPE, 
        blank=True, 
        null=True 
    ) 
    logical_type = models.CharField( 
        max_length=1, 
        choices=TECH_POINT_LOGICAL_TYPE, 
        blank=True, 
        null=True 
    ) 
    nature = models.CharField( 
        max_length=20, 
        choices=TECH_POINT_NATURE, 
        db_index=True, 
        blank=True, 
        null=True 
    ) 
    occup = models.CharField( 
        max_length=10, 
        choices=OCCUPATION_TYPE, 
        blank=True, 
        null=True 
    ) 
    comment = models.TextField( 
        blank=True, 
        null=True 
    ) 
    created_at = models.DateField( 
        auto_now_add=True 
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
        return f'''{self.racine}{self.id}, 
        Nature : {self.nature}, 
        Occupation : {self.occup} ''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

