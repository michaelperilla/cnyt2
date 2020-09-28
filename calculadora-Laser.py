##Michael Perilla
##Este codigo esta echo por mi y con apoyo de mi compañero Simon que me explico
##la parte de la doble rendija 
##p1--------------------------------------------

##lo funcion simula los golpes de las canicas 

def canicas(adjunta, estado_inicial, golpes):
    ans = []
    for i in range(golpes):     
        for j in range(len(adjunta)):
            su = (0,0)
            for k in range(len(estado_inicial)):
               su = suma(su,multiplicacion(estado_inicial[k],adjunta[j][k]))
            ans.append(su)
        estado_inicial  = ans
    return ans


##p2--------------------------------------------

##simula el experimento de la doble con balas


def doble_rendija_balas(estado_inicial,posicion_inicial,golpes):
    posicion_inicial = [[i for i in posicion_inicial]]
    for i in range(0,golpes-1):
        estado_inicial = matrizTranspuesta(multiplicacion(estado_inicial,estado_inicial))
        final = multiplicacion(estado_inicial*posicion_inicial)
    return final 

##p3--------------------------------------------

##simula el esperimento de la doble rendija 


def doble_rendija(matriz,golpes):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for x in range(golpes):
                matriz[i][j] = matriz[i][j]*matriz[i][j]
                matriz_final = matriz[i][j]
    return matriz

##p4--------------------------------------------

##simula el de las barras


def barras(adjunta, estado_inicial, golpes):
    ans = []
    for i in range(golpes):
        for j in range(len(adjunta)):
            su = (0,0)
            for k in range(len(estado_inicial)):
               su = suma(su,multiplicacion(estado_inicial[k],adjunta[j][k]))
            ans.append(su)
        estado_inicial  = ans
    return ans

