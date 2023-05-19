from FreshPy import *
import datetime
import matplotlib.pyplot as plt
from tabulate import tabulate


def departamentos(fecha_limite_superior, fecha_limite_inferior):
    # Credenciales del portal web
    api_key = 'sCcA1K0EQhvuJH0OVgec'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)

    # Obtener todos los departamentos y asociarlos
    departamentos = FS.all_departments()
    departamentos_procesados = [{"id": depto["id"], "name": depto["name"]} for depto in departamentos]
    departamentos_dict = {depto['id']: depto['name'] for depto in departamentos_procesados}

    # Obtener los tickets de la página web
    tickets = FS.all_tickets()

    # Contador de los tickets
    count = {}
    tickets_por_departamento = {}

    # Revisión de los tickets para su categorización
    for ticket in tickets:
        if 'department_id' in ticket and ticket[
            'department_id'] in departamentos_dict and fecha_limite_superior >= datetime.datetime.strptime(
                ticket.get("created_at"), '%Y-%m-%dT%H:%M:%SZ') >= fecha_limite_inferior:
            depto_id = ticket['department_id']
            if depto_id in count:
                count[depto_id] += 1
            else:
                count[depto_id] = 1

            # Agrega el ID del ticket a la lista de tickets por departamento
            if depto_id in tickets_por_departamento:
                tickets_por_departamento[depto_id].append(ticket['id'])
            else:
                tickets_por_departamento[depto_id] = [ticket['id']]

    # Crear tabla de tickets por departamento
    table_data = []
    for depto_id, depto_name in departamentos_dict.items():
        if depto_id in tickets_por_departamento:
            tickets = tickets_por_departamento[depto_id]
            ids = ', '.join(str(ticket_id) for ticket_id in tickets)
            table_data.append([depto_name, len(tickets), ids])

    # Mostrar tabla de tickets por departamento
    print(tabulate(table_data, headers=['Departamento', 'Cantidad de Tickets', 'IDs de Tickets']))

    # Crear lista de URLs de tickets
    ticket_urls = [f'{FreshService_domain}/helpdesk/tickets/{ticket_id}' for ticket_ids in
                   tickets_por_departamento.values() for ticket_id in ticket_ids]

    # Mostrar lista de URLs de tickets
    print('\n'.join(ticket_urls))

    # Graficar los resultados en una gráfica de pastel junto con los labels
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Calcula la suma total de elementos
    total = sum(count.values())

    # Crea una lista de strings con el valor real y el nombre del departamento correspondiente
    percentages_and_names = [f'{value} ({departamentos_dict[key]})' for key, value in count.items()]

    # Agrega la gráfica de pastel con porcentaje relativo y los labels
    ax1.pie(count.values(), labels=percentages_and_names, autopct='%1.1f%%')
    ax1.axis('equal')
    ax1.set_title('Tickets por Departamentos desde el '+ str(fecha_limite_inferior) + ' al ' + str(fecha_limite_superior))

    # Agrega un label con el total de elementos
    ax1.text(0, -1.1, f'Total: {total}', fontsize=12, ha='center')

    # Crea una tabla de resumen de tickets por departamento
    table = ax2.table(cellText=table_data, colLabels=['Departamento', 'Cantidad de Tickets', 'IDs de Tickets'],
                      cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    ax2.axis('off')

    plt.show()


