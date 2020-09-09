from django.urls import path,include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("",views.DepremView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
