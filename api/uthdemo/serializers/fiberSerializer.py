from uthdemo.models import Fiber 
from rest_framework import serializers 
from django.db.models import Q 
from uthdemo.serializers import CableSerializer 

class FiberSerializer(serializers.ModelSerializer): 
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
    # obligatoire 
    cable = CableSerializer( 
        required=False, 
    ) 
    num_in_cb = serializers.IntegerField( 
        required=False, 
    ) 
    tube_num = serializers.IntegerField( 
        required=False, 
    ) 
    num_in_tube = serializers.IntegerField( 
        required=False, 
    ) 
    type = serializers.CharField( 
        required=False, 
    ) 
    state = serializers.CharField( 
        required=False, 
    ) 
    color = serializers.CharField( 
        required=False, 
    ) 
    caracteristics = serializers.CharField( 
        required=False, 
    ) 
    property_type = serializers.CharField( 
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
        model = Fiber 

        fields = [ 
            'uuid', 'racine', 'id', 
            # 'code', 
            'ext_code', 'cable', 'num_in_cb', 
            'tube_num', 'num_in_tube', 'type', 'state', 'color', 
            'caracteristics', 'property_type', 'comment', 'created_at', 
            'updated_at', 'archived_at', 'archive_reason', 
        ] 

    def create(self, validated_data): 
        # print(f'validated_data IS383 : {validated_data}') 

        fiber_code = validated_data.pop('code') 
        last_fibers = Fiber.objects.filter( 
            Q(code=fiber_code) | Q(**validated_data) 
        ) 
        if not last_fibers: 
            new_fiber = Fiber.objects.create( 
                code=fiber_code, 
                **validated_data 
            ) 
        else: 
            new_fiber = Fiber.objects.get( 
                Q(code=fiber_code) | Q(**validated_data) 
            ) 

        return new_fiber 
