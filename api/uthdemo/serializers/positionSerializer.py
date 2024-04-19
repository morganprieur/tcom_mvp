from uthdemo.models import ( 
    Cassette, 
    Drawer, 
    Position, 
    Suf 
) 
from uthdemo.serializers import ( 
    CassetteSerializer, 
    DrawerSerializer, 
    SufSerializer, 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class PositionSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References 
        CassetteSerializer, 
        DrawerSerializer, 
        SufSerializer 
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
    number = serializers.IntegerField( 
        required=False, 
    ) 
    cassette = CassetteSerializer( 
        required=False, 
    ) 
    drawer = DrawerSerializer( 
        required=False, 
    ) 
    equipment = serializers.CharField( 
        required=False, 
    ) 
    card = serializers.CharField( 
        required=False, 
    ) 
    type = serializers.CharField( 
        # source='get_type_display', 
        required=False, 
    ) 
    function = serializers.CharField( 
        # source='get_function_display', 
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
    suf = SufSerializer( 
        required=False, 
    ) 
    preaffected = serializers.BooleanField( 
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
        model = Position 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'number', 'cassette', 'drawer', 'equipment', 
            'card', 'type', 'function', 'state', 'occup', 'suf', 
            'preaffected', 'comment', 'created_at', 'updated_at', 
            'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_position = self.check_sub_entity(validated_data, Position) 

        # returns a Position instance 
        return new_position 


