
import numpy as np

# Matriz Generadora
G_24 = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1]])

G_23 = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]])

# Matrices Generadoras transpuesta
G_24tr = np.transpose(G_24)
G_23tr = np.transpose(G_23)

# Matriz Identidad
I = np.diag([1,1,1,1,1,1,1,1,1,1,1,1])

# Matriz A
A = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
              [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
              [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
              [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
              [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
              [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
              [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
              [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
              [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
              [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1]])

# Array de ceros
ceros = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def trunca_binario(palabra): # Hacemos que la matriz sea binaria
    for i in range(len(palabra)):
        if palabra[i] % 2 == 0:
            palabra[i] = 0
        else:
            palabra[i] = 1
    return palabra

def peso_palabra(palabra):
    toret = 0;
    for i in range(len(palabra)):
        if palabra[i] == 1:
            toret += 1
            i += 1
    return toret

def simbolo_fuente(palabra):
    if palabra is not None:
        m, d = np.split(palabra,2)
        return m
    else:
        return None

def codificar_palabra_24(palabra):
    return trunca_binario(np.dot(palabra,G_24))

def codificar_palabra_23(palabra):
    return trunca_binario(np.dot(palabra,G_23))

def sindrome(palabra):
    return trunca_binario(np.dot(palabra,G_24tr))

def añadir_bit(palabra):
    if peso_palabra(palabra) % 2 == 0:
        palabra = np.concatenate((palabra,1), axis=None)
        return palabra
    else:
        palabra = np.concatenate((palabra, 0), axis=None)
        return palabra

def eliminar_bit_final(palabra):
    palabra = np.delete(palabra, -1)
    return palabra

# c = r + e
def palabra_original(palabra_error,palabra_recibida):
    return trunca_binario(palabra_error+palabra_recibida)

def decodificar(r):

    e = None
    palabra_origen = None

    # paso i -- Se calcula el síndrome de la palabra recibida, s = r G_24tr.
    s = sindrome(r)  # <- Calculo el sindrome de r
    if peso_palabra(s) == 0:
        return r

    # paso ii -- Si w(s) ≤ 3, entonces el vector error es e = (s,0)
    elif peso_palabra(s) <= 3:
        e = np.concatenate((s, ceros), axis=None)  # Concatena s (sindrome de r) con un narray de 0s
        print("Holas9")
    else:
        num_fila = -1
        fila = None
        for i in range(len(A[0])):  # A[0] -> numero de filas
            # paso iii -- Si w(s + ai) ≤ 2 para alguna fila ai de la matriz A, entonces el vector error es e = (s + ai,ui).
            if peso_palabra(trunca_binario(s + A[i])) <= 2:
                print("Holas2")
                num_fila = i
                fila = A[i]
                break
        if num_fila == -1:
            # paso iV -- Se calcula el segundo síndrome de la palabra r, s*A.
            s = np.sindrome(trunca_binario(np.dot(s, A)))
            print("Holas3")
            # paso v -- Si w(s A) ≤ 3, entonces el vector error es e = (0,s*A).
            if peso_palabra(s) <= 3:
                e = np.concatenate((ceros, s), axis=None)
                print("Holas7")
            # paso vi -- Si w(s A + ai) ≤ 2 para alguna fila ai de la matriz A, entonces el vector error es e = (ui,s A + ai).
            else:
                print("Holas4")
                num_fila = -1
                fila = None
                for i in range(len(A[0])):  # A[0] -> numero de filas
                    if peso_palabra(trunca_binario(s + A[i])) <= 2:
                        num_fila = i
                        fila = A[i]
                        break
                # paso vii -- Si todavía no se ha determinado el vector error e, solicitar una retransmisión pues se han producido más de tres errores.
                if e is None:
                    print("Se ha recibido mas de cuatro errores")
                else:
                    print("Holas5")
                    e = np.concatenate((trunca_binario(fila + s), I[num_fila]), axis=None)
        else:
            print("Holas6")
            e = np.concatenate((trunca_binario(fila + s), I[num_fila]), axis=None)

    if e is not None:
        print("Holas8")
        palabra_origen = palabra_original(e,r)
    return palabra_origen


palabra = np.array([0,0,0,0,0,0,1,1,1,1,1,1])
palabra2 = np.array([1,1,1,1,1,1,0,0,0,0,0,0])
palabra3 = np.array([0,0,0,1,1,1,1,1,1,0,0,0])

palabra23 = np.array([0,0,0,0,0,0,1,1,1,1,1,1])

print("Palabra con recibida", palabra23)

palabra_codificada_23 = codificar_palabra_23(palabra23) # -> 23 bits
palabra_codificada_24 = codificar_palabra_24(palabra23) # -> 24 bits
print(palabra_codificada_23, len(palabra_codificada_23))
print(palabra_codificada_24, len(palabra_codificada_24))
palabra_codificada_24 = añadir_bit(palabra_codificada_23)
print("Palabra codifcada: ", palabra_codificada_24)
decodificada = decodificar(palabra_codificada_24)

simbolo_palabra = simbolo_fuente(decodificada)
simbolo_palabra_final = eliminar_bit_final(simbolo_palabra)
print(f"Si probamos la corrección de errores el resultado es {decodificada}, por lo que su simbolo fuente es {simbolo_palabra_final}")

# print(f"CODIFICACIÓN DE UNA PALABRA SIN ERRORES\n")
# print("Palabra recibida", palabra)
# codificada = codificar_palabra(palabra)
# print("Palabra codificada", codificada)
# descodificacion_palabra = decodificar(codificada)
# simbolo_palabra = simbolo_fuente(descodificacion_palabra)
# print(f"Si probamos la corrección de errores el resultado es {descodificacion_palabra}, por lo que su simbolo fuente es {simbolo_palabra}")
# print(f"-----------------------------------------------------------------------------")
#
# print(f"CODIFICACIÓN DE UN VECTOR CON UN ERRORES\n")
# print(f"\tProbamos a codificar una palabra: ")
# codificacion_palabra2 = np.array([0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0])
# print(f"\tLa codificación de la palabra {palabra2} es {codificacion_palabra2}")
# print(f"\tVemos que no es correcta, por lo que vamos a usar la corrección de errores")
# decodificacion_palabra2 = decodificar(codificacion_palabra2)
# simbolo_fuente_palabra2 = simbolo_fuente(decodificacion_palabra2)
# print(f"\tEl resultado de la correción de errores nos proporciona el vector corregido {decodificacion_palabra2}, por lo que su simbolo fuente es {simbolo_fuente_palabra2}")
# print(f"-----------------------------------------------------------------------------")
#
# print(f"CODIFICACIÓN DE UN VECTOR CON DOS ERRORES\n")
# print(f"\tProbamos a codificar el punto cardinal Oeste: ")
# decodificacion_palabra3 = np.array([1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0])
# print(f"\tLa codificación de la {palabra3} es {decodificacion_palabra3}")
# print(f"\tVemos que no es correcta, por lo que vamos a usar la corrección de errores")
# decodificacion_palabra3 = decodificar(decodificacion_palabra3)
# simbolo_fuente_palabra3 = simbolo_fuente(decodificacion_palabra3)
# print(f"\tEl resultado de la correción de errores nos proporciona el vector corregido {decodificacion_palabra3}, por lo que su simbolo fuente es {simbolo_fuente_palabra3}")
