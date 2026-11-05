from clases.paqueteria import Envio, EnvioExpress, EnvioSobre

def main():
    envio = Envio ("Hugo", 10)
    express = EnvioExpress ("Paco", 20)
    sobre = EnvioSobre ("Luis")

    print (envio.resumen())
    print (express.resumen())
    print (sobre.resumen())

if __name__ == '__main__':
    main()
