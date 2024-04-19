from django.contrib import admin 
from django.urls import include, path 
from uthdemo import views 
from rest_framework import routers 


router = routers.DefaultRouter() 
router.register(r'users', views.UserViewSet) 
# router.register(r'groups', views.GroupViewSet) 


app_name = 'uthdemo' 

# ==== GET POST ==== # 
router.register(r'readers', views.ReaderViewSet) 
router.register(r'recorders', views.RecorderViewSet) 
router.register(r'editors', views.EditorViewSet) 
# router.register(r'reader_profiles', views.Reader_profileViewSet) 
# router.register(r'recorder_profiles', views.Recorder_profileViewSet) 
# router.register(r'editor_profiles', views.Editor_profileViewSet) 

# ==== GET ==== # 
router.register(r'addresses', views.AddressViewSet) 
router.register(r'cables', views.CableViewSet) 
router.register(r'cassettes', views.CassetteViewSet) 
router.register(r'cassettes', views.CassetteViewSet) 
router.register(r'drawers', views.DrawerViewSet) 
router.register(r'ebps', views.EbpViewSet) 
router.register(r'organisms', views.OrganismViewSet) 
router.register(r'positions', views.PositionViewSet) 
router.register(r'references', views.ReferenceViewSet) 
router.register(r'routes', views.RouteViewSet) 
router.register(r'sufs', views.SufViewSet) 
router.register(r'tech_points', views.Tech_pointViewSet) 
router.register(r'tech_sites', views.Tech_siteViewSet) 
router.register(r'cables', views.CableViewSet) 
router.register(r'documents', views.DocumentViewSet) 
router.register(r'work_orders', views.Work_orderViewSet) 
# router.register(r'cabinets_list', views.CabinetListView) # error 'get_extra_actions' essai autrement + bas 

urlpatterns = [ 
    path('', include(router.urls)), 
    # path('', authentication.views.login_page, name='login'),

    # path('cabinets_list/', views.CabinetListView.as_view(), name="cabinets_list"), 

    # ==== POST ==== # 
    path(r'new_address/', views.NewAddressView.as_view()), 
    path(r'new_organism/', views.NewOrganismView.as_view()), 
    path(r'new_tech_site/', views.NewTech_siteView.as_view()), 
    path(r'new_reference/', views.NewReferenceView.as_view()), 
    path(r'new_drawer/', views.NewDrawerView.as_view()), 
    path(r'new_suf/', views.NewSufView.as_view()), 
    path(r'new_tech_point/', views.NewTech_pointView.as_view()), 
    path(r'new_ebp/', views.NewEbpView.as_view()),
    path(r'new_cassette/', views.NewCassetteView.as_view()),
    path(r'new_cable/', views.NewCableView.as_view()),
    path(r'new_document/', views.NewDocumentView.as_view()),
    path(r'new_work_order/', views.NewWork_orderView.as_view()),

    # api-auth/login/ 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
] 


