from uthdemo.models import Reader_profile 
from uthdemo.serializers import ReaderSerializer, UserSerializer 
from rest_framework import serializers 


class Reader_profileSerializer(serializers.ModelSerializer): 
    uuid = serializers.UUIDField( 
        required=False, 
    ) 
    reader_user = UserSerializer( 
        required=False, 
    ) 
    reader = ReaderSerializer( 
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
        # allow_blank=True, 
    ) 

    class Meta: 
        model = Reader_profile 
        fields = ( 
            'uuid', 'reader_user', 'reader', 
            'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ) 
