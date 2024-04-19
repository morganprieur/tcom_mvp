from uthdemo.models import ( 
    Drawer, 
    Reference 
) 
from uthdemo.serializers import ( 
    OrganismSerializer, 
    ReferenceSerializer 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class DrawerSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References OrganismSerializer and ReferenceSerializer. """
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
    cabinet = serializers.CharField(
        required=False, 
    ) 
    owner = OrganismSerializer(
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
    reference = ReferenceSerializer(
        required=False, 
    ) 
    size = serializers.IntegerField(
        required=False, 
    ) 
    start_u = serializers.IntegerField(
        required=False, 
    ) 
    cabinet_face = serializers.CharField( 
        # source='get_cabinet_face_display', 
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
        model = Drawer 
        fields = [ 
            'uuid', 'racine', 'id' 
            # 'code', 
            'ext_code', 'label', 'cabinet', 'owner', 
            'state', 'type', 'reference', 'size', 'start_u', 
            'cabinet_face', 'comment', 'created_at', 'updated_at', 
            'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_drawer = self.check_sub_entity(validated_data, Drawer) 

        # returns a Drawer instance 
        return new_drawer 

