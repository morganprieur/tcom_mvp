from uthdemo.models import ( 
    Address, 
    Ebp, 
    Tech_point, 
    Tech_site, 
    Work_order, 
) 
from uthdemo.serializers import ( 
    AddressSerializer, 
    EbpSerializer, 
    Tech_pointSerializer, 
    # Tech_siteSerializer,  
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class Work_orderSerializer(serializers.ModelSerializer, MySerializerFunctions):
    """ 
        References AddressSerializer, 
            EbpSerializer, 
            Tech_pointSerializer and 
            Tech_siteSerializer 
    """ 
    uuid = serializers.CharField( 
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
    address = AddressSerializer( 
        required=False, 
    ) 
    ebp = EbpSerializer( 
        required=False, 
    ) 
    tech_point = Tech_pointSerializer( 
        required=False, 
    ) 
    """ 
    tech_site = serializers.CharField( 
        required=False, 
    ) 
    """ 
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
        model = Work_order 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'ext_code', 'label', 
            'address', 'ebp', 'tech_point',  # 'tech_site', 
            'comment', 'created_at', 'updated_at', 'archived_at', 
            'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_work_order = self.check_sub_entity(validated_data, Work_order) 

        # returns a Work_order instance 
        return new_work_order 


