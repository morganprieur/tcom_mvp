from django.db import models  
from django.contrib.auth.models import User  
import uuid 


class Reader_profile(models.Model): 
    """ A user who can only send GEt requests """ 
    uuid = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False 
    ) 
    reader_user = models.OneToOneField( 
        'auth.User', 
        on_delete=models.SET_NULL, 
        related_name='reader_profile_user', 
        blank=True, 
        null=True 
    ) 
    reader = models.ForeignKey( 
        'uthdemo.Reader', 
        on_delete=models.SET_NULL, 
        related_name='reader_profile', 
        blank=True, 
        null=True, 
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

    def __str__(self) -> str: 
        return f'{self.uuid} username : {self.reader_user.username}' 

    # Metadata
    class Meta:
        # ordering = ['-created_at']
        ordering = ['created_at'] 

