from uthdemo.models import ( 
    Document, 
    Reference, 
    Work_order, 
) 
from uthdemo.serializers import ( 
    ReferenceSerializer, 
    Work_orderSerializer, 
) 
# from uthdemo.utils import choices 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class DocumentSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ 
    References ReferenceSerializer 
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
    name = serializers.CharField( 
        required=False, 
    ) 
    reference = ReferenceSerializer( 
        required=False, 
    ) 
    work_order = Work_orderSerializer( 
        required=False, 
    ) 
    type = serializers.CharField( 
        # choices.DOCUMENT_TYPE(), 
        required=False, 
    ) 
    indice = serializers.CharField( 
        required=False, 
    ) 
    indice_date = serializers.CharField( 
        required=False, 
    ) 
    cartographic_class = serializers.CharField( 
        required=False, 
    ) 
    document_url = serializers.CharField( 
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
        model = Document 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'ext_code', 'name', 'reference', 
            'work_order', 'type', 
            'indice', 'indice_date', 'cartographic_class', 
            'document_url', 'comment', 'created_at', 
            'updated_at', 'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_document = self.check_sub_entity(validated_data, Document) 

        # returns a Document instance 
        return new_document 

