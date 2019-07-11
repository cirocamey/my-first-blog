from django.shortcuts import render

# Se importa para poder hacer el odenamiento en el post_list()
from django.utils import timezone

# Importamos el modelo Post
from .models import Post

# Create your views here.

# Fíjate en que creamos una variable para el QuerySet: posts. Trátala como si fuera el nombre de nuestro QuerySet. De aquí en adelante vamos a referirnos al QuerySet con ese nombre.
def post_list(request):

	# Se agrega el ordenamiento a la pagina de los post
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


	return render(request, 'blog/post_list.html', {'posts': posts})