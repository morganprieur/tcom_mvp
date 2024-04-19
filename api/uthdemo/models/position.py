from django.db import models 
from uthdemo.models import ( 
    Cassette, 
    Drawer, 
    Fiber, 
    Suf 
) 
import uuid 
from uthdemo.utils.choices import ( 
    OCCUPATION_TYPE, 
    POSITION_FUNCTION, 
    POSITION_TYPE,  
    STATE_TYPE,  
) 

class Position(models.Model): 
    """ References Cassette, Drawer, Fiber, Suf  """ 
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
    number = models.IntegerField( 
        blank=True, 
        null=True 
    ) 
    fiber_start = models.ForeignKey( 
        Fiber, 
        on_delete=models.CASCADE, 
        related_name='fiber_start', 
        blank=True, 
        null=True, 
    ) 
    fiber_end = models.ForeignKey( 
        Fiber, 
        on_delete=models.CASCADE, 
        related_name='fiber_end', 
        blank=True, 
        null=True, 
    ) 
    cassette = models.ForeignKey( 
        Cassette, 
        on_delete=models.CASCADE, 
        related_name='position_cassette', 
        blank=True, 
        null=True 
    ) 
    """ doublon avec Cassette.drawer : 
    drawer = models.ForeignKey( 
        Drawer, 
        on_delete=models.CASCADE, 
        related_name='position_drawer', 
        blank=True, 
        null=True, 
    ) 
    card = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    """ 
    type = models.CharField( 
        max_length=10, 
        choices=POSITION_TYPE, 
        blank=True, 
        null=True, 
    )  
    function = models.CharField( 
        max_length=2, 
        choices=POSITION_FUNCTION, 
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
        max_length=254, 
        choices=OCCUPATION_TYPE, 
        blank=True, 
        null=True, 
    )  
    suf = models.ForeignKey( 
        Suf, 
        on_delete=models.CASCADE, 
        related_name='position_suf', 
        blank=True, 
        null=True 
    ) 
    preaffected = models.BooleanField( 
        default=False, 
    ) 
    interface_number = models.IntegerField( 
        blank=True, 
        null=True, 
    ) 
    interface_type = models.CharField(  # liste ? 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    interface_bandswidth = models.CharField(  # liste ? 
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
        null=True 
    ) 
    archive_reason = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) 

    def __str__(self) -> str: 
        return f'''{self.racine}{self.id}, 
        Type : {self.type}, 
        fiber end : {self.fiber_end}, 
        fiber start : {self.fiber_start}, 
         number : {self.number}, 
        suf : {self.suf}''' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

