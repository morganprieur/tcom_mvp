from django.contrib import admin

from uthdemo.models import ( 
    Address, Cable, Cassette, Cri, Document, Drawer, 
    Ebp, Fiber, Organism, Photo, Position, Reference, 
    Route, Suf, Tech_point, Tech_site, 
    Work_order, Reader, Reader_profile, 
    Recorder, Recorder_profile, 
    Editor, Editor_profile 
) 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  
from django.contrib.auth.models import User 


# Override UserAdmin in order to 
# custom displaying its columns in admin itf 

# =============== users ================ # 
class UserAdmin(BaseUserAdmin): 
    list_display = ( 
        'id', 'username', 'groups_ids', 'groups_names', 'is_staff' 
    ) 

    # columns titles : 
    def groups_ids(self, user): 
        user_group_ids = user.groups.values_list('id', flat=True)      # QuerySet Object  
        group_ids_as_list = list(user_group_ids)                        # QuerySet to `list`

        text = group_ids_as_list  
        return text 
    groups_ids.short_description = 'Groups ids'

    def groups_names(self, user): 
        user_group_names = user.groups.values_list('name', flat=True)  # QuerySet Object 
        group_names_as_list = list(user_group_names)                    # QuerySet to `list` 

        text = group_names_as_list  
        return text 
    groups_names.short_description = 'Groups names' 
# Re-register UserAdmin
admin.site.unregister(User) 
admin.site.register(User, UserAdmin) 

class ReaderAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'name', 
        'password', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def reader_description(self, Reader): 
        return Reader.name 
    reader_description.short_description = 'name' 
admin.site.register(Reader, ReaderAdmin) 

class Reader_profileAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'reader_user', 
        'reader', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def reader_profile_description(self, Reader_profile): 
        return Reader_profile.reader 
    reader_profile_description.short_description = 'reader' 
admin.site.register(Reader_profile, Reader_profileAdmin) 

class RecorderAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'name', 
        'password', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def recorder_description(self, Recorder): 
        return Recorder.name 
    recorder_description.short_description = 'name' 
admin.site.register(Recorder, RecorderAdmin) 

class Recorder_profileAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'recorder_user', 
        'recorder', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def recorder_profile_description(self, Recorder_profile): 
        return Recorder_profile.recorder 
    recorder_profile_description.short_description = 'recorader' 
admin.site.register(Recorder_profile, Recorder_profileAdmin) 

class EditorAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'name', 
        'password', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def editor_description(self, Editor): 
        return Editor.name 
    editor_description.short_description = 'name' 
admin.site.register(Editor, EditorAdmin) 

class Editor_profileAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'editor_user', 
        'editor', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def editor_profile_description(self, Editor_profile): 
        return Editor_profile.editor 
    editor_profile_description.short_description = 'editor' 
admin.site.register(Editor_profile, Editor_profileAdmin) 
# =============== /users ================ # 


# =============== métier ================ # 
class AddressAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'street_name', 
        'number', 
        'rep', 
        'insee', 
        'zip_code', 
        'place_name', 
        'lat', 
        'lng', 
        'city', 
        'building_name', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 

    def address_description(self, Address): 
        return Address.number + Address.rep + ', ' + Address.street_name + Address.city 
    address_description.short_description = 'City address' 
admin.site.register(Address, AddressAdmin) 

class CableAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'ext_code', 
        'label', 
        'owner', 
        'manager', 
        'user', 
        'state', 
        'type', 
        'physical_type', 
        'reference', 
        'supply_type', 
        'diameter', 
        'color', 
        'length', 
        'actual_length', 
        'ebp_start', 
        'ebp_end', 
        # 'type_start', 
        # 'type_end', 
        # 'code_start', 
        # 'code_end', 
        'pdu', 
        'terminal', 
        'start',  # table eqt elec à faire 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason',  
    ) 
admin.site.register(Cable, CableAdmin) 

class FiberAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        'ext_code', 
        # 'code', 
        'cable', 
        'num_in_cb', 
        'tube_num', 
        'num_in_tube', 
        'type', 
        'state', 
        'color', 
        'caracteristics', 
        'property_type', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Fiber, FiberAdmin) 

class EbpAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        'qrcode', 
        # 'code', 
        'ext_code', 
        'label', 
        'tech_point', 
        'owner', 
        'manager', 
        'user', 
        'property_type', 
        'status', 
        'state', 
        'occup', 
        'physical_type', 
        'logical_type', 
        'reference', 
        'inputs_nb', 
        'cassettes_nb', 
        'steps_nb', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Ebp, EbpAdmin) 

class CassetteAdmin(admin.ModelAdmin): 
    list_display = (
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'num', 
        'type', 
        'ebp', 
        'ebp_face', 
        'reference', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Cassette, CassetteAdmin) 

class CriAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        'ext_code', 
        'work_order', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Cri, CriAdmin) 

class SufAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'address', 
        # 'equipment', 
        'type', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Suf, SufAdmin) 

class OrganismAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'siren', 
        'name', 
        'type', 
        'activity', 
        'siret', 
        'estab_name', 
        'street_name', 
        'number', 
        'rep', 
        'zip_code', 
        'city', 
        'phone', 
        'email', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
    def organism_description(self, Organism): 
        for org in Organism.objects.all().order_by('name'): 
            return org.name 
            # return Organism.name 
    organism_description.short_description = 'Organism name' 
admin.site.register(Organism, OrganismAdmin) 

class PhotoAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'image', 
        'name', 
        'created_at', 
    ) 
admin.site.register(Photo, PhotoAdmin) 

class PositionAdmin(admin.ModelAdmin): 
    list_display = ( 
        'racine', 
        'id', 
        # 'code', 
        'number', 
        'fiber_start', 
        'fiber_end', 
        'cassette', 
        # 'drawer', 
        # 'equipment', 
        # 'card', 
        'type', 
        'function', 
        'state', 
        'occup', 
        'suf', 
        'preaffected', 
        'interface_number', 
        'interface_type', 
        'interface_bandswidth', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Position, PositionAdmin) 

class Tech_pointAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        'ext_code', 
        # 'code', 
        'label', 
        'address', 
        'dom_manager', 
        'dom_owner', 
        'owner', 
        'manager', 
        'user', 
        'property_type', 
        'status', 
        'state', 
        'physical_type', 
        'logical_type', 
        'nature', 
        'occup', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
    # def tech_point_description(self, Tech_point): 
    #     for tp in Tech_point.objects.all().order_by('manager'): 
    #         return tp.name 
    # tech_point_description.short_description = 'Tech_point name' 
admin.site.register(Tech_point, Tech_pointAdmin) 

class ReferenceAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'type', 
        'manufacturer', 
        'model', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Reference, ReferenceAdmin) 

class Tech_siteAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        'ext_code', 
        # 'code', 
        'name', 
        'owner', 
        'manager', 
        'user', 
        'property_type', 
        'status', 
        'state', 
        'physical_type', 
        'logical_type', 
        'address', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Tech_site, Tech_siteAdmin) 

class DrawerAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'ext_code', 
        'label', 
        'cabinet', 
        'owner', 
        'state', 
        'type', 
        'reference', 
        'size', 
        'start_u', 
        'cabinet_face', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Drawer, DrawerAdmin) 

class RouteAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        'ext_code', 
        # 'code', 
        'tech_point_start', 
        'tech_point_end', 
        'street_name', 
        'dom_manager', 
        'dom_owner', 
        'state', 
        'logical_type', 
        'install_type', 
        'nature', 
        # 'composition', 
        'pipe_available', 
        'install_method', 
        'way', 
        # 'length', 
        # 'actual_length', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Route, RouteAdmin) 

class Work_orderAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'ext_code', 
        'label', 
        'address', 
        'ebp', 
        'tech_point', 
        # 'tech_site', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Work_order, Work_orderAdmin) 

class DocumentAdmin(admin.ModelAdmin): 
    list_display = ( 
        'uuid', 
        'racine', 
        'id', 
        # 'code', 
        'ext_code', 
        'name', 
        'reference', 
        'work_order', 
        'type', 
        'indice', 
        'indice_date', 
        'cartographic_class', 
        'document_url', 
        'comment', 
        'created_at', 
        'updated_at', 
        'archived_at', 
        'archive_reason', 
    ) 
admin.site.register(Document, DocumentAdmin) 


# =============== /métier ================ # 

