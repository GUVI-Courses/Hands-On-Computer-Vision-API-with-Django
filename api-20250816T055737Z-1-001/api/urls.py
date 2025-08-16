from django.urls import path
from api import views
from .views import OCRUploadView


urlpatterns = [
  path('',views.index,name='index'),
  path('upload/',OCRUploadView.as_view(),name='upload')
]
