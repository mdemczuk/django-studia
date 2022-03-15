from django.shortcuts import render

from .models import Post

# Create your views here.
def post_list_view(request):
	context = {
		'object_list': Post.objects.all().filter(public=True).order_by('-date_publish')
	}
	return render(request, 'blog/post_list.html', context)