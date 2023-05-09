from FreshPy import *
import datetime
import matplotlib.pyplot as plt

def main():
    # Credenciales del portal web
    api_key = 'rSkqfcvIaeSD1uVLVunk'
    FreshService_domain = 'https://camen-q.freshservice.com/'
    FS = FreshPy(api_key, FreshService_domain)

    # Se obtienen los tickets de la pagina web
    Answer = FS.getAnswer("2")

    print(Answer)



if __name__ == '__main__':
    main()