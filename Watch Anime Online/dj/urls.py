from django.urls import path
from . import views
urlpatterns = [   
    path('',views.index,name='index'),
    path('animelink/',views.animelink,name="rr"),
    path('search/',views.search,name='search')
]
