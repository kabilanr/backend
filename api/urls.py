from django.urls import path,include
from api import views
urlpatterns=[
    path('person',views.person_list),
]
