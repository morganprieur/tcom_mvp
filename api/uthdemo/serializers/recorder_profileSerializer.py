from uthdemo.models import Recorder_profile 
from uthdemo.serializers import RecorderSerializer, UserSerializer 
from rest_framework import serializers 


class Recorder_profileSerializer(serializers.ModelSerializer): 
    uuid = serializers.UUIDField( 
        required=False, 
    ) 
    recorder_user = UserSerializer( 
        required=False, 
    ) 
    recorder = RecorderSerializer( 
        required=False, 
    ) 
    created_at = serializers.DateField( 
        required=False, 
    ) 
    updated_at = serializers.DateField( 
        required=False, 
    ) 
    archived_at = serializers.DateField( 
        required=False, 
    ) 
    archive_reason = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 

    class Meta: 
        model = Recorder_profile 
        fields = ( 
            'uuid', 'recorder_user', 'recorder', 
            'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ) 
