from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.files import File
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
import os

import draw_table as draw # тут все правильно

from .models import DrawingTables, UserProfile


# Create your views here.

def index(request):
    if request.user.username:
        user = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(id_user=user.id)

        if request.method == "POST":
            avatar = request.FILES['avatar']  # Довжина столу
            user_prof = UserProfile.objects.get(id_user=user.id)
            user_prof.avatar = avatar
            user_prof.save()

        context = {
            "user": user,
            "user_profile": user_profile,
        }
        return render(request, 'Drawing/base.html', context=context)

    return render(request, 'Drawing/base.html')


def table(request):
    context = {}
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

        path1 = draw.table_gener(list_size)
        a = path1[-10:-4]

        try:
            drawing0 = DrawingTables(id_user=request.user)
            with open(path1, 'rb') as file:
                drawing0.drawing.save(f'table_{a}.pdf', File(file))

            drawing0.save()


            print(f"Файл успішно записано.table_{a}.pdf")
        except FileNotFoundError:
            print(f"Файл {path1} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при записі файлу: {e}")


        try:
            os.remove(path1)
            print(f"Файл {path1} успішно видалено.")
        except FileNotFoundError:
            print(f"Файл {path1} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при видаленні файлу: {e}")

    user = User.objects.get(username=request.user.username)
    drawing = DrawingTables.objects.filter(id_user=user.id)

    buf = {"drawing": drawing}

    context.update(buf)


    return render(request, 'Drawing/table.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


def download_file(request, id=None):
    drawing = get_object_or_404(DrawingTables, id=id)
    file_path = drawing.drawing.path
    a = drawing.drawing.name[-10:]
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="Table_{a}"'
    return response