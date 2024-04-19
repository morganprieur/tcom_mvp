from uthdemo.models import ( 
    Address, 
    Suf 
) 
from uthdemo.serializers import ( 
    AddressSerializer, 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class SufSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References AddressSerializer  """ 
    uuid = serializers.CharField( 
        max_length=254, 
        required=False 
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
    address = AddressSerializer( 
        required=False, 
    ) 
    equipment = serializers.CharField( 
        required=False, 
    ) 
    type = serializers.CharField( 
        # source='get_type_display', 
        required=False, 
    ) 
    comment = serializers.CharField( 
        max_length=254, 
        required=False 
    )  
    created_at = serializers.CharField( 
        max_length=254, 
        required=False, 
    )  
    updated_at = serializers.CharField( 
        max_length=254, 
        required=False 
    )  
    archived_at = serializers.CharField( 
        max_length=254, 
        required=False 
    )  
    archive_reason = serializers.CharField( 
        max_length=254, 
        required=False 
    )  

    class Meta: 
        model = Suf 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'address', 'equipment', 'type', 
            'comment', 'created_at', 'updated_at', 'archived_at', 'archive_reason' 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_suf = self.check_sub_entity(validated_data, Suf) 

        # returns a Suf instance 
        return new_suf 

