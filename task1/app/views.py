from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    inflation = []
    with open(settings.INFLATION_CSV, newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            inflation.append(row)

    # чтение csv-файла и заполнение контекста
    context = {
        'head': inflation[0],
        'data': inflation[1:],
        # 'year': year,
        #         # 'stats': stats,
        #         # 'result': result,
    }

    return render(request, template_name,
                  context)
