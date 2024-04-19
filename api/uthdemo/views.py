from django.contrib.auth.models import User, Group 
from uthdemo.models import ( 
    Address, Cable, Cassette, Document, Drawer, 
    Ebp, Organism, Position, Reference, Route, 
    Suf, Tech_point, Tech_site, Work_order,  
    Reader, Reader_profile, 
    Recorder, Recorder_profile, 
    Editor, Editor_profile, 
) 
from uthdemo.serializers import ( 
    UserSerializer, GroupSerializer, 
    AddressSerializer, 
    # CabinetListSerializer, 
    CableSerializer, 
    CassetteSerializer, 
    DocumentSerializer, 
    DrawerSerializer, 
    EbpSerializer, 
    OrganismSerializer, 
    PositionSerializer, 
    ReferenceSerializer, RouteSerializer, 
    SufSerializer, 
    Tech_pointSerializer, Tech_siteSerializer, 
    Work_orderSerializer, 
    ReaderSerializer, Reader_profileSerializer, 
    RecorderSerializer, Recorder_profileSerializer, 
    EditorSerializer, Editor_profileSerializer, 
) 
from uthdemo.utils import choices 
from rest_framework.permissions import IsAuthenticated 
from uthdemo.permissions import ( 
    IsAdminAuthenticated, 
    IsEditorGroup, 
    IsRecorderGroup, 
    IsReaderGroup 
) 
from rest_framework import generics, viewsets 
from rest_framework.response import Response 
from rest_framework.generics import CreateAPIView 
from rest_framework.parsers import JSONParser 

# authentication/views.py 
from django.views.generic import View 
from django.shortcuts import redirect, render 

from django.conf import settings 

from . import forms 

# import des fonctions authenticate, login et logout 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 

from django.db.models import Q 

from django.shortcuts import get_object_or_404 

# django_ip_geolocation : à implémenter avec adresse IP publique # 
from django_ip_geolocation.decorators import with_ip_geolocation 


# ============ Contrib.auth (tuto drf) ======================= # 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminAuthenticated, ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminAuthenticated, ] 
# ============ /tuto drf ====================== # 


# ============ Utilisateurs ======================= # 
# ================= GET & POST ==================== # 
class ReaderViewSet(viewsets.ModelViewSet): 
    queryset = Reader.objects.all().order_by('-created_at') 
    serializer_class = ReaderSerializer 
    permission_classes = [IsAuthenticated, IsEditorGroup] 

class RecorderViewSet(viewsets.ModelViewSet): 
    queryset = Recorder.objects.all().order_by('-created_at') 
    serializer_class = RecorderSerializer 
    permission_classes = [IsAuthenticated, IsEditorGroup] 

class EditorViewSet(viewsets.ModelViewSet): 
    queryset = Editor.objects.all().order_by('-created_at') 
    serializer_class = EditorSerializer 
    permission_classes = [IsAuthenticated, IsEditorGroup] 


# TODO: make profile pages + send them to front 
# class Reader_profileViewSet(viewsets.ModelViewSet): 
#     queryset = Reader_profile.objects.all().order_by('-created_at') 
#     serializer_class = ReaderSerializer 
#     permission_classes = [IsAuthenticated, ] 

# ============ /Utilisateurs ======================= # 


# ============ Métier ============================== # 
# ================= GET ======================== # 
class AddressViewSet(viewsets.ModelViewSet): 
    queryset = Address.objects.all().order_by('city') 
    serializer_class = AddressSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


# class CabinetListView(generics.ListAPIView): 
#     """ The endpoint to view the list of cabinets. """ 
#     http_method_names = ['get'] 
#     queryset = Cabinet.objects.all() 
#     filter_backends = [filters.DjangoFilterBackend] 
#     filterset_class = CabinetFilterSet 
#     serializer_class = CabinetListSerializer 
#     # pagination_class = CabinetSetPagination 


class CableViewSet(viewsets.ModelViewSet): 
    queryset = Cable.objects.all()  # .order_by('-created_at') 
    serializer_class = CableSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class CassetteViewSet(viewsets.ModelViewSet): 
    queryset = Cassette.objects.all() 
    serializer_class = CassetteSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class DrawerViewSet(viewsets.ModelViewSet): 
    queryset = Drawer.objects.all() 
    serializer_class = DrawerSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class EbpViewSet(viewsets.ModelViewSet): 
    queryset = Ebp.objects.all() 
    serializer_class = EbpSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class OrganismViewSet(viewsets.ModelViewSet): 
    queryset = Organism.objects.all() 
    serializer_class = OrganismSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class PositionViewSet(viewsets.ModelViewSet): 
    queryset = Position.objects.all() 
    serializer_class = PositionSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class ReferenceViewSet(viewsets.ModelViewSet): 
    queryset = Reference.objects.all() 
    serializer_class = ReferenceSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class RouteViewSet(viewsets.ModelViewSet): 
    queryset = Route.objects.all() 
    serializer_class = RouteSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class SufViewSet(viewsets.ModelViewSet): 
    queryset = Suf.objects.all() 
    serializer_class = SufSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class Tech_pointViewSet(viewsets.ModelViewSet): 
    queryset = Tech_point.objects.all() 
    serializer_class = Tech_pointSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class Tech_siteViewSet(viewsets.ModelViewSet): 
    queryset = Tech_site.objects.all().order_by() 
    serializer_class = Tech_siteSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class DocumentViewSet(viewsets.ModelViewSet): 
    queryset = Document.objects.all() 
    serializer_class = DocumentSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


class Work_orderViewSet(viewsets.ModelViewSet): 
    queryset = Work_order.objects.all().order_by('-created_at') 
    serializer_class = Work_orderSerializer 
    # permission_classes = [IsAuthenticated, IsReaderGroup] 


# ================= POST ===================== # 

class NewAddressView(CreateAPIView): 
    """ 
        Creates an Address instance. 
    """ 
    # permission_classes = [IsRecorderGroup, ] 
    serializer_class = AddressSerializer 

    def post(self, request): 
        """ Sends data for création of an Address instance
        Args:
            request (dict): the data posted. 
        Returns:
            Response: 
                201 if the entity/ies has/have been created, 
                400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        serializer = AddressSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewOrganismView(CreateAPIView): 
    """ 
        Creates an Organism and/or an Address instances. 
        If the address exists, it is associated with the new organism. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = OrganismSerializer 

    def post(self, request): 
        """ 
            Sends data for création of an Organism instance, 
            bind an Address if needed, 
            and create an Address instance if data is given. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = OrganismSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewTech_siteView(CreateAPIView): 
    """ 
        Creates an Address, an Organism and a Tech_site instances. 
        If the address exists, it is associated to the new Tech_site. 
        If the organism exists, it is setted to the new Tech_site, as owner, manager and/or user. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = Tech_siteSerializer 

    def post(self, request): 
        """ Sends data for création of a Tech_site instance, 
            binds an Organism, and an Address if needed, 
            and creates an Organism and/or an Address instance 
            if data is given. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 

        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = Tech_siteSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewReferenceView(CreateAPIView): 
    """ 
        Creates a Reference and an Organism instances. 
        If the organism already exists, it is set to the new Reference, as a manufacturer. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = ReferenceSerializer 

    def post(self, request): 
        """ Sends data for création of a Reference instance, 
            creates an Organism instance if data is given. 
            and binds it to the new Reference. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = ReferenceSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewDrawerView(CreateAPIView): 
    """ 
        Creates a Drawer, an Organism and a Reference instances. 
        If the Organism already exists, it is set to the new Drawer. 
        If the Reference already exists, it is set to the new Drawer. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = DrawerSerializer 

    def post(self, request): 
        """ Sends data for création of a Drawer instance, 
            creates an Organism and a Reference instances if data is given 
            and binds them to the new Drawer. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = DrawerSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewSufView(CreateAPIView): 
    """ 
        Creates a Suf and an Address instances. 
        If the Address already exists, it is set to the new Suf. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = SufSerializer 

    def post(self, request): 
        """ Sends data for création of a Suf instance, 
            creates an Address and a Drawer instances if data is given 
            and binds them to the new Suf. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = SufSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewTech_pointView(CreateAPIView): 
    """ 
        Creates a Tech_point, an Address, one or more Organisms 
        (as dom_manager, dom_owner, manager, owner and/or user) 
        and a Reference instances. 
        If the Address already exists, it is set to the new Tech_point. 
        If the Organisms already exist, they are set to the new Tech_point. 
        If the Reference already exists, it is set to the new Tech_point. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = Tech_pointSerializer 

    def post(self, request): 
        """ Sends data for création of a Tech_point instance, 
            creates an Address, Organism(s) and a Reference instances if data is given 
            and binds them to the new Tech_point. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = Tech_pointSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 


class NewEbpView(CreateAPIView): 
    """ 
        Creates an Ebp, a Tech_point, one or more Organisms 
        (as dom_manager, dom_owner, manager, owner and/or user) 
        and a Reference instances. 
        If the Tech_point already exists, it is set to the new Ebp. 
        If the Organisms already exist, they are set to the new Ebp. 
        If the Reference already exists, it is set to the new Ebp. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = EbpSerializer 

    def post(self, request): 
        """ Sends data for création of an Ebp instance, 
            creates a Tech_point, Organism(s) and a Reference instances 
            if data is given 
            and binds them to the new Ebp. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = EbpSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)


class NewCassetteView(CreateAPIView): 
    """ 
        Creates a Cassette, an Ebp, a Drawer and a Reference instances. 
        If the Ebp already exists, it is set to the new Cassette. 
        If the Drawer already exist, they are set to the new Cassette. 
        If the Reference already exists, it is set to the new Cassette. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = CassetteSerializer 

    def post(self, request): 
        """ Sends data for création of a Cassette instance, 
            creates an Ebp, a Drawer and a Reference instances 
            if data is given 
            and binds them to the new Ebp. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = CassetteSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)


class NewCableView(CreateAPIView): 
    """ 
        Creates a Cable and set the given Ebp, Drawer, Reference to it. 
    """ 
    permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = CableSerializer 

    def post(self, request): 
        """ Sends data for création of a Cable instance, 
            If data is given, binds them to the new Cable instance. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = CableSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)


class NewDocumentView(CreateAPIView): 
    """ 
        Creates a Document and sets the given Reference to it. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = DocumentSerializer 

    def post(self, request): 
        """ Sends data for création of a Document instance, 
            If data is given, binds them to the new Document instance. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = DocumentSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)


class NewWork_orderView(CreateAPIView): 
    """ 
        Creates a Work_order and set the given Ebp, Tech_point, Tech_site to it. 
    """ 
    # permission_classes = [IsAuthenticated, IsRecorderGroup, ] 
    serializer_class = Work_orderSerializer 

    def post(self, request): 
        """ Sends data for création of a Work_order instance, 
            If data is given, binds them to the new Work_order instance. 
            Args:
                request (dict): the data posted. 
            Returns:
                Response: 
                    201 if the entity/ies has/have been created, 
                    400 with the error if the request has not been completely executed. 
        """ 
        data = JSONParser().parse(request) 

        # Save the data to the serializer for validating and saving them into the DB 
        serializer = Work_orderSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)

# ============ /Métier ============================== # 

# ============ login ============================== # 

def logout_user(request):
    logout(request)
    return redirect('login')


class SignupPageView(View): 
    template_name = 'uthdemo/signup.html' 
    form_class = forms.SignupForm 

    def get(self, request): 
        form = self.form_class() 
        # message = '' 
        return render(request, self.template_name, context={'form': form}) 

    def post(self, request): 
        form = self.form_class(request.POST) 
        if form.is_valid(): 
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL) 


# @with_ip_geolocation 
@login_required 
def home(request): 
    ots = Work_order.objects.all() 
    ots_count = ots.count 
    for ot in ots: 
        documents = Document.objects.filter( 
            work_order__id=ot.id, type='ORDRE DE TRAVAUX') | Document.objects.filter( 
            work_order__id=ot.id, type='COMPTE-RENDU D\'INTERVENTION') 
        docs_count = documents.count 
    return render( 
        request, 'uthdemo/home.html', context={
            'ots': ots, 
            'ots_count': ots_count, 
            'documents': documents, 
            'docs_count': docs_count, 
        } 
    ) 


@login_required 
def work_order_detail(request, work_order_id): 
    print('request : ', request) 
    ot = get_object_or_404(Work_order, id=work_order_id) 
    documents = Document.objects.filter(work_order__id=ot.id) 
    docs_count = documents.count 
    return render( 
        request, 'uthdemo/work_order_detail.html', context={ 
            'ot': ot, 
            'documents': documents, 
            'docs_count': docs_count  
        } 
    ) 


@login_required 
def ebp_detail(request, ebp_id): 
    ebp = get_object_or_404(Ebp, id=ebp_id) 
    ots = Work_order.objects.filter(ebp__id=ebp_id) 
    docs = Document.objects.filter(work_order__ebp__id=ebp.id) 
    documents = [] 
    for doc in docs: 
        if 'DOCUMENTATION TECHNIQUE' in doc.type: 
            document = doc 
            documents.append(document) 

    return render( 
        request, 'uthdemo/ebp_detail.html', context={ 
            'ebp': ebp, 
            'ots': ots, 
            'documents': documents 
        } 
    ) 


@login_required 
def pt_detail(request, pt_id): 
    pt = get_object_or_404(Tech_point, id=pt_id) 
    ebps = Ebp.objects.filter(tech_point__id=pt_id) 
    ots = Work_order.objects.filter(tech_point__id=pt_id) 
    return render( 
        request, 
        'uthdemo/pt_detail.html', 
        context={ 
            'pt': pt, 
            'ebps': ebps, 
            'ots': ots, 
        } 
    ) 

