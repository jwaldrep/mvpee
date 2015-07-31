# from django.http import HttpResponse
from django.shortcuts import render
from pottytimer.models import Sticker

def home_page(request):
    if request.method == 'POST':
        new_sticker_text = request.POST['sticker_text']
        Sticker.objects.create(text=new_sticker_text)
    else:
        new_sticker_text = ''

    return render(request, 'home.html', {
        'new_sticker_text': new_sticker_text,
    })
