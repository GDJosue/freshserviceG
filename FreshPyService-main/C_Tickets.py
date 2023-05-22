from FreshPy import *
import matplotlib.pyplot as plt
from tabulate import tabulate
from collections import defaultdict
import datetime
class C_Tickets():
    api_key = 'sCcA1K0EQhvuJH0OVgec'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)
    # Se obtienen los tickets de la página web
    tickets = FS.all_tickets()
    def categorias(self, fecha_limite_superior, fecha_limite_inferior):
        # Se establecen las categorías a tomarse en cuenta para el gráfico
        sub_category = ['Computadora', 'Impresoras', 'Celular', 'Telefono', 'Perifericos', 'Red', 'MS Office',
                        'Adobe Reader', 'Correo Electronico', 'Alpha ERP', 'Windows', 'Chrome', 'Ring Central',
                        'Biometrico', 'Otro Sotware', 'Acceso a internet', 'Red lenta', 'Tarjeta de red',
                        'Grabaciones', 'Monitoreo', 'No contemplado']
        # Contador de los tickets
        count = {}
        # Revisión de los tickets para su categorización
        for ticket in self.tickets:
            if ticket.get('sub_category') is not None and ticket['sub_category'] in sub_category and fecha_limite_superior >= datetime.datetime.strptime(
                    ticket.get("created_at"), '%Y-%m-%dT%H:%M:%SZ').date() >= fecha_limite_inferior:
                if ticket['sub_category'] in count:
                    count[ticket['sub_category']] += 1
                else:
                    count[ticket['sub_category']] = 1
        fig, ax = plt.subplots()
        # Calcula la suma total de elementos
        total = sum(count.values())
        # Agrega la gráfica de pastel con porcentaje relativo
        ax.pie(count.values(), labels=count.keys(), autopct='%1.1f%%')
        # Agrega un label con el total de elementos
        ax.text(0, -1.1, f'Total: {total}', fontsize=12, ha='center')
        ax.axis('equal')
        ax.set_title(
            'Tickets por Subcategoría desde el ' + str(fecha_limite_inferior) + ' al ' + str(fecha_limite_superior))
        # Crea una lista de strings con el valor real
        percentages = [f'{value}' for key, value in count.items()]
        # Agrega los porcentajes como labels en la leyenda
        legend_labels = [f'{key}: {percentages[i]}' for i, key in enumerate(count.keys())]
        legend = ax.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.setp(legend.get_title(), fontsize=12)
        plt.subplots_adjust(right=0.6)
        plt.show()
    def departamentos(self, fecha_limite_superior, fecha_limite_inferior):
        # Obtener todos los departamentos y asociarlos
        departamentos = self.FS.all_departments()
        departamentos_dict = {depto['id']: depto['name'] for depto in departamentos}
        # Contador de los tickets
        count = defaultdict(int)
        tickets_por_departamento = defaultdict(list)
        # Revisión de los tickets para su categorización y creación de lista de IDs de tickets por departamento
        for ticket in self.tickets:
            if 'department_id' in ticket and ticket[
                'department_id'] in departamentos_dict and fecha_limite_superior >= datetime.datetime.strptime(
                    ticket.get("created_at"), '%Y-%m-%dT%H:%M:%SZ').date() >= fecha_limite_inferior:
                depto_id = ticket['department_id']
                count[depto_id] += 1
                tickets_por_departamento[depto_id].append(ticket['id'])
        # Crear tabla de tickets por departamento
        table_data = [[departamentos_dict[depto_id], len(tickets), ', '.join(map(str, tickets[:5])) + '...'
            if len(tickets) > 5 else ', '.join(map(str, tickets))] for depto_id, tickets
                in tickets_por_departamento.items()]
        # Graficar los resultados en una gráfica de pastel junto con los labels
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        # Calcula la suma total de elementos
        total = sum(count.values())
        # Crea una lista de strings con el valor real y el nombre del departamento correspondiente
        percentages_and_names = [f'{value} ({departamentos_dict[key]})' for key, value in count.items()]
        # Agrega la gráfica de pastel con porcentaje relativo y los labels
        ax1.pie(count.values(), labels=percentages_and_names, autopct='%1.1f%%')
        ax1.axis('equal')
        ax1.set_title(f'Tickets por Departamentos desde el {fecha_limite_inferior} al {fecha_limite_superior}')
        # Agrega un label con el total de elementos
        ax1.text(0, -1.1, f'Total: {total}', fontsize=12, ha='center')
        # Crea una tabla de resumen de tickets por departamento
        table = ax2.table(cellText=table_data, colLabels=['Departamento', 'Cantidad de Tickets', 'IDs de Tickets'],
                          cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)
        ax2.axis('off')
        plt.show()

    def prioridad(self, fecha_limite_superior, fecha_limite_inferior):
        # Se establecen las categorías a tomarse en cuenta para el gráfico
        prioridad = [1, 2, 3, 4]
        # Etiquetas personalizadas para cada prioridad
        etiquetas = {
            1: 'Bajo',
            2: 'Medio',
            3: 'Alto',
            4: 'Urgente'
        }
        # Contador de los tickets
        count = {p: 0 for p in prioridad}

        # Revisión de los tickets para su categorización
        for ticket in self.tickets:
            created_at = datetime.datetime.strptime(ticket.get("created_at"), '%Y-%m-%dT%H:%M:%SZ').date()
            if ticket.get('priority') in prioridad and fecha_limite_superior >= created_at >= fecha_limite_inferior:
                count[ticket['priority']] += 1

        fig, ax = plt.subplots()
        # Calcula la suma total de elementos
        total = sum(count.values())
        # Agrega la gráfica de pastel con porcentaje relativo
        ax.pie(count.values(), labels=[etiquetas[p] for p in prioridad], autopct='%1.1f%%')
        # Agrega un label con el total de elementos
        ax.text(0, -1.1, f'Total: {total}', fontsize=12, ha='center')
        ax.axis('equal')
        ax.set_title(
            'Tickets por prioridad desde el ' + str(fecha_limite_inferior) + ' al ' + str(fecha_limite_superior))

        # Crea una lista de strings con el valor real
        percentages = [f'{value}' for value in count.values()]
        # Agrega los porcentajes como labels en la leyenda
        legend_labels = [f'{etiquetas[prioridad[i]]}: {percentages[i]}' for i in range(len(prioridad))]
        legend = ax.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.setp(legend.get_title(), fontsize=12)
        plt.subplots_adjust(right=0.6)
        plt.show()
