from uthdemo.models import Editor 
from django.contrib.auth.hashers import make_password 
from rest_framework import serializers 


class EditorSerializer(serializers.ModelSerializer): 
    uuid = serializers.UUIDField( 
        required=False, 
    ) 
    name = serializers.CharField( 
        max_length=50, 
        required=False, 
    )  
    password = serializers.CharField( 
        max_length=100, 
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
        model = Editor 
        fields = [ 
            'uuid', 'name', 'password', 
            'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ] 

    def create(self, validated_data): 
        validated_data['password'] = make_password(validated_data['password']) 
        return Editor.objects.create(**validated_data) 

