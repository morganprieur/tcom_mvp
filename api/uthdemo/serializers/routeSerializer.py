from uthdemo.models import ( 
    Organism, 
    Route, 
    Tech_point 
) 
from uthdemo.serializers import ( 
    OrganismSerializer, 
    Tech_pointSerializer 
) 
from rest_framework import serializers 
from uthdemo.utils.mySerializerFunctions import MySerializerFunctions 


class RouteSerializer(serializers.ModelSerializer, MySerializerFunctions): 
    """ References OrganismSerializer and Tech_pontSerializer 
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
    code = serializers.CharField( 
        required=False, 
    ) 
    ext_code = serializers.CharField( 
        required=False, 
    ) 
    tech_point_start = Tech_pointSerializer( 
        required=False, 
    ) 
    tech_point_end = Tech_pointSerializer( 
        required=False, 
    ) 
    street_name = serializers.CharField( 
        required=False, 
    ) 
    dom_manager = OrganismSerializer( 
        required=False, 
    ) 
    dom_owner = OrganismSerializer( 
        required=False, 
    ) 
    state = serializers.CharField( 
        required=False, 
    ) 
    logical_type = serializers.CharField( 
        required=False, 
    ) 
    install_type = serializers.CharField( 
        required=False, 
    ) 
    nature = serializers.CharField( 
        required=False, 
    ) 
    composition = serializers.CharField( 
        required=False, 
    ) 
    pipe_available = serializers.BooleanField( 
        required=False, 
    ) 
    install_method = serializers.CharField( 
        required=False, 
    ) 
    way = serializers.CharField( 
        required=False, 
    ) 
    length = serializers.FloatField( 
        required=False, 
    ) 
    actual_length = serializers.FloatField( 
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
        model = Route 
        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'ext_code', 'tech_point_start', 'tech_point_end', 
            'street_name', 'dom_manager', 'dom_owner', 'state', 
            'logical_type', 'install_type', 'nature', 'composition', 
            'pipe_available', 'install_method', 'way', 'length', 
            'actual_length', 'comment', 'created_at', 'updated_at', 
            'archived_at', 'archive_reason', 
        ] 

    # Custom create() 
    def create(self, validated_data): 

        new_route = self.check_sub_entity(validated_data, Route) 

        # returns a Route instance 
        return new_route 

