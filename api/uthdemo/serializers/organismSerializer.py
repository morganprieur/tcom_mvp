from uthdemo.models import Organism 
from rest_framework import serializers 
from django.db.models import Q 

class OrganismSerializer(serializers.ModelSerializer): 
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
    #     max_length=254 
    # ) 
    siren = serializers.CharField( 
        max_length=9, 
        required=False, 
    ) 
    name = serializers.CharField( 
        max_length=254,  
        required=False 
    ) 
    type = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    activity = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    siret = serializers.CharField( 
        max_length=14, 
        required=False, 
    ) 
    estab_name = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    # address = AddressSerializer( 
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
    zip_code = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    city = serializers.CharField( 
        max_length=20, 
        required=False, 
    ) 
    phone = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    email = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    comment = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    # TODO: voir timezone Paris 
    created_at = serializers.DateField( 
        required=False, 
    ) 
    updated_at = serializers.DateField( 
        required=False, 
    ) 
    archived_at = serializers.DateField( 
        required=False 
    ) 
    archive_reason = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 

    class Meta: 
        model = Organism 

        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'siren', 'name', 'type', 'activity', 
            'siret', 'estab_name', 'street_name', 'number', 
            'rep', 'zip_code', 'city', 'phone', 'email', 'comment', 
            'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ] 

    def create(self, validated_data): 

        organism_code = validated_data.pop('code') 
        last_organisms = Organism.objects.filter( 
            Q(code=organism_code) | Q(**validated_data) 
        ) 
        if not last_organisms: 
            new_organism = Organism.objects.create( 
                code=organism_code, 
                **validated_data 
            ) 
        else: 
            new_organism = Organism.objects.get( 
                Q(code=organism_code) | Q(**validated_data) 
            ) 

        return new_organism 
