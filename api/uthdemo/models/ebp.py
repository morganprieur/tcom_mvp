from django.db import models 
from uthdemo.models import ( 
    Organism, 
    Reference, 
    Tech_point,  
)
import uuid 
from uthdemo.utils.choices import ( 
    EBP_LOGICAL_TYPE, 
    EBP_PHYSICAL_TYPE, 
    OCCUPATION_TYPE, 
    PROPERTY_TYPE, 
    STATE_TYPE, 
    STATUS, 
)


# t_ebp 
class Ebp(models.Model): 
    """ References Organism, Reference, Tech_point """ 
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
    qrcode = models.CharField( 
        max_length=254, 
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
        null=True, 
    ) 
    label = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    tech_point = models.ForeignKey( 
        Tech_point, 
        on_delete=models.CASCADE, 
        related_name='ebp_tech_point', 
        blank=True, 
        null=True, 
    ) 
    owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='ebp_owner', 
    ) 
    manager = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='ebp_manager', 
    ) 
    user = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='ebp_user', 
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
    occup = models.CharField( 
        max_length=10, 
        choices=OCCUPATION_TYPE, 
        blank=True, 
        null=True, 
    ) 
    physical_type = models.CharField( 
        max_length=5, 
        choices=EBP_PHYSICAL_TYPE, 
        blank=True, 
        null=True, 
    ) 
    logical_type = models.CharField( 
        max_length=3, 
        choices=EBP_LOGICAL_TYPE, 
        blank=True, 
        null=True, 
    ) 
    reference = models.ForeignKey( 
        Reference, 
        on_delete=models.CASCADE, 
        related_name='ebp_reference', 
        blank=True, 
        null=True, 
    ) 
    inputs_nb = models.IntegerField( 
        blank=True, 
        null=True, 
    ) 
    cassettes_nb = models.IntegerField( 
        blank=True, 
        null=True, 
    ) 
    steps_nb = models.IntegerField( 
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
        return f'''{self.racine}{self.id}, 
            occupation : {self.occup}, 
            PT : {self.tech_point} '''  

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

