
from django.db import models 
from uthdemo.models import ( 
    Ebp, 
    Reference, 
    Drawer 
) 
from uthdemo.utils.choices import ( 
    CASSETTE_TYPE
) 
import uuid 


class Cassette(models.Model): 
    """ References Ebp, Reference and Drawer models """ 
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
    num = models.IntegerField( 
        blank=True, 
        null=True, 
    ) 
    type = models.CharField( 
        max_length=1, 
        choices=CASSETTE_TYPE, 
        blank=True, 
        null=True, 
    ) 
    ebp = models.ForeignKey( 
        Ebp, 
        on_delete=models.CASCADE, 
        related_name='cassette_ebp', 
        blank=True, 
        null=True, 
    ) 
    ebp_face = models.CharField( 
        max_length=20, 
        blank=True, 
        null=True, 
    ) 
    reference = models.ForeignKey( 
        Reference, 
        on_delete=models.CASCADE, 
        related_name='cassette_reference', 
        blank=True, 
        null=True, 
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
        return f'''{self.racine}{self.id}, ref : {self.reference}, 
            EBP : {self.ebp} ''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

