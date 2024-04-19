from uthdemo.models import ( 
    Ebp, 
    Organism, 
    Reference, 
    Tech_point 
) 
from uthdemo.serializers import ( 
    OrganismSerializer, 
    ReferenceSerializer, 
    Tech_pointSerializer 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class EbpSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References Tech_pointSerializer, 
        OrganismSerializer (as owner, manager and/or user), 
        and ReferenceSerializer. """ 
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
    label = serializers.CharField(
        required=False, 
    ) 
    ext_code = serializers.CharField(
        required=False, 
    ) 
    tech_point = Tech_pointSerializer(
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
    occup = serializers.CharField( 
        # source='get_occup_display', 
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
    reference = ReferenceSerializer(
        required=False, 
    ) 
    inputs_nb = serializers.IntegerField(
        required=False, 
    ) 
    cassettes_nb = serializers.IntegerField(
        required=False, 
    ) 
    steps_nb = serializers.IntegerField(
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
        model = Ebp 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'label', 'ext_code', 'tech_point', 
            'owner', 'manager', 'user', 'property_type', 'status', 
            'state', 'occup', 'physical_type', 'logical_type', 
            'reference', 'inputs_nb', 'cassettes_nb', 'steps_nb', 
            'comment', 'created_at', 'updated_at', 'archived_at', 
            'archive_reason' 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_ebp = self.check_sub_entity(validated_data, Ebp) 

        # returns an Ebp instance 
        return new_ebp 


