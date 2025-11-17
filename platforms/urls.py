from django.urls import path
from . import views
from .views import PlatformListView

urlpatterns = [
    path('', PlatformListView.as_view()),
]