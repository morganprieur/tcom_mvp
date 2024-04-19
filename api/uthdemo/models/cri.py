
from django.db import models 
from uthdemo.models import ( 
    Address, 
    Cable, 
    Cassette, 
    Position, 
    Work_order, 
) 
import uuid 


class Cri(models.Model): 
    """ References Address, Document, Ebp and Tech_point models """ 
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
    #     blank=True, 
    #     null=True, 
    # ) 
    ext_code = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    work_order = models.ForeignKey( 
        Work_order, 
        on_delete=models.CASCADE, 
        related_name='cri_work_order', 
        blank=True, 
        null=True, 
    ) 
    comment = models.TextField( 
        blank=True, 
        null=True, 
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
        if self.work_order.address.rep: 
            rep = self.work_order.address.rep 
        else: 
            rep = '' 
        return f'''{self.uuid} code : {self.racine}{self.id}, 
            adresse : {self.work_order.address.number}{rep} {self.work_order.address.street_name}, 
            ville : {self.work_order.address.zip_code} {self.work_order.address.city}, 
            OT : {self.work_order.racine}{self.work_order.id} {self.work_order.label}''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 


