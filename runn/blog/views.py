from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog

@api_view()
def list_blogs(request):
    blogs=Blog.objects.all()
    blog_json=BlogSerializer(blogs,many=True)
    print(blog_json)
    return Response(blog_json.data)

@api_view()
def detail_blog(request,id):
    blogdetail=Blog.objects.get(id=id)
    detailed_json=BlogSerializer(blogdetail)
    return Response(detailed_json.data)    