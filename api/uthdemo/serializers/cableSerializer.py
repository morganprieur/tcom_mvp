from uthdemo.models import ( 
    Cable, 
    Drawer, 
    Ebp, 
    Organism, 
    Reference 
) 
from uthdemo.serializers import ( 
    DrawerSerializer, 
    EbpSerializer, 
    OrganismSerializer, 
    ReferenceSerializer 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class CableSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References DrawerSerializer, 
        EbpSerializer, 
        OrganismSerializer, 
        and ReferenceSerializer 
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
    #     required=False, 
    # ) 
    ext_code = serializers.CharField( 
        required=False, 
    ) 
    label = serializers.CharField( 
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
    state = serializers.CharField( 
        # source='get_state_display', 
        required=False, 
    ) 
    type = serializers.CharField( 
        # source='get_type_display', 
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
    fibers_capacity = serializers.IntegerField( 
        required=False, 
    ) 
    fibers_dispo = serializers.IntegerField( 
        required=False, 
    ) 
    useful_fibers = serializers.IntegerField( 
        required=False, 
    ) 
    fiber_modulo = serializers.IntegerField( 
        required=False, 
    ) 
    supply_type = serializers.CharField( 
        # source='get_supply_type_display', 
        required=False, 
    ) 
    diameter = serializers.FloatField( 
        required=False, 
    ) 
    color = serializers.CharField( 
        required=False, 
    ) 
    length = serializers.FloatField( 
        required=False, 
    ) 
    actual_length = serializers.FloatField( 
        required=False, 
    ) 
    ebp_start = EbpSerializer( 
        required=False, 
    ) 
    ebp_end = EbpSerializer( 
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
        model = Cable 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            # 'ext_code', 'label', 'owner', 'manager', 
            'user', 'state', 'type', 'physical_type', 'logical_type', 
            'reference', 'fibers_capacity', 'fibers_dispo', 
            'useful_fibers', 'fiber_modulo', 'supply_type', 'diameter', 
            'color', 'length', 'actual_length', 'ebp_start', 'ebp_end', 
            'comment', 'created_at', 
            'updated_at', 'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_cable = self.check_sub_entity(validated_data, Cable) 

        # returns a Cable instance 
        return new_cable 

