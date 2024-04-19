from django.db import models 
from .cable import Cable 
import uuid 
from uthdemo.utils.choices import ( 
    FO_TYPE, 
    FO_COLOR, 
    TUBE, 
    #     CABINET_TYPE, 
    PROPERTY_TYPE, 
    STATE_TYPE, 
    #     STATUS, 
) 

class Fiber(models.Model): 
    """ References Cable """ 
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
    # # obligatoire 
    # code = models.CharField( 
    #     max_length=254, 
    #     null=True, 
    #     blank=True, 
    # ) 
    ext_code = models.CharField( 
        max_length=254, 
        null=True, 
        blank=True, 
    ) 
    # obligatoire 
    cable = models.ForeignKey( 
        Cable, 
        on_delete=models.CASCADE, 
        related_name='fiber_cable', 
    ) 
    # Numéro fibre dans cable 
    num_in_cb = models.IntegerField( 
        null=True, 
        blank=True, 
    ) 
    # Numéro tube 
    tube_num = models.IntegerField( 
        null=True, 
        blank=True, 
    ) 
    # Numéro fibre dans tube 
    num_in_tube = models.IntegerField( 
        null=True, 
        blank=True, 
    ) 
    type = models.CharField( 
        max_length=20, 
        choices=FO_TYPE, 
        blank=True, 
        null=True, 
    ) 
    state = models.CharField( 
        max_length=3, 
        choices=STATE_TYPE, 
        null=True, 
        blank=True, 
    ) 
    color = models.CharField( 
        max_length=10, 
        choices=FO_COLOR, 
        null=True, 
        blank=True, 
    ) 
    caracteristics = models.CharField( 
        max_length=5, 
        choices=TUBE, 
        null=True, 
        blank=True, 
    ) 
    property_type = models.CharField( 
        max_length=3, 
        choices=PROPERTY_TYPE, 
        null=True, 
        blank=True, 
    ) 
    comment = models.TextField( 
        null=True, 
        blank=True, 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
    )	
    updated_at = models.DateField( 
        null=True, 
        blank=True, 
    )	
    archived_at = models.DateField( 
        null=True, 
        blank=True, 
    ) 
    archive_reason = models.CharField( 
        max_length=254, 
        null=True, 
        blank=True, 
    ) 

    def __str__(self) -> str: 
        return f'''{self.racine}{self.id}, 
            Cable : {self.cable.racine}{self.cable.id}, 
            Type : {self.type}, 
            Repérage : {self.caracteristics}, 
            N° dans cable : {self.num_in_cb}, 
            N° du tube : {self.tube_num}
            N° dans tube : {self.num_in_tube} ''' 

    # Metadata
    class Meta:
        ordering = ['created_at'] 



