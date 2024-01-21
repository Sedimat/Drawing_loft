from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.files import File
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
import os

import draw_table as draw  # тут все правильно
import draw_table_A as draw_A  # тут все правильно
from django.utils import timezone

from .models import DrawingTables, UserProfile, News


# Create your views here.

def userinfo(request):
    try:
        user = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(id_user=user.id)
        dict_user = {"user": user,
                     "user_profile": user_profile}

        return dict_user
    except:
        return None


def index(request):
    news = News.objects.all().order_by("-published_date")
    context = {"news": news}
    if request.user.username:
        context.update(userinfo(request))
        if request.method == "POST":
            user = User.objects.get(username=request.user.username)
            avatar = request.FILES['avatar']  # Довжина столу
            user_prof = UserProfile.objects.get(id_user=user.id)
            user_prof.avatar = avatar
            user_prof.save()

        return render(request, 'Drawing/index.html', context=context)

    return render(request, 'Drawing/index.html')


def table(request):
    context = {}
    if request.method == "POST":
        length_table = request.POST.get('length_table')  # Довжина столу
        if not 999 < int(length_table) < 2001:
            context.update(userinfo(request))
            context.update({"text": "Довжина столу не може бути більше 2000 мм або менше 1000 мм"})
            return render(request, 'Drawing/table.html', context=context)

        width_table = request.POST.get('width_table')  # Ширина столу

        if not 499 < int(width_table) < 1201:
            context.update(userinfo(request))
            context.update({"text": "Ширина столу не може бути більше 1200 мм або менше 500 мм"})
            return render(request, 'Drawing/table.html', context=context)

        height_table = request.POST.get('height_table')  # Висота столу

        if not 749 < int(height_table) < 1201:
            context.update(userinfo(request))
            context.update({"text": "Висота столу не може бути більше 1200 мм або менше 750 мм"})
            return render(request, 'Drawing/table.html', context=context)

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
        name = path1[-10:-4]

        try:
            drawing0 = DrawingTables(id_user=request.user)
            drawing0.published_date = timezone.now()
            drawing0.type = "Прямокутний Square"
            drawing0.details = f"{width_table},{height_table},{tube[:2]}x{tube[3:]}"
            with open(path1, 'rb') as file:
                drawing0.drawing.save(f'table_type_Square_{name}.pdf', File(file))

            drawing0.save()

            print(f"Файл успішно записано.table_{name}.pdf")
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

        return redirect('user')

    if request.user.username:
        context.update(userinfo(request))

    return render(request, 'Drawing/table.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


def download_file(request, id=None):
    drawing = get_object_or_404(DrawingTables, id=id)
    file_path = drawing.drawing.path
    a = drawing.drawing.name[-22:]
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="Table_{a}"'
    return response


def user(request):
    context = {}
    if request.user.username:
        user = User.objects.get(username=request.user.username)
        drawing = DrawingTables.objects.filter(id_user=user.id).order_by("-published_date")
        if len(drawing):
            draw ={
               "drawing_first": drawing[0],
               "drawing_all": drawing[1:],
               "len_drawing": len(drawing),
               }
            context.update(draw)

        context.update(userinfo(request))

    return render(request, 'Drawing/user.html', context=context)


def table_type_A(request):
    context = {}

    if request.method == "POST":
        length_table = request.POST.get('length_table')  # Довжина столу
        if not 999 < int(length_table) < 2001:
            context.update(userinfo(request))
            context.update({"text": "Довжина столу не може бути більше 2000 мм або менше 1000 мм"})
            return render(request, 'Drawing/table.html', context=context)

        width_table = request.POST.get('width_table')  # Ширина столу

        if not 499 < int(width_table) < 1201:
            context.update(userinfo(request))
            context.update({"text": "Ширина столу не може бути більше 1200 мм або менше 500 мм"})
            return render(request, 'Drawing/table.html', context=context)

        height_table = request.POST.get('height_table')  # Висота столу

        if not 749 < int(height_table) < 1201:
            context.update(userinfo(request))
            context.update({"text": "Висота столу не може бути більше 1200 мм або менше 750 мм"})
            return render(request, 'Drawing/table.html', context=context)

        thickness = request.POST.get('thickness')  # Товщина стільниці
        tube = request.POST.get('tube')  # Труба основна
        long_circle = request.POST.get('long_circle')  # Отвори від краю
        rog = request.POST.get('rog')  # Довжина рожка
        rog_tube = request.POST.get('rog_tube')  # Труба рожка
        rog_coor = request.POST.get('rog_coor')  # Відстань до рожка
        len_incline = request.POST.get('len_incline')  # Відступ наклону

        list_size = [int(thickness), int(height_table), int(width_table),
                     int(length_table), int(tube[:2]), int(tube[3:]),
                     int(long_circle), int(rog), int(rog_tube[:2]), int(rog_tube[3:]),
                     int(rog_coor),int(len_incline)]
        print(list_size)

        path1 = draw_A.table_gener_A(list_size)
        name = path1[-10:-4]

        try:
            drawing0 = DrawingTables(id_user=request.user)
            drawing0.published_date = timezone.now()
            drawing0.type = "A-подібний Alpha"
            drawing0.details = f"{width_table},{height_table},{tube[:2]}x{tube[3:]}"
            with open(path1, 'rb') as file:
                drawing0.drawing.save(f'table_type_Alpha_{name}.pdf', File(file))

            drawing0.save()

            print(f"Файл успішно записано.table_{name}.pdf")
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

        return redirect('user')


    if request.user.username:
        context.update(userinfo(request))

    return render(request, 'Drawing/table_type_A.html', context=context)


def drw_dell(request, id=None):
    drawing = get_object_or_404(DrawingTables, id=id)
    drawing.drawing.delete()
    drawing.delete()
    # Видаляємо файл з поля drawing
    return redirect('user')