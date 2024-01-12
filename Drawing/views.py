from django.shortcuts import render

import draw_table as draw

# Create your views here.

def index(request):
    return render(request, 'Drawing/base.html')


def table(request):
    if request.method == "POST":
        length_table = request.POST.get('length_table')  # Довжина столу
        width_table = request.POST.get('width_table')  # Ширина столу
        height_table = request.POST.get('height_table')  # Висота столу
        thickness = request.POST.get('thickness')  # Товщина стільниці
        tube = request.POST.get('tube')  # Труба основна
        long_circle = request.POST.get('long_circle')  # Отвори від краю
        rog = request.POST.get('rog')  # Довжина рожка
        rog_tube = request.POST.get('rog_tube')  # Труба рожка
        rog_coor = request.POST.get('rog_coor')  # Відстань до рожка

        list_size = [int(thickness), int(height_table), int(width_table),
                     int(length_table), int(tube[:2]), int(tube[3:]),
                     int(long_circle), int(rog), int(rog_tube[:2]), int(rog_tube[3:]),
                     int(rog_coor)]
        print(draw.table_gener(list_size))

    return render(request, 'Drawing/table.html')
