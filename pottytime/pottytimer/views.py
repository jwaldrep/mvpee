from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_sticker_text': request.POST.get('sticker_text', ''),
    })
