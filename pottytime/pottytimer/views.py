# from django.http import HttpResponse
from django.shortcuts import redirect, render
from pottytimer.models import Sticker

def home_page(request):
    if request.method == 'POST':
        Sticker.objects.create(text=request.POST['sticker_text'])
        return redirect('/')

    stickers = Sticker.objects.all()

    return render(request, 'home.html', {'stickers': stickers}  )
