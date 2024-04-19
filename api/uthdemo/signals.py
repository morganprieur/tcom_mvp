from uthdemo.models import (
    Reader, Reader_profile, 
    Recorder, Recorder_profile, 
    Editor, Editor_profile, 
) 
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User, Group 
from django.db.models.signals import post_save 
from django.dispatch import receiver 
# from datetime import datetime 


# Reader 
@receiver(post_save, sender=Reader) 
def create_reader_user(sender, instance, created, **kwargs): 
    """ When a Reader instance is created: 
            creates a User with name 'R_' + instance name 
            and assigns the new User the 'reader' group.  
        Args:
            sender (Reader): the model which sends a signal when an instance is created 
            instance (Reader): the just created Reader 
            created (bool): the Reader instance is created True/False : trigger. 
            If False, the program exits the method.  
    """ 
    # Création d'un User, avec mot de pass hashé 
    if created: 
        new_user = User(username='R_' + str(instance.name), email='') 
        if len(instance.password) < 50: 
            new_user.password = make_password(instance.password) 
        else: 
            # instance.password is already hashed: 
            new_user.password = instance.password 
        new_user.save() 

        # Get the latest instance of created User: 
        user = User.objects.filter().last() 
        # print(f'last reader user signal37 : {user}') 

        if user.username == 'R_' + str(instance.name): 
            # Adds the group 'reader' to the user's instance groups 
            reader_group = Group.objects.get(name='reader') 
            user.groups.add(reader_group) 

            # Afficher la réussite de la création du User et la liste de ses groupes 
            user_groups = user.groups.values_list('name', flat=True) 
            groups_as_list = list(user_groups) 
            print('User ' + str(user.username) + ' - groupes : ' + str(groups_as_list) + ' successfully saved!') 


@receiver(post_save, sender=User) 
def create_reader_profile(sender, instance, created, **kwargs): 
    """ When a User named 'R_'+ is created, a Reader_profile is created in order to bind the User and the Reader 
        Args:
            sender (User): the User model, who sends a signal when a new User 
            with name starting with 'R_' is created.  
            instance (User): the just created User named 'R_'+. 
            created (bool): determines if the User has been created. 
            If not: the program exits the method. 
    """ 
    if created: 
        # Automatically creates a reader_profile on User creation 
        # and links it with the Reader 
        reader = Reader.objects.filter().last() 
        user = User.objects.filter(username__startswith='R_').last() 

        if user == instance: 
            Reader_profile.objects.create( 
                reader_user=instance, 
                reader=reader 
            ) 


# Recorder (technicians) 
@receiver(post_save, sender=Recorder) 
def create_recorder_user(sender, instance, created, **kwargs): 
    """ When a Recorder instance is created: 
            creates a User with name 'T_' (for 'technician') + instance name 
            and assigns the new User the 'recorder' group.  
        Args:
            sender (Recorder): the model which sends a signal when an instance is created 
            instance (Recorder): the just created Recorder 
            created (bool): the Recorder instance is created True/False : trigger. 
            If False, the program exits the method.  
    """ 
    # Création d'un User, avec mot de pass hashé 
    if created: 
        new_user = User(username='T_' + str(instance.name), email='') 
        if len(instance.password) < 50: 
            new_user.password = make_password(instance.password) 
        else: 
            # if instance.password is already hashed: 
            new_user.password = instance.password 
        new_user.save() 

        # Get the latest instance of created User: 
        user = User.objects.filter().last() 
        # print(f'last recorder user (signal97) : {user}') 

        if user.username == 'T_' + str(instance.name): 
            # Adds the group 'recorder' to the user's instance groups 
            recorder_group = Group.objects.get(name='recorder') 
            user.groups.add(recorder_group) 

            # Afficher la réussite de la création du User et la liste de ses groupes 
            user_groups = user.groups.values_list('name', flat=True) 
            groups_as_list = list(user_groups) 
            print(f'''User {str(user.username)} - groupes : {str(groups_as_list)} 
            successfully saved!''') 

# Quand un User est créé et que son nom commence par 'T_' : 
#   un Recorder_profile est créé, qui lie le User et le Recorder. 
@receiver(post_save, sender=User) 
def create_recorder_profile(sender, instance, created, **kwargs): 
    """ When a User named 'T_'+ is created, a Recorder_profile is created 
        in order to bind the User and the Recorder. 
        Args:
            sender (User): the User model, who sends a signal when a new User 
                with name starting with 'T_' is created.  
            instance (User): the just created User named 'T_'+. 
            created (bool): determines if the User has been created. 
                If not: the program exits the method. 
    """ 
    if created: 
        # Automatically creates a recorder_profile on User creation 
        # and links it with the Recorder 
        recorder = Recorder.objects.filter().last() 
        user = User.objects.filter(username__startswith='T_').last() 

        if user == instance: 
            Recorder_profile.objects.create( 
                recorder_user=instance, 
                recorder=recorder 
            ) 


# Editor (managers) 
@receiver(post_save, sender=Editor) 
def create_editor_user(sender, instance, created, **kwargs): 
    """ When an Editor instance is created: 
            creates a User with name 'M_' (for 'manager') + instance name 
            and assigns the new User the 'editor' group.  
        Args:
            sender (Editor): the model which sends a signal when an instance is created 
            instance (Editor): the just created Editor 
            created (bool): the Editor instance is created True/False : trigger. 
            If False, the program exits the method.  
    """ 
    # Création d'un User, avec mot de pass hashé 
    if created: 
        new_user = User(username='M_' + str(instance.name), email='') 
        if len(instance.password) < 50: 
            new_user.password = make_password(instance.password) 
        else: 
            # if instance.password is already hashed: 
            new_user.password = instance.password 
        new_user.save() 

        # Get the latest instance of created User: 
        user = User.objects.filter().last() 
        # print(f'last editor user (signal160) : {user}') 

        if user.username == 'M_' + str(instance.name): 
            # Adds the group 'editor' to the user's instance groups 
            editor_group = Group.objects.get(name='editor') 
            user.groups.add(editor_group) 

            # Afficher la réussite de la création du User et la liste de ses groupes 
            user_groups = user.groups.values_list('name', flat=True) 
            groups_as_list = list(user_groups) 
            print(f'''User {str(user.username)} - groupes : {str(groups_as_list)} 
            successfully saved!''') 

@receiver(post_save, sender=User) 
def create_editor_profile(sender, instance, created, **kwargs): 
    """ When a User named 'M_'+ is created, a Editor_profile is created 
        in order to bind the User and the Editor. 
        Args:
            sender (User): the User model, who sends a signal when a new User 
                with name starting with 'M_' is created.  
            instance (User): the just created User named 'M_'+. 
            created (bool): determines if the User has been created. 
                If not: the program exits the method. 
    """ 
    if created: 
        # Automatically creates a recorder_profile on User creation 
        # and links it with the Recorder 
        editor = Editor_profile.objects.filter().last() 
        user = User.objects.filter(username__startswith='M_').last() 

        if user == instance: 
            Editor_profile.objects.create( 
                editor_user=instance, 
                editor=editor 
            ) 



