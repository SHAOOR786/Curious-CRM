import imp
from django.urls import path
from .views import lead_detail, lead_list, lead_create, lead_update, lead_delete, LeadCreateView
app_name = "leads"
urlpatterns = [
    path('',lead_list, name='lead_list'),
    path('<int:pk>/',lead_detail, name='lead_detail'),
    path('create/',LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/update/',lead_update, name='lead_update'),
    path('<int:pk>/delete/',lead_delete, name='lead_delete')

]