from uthdemo.models import Address 
from rest_framework import serializers 
from django.db import models 
from django.db.models import Q 

from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class AddressSerializer(serializers.ModelSerializer, MySerializerFunctions): 

    uuid = serializers.UUIDField( 
        required=False, 
    ) 
    racine = serializers.CharField( 
        required=False, 
    ) 
    id = serializers.CharField( 
        required=False, 
    ) 
    # code = serializers.CharField( 
    #     required=False, 
    # ) 
    street_name = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    number = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    rep = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    insee = serializers.CharField( 
        max_length=6, 
        required=False, 
    ) 
    zip_code = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    place_name = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    lat = serializers.FloatField( 
        required=False, 
    ) 
    lng = serializers.FloatField( 
        required=False, 
    ) 
    city = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    building_name = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    comment = serializers.CharField( 
        max_length=254, 
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
        model = Address 
        fields = [
            'uuid', 'racine', 'id', 
            # 'code', 
            'street_name', 'number', 'rep', 'insee', 'zip_code', 
            'place_name', 'lat', 'lng', 'city', 'building_name', 
            'comment', 'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_address = self.check_if_entity_exists(validated_data, Address) 
        #  TODO: tester si ya une répétition 

        return new_address 

