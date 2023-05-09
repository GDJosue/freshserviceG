from FreshPy import *
import datetime
import matplotlib.pyplot as plt

def main():
    # initiate class
    api_key = 'rSkqfcvIaeSD1uVLVunk'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)

    tickets = FS.all_tickets()

    fecha_limite = datetime.datetime(2023, 5, 1)
    sub_category = ['Computadora', 'Impresoras', 'Celular', 'Telefono', 'Perifericos', 'Red', 'MS Office',
                    'Adobe Reader', 'Correo Electronico','Alpha ERP','Windows','Chrome','Ring Central','Biometrico'
                    'Otro Sotware','Acceso a internet','Red lenta','Tarjeta de red','Grabaciones','Monitoreo']

    count = {}
    for ticket in tickets:
        if 'sub_category' in ticket and ticket['sub_category'] in sub_category and datetime.datetime.strptime(ticket.get("created_at"), '%Y-%m-%dT%H:%M:%SZ') >= fecha_limite:
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
    ax.set_title('Tickets por Subcategoría desde el 01/05/2023')

    # Crea una lista de strings con los porcentajes relativos
    percentages = [f'{value / total:.1%}' for key, value in count.items()]

    # Agrega los porcentajes como labels en la leyenda
    legend_labels = [f'{key}: {percentages[i]}' for i, key in enumerate(count.keys())]
    legend = ax.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.setp(legend.get_title(), fontsize=12)
    plt.subplots_adjust(right=0.6)

    plt.show()

if __name__ == '__main__':
    main()