
from django.db import models 
from uthdemo.models import ( 
    Address, 
    Cable, 
    Cassette, 
    Ebp, 
    Fiber, 
    Position, 
    Tech_point, 
    Tech_site, 
) 
import uuid 


class Work_order(models.Model): 
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
    ext_code = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    label = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    address = models.ForeignKey( 
        Address, 
        on_delete=models.CASCADE, 
        related_name='work_order_address', 
        blank=True, 
        null=True, 
    ) 
    tech_site = models.ForeignKey( 
        Tech_site, 
        on_delete=models.CASCADE, 
        related_name='work_order_tech_site', 
        blank=True, 
        null=True, 
    ) 
    tech_point = models.ForeignKey( 
        Tech_point, 
        on_delete=models.CASCADE, 
        related_name='work_order_tech_point', 
        blank=True, 
        null=True, 
    ) 
    ebp = models.ForeignKey( 
        Ebp, 
        on_delete=models.CASCADE, 
        related_name='work_order_ebp', 
        blank=True, 
        null=True, 
    ) 
    cassette = models.ForeignKey( 
        Cassette, 
        on_delete=models.CASCADE, 
        related_name='work_order_cassette', 
        blank=True, 
        null=True, 
    ) 
    cable = models.ForeignKey( 
        Cable, 
        on_delete=models.CASCADE, 
        related_name='work_order_cable', 
        blank=True, 
        null=True, 
    ) 
    fiber = models.ForeignKey( 
        Fiber, 
        on_delete=models.CASCADE, 
        related_name='work_order_fiber', 
        blank=True, 
        null=True, 
    ) 
    position = models.ForeignKey( 
        Position, 
        on_delete=models.CASCADE, 
        related_name='work_order_position', 
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
        if self.address.rep: 
            rep = self.address.rep 
        else: 
            rep = '' 
        return f'''{self.uuid} code : {self.racine}{self.id}, 
            adresse : {self.address.number}{rep} {self.address.street_name}, 
            ville : {self.address.zip_code} {self.address.city}, 
            GPS : {self.address.lat} {self.address.lng}. ''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 


