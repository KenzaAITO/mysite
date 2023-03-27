from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.my_view, name='views')
]

#tag template de Django qui génère l'URL complet de votre image.
#<img src="{% static 'hammer.png' %}" alt="Hammer">

