from django.shortcuts import render
from django.http import Http404
from .models import Post, Author, subscribe
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def index(request):

	if request.method == 'GET':
		email = request.GET.get('email')
		if email:
			subscribe(email=email).save()

	week_ago = datetime.date.today() - datetime.timedelta(days = 7)
	trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')
	TopAuthors =Author.objects.order_by('-rate')[:4]
	AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors]

	all_post = Paginator(Post.objects.filter(publish = True),3)
	page = request.GET.get('page')
	try:
		posts = all_post.page(page)

	except PageNotAnInteger:
		posts = all_post.page(1)
	except EmptyPage:
		posts = all_post.page(all_post.num_pages)

	parms = {
		'posts': posts,
		'trends': trends[:5],
		'author_post':AuthorsPost,
		'pop_post': Post.objects.order_by('-read')[:9],
	}
	return render(request, 'index.html', parms)

def about(request):
	parms = {
		'title': 'About | Codingunda',

		}
	return render(request, 'about.html', parms)

def post(request, id, slug):
	try:
		post = Post.objects.get(pk=id, slug=slug)
	except:
		raise Http404("Post Does Not Exist")

	return render(request, 'blog-single.html', {'post':post})

def contact(request):
	return render(request, 'contact.html')

def search(request):
	q = request.GET.get('q')
	posts = Post.objects.filter(
		Q(title__icontains = q) |
		Q(overview__icontains = q)
		).distinct()

	parms = {
		'posts':posts,
		'title':f'Search Results for {q}',
		'pop_post': Post.objects.order_by('-read')[:9],
		}

	return render(request, 'all.html', parms)

def view_all(request, query):
	week_ago = datetime.date.today() - datetime.timedelta(days = 7)
	
	acpt = ['trending', 'popular']
	q = query.lower()
	if q in acpt:
		if q==acpt[0]:
			parms={
			'posts' : Post.objects.filter(time_upload__gte = week_ago).order_by('-read'),
			'title': "Trending Posts",
			'pop_post': Post.objects.order_by('-read')[:9],
			}
		elif q==acpt[1]:
			parms= {
			'posts' : Post.objects.order_by('-read'),
			'title' : "Trending Posts",
			'pop_post': Post.objects.order_by('-read')[:9],
			}
		else:
			pass

	return render(request, 'all.html', parms)