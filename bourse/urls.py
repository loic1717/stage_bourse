from django.urls import path
from bourse.views import index,description
urlpatterns = [
    path('', index, name='home' ),
    path('<int:myid>/',description, name='description')
]
