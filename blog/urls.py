# Aquí estamos importando la función de Django path y todos nuestras views desde la aplicación blog
from django.urls import path
from . import views

# Esto es un patron URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
]

# Como puedes ver, estamos asociando una vista (view) llamada post_list a la URL raíz. Este patrón de URL detectará la cadena vacía, y el URL resolver de Django no tiene en cuenta el nombre el dominio (i.e., http://127.0.0.1:8000/) que viene antes del path de la url. Este patrón le dirá a Django que views.post_list es el lugar correcto al que ir si alguien entra a tu sitio web con la dirección 'http://127.0.0.1:8000/'.
