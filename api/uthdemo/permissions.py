from rest_framework import permissions 


class IsAdminAuthenticated(permissions.BasePermission): 
    """ permission class that permits only superusers to request on urls 
        Args:
            permissions (permissions): class that defines the permissions and their conditions 
    """ 
    def has_permission(self, request, view): 
        # Access allowed only for superuser users 
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser) 


def get_users_groups(request): 
    """ Get the list of the request.user's groups 
        Args:
            request (request) 
        Returns:
            groups_as_list: list of strings 
    """ 
    users_groups = request.user.groups.values_list('name', flat=True) 
    groups_as_list = list(users_groups) 
    # print(str(request.user) + ' permissions : ' + str(groups_as_list)) 
    return groups_as_list 


class IsEditorGroup(permissions.BasePermission): 
    """ permission class that permits only Editors and over to request on urls 
        Args:
            permissions (permissions): class that defines the permissions and their conditions 
    """ 
    def has_permission(self, request, view): 

        groups_as_list = get_users_groups(request) 
        print(f'groupes : {groups_as_list}') 
        if len(groups_as_list) > 0:  
            if ('editor' in groups_as_list) or (request.user.is_superuser): 
                return True 
        else: 
            if request.user.is_superuser: 
                print(f'superuser ? : {request.user.is_superuser}') 
                return True 
            else: 
                print(f'groupes : {groups_as_list} -> pas ok') 
                print(f'superuser ? : {request.user.is_superuser}') 
                return False 


class IsRecorderGroup(permissions.BasePermission): 
    """ permission class that permits only Recorders and over to send requests on urls 
        Args:
            permissions (permissions): class that defines the permissions and their conditions 
    """ 

    def has_permission(self, request, view): 

        groups_as_list = get_users_groups(request) 
        if len(groups_as_list) > 0:  
            print(f'groupes : {groups_as_list}') 
            if ('recorder' in groups_as_list) or ('editor' in groups_as_list) or (request.user.is_superuser): 
                # print('permission group ok') 
                return True 
        else: 
            if request.user.is_superuser: 
                print(f'superuser ? : {request.user.is_superuser}') 
                return True 
            else: 
                print(f'groupes : {groups_as_list} -> pas ok') 
                print(f'superuser ? : {request.user.is_superuser}') 
                return False 


class IsReaderGroup(permissions.BasePermission): 
    """ permission class that permits only Readers and over to send requests on urls 
        Args:
            permissions (permissions): class that defines the permissions and their conditions 
    """ 

    def has_permission(self, request, view): 

        groups_as_list = get_users_groups(request) 
        if len(groups_as_list) > 0:  
            print(f'groupes : {groups_as_list}') 
            if (('reader' or 'editor' or 'recorder') in groups_as_list) or (request.user.is_superuser): 
                # print('permission group ok') 
                return True 
        else:
            if request.user.is_superuser: 
                print(f'superuser ? : {request.user.is_superuser}') 
                return True 
            else: 
                print(f'groupes : {groups_as_list} -> pas ok') 
                print(f'superuser ? : {request.user.is_superuser}') 
                return False 


