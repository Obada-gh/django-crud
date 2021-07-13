from django.urls import path
from .views import   SnackCreateView, SnackDeleteView,SnackListView,SnackUpdateView,SnackDetailView


urlpatterns = [
   
    path('', SnackListView.as_view(), name='view'), 
    path('<int:pk>/', SnackDetailView.as_view(), name='detailView'),
    path('<int:pk>/update/',SnackUpdateView.as_view(), name='update') ,
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name='delete') ,
    path('create/',SnackCreateView.as_view(), name='create') ,

]