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

    # Solicitar la matriz de costos de envío
    costos = []
    for ciudad_origen in ciudades_origen:
        costos_fila = list(map(int, input(f"Ingrese los costos de envío desde {ciudad_origen} (separados por comas): ").split(',')))
        costos.append(costos_fila)
    
    # Crear el problema de programación lineal con la libreria pulp
    prob = pulp.LpProblem("Problema_de_Transporte", pulp.LpMinimize)

    #Crear variables de decisión
    x = pulp.LpVariable.dicts("x", (range(len(ciudades_origen)), range(len(ciudades_destino))), lowBound=0, cat='Continuous')

    # Función objetivo: minimizar el costo total
    prob += pulp.lpSum([costos[i][j] * x[i][j] for i in range(len(ciudades_origen)) for j in range(len(ciudades_destino))]), "Costo_Total"

    # Restricciones de oferta y demanda
    for i in range(len(ciudades_origen)):
        prob += pulp.lpSum([x[i][j] for j in range(len(ciudades_destino))]) <= oferta[i], f"Oferta_{i}"
    
    for j in range(len(ciudades_destino)):
        prob += pulp.lpSum([x[i][j] for i in range(len(ciudades_origen))]) >= demanda[j], f"Demanda_{j}"
    
    # Resolver el problema
    prob.solve()
    # Mostrar resultados
    print("\nEstado de la solución:", pulp.LpStatus[prob.status])
    print("Costo mínimo total de transporte: $", pulp.value(prob.objective))
    print("Cantidad de productos enviados:")
    
    for i in range(len(ciudades_origen)):
        for j in range(len(ciudades_destino)):
            if x[i][j].varValue > 0:
                print(ciudades_origen[i], "->", ciudades_destino[j], ":", x[i][j].varValue)

