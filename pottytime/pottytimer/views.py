# from django.http import HttpResponse
from django.shortcuts import redirect, render
from pottytimer.models import Sticker

def home_page(request):
    if request.method == 'POST':
        Sticker.objects.create(text=request.POST['sticker_text'])
        return redirect('/charts/lone-chart/')

    stickers = Sticker.objects.all()

    return render(request, 'home.html', {'stickers': stickers}  )

def view_chart(request):
    stickers = Sticker.objects.all()
    return render(request, 'chart.html', {'stickers': stickers}  )

