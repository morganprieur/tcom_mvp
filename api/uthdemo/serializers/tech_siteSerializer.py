from uthdemo.models import ( 
    Address, 
    Organism, 
    Tech_site 
)  
from uthdemo.serializers import ( 
    AddressSerializer, 
    OrganismSerializer 
) 
from rest_framework import serializers 
from django.db.models import Q 

from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class Tech_siteSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References: 
            AddressSerializer, 
            OrganismSerializer as owner, manager and/or user 
    """ 
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
    #     max_length=254, 
    # ) 
    ext_code = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    name = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 
    owner = OrganismSerializer( 
        required=False 
    ) 
    manager = OrganismSerializer( 
        required=False 
    ) 
    user = OrganismSerializer( 
        required=False 
    ) 
    property_type = serializers.CharField( 
        # source='get_property_type_display()', 
        required=False, 
    ) 
    status = serializers.CharField( 
        # source='get_state_display', 
        required=False, 
    ) 
    state = serializers.CharField( 
        # source='get_status_display', 
        required=False, 
    ) 
    physical_type = serializers.CharField( 
        # source='get_physical_type_display', 
        required=False, 
    ) 
    logical_type = serializers.CharField( 
        # source='get_logical_type_display', 
        required=False, 
    ) 
    address = AddressSerializer(  
        required=False, 
    ) 
    comment = serializers.CharField( 
        max_length=254, 
        required=False,  
    ) 
    created_at = serializers.DateField(required=False, )  # TODO default_timezone='Paris' 
    updated_at = serializers.DateField(required=False, ) 
    archived_at = serializers.DateField(required=False, ) 
    archive_reason = serializers.CharField( 
        max_length=254, 
        required=False, 
    ) 

    class Meta: 
        model = Tech_site 
        # user = OrganismSerializer() 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'ext_code', 'name', 'owner', 
            'manager', 'user', 'property_type', 'status', 
            'state', 'physical_type', 'logical_type', 'address', 
            'comment', 'created_at', 'updated_at', 'archived_at', 
            'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 
        new_tech_site = self.check_sub_entity(validated_data, Tech_site) 
        # Return a Tech_site instance 
        return new_tech_site 
