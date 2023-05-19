from FreshPy import *
import datetime
import matplotlib.pyplot as plt

def main():
    # Credenciales del portal web
    api_key = 'rSkqfcvIaeSD1uVLVunk'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)

    #Se obtienen los tickets de la pagina web
    tickets = FS.all_tickets()

    #se establece la fecha para la toma de los tickers

    fecha_limite_superior = datetime.datetime(2023, 5, 31)
    fecha_limite_inferior = datetime.datetime(2023, 5, 1)

    #Se establecen las categorias a tomarse en cuenta para el grafico
    sub_category = ['Computadora', 'Impresoras', 'Celular', 'Telefono', 'Perifericos', 'Red', 'MS Office',
                    'Adobe Reader', 'Correo Electronico','Alpha ERP','Windows','Chrome','Ring Central','Biometrico'
                    'Otro Sotware','Acceso a internet','Red lenta','Tarjeta de red','Grabaciones','Monitoreo','No contemplado']

    #Contador de los tickets
    count = {}

    #revision de los tickers para su categorización
    for ticket in tickets:
        if 'sub_category' in ticket and ticket['sub_category'] in sub_category and fecha_limite_superior >= datetime.datetime.strptime(ticket.get
        ("created_at"), '%Y-%m-%dT%H:%M:%SZ') >= fecha_limite_inferior:
            if ticket['sub_category'] in count:
                count[ticket['sub_category']] += 1
            else:
                count[ticket['sub_category']] = 1
            print(ticket)

    fig, ax = plt.subplots()

    # Calcula la suma total de elementos
    total = sum(count.values())

    # Agrega la gráfica de pastel con porcentaje relativo
    ax.pie(count.values(), labels=count.keys(), autopct='%1.1f%%')

    # Agrega un label con el total de elementos
    ax.text(0, -1.1, f'Total: {total}', fontsize=12, ha='center')

    ax.axis('equal')
    ax.set_title('Tickets por Subcategoría desde el 01/05/2023')

    # Crea una lista de strings con el valor real
    percentages = [f'{value}' for key, value in count.items()]

    # Agrega los porcentajes como labels en la leyenda
    legend_labels = [f'{key}: {percentages[i]}' for i, key in enumerate(count.keys())]
    legend = ax.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.setp(legend.get_title(), fontsize=12)
    plt.subplots_adjust(right=0.6)

    plt.show()

if __name__ == '__main__':
    main()