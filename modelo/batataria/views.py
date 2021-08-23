from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'teste': 'shflkjnvlkrej'}
    return render(request, 'forum/base.html', context)