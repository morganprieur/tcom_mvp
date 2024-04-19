from django.db import models  
from django.contrib.auth.models import User  
import uuid 


class Recorder_profile(models.Model): 
    """ A user who can send GEt and POST requests """ 
    uuid = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False 
    ) 
    recorder_user = models.OneToOneField( 
        'auth.User', 
        on_delete=models.SET_NULL, 
        related_name='recorder_profile_user', 
        blank=True, 
        null=True 
    ) 
    recorder = models.ForeignKey( 
        'uthdemo.Recorder', 
        on_delete=models.SET_NULL, 
        related_name='recorder_profile', 
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
        return f'{self.uuid} username : {self.recorder_user.username}' 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 

