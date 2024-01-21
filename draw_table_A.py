import os
import string
import random

from website.settings import BASE_DIR
from datetime import datetime
import math
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def circle(circ, center_x, center_y, radius):
    path = circ.beginPath()
    circ.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    circ.setLineWidth(1)  # Ширина линии

    num_faces = max(24, int(radius / 0.25))  # Збільште кількість вузлів
    for i in range(num_faces + 1):
        angle = 2 * math.pi * i / num_faces
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        if i == 0:
            path.moveTo(x, y)
        else:
            path.lineTo(x, y)
    circ.setFillColorRGB(0, 0, 0)

    # Применяем путь на холсте
    circ.drawPath(path, fill=True)
    return circ

def table_gener_A(size):
    """
        :param name: колір та текстура стільниці
        :param thickness:  товщина стільниці
        :param height_table: висота столу
        :param width_table: ширина столу
        :param length_table: довжина столу
        :param tubex: ширина труби основної
        :param tubey: товщина труби основної
        :param long_circle: відстань від краю отворів
        :param rog: довжина рожку
        :param rog_tubex: ширина труби рожка
        :param rog_tubey: товщина труби рожка
        :param rog_coor: відстань до рожка від краю рамки
        :param len_incline: відступ наклону
        :return:
    """
    # Створюємо рондомний рядок
    random_prefix = ''.join(random.choices(string.ascii_lowercase, k=6))

    pdf_canvas = canvas.Canvas(f"{BASE_DIR}\\func\\1\\table_A_{random_prefix}.pdf",
                               pagesize=(1500, 1000))

    pdfmetrics.registerFont(TTFont('Autoproject', f'{BASE_DIR}\\func\Autoproject.ttf'))

    name = "Дуб острава"

    # довжина стільниці
    length_table = size[3]

    # Висота столу
    height = size[1]

    # Ширина столу
    width = size[2]

    # відступ наклону
    len_incline = size[11]

    # товщина стільниці
    thickness = size[0]

    # товщина ніжки
    leg = 4

    # труба основна
    tubex = size[4]
    tubey = size[5]

    # Розмір від краю до отворів
    long_circle = size[6]

    # труба рожка
    tubex_rog = size[8]
    tubey_rog = size[9]

    # від краю до рожка
    len_rog = size[10]

    # довжина рожка
    rog = size[7]

    # Внутрішні розміри

    up_width = width - len_incline * 2

    # довжина ніжок  # Обчислюємо відстань теоремою Піфагора
    long_l = math.sqrt(height**2 + len_incline**2)
    long_l_r = round(long_l)

    # # Обчислюємо тангенс кута нахилу
    tan_theta = len_incline / height

    # Знаходимо кут нахилу в радіанах
    angle_of_inclination_rad = math.atan(tan_theta)

    # Перетворюємо кут нахилу з радіан в градуси
    tilt_angle = math.degrees(angle_of_inclination_rad)

    tilt_angle_rounded = round(tilt_angle, 2)

    # кут нахилу правої ніжки
    right_angle = tilt_angle_rounded + 90

    # кут нахилу лівої ніжки
    left_angle = 90 - tilt_angle_rounded

    clear_height = height - thickness - leg

    # Початкові координати

    x = 200
    y = 100

    x2 = 700


    current_date = datetime.now().date()
    current_time = datetime.now().time()

    # Рамка та табличка
    pdf_canvas.rect(55, 15, 1430, 970, fill=False)
    pdf_canvas.rect(1155, 15, 330, 97, fill=False)
    pdf_canvas.rect(1285, 15, 100, 70, fill=False)

    pdf_canvas.rect(1285, 85, 200, 27, fill=False)

    pdf_canvas.rect(1155, 15, 130, 12, fill=False)
    pdf_canvas.rect(1155, 39, 130, 12, fill=False)
    pdf_canvas.rect(1155, 63, 130, 12, fill=False)
    pdf_canvas.rect(1155, 87, 130, 12, fill=False)
    pdf_canvas.rect(1185, 15, 50, 97, fill=False)
    pdf_canvas.rect(1265, 15, 20, 97, fill=False)

    pdf_canvas.rect(1385, 73, 100, 12, fill=False)
    pdf_canvas.rect(1385, 61, 100, 12, fill=False)
    pdf_canvas.rect(1418, 61, 33, 24, fill=False)


    # деталь з рожками

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x + 50, y + 550, 200, 30, fill=True)

    # лівий рожок
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x + 100, y + 580, 15, 90, fill=True)

    # правий рожок
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x + 185, y + 580, 15, 90, fill=True)

    # відстань від ркаю до рожка
    pdf_canvas.line(x + 250, y + 580, x + 250, y + 670)
    pdf_canvas.line(x + 200, y + 670, x + 270, y + 670)
    pdf_canvas.line(x + 250, y + 580, x + 270, y + 580)
    pdf_canvas.line(x + 200, y + 610, x + 250, y + 610)

    pdf_canvas.setFont("Autoproject", 16)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x + 205, y + 615, f"{len_rog} мм")

    # довжина рожка
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.rotate(-90)
    pdf_canvas.drawString(-740, 455, f"{rog} мм")
    pdf_canvas.rotate(90)

    # від краю до отворів в верхній деталі
    pdf_canvas = circle(pdf_canvas, x + 90, y + 557, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 130, y + 557, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 170, y + 557, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 210, y + 557, 1.5)

    pdf_canvas.line(x - 30, y + 557, x + 210, y + 557)
    pdf_canvas.line(x - 30, y + 550, x + 50, y + 550)
    pdf_canvas.line(x - 20, y + 570, x - 20, y + 500)

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.rotate(90)
    pdf_canvas.drawString(x + 410, -y + -75, f"{long_circle} мм")
    pdf_canvas.rotate(-90)


    # отвори рожків
    # лівий
    pdf_canvas = circle(pdf_canvas, x + 107.5, y + 660, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 107.5, y + 635, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 107.5, y + 610, 1.5)

    # правий
    pdf_canvas = circle(pdf_canvas, x + 192.5, y + 660, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 192.5, y + 635, 1.5)
    pdf_canvas = circle(pdf_canvas, x + 192.5, y + 610, 1.5)

    # розміри отворів рожків
    pdf_canvas.line(x + 100, y + 670, x + 70, y + 670)
    pdf_canvas.line(x + 107.5, y + 660, x - 10, y + 660)
    pdf_canvas.line(x + 107.5, y + 635, x - 10, y + 635)
    pdf_canvas.line(x + 107.5, y + 610, x - 10, y + 610)
    pdf_canvas.line(x + 70, y + 670, x + 70, y + 610)

    pdf_canvas.setFont("Autoproject", 16)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x - 10, y + 663, f"{25} мм д.5 мм")
    pdf_canvas.drawString(x - 10, y + 638, f"{75} мм д.5 мм")
    pdf_canvas.drawString(x - 10, y + 613, f"{125} мм д.5 мм")




    # ліва деталь

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x, y)
    path.lineTo(x + 50, y + 350)
    path.lineTo(x + 70, y + 330)
    path.lineTo(x + 28, y + 22)
    path.lineTo(x, y)

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)


    # розміри висоти
    pdf_canvas.line(x, y, x - 50, y)
    pdf_canvas.line(x + 50, y + 350, x - 50, y + 350)
    pdf_canvas.line(x - 30, y, x - 30, y + 350)

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.rotate(90)
    pdf_canvas.drawString(x + 60, -y + -65, f"{clear_height} мм")
    pdf_canvas.rotate(-90)

    # розміри наклону
    pdf_canvas.line(x, y, x, y - 60)
    pdf_canvas.line(x + 50, y + 350, x + 50, y + 420)
    pdf_canvas.line(x + 250, y + 350, x + 250, y + 420)
    pdf_canvas.line(x + 300, y - 60, x + 300, y + 420)
    pdf_canvas.line(x + 50, y + 400, x + 340, y + 400)
    pdf_canvas.line(x, y - 40, x + 300, y - 40)

    # розміри ширини нижньої деталі
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x + 120, y - 35, f"{width} мм")

    pdf_canvas.drawString(x + 130, y + 405, f"{up_width} мм")

    pdf_canvas.drawString(x + 255, y + 405, f"{len_incline} мм")

    # кут нахилу
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x + 275, y + 175)
    path.lineTo(x + 277, y + 176)
    path.lineTo(x + 280, y + 177)
    path.lineTo(x + 284, y + 178)
    path.lineTo(x + 287, y + 178.3)
    path.lineTo(x + 292, y + 178)
    path.lineTo(x + 295, y + 177.3)
    path.lineTo(x + 300, y + 176)
    path.lineTo(x + 380, y + 176)
    pdf_canvas.drawPath(path, fill=False)
    pdf_canvas.drawString(x + 310, y + 183, f"Кут {right_angle} гр")

    # верхня деталь

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x + 50, y + 350)
    path.lineTo(x + 250, y + 350)
    path.lineTo(x + 230, y + 330)
    path.lineTo(x + 70, y + 330)
    path.lineTo(x + 50, y + 350)

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    # права деталь
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x + 250, y + 350)
    path.lineTo(x + 300, y)
    path.lineTo(x + 273, y + 22)
    path.lineTo(x + 230, y + 330)
    path.lineTo(x + 250, y + 350)

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    # нижня деталь
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x, y)
    path.lineTo(x + 28, y + 22)
    path.lineTo(x + 273, y + 22)
    path.lineTo(x + 300, y)
    path.lineTo(x, y)

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)


    # окремі деталі та їх розміри
    # верхня деталь

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x2, y + 820)
    path.lineTo(x2 + 28, y + 820 + 22)
    path.lineTo(x2 + (up_width / 2) - 28, y + 820 + 22)
    path.lineTo(x2 + up_width / 2, y + 820)
    path.lineTo(x2, y + 820)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    pdf_canvas.line(x2, y + 820, x2, y + 795)
    pdf_canvas.line(x2 + (up_width / 2), y + 820, x2 + (up_width / 2), y + 795)
    pdf_canvas.line(x2, y + 800, x2 + (up_width / 2), y + 800)

    pdf_canvas.setFont("Autoproject", 15)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + (up_width / 4) - 20, y + 802, f"{up_width} мм")

    # кут нахилу
    pdf_canvas.line(x2 + 12, y + 830, x2, y + 840)
    pdf_canvas.line(x2, y + 840, x2 - 70, y + 840)
    pdf_canvas.drawString(x2 - 70, y + 843, f"Кут {round(right_angle / 2, 2)} гр")

    pdf_canvas.line(x2 + (up_width / 2) - 16, y + 820 + 12, x2 + (up_width / 2), y + 840)
    pdf_canvas.line(x2 + (up_width / 2), y + 840, x2 + (up_width / 2) + 70, y + 840)
    pdf_canvas.drawString(x2 + (up_width / 2), y + 843, f"Кут {round(right_angle / 2, 2)} гр")

    # сама деталь
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x2, y + 750, up_width / 2, tubex / 2, fill=True)

    pdf_canvas.line(x2, y + 750, x2 - 20, y + 750)
    pdf_canvas.line(x2 + 160, y + 758, x2 - 50, y + 758)
    pdf_canvas.line(x2 - 10, y + 750, x2 - 10, y + 758)

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 - 50, y + 760, f"{long_circle} мм")

    pdf_canvas.line(x2 + up_width / 2, y + 750, x2 + up_width / 2 + 30, y + 750)
    pdf_canvas.line(x2 + up_width / 2, y + 750 + tubex / 2, x2 + up_width / 2 + 30, y + 750 + tubex / 2)
    pdf_canvas.line(x2 + up_width / 2 + 20, y + 750, x2 + up_width / 2 + 20, y + 750 + tubex / 2)

    pdf_canvas.drawString(x2 + up_width / 2 + 28, y + 755, f"{tubex} мм")
    pdf_canvas.drawString(x2 + up_width / 2 + 50, y + 810, f"Деталі верхні з отворами 2 шт")
    pdf_canvas.drawString(x2 + up_width / 2 + 50, y + 790, f"Труба {tubex}x{tubey} мм")


    pdf_canvas = circle(pdf_canvas, x2 + 40, y + 758, 1.5)
    pdf_canvas = circle(pdf_canvas, x2 + 80, y + 758, 1.5)
    pdf_canvas = circle(pdf_canvas, x2 + 120, y + 758, 1.5)
    pdf_canvas = circle(pdf_canvas, x2 + 160, y + 758, 1.5)


    pdf_canvas.line(x2, y + 750, x2, y + 710)
    pdf_canvas.line(x2 + 40, y + 758, x2 + 40, y + 710)
    pdf_canvas.line(x2 + 80, y + 758, x2 + 80, y + 710)
    pdf_canvas.line(x2 + 120, y + 758, x2 + 120, y + 710)
    pdf_canvas.line(x2 + 160, y + 758, x2 + 160, y + 710)
    pdf_canvas.line(x2, y + 720, x2 + 160, y + 720)

    pdf_canvas.setFont("Autoproject", 15)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + 3, y + 725, f"{80} мм")
    pdf_canvas.drawString(x2 + 3, y + 705, f"д.{5} мм")

    pdf_canvas.drawString(x2 + 42, y + 725, f"{160} мм")
    pdf_canvas.drawString(x2 + 42, y + 705, f"д.{5} мм")

    pdf_canvas.drawString(x2 + 82, y + 725, f"{240} мм")
    pdf_canvas.drawString(x2 + 82, y + 705, f"д.{5} мм")

    pdf_canvas.drawString(x2 + 122, y + 725, f"{320} мм")
    pdf_canvas.drawString(x2 + 122, y + 705, f"д.{5} мм")


    if up_width > 499:

        pdf_canvas = circle(pdf_canvas, x2 + 200, y + 758, 1.5)

        pdf_canvas.drawString(x2 + 162, y + 725, f"{400} мм")
        pdf_canvas.drawString(x2 + 162, y + 705, f"д.{5} мм")

        pdf_canvas.line(x2 + 200, y + 758, x2 + 200, y + 710)
        pdf_canvas.line(x2 + 160, y + 720, x2 + 200, y + 720)
        pdf_canvas.line(x2 + 160, y + 758, x2 + 200, y + 758)


    # бокові деталі (ніжки)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x2, y + 660)
    path.lineTo(x2 + 28, y + 660 + 22)
    path.lineTo(x2 + long_l_r / 2 - 28, y + 660 + 22)
    path.lineTo(x2 + long_l_r / 2, y + 660)
    path.lineTo(x2, y + 660)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    pdf_canvas.line(x2, y + 660, x2, y + 635)
    pdf_canvas.line(x2 + long_l_r / 2, y + 660, x2 + long_l_r / 2, y + 635)
    pdf_canvas.line(x2, y + 640, x2 + long_l_r / 2, y + 640)

    pdf_canvas.setFont("Autoproject", 15)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + long_l_r / 4 - 20, y + 642, f"{long_l_r} мм")

    # кут нахилу
    pdf_canvas.line(x2 + 12, y + 670, x2, y + 680)
    pdf_canvas.line(x2, y + 680, x2 - 70, y + 680)
    pdf_canvas.drawString(x2 - 70, y + 683, f"Кут {round(right_angle / 2, 2)} гр")

    pdf_canvas.line(x2 + (long_l_r / 2) - 12, y + 670, x2 + (long_l_r / 2), y + 680)
    pdf_canvas.line(x2 + (long_l_r / 2), y + 680, x2 + (long_l_r / 2) + 70, y + 680)
    pdf_canvas.drawString(x2 + (long_l_r / 2), y + 683, f"Кут {round(left_angle / 2, 2)} гр")

    pdf_canvas.line(x2 + long_l_r / 2, y + 590, x2 + long_l_r / 2 + 30, y + 590)
    pdf_canvas.line(x2 + long_l_r / 2, y + 590 + tubex / 2, x2 + long_l_r / 2 + 30, y + 590 + tubex / 2)
    pdf_canvas.line(x2 + long_l_r / 2 + 20, y + 590, x2 + long_l_r / 2 + 20, y + 590 + tubex / 2)

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)

    pdf_canvas.drawString(x2 + long_l_r / 2 + 28, y + 595, f"{tubex} мм")
    pdf_canvas.drawString(x2 + long_l_r / 2 + 50, y + 650, f"Деталі бокові 4 шт")
    pdf_canvas.drawString(x2 + long_l_r / 2 + 50, y + 630, f"Труба {tubex}x{tubey} мм")

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x2, y + 590, long_l_r / 2, tubex / 2, fill=True)

    # Нижні деталі

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(x2, y + 540)
    path.lineTo(x2 + 28, y + 540 + 22)
    path.lineTo(x2 + width / 2 - 28, y + 540 + 22)
    path.lineTo(x2 + width / 2, y + 540)
    path.lineTo(x2, y + 540)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    pdf_canvas.line(x2, y + 540, x2, y + 515)
    pdf_canvas.line(x2 + width / 2, y + 540, x2 + width / 2, y + 515)
    pdf_canvas.line(x2, y + 520, x2 + width / 2, y + 520)

    pdf_canvas.setFont("Autoproject", 15)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + width / 4 - 20, y + 522, f"{width} мм")

    pdf_canvas.line(x2 + 12, y + 550, x2, y + 560)
    pdf_canvas.line(x2, y + 560, x2 - 70, y + 560)
    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 - 70, y + 563, f"Кут {round(left_angle / 2, 2)} гр")

    pdf_canvas.line(x2 + (width / 2) - 12, y + 550, x2 + (width / 2), y + 560)
    pdf_canvas.line(x2 + (width / 2), y + 560, x2 + (width / 2) + 70, y + 560)
    pdf_canvas.drawString(x2 + (width / 2), y + 563, f"Кут {round(left_angle / 2, 2)} гр")

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x2, y + 470, width / 2, tubex / 2, fill=True)

    pdf_canvas.line(x2 + width / 2, y + 470, x2 + width / 2 + 30, y + 470)
    pdf_canvas.line(x2 + width / 2, y + 470 + tubex / 2, x2 + width / 2 + 30, y + 470 + tubex / 2)
    pdf_canvas.line(x2 + width / 2 + 20, y + 470, x2 + width / 2 + 20, y + 470 + tubex / 2)

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + width / 2 + 28, y + 475, f"{tubex} мм")
    pdf_canvas.drawString(x2 + width / 2 + 50, y + 530, f"Деталі нижні з отворами під ніжки 2 шт")
    pdf_canvas.drawString(x2 + width / 2 + 50, y + 510, f"Труба {tubex}x{tubey} мм")

    # отвори ніжок
    pdf_canvas = circle(pdf_canvas, x2 + tubex / 4, y + 470 + tubex / 4, 1.5)
    pdf_canvas.line(x2, y + 470, x2, y + 430)
    pdf_canvas.line(x2 + tubex / 4, y + 470 + tubex / 4, x2 + tubex / 4, y + 430)
    pdf_canvas.line(x2, y + 435, x2 + 70, y + 435)

    pdf_canvas.setFont("Autoproject", 16)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + tubex / 4 + 5, y + 440, f"Відступ {int(tubey / 2)}мм д. 9мм")

    pdf_canvas = circle(pdf_canvas, x2 + width / 2 - tubex / 4, y + 470 + tubex / 4, 1.5)

    # Рожки

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.rect(x2, y + 390, rog / 2, tubex_rog / 2, fill=True)

    pdf_canvas = circle(pdf_canvas, x2 + 12.5, y + 390 + tubex_rog / 4, 1.5)
    pdf_canvas = circle(pdf_canvas, x2 + 37.5, y + 390 + tubex_rog / 4, 1.5)
    pdf_canvas = circle(pdf_canvas, x2 + 62.5, y + 390 + tubex_rog / 4, 1.5)

    pdf_canvas.line(x2, y + 390, x2, y + 370)
    pdf_canvas.line(x2 + rog / 2, y + 390, x2 + rog / 2, y + 370)
    pdf_canvas.line(x2, y + 375, x2 + rog / 2, y + 375)

    pdf_canvas.setFont("Autoproject", 15)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.drawString(x2 + rog / 4 - 20, y + 377, f"{rog} мм")
    pdf_canvas.drawString(x2 + rog / 2 + 30, y + 393, f"{tubex_rog} мм")

    pdf_canvas.line(x2 + rog / 2, y + 390, x2 + rog / 2 + 60, y + 390)
    pdf_canvas.line(x2 + rog / 2, y + 390 + tubex_rog / 2, x2 + rog / 2 + 25, y + 390 + tubex_rog / 2)
    pdf_canvas.line(x2 + rog / 2 + 20, y + 390, x2 + rog / 2 + 20, y + 390 + tubex_rog / 2)

    pdf_canvas.setFont("Autoproject", 18)
    pdf_canvas.setFillColor(colors.black)

    pdf_canvas.drawString(x2 + rog / 2 + 80, y + 413, f"Деталі рожки з отворами 4 шт")
    pdf_canvas.drawString(x2 + rog / 2 + 80, y + 393, f"Труба {tubex_rog}x{tubey_rog} мм")

    # Загальний вигляд
    # права деталь
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(900, 340)
    path.lineTo(928, 362)
    path.lineTo(968, 62)
    path.lineTo(940, 42)
    path.lineTo(900, 340)
    path.lineTo(890, 330)
    path.lineTo(928, 62)
    path.lineTo(940, 42)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    # верхня деталь
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(928, 362)
    path.lineTo(805, 422)
    path.lineTo(775, 400)
    path.lineTo(900, 340)
    path.lineTo(928, 362)
    path.lineTo(900, 340)
    path.lineTo(890, 330)
    path.lineTo(781, 385)
    path.lineTo(775, 400)
    path.lineTo(900, 340)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    pdf_canvas = circle(pdf_canvas, 905, 365, 1)
    pdf_canvas = circle(pdf_canvas, 875, 380, 1)
    pdf_canvas = circle(pdf_canvas, 845, 395, 1)
    pdf_canvas = circle(pdf_canvas, 815, 409, 1)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(775, 400)
    path.lineTo(730, 162)
    path.lineTo(742, 168)
    path.lineTo(781, 385)
    path.lineTo(775, 400)
    path.lineTo(781, 385)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(781, 385)
    path.lineTo(800, 375.5)
    path.lineTo(765, 185)
    path.lineTo(742, 168)
    path.lineTo(781, 385)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(940, 42)
    path.lineTo(730, 162)
    path.lineTo(742, 168)
    path.lineTo(928, 62)

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(923.5, 92)
    path.lineTo(765, 185)
    path.lineTo(742, 168)
    path.lineTo(928, 62)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    # рожки
    # лівий
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(796, 390)
    path.lineTo(736, 350)
    path.lineTo(736, 338)
    path.lineTo(745, 333)
    path.lineTo(745, 345)
    path.lineTo(736, 350)
    path.lineTo(745, 345)
    path.lineTo(806, 385)
    path.lineTo(796, 390)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(806, 385)
    path.lineTo(805, 373)
    path.lineTo(745, 333)
    path.lineTo(745, 345)
    path.lineTo(806, 385)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    pdf_canvas = circle(pdf_canvas, 748, 353, 1)
    pdf_canvas = circle(pdf_canvas, 763, 362, 1)
    pdf_canvas = circle(pdf_canvas, 778, 372, 1)

    # правий
    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(866, 356)
    path.lineTo(806, 313)
    path.lineTo(806, 300)
    path.lineTo(817, 293.5)
    path.lineTo(817, 307)
    path.lineTo(806, 313)
    path.lineTo(817, 307)
    path.lineTo(878, 350)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    path = pdf_canvas.beginPath()
    pdf_canvas.setStrokeColorRGB(0, 0, 0)  # Цвет линии: черный
    pdf_canvas.setLineWidth(1)  # Ширина линии
    path.moveTo(878, 350)
    path.lineTo(877, 336.5)
    path.lineTo(817, 293.5)
    path.lineTo(817, 307)
    path.lineTo(878, 350)
    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.drawPath(path, fill=True)

    pdf_canvas = circle(pdf_canvas, 818, 315, 1)
    pdf_canvas = circle(pdf_canvas, 833, 325, 1)
    pdf_canvas = circle(pdf_canvas, 848, 335, 1)

    # Шлях до зображення
    image_path1 = f'{BASE_DIR}/func/2.jpeg'
    pdf_canvas.drawImage(image_path1, 1160, 130, 200, 400, mask='auto')

    pdf_canvas.setFillColor(colors.HexColor("#9c9998"))
    pdf_canvas.setLineWidth(2)
    pdf_canvas.rect(1160, 130, 200, 400, fill=False)

    pdf_canvas.setLineWidth(1)
    pdf_canvas.line(1160, 530, 1160, 550)
    pdf_canvas.line(1360, 530, 1360, 550)
    pdf_canvas.line(1160, 540, 1360, 540)

    pdf_canvas.line(1360, 530, 1380, 550)
    pdf_canvas.line(1380, 550, 1480, 550)

    pdf_canvas.line(1360, 530, 1390, 530)
    pdf_canvas.line(1360, 130, 1390, 130)
    pdf_canvas.line(1380, 530, 1380, 130)

    pdf_canvas.setFont("Autoproject", 16)
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.rotate(-90)
    pdf_canvas.drawString(-390, 1385, f"{length_table} мм")
    pdf_canvas.rotate(90)

    pdf_canvas.setFont("Autoproject", 16)  # Устанавливаем шрифт и размер текста
    pdf_canvas.setFillColor(colors.black)  # Устанавливаем цвет текста
    pdf_canvas.drawString(1240, 545, f"{width} мм")  # Ширина стільниці
    pdf_canvas.drawString(1380, 552, f"Товщина {thickness} мм")  # Товщина столешніци

    pdf_canvas.setFont("Autoproject", 22)  # Устанавливаем шрифт и размер текста
    pdf_canvas.setFillColor(colors.black)  # Устанавливаем цвет текста
    pdf_canvas.drawString(1160, 610, f"Стільниця: {name}")  # Назва стільниці


    pdf_canvas.setFont("Autoproject", 18)  # Устанавливаем шрифт и размер текста
    pdf_canvas.setFillColor(colors.black)  # Устанавливаем цвет текста
    pdf_canvas.drawString(1292, 92, "Стіл Loft Alpha")  # Назва

    pdf_canvas.drawString(1390, 43, f"{current_date}")  # Дата
    pdf_canvas.drawString(1390, 22, f"{str(current_time)[:8]}")  # Час

    pdf_canvas.save()

    return os.path.join(BASE_DIR, 'func', '1', f'table_A_{random_prefix}.pdf')
