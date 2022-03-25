import imp
from django.urls import path
from .views import lead_detail, lead_list, lead_create, lead_update, lead_delete, LeadCreateView, LeadListView, LeadDeleteView, LeadUpdateView, LeadDetailView,AssignAgentView,CategoryListView,CategoryDetailView,LeadCategoryUpdateView
app_name = "leads"
urlpatterns = [
    path('',LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/',LeadDetailView.as_view(), name='lead_detail'),
    path('create/',LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/update/',LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    ]  