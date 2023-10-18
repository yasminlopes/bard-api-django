from django.contrib import admin
from django.urls import path
from django.urls import re_path
from api.views import BardApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bard-api/', BardApiView.as_view()),
    path('bard-api/history/<str:id_conversation>', BardApiView.as_view()),
]
