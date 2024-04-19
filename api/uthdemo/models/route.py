from django.db import models 
from uthdemo.models import Organism, Tech_point
import uuid 
from uthdemo.utils.choices import ( 
    IMPLANTATION_TYPE, 
    INFRA_NATURE, 
    INFRA_LOGICAL_TYPE, 
    INSTALLATION_METHOD, 
    STATE_TYPE, 
    WAY_TYPE, 
)


class Route(models.Model):  # voir cddispo 
    """ References Tech_point, Organism """ 
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
    tech_point_start = models.ForeignKey( 
        Tech_point, 
        on_delete=models.CASCADE, 
        related_name='route_tech_point_start', 
        blank=True, 
        null=True 
    )  
    tech_point_end = models.ForeignKey( 
        Tech_point, 
        on_delete=models.CASCADE, 
        related_name='route_tech_point_end', 
        blank=True, 
        null=True 
    ) 
    street_name = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    )  
    dom_manager = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='route_dom_manager', 
        blank=True, 
        null=True 
    )  
    dom_owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        related_name='route_dom_owner', 
        blank=True, 
        null=True 
    ) 
    state = models.CharField( 
        max_length=2, 
        choices=STATE_TYPE, 
        blank=True, 
        null=True 
    )  
    logical_type = models.CharField( 
        max_length=2, 
        choices=INFRA_LOGICAL_TYPE, 
        blank=True, 
        null=True 
    ) 
    install_type = models.CharField( 
        max_length=2, 
        choices=IMPLANTATION_TYPE, 
        blank=True, 
        null=True 
    )  
    nature = models.CharField( 
        max_length=3, 
        choices=INFRA_NATURE, 
        blank=True, 
        null=True 
    ) 
    """ 
    composition = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) """ 
    pipe_available = models.BooleanField( 
        default=True, 
    ) 
    install_method = models.CharField( 
        max_length=20, 
        choices=INSTALLATION_METHOD, 
        blank=True, 
        null=True 
    )  
    way = models.CharField( 
        max_length=254, 
        choices=WAY_TYPE, 
        blank=True, 
        null=True 
    ) 
    """ 
    length = models.FloatField(  # NUMERIC(8,2) 
        blank=True, 
        null=True 
    )  
    actual_length = models.FloatField(  # NUMERIC(8,2) 
        blank=True, 
        null=True 
    ) """ 
    comment = models.TextField( 
        blank=True, 
        null=True 
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
            rue : {self.street_name}, conduite disponible : {self.pipe_available}''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

