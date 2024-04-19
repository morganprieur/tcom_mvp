
from uthdemo import models 
from django.db.models import Q 

class MySerializerFunctions: 

    def check_if_entity_exists(self, validated_data, model): 

        model_code = validated_data.pop('code') 
        last_model_list = model.objects.filter( 
            Q(code=model_code) | Q(**validated_data) 
        ) 
        if not last_model_list: 
            new_model = model.objects.create( 
                code=model_code, 
                **validated_data 
            ) 
        else: 
            if model.objects.get(Q(code=model_code) | Q(**validated_data)): 
                new_model = model.objects.get( 
                    Q(code=model_code) 
                ) 
            else: 
                new_model = model.objects.get( 
                    Q(**validated_data) 
                ) 
        return new_model 


    def check_sub_entity(self, validated_data, model): 

        model_code = validated_data.pop('code') 
        submodels_dict = { 
            'address': models.Address, 
            'manager': models.Organism, 
            'owner': models.Organism, 
            'user': models.Organism, 
            'manufacturer': models.Organism, 
            'reference': models.Reference, 
            'cabinet': models.Cabinet, 
            'dom_manager': models.Organism, 
            'dom_owner': models.Organism, 
            'ebp': models.Ebp, 
            'tech_point': models.Tech_point, 
            'tech_point_start': models.Tech_point, 
            'tech_point_end': models.Tech_point, 
            'drawer': models.Drawer, 
            'cassette': models.Cassette, 
            'fiber': models.fiber, 
            'suf': models.Suf 
        } 
        new_submodelsList = {} 
        for subkey in submodels_dict.keys(): 
            if subkey in validated_data.keys(): 
                submodel = submodels_dict[subkey] 
                submodel_data = validated_data.pop(subkey) 
                submodel_code = submodel_data.pop('code') 

                last_submodel_list = submodel.objects.filter( 
                    Q(code=submodel_code) | Q(**submodel_data) 
                ) 
                if not last_submodel_list: 
                    new_submodel = submodel.objects.create( 
                        code=submodel_code, 
                        **submodel_data 
                    ) 
                else: 
                    if submodel.objects.get(Q(code=submodel_code)): 
                        new_submodel = submodel.objects.get( 
                            Q(code=submodel_code) 
                        ) 
                    else: 
                        new_submodel = submodel.objects.get( 
                            Q(**submodel_data) 
                        ) 
                new_submodelsList[subkey] = new_submodel 

        last_models_list = model.objects.filter( 
            Q(code=model_code) | Q(**validated_data) 
        ) 
        if not last_models_list: 
            new_model = model.objects.create( 
                code=model_code, 
                **new_submodelsList, 
                **validated_data 
            ) 
        else: 
            if model.objects.get(Q(code=model_code) | Q(**validated_data)): 
                new_model = model.objects.get( 
                    Q(code=model_code) 
                ) 
            else: 
                new_model = model.objects.get( 
                    Q(**validated_data) 
                ) 
        return new_model 

