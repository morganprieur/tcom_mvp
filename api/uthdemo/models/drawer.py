from django.db import models 
from uthdemo.models import ( 
    Organism, 
    Reference 
) 
import uuid 
from ..utils.choices import ( 
    DRAWER_TYPE, 
    STATE_TYPE, 
    CABINET_FACE, 
) 

# t_tiroir 
class Drawer(models.Model): 
    """ References Organism and Reference table. """ 
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
    ) 
    cabinet = models.CharField( 
        max_length=254, 
        db_index=True, 
        null=True, 
        blank=True, 
    ) 
    owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='drawer_owner', 
        blank=True, 
        null=True, 
    ) 
    state = models.CharField( 
        max_length=3, 
        choices=STATE_TYPE, 
        blank=True, 
        null=True, 
    )  
    type = models.CharField( 
        max_length=10, 
        choices=DRAWER_TYPE, 
        blank=True, 
        null=True, 
    )  
    reference = models.ForeignKey( 
        Reference, 
        on_delete=models.CASCADE, 
        related_name='drawer_reference', 
        db_index=True, 
    )  
    size = models.IntegerField( 
        blank=True, 
        null=True, 
    ) 
    start_u = models.IntegerField( 
        blank=True, 
        null=True, 
    ) 
    cabinet_face = models.CharField( 
        max_length=2, 
        choices=CABINET_FACE 
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
        return f'{self.racine}{self.id}, {self.type}' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

