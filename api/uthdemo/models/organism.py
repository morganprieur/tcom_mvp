from django.db import models 
import uuid 


class Organism(models.Model): 
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
    #     blank=True, 
    #     null=True 
    # ) 
    siren = models.CharField( 
        max_length=9, 
        blank=True, 
        null=True 
    ) 
    name = models.CharField( 
        max_length=254, 
        db_index=True, 
    ) 	
    # classification jurique (littéral ou INSEE) 
    type = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    activity = models.CharField( 
        max_length=254, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    siret = models.CharField( 
        max_length=14, 
        blank=True, 
        null=True 
    ) 
    # TODO A mettre "unique" ? 
    estab_name = models.CharField( 
        max_length=254, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    street_name = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True, 
    ) 
    number = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) 
    rep = models.CharField( 
        max_length=20, 
        blank=True, 
        null=True 
    ) 
    zip_code = models.CharField( 
        max_length=20, 
        blank=True, 
        null=True, 
    )  
    city = models.CharField( 
        max_length=254, 
        db_index=True, 
        blank=True, 
        null=True, 
    ) 
    phone = models.CharField( 
        max_length=20, 
        blank=True, 
        null=True 
    ) 
    email = models.CharField( 
        max_length=254, 
        blank=True, 
        null=True 
    ) 
    comment = models.TextField( 
        blank=True, 
        null=True 
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
        if self.rep: 
            rep = self.rep 
        else: 
            rep = '' 
        return f'''{self.racine}{self.id}, {self.name}, 
            {self.number}{rep} {self.street_name} - {self.city}''' 

    # Metadata
    class Meta:
        ordering = ['created_at'] 

