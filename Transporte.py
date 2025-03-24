#Programa que simula el problema de transporte
import pulp #Libreria para resolver problemas de programación lineal

def main():
    # Solicitar al usuario las ciudades de origen y destino
    ciudades_origen = input("Ingrese las ciudades de origen (separadas por comas): ").split(',')
    ciudades_origen = [ciudad.strip() for ciudad in ciudades_origen]

    ciudades_destino = input("Ingrese las ciudades de destino (separadas por comas): ").split(',')
    ciudades_destino = [ciudad.strip() for ciudad in ciudades_destino]

    # Solicitar la oferta y demanda
    oferta = list(map(int, input("Ingrese la oferta de cada ciudad de origen (separadas por comas): ").split(',')))

    demanda = list(map(int, input("Ingrese la demanda de cada ciudad de destino (separadas por comas): ").split(',')))

    