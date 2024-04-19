from uthdemo.models import Editor_profile 
from uthdemo.serializers import EditorSerializer, UserSerializer 
from rest_framework import serializers 


class Editor_profileSerializer(serializers.ModelSerializer): 
    uuid = serializers.UUIDField( 
        required=False, 
    ) 
    editor_user = UserSerializer( 
        required=False, 
    ) 
    editor = EditorSerializer( 
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
        model = Editor_profile 
        fields = ( 
            'uuid', 'editor_user', 'editor', 
            'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ) 
