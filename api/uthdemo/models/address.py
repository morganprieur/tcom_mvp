from django.db import models 
import uuid 


class Address(models.Model): 
    """ Used for tech_point and Suf only """ 
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
    street_name = models.CharField( 
        max_length=254, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    number = models.CharField( 
        max_length=254, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    rep = models.CharField( 
        max_length=20, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    insee = models.CharField( 
        max_length=6, 
        blank=True, 
        null=True, 
    ) 
    zip_code = models.CharField( 
        max_length=20, 
        blank=True, 
        null=True, 
    ) 
    place_name = models.CharField( 
        max_length=20, 
        blank=True, 
        null=True, 
    ) 
    lat = models.FloatField( 
        blank=True, 
        null=True 
    )  
    lng = models.FloatField(
        blank=True, 
        null=True 
    ) 
    city = models.CharField( 
        max_length=20, 
        db_index=True
    ) 
    building_name = models.CharField( 
        db_index=True, 
        max_length=20, 
        blank=True, 
        null=True, 
    ) 
    comment = models.TextField( 
        blank=True, 
        null=True 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
        blank=True, 
        null=True, 
    ) 
    updated_at = models.DateField( 
        blank=True, 
        null=True, 
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

    class Meta: 
        ordering = ['-created_at'] 
        verbose_name_plural = 'addresses'
        # unique_together = ('number', 'street_name', 'city') 
        constraints = [
            models.UniqueConstraint(fields=['number', 'rep', 'street_name', 'city'], name='unique_address')
        ] 

    def __str__(self) -> str: 
        if self.rep: 
            rep = self.rep 
        else: 
            rep = '' 
        return f'{self.uuid} code : {self.racine}{self.id}, {self.number}{rep} {self.street_name}, {self.zip_code} {self.city}' 
