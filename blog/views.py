from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

#This is used for declaring views "Similar to android"

# Create your views here.
