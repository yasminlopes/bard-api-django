from django.contrib import admin
from django.urls import path
from django.urls import re_path
from api.views import RespostaAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bard-api/', RespostaAPIView.as_view()),
    #  path('bard-api/history/<str:id_conversation>', RespostaAPIView.as_view()),
]
