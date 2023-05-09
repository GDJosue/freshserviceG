import datetime
import pandas as pd
import matplotlib.pyplot as plt
from FreshPy import *

def generar_reporte():
    # Iniciar clase FreshPy
    api_key = 'rSkqfcvIaeSD1uVLVunk'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)

    # Obtener todos los tickets
    tickets = FS.all_tickets()

    # Definir fecha límite para los tickets
    fecha_limite = datetime.datetime(2023, 5, 1)

    # Definir categorías
    sub_category = ['Computadora', 'Impresoras', 'Celular', 'Telefono', 'Perifericos', 'Red', 'MS Office',
                    'Adobe Reader', 'Correo Electronico','Alpha ERP','Windows','Chrome','Ring Central','Biometrico',
                    'Otro Sotware','Acceso a internet','Red lenta','Tarjeta de red','Grabaciones','Monitoreo']

    # Contar tickets por categoría
    count = [0] * len(sub_category)
    for ticket in tickets:
        created_at = datetime.datetime.strptime(ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if created_at < fecha_limite:
            category = ticket['category']
            if category in sub_category:
                count[sub_category.index(category)] += 1

    # Crear DataFrame con los datos
    df = pd.DataFrame({'sub_category': sub_category, 'count': count})

    # Generar gráfica de pastel
    plt.pie(count, labels=sub_category, autopct='%1.1f%%')
    plt.title('Tickets por categoría')
    plt.axis('equal')
    plt.show()

    # Exportar datos y gráfica a Excel
    filename = 'reporte.xlsx'
    df.to_excel(filename, index=False)

    workbook = pd.ExcelWriter(filename, engine='xlsxwriter')
    worksheet = workbook.add_worksheet()

    chart = workbook.add_chart({'type': 'pie'})
    chart.add_series({
        'name': 'Tickets por categoría',
        'categories': ['Sheet1', 1, 0, len(sub_category), 0],
        'values': ['Sheet1', 1, 1, len(sub_category), 1],
    })
    chart.set_title({'name': 'Tickets por categoría'})
    chart.set_legend({'position': 'right'})
    worksheet.insert_chart('C1', chart)

    workbook.save()

generar_reporte()
