from uthdemo.models import ( 
    Organism, 
    Reference 
) 
from uthdemo.serializers import OrganismSerializer 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class ReferenceSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References OrganismSerializer as manufacturer """ 
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
    type = serializers.CharField( 
        # source="get_type_display", 
        required=False, 
    ) 
    manufacturer = OrganismSerializer( 
        required=False, 
    ) 
    model = serializers.CharField( 
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
        model = Reference 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'type', 'manufacturer', 'model', 'comment', 
            'created_at', 'updated_at', 'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 
        new_reference = self.check_sub_entity(validated_data, Reference) 
        # Returns a Reference instance 
        return new_reference 
