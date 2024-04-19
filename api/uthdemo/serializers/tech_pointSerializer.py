from uthdemo.models import ( 
    Address, 
    Organism, 
    Tech_point 
) 
from uthdemo.serializers import ( 
    AddressSerializer, 
    OrganismSerializer, 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class Tech_pointSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References AddressSerializer and 
        OrganismSerializer (as dom_manager, dom_owner, manager, owner, and user). 
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
    # code = serializers.CharField() 
    ext_code = serializers.CharField( 
        required=False, 
    ) 
    label = serializers.CharField( 
        required=False, 
    ) 
    address = AddressSerializer( 
        required=False, 
    ) 
    dom_manager = OrganismSerializer( 
        required=False, 
    ) 
    dom_owner = OrganismSerializer( 
        required=False, 
    ) 
    owner = OrganismSerializer( 
        required=False, 
    ) 
    manager = OrganismSerializer( 
        required=False, 
    ) 
    user = OrganismSerializer( 
        required=False, 
    ) 
    property_type = serializers.CharField( 
        # source='get_property_type_display',  
        required=False, 
    ) 
    status = serializers.CharField( 
        # source='get_status_display',  
        required=False, 
    ) 
    state = serializers.CharField( 
        # source='get_state_display',  
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
    nature = serializers.CharField( 
        # source='get_nature_display',  
        required=False, 
    ) 
    occup = serializers.CharField( 
        # source='get_occup_display',  
        required=False, 
    ) 
    comment = serializers.CharField( 
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
        required=False, 
    ) 

    class Meta: 
        model = Tech_point 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'ext_code', 'label', 'address', 'dom_manager', 
            'dom_owner', 'owner', 'manager', 'user', 'property_type', 
            'status', 'state', 'physical_type', 'logical_type', 
            'nature', 'occup', 'comment', 'created_at', 'updated_at', 
            'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_tech_point = self.check_sub_entity(validated_data, Tech_point) 

        # returns a Tech_point instance 
        return new_tech_point 


