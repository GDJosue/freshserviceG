from FreshPy import *
import datetime
import matplotlib.pyplot as plt

def main():
    # initiate class
    api_key = 'rSkqfcvIaeSD1uVLVunk'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)

    tickets = FS.all_tickets()

    sub_category = ['Computadora', 'Impresoras', 'Celular', 'Telefono', 'Perifericos', 'Red', 'MS Office',
                    'Adobe Reader', 'Correo Electronico','Alpha ERP','Windows','Chrome','Ring Central','Biometrico'
                    'Otro Sotware','Acceso a internet','Red lenta','Tarjeta de red','Grabaciones','Monitoreo']

    count = {}
    for ticket in tickets:
        if 'sub_category' in ticket and ticket['sub_category'] in sub_category:
            if ticket['sub_category'] in count:
                count[ticket['sub_category']] += 1
            else:
                count[ticket['sub_category']] = 1

    fig, ax = plt.subplots()
    ax.pie(count.values(), labels=count.keys(), autopct='%1.1f%%')
    ax.axis('equal')
    ax.set_title('Tickets por Subcategoría todos los tickets')

    legend_labels = [f'{key}: {value}' for key, value in count.items()]
    legend = ax.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.setp(legend.get_title(), fontsize=12)
    plt.subplots_adjust(right=0.6)

    plt.show()

if __name__ == '__main__':
    main()