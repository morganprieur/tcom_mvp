from django.db import models 
from uthdemo.models import ( 
    Drawer, 
    Ebp, 
    Organism, 
    Reference 
) 
import uuid 
from uthdemo.utils.choices import ( 
    INFRA_LOGICAL_TYPE, 
    STATE_TYPE,  
    TECHNOLOGY_TYPE, 
    CABLE_ALIM_TYPE,  
    CABLE_TYPE, 
    REFERENCE_TYPE, 
) 

class Cable(models.Model): 
    """ Reference Organism, Reference, Ebp, Drawer tables """ 
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
        null=True, 
    ) 
    label = models.CharField( 
        max_length=254, 
        db_index=True, 
        null=True, 
    ) 
    owner = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='cable_owner', 
    ) 
    manager = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='cable_manager' 
    ) 
    user = models.ForeignKey( 
        Organism, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='cable_user' 
    ) 
    state = models.CharField( 
        max_length=3, 
        choices=STATE_TYPE, 
        blank=True, 
        null=True, 
    ) 
    type = models.CharField( 
        max_length=3, 
        choices=TECHNOLOGY_TYPE, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    physical_type = models.CharField( 
        max_length=1, 
        choices=CABLE_TYPE, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    reference = models.ForeignKey( 
        Reference, 
        on_delete=models.CASCADE, 
        related_name='cable_reference', 
        blank=True, 
        null=True, 
    ) 
    supply_type = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
        choices=CABLE_ALIM_TYPE 
    ) 
    diameter = models.FloatField( 
        blank=True, 
        null=True, 
    ) 
    color = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    length = models.FloatField( 
        blank=True, 
        null=True, 
    ) 
    actual_length = models.FloatField( 
        blank=True, 
        null=True, 
    ) 
    # A améliorer (4 champs) : 
    ebp_start = models.ForeignKey( 
        Ebp, 
        on_delete=models.CASCADE, 
        related_name='cable_ebp_start', 
        blank=True, 
        null=True, 
    ) 
    ebp_end = models.ForeignKey( 
        Ebp, 
        on_delete=models.CASCADE, 
        related_name='cable_ebp_end', 
        blank=True, 
        null=True, 
    ) 
    drawer_start = models.ForeignKey(  # pour regrouper cb_ti1 et cb_ti2  
        Drawer, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='cable_drawer_start' 
    ) 
    drawer_end = models.ForeignKey(  # pour regrouper cb_ti1 et cb_ti2  
        Drawer, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='cable_drawer_end' 
    ) 
    pdu = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    terminal = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) 
    start = models.CharField(  # REFERENCES t_eq_elec (el_code) 
        max_length=254, 
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
        null=True, 
    ) 
    archive_reason = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 

    def __str__(self) -> str: 
        return f'''{self.racine}{self.id}, 
            actual length : {self.actual_length}, 
            start : {self.ebp_start}, 
            end : {self.ebp_end}''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

