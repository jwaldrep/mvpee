# from django.http import HttpResponse
from django.shortcuts import redirect, render
from pottytimer.models import Chart, Sticker



def home_page(request):
    # if request.method == 'POST':
    #     Sticker.objects.create(text=request.POST['sticker_text'])
    #     return redirect('/charts/lone-chart/')

    stickers = Sticker.objects.all()

    return render(request, 'home.html', {'stickers': stickers}  )

def view_chart(request, chart_id):
    chart = Chart.objects.get(id=chart_id)
    stickers = Sticker.objects.filter(chart=chart)
    return render(request, 'chart.html', {'stickers': stickers}  )

def new_chart(request):
    chart = Chart.objects.create()
    Sticker.objects.create(text=request.POST['sticker_text'], chart=chart)
    return redirect('/charts/%d/' % (chart.id,))

def add_sticker(request, chart_id):
    chart = Chart.objects.get(id=chart_id)
    Sticker.objects.create(text=request.POST['sticker_text'], chart=chart)
    return redirect('/charts/%d/' % (chart.id,))
