from uthdemo.models import ( 
    Cassette, 
    Ebp, 
    Reference 
) 
from uthdemo.serializers import ( 
    EbpSerializer, 
    ReferenceSerializer 
)
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class CassetteSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ 
        References EbpSerializer and ReferenceSerializer  
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
    num = serializers.IntegerField( 
        required=False, 
    ) 
    type = serializers.CharField( 
        source='get_type_display', 
        required=False, 
    ) 
    ebp = EbpSerializer( 
        required=False, 
    ) 
    bp_face = serializers.CharField( 
        required=False, 
    ) 
    reference = ReferenceSerializer( 
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
        model = Cassette 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'num', 'type', 'ebp', 'bp_face', 'reference', 
            'comment', 'created_at', 'updated_at', 'archived_at', 'archive_reason' 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_cassette = self.check_sub_entity(validated_data, Cassette) 

        # returns a Cassette instance 
        return new_cassette 


