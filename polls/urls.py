from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
]

#tag template de Django qui génère l'URL complet de votre image.
#<img src="{% static 'hammer.png' %}" alt="Hammer">

