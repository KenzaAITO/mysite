from django.urls import path
from polls import views

urlpatterns = [
    path('', views.my_view, name='index'),
]


#tag template de Django qui génère l'URL complet de votre image.
#<img src="{% static 'hammer.png' %}" alt="Hammer">

