
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

def a??adir_bit(palabra):
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

def descodificar(r):

    e = None
    palabra_origen = None

    # paso i -- Se calcula el s??ndrome de la palabra recibida, s = r G_24tr.
    s = sindrome(r)  # <- Calculo el sindrome de r
    if peso_palabra(s) == 0:
        print(r)
        return r

    # paso ii -- Si w(s) ??? 3, entonces el vector error es e = (s,0)
    elif peso_palabra(s) <= 3:
        e = np.concatenate((s,ceros),axis=None)  # Concatena s (sindrome de r) con un narray de 0s
    else:
        num_fila = -1
        fila = None
        for i in range(len(A[0])):  # A[0] -> numero de filas
            # paso iii -- Si w(s + ai) ??? 2 para alguna fila ai de la matriz A, entonces el vector error es e = (s + ai,ui).
            if peso_palabra(trunca_binario(s+A[i])) <= 2:
                num_fila = i # En indice_u guarda la posision de la fila
                fila = A[i] # en vector_a guarda la fila
                break
        if num_fila == -1:
            # paso iV -- Se calcula el segundo s??ndrome de la palabra r, s*A.
            s = trunca_binario(np.dot(s,A))
            # paso v -- Si w(s A) ??? 3, entonces el vector error es e = (0,s*A).
            if peso_palabra(s) <= 3:
                e = np.concatenate((ceros,s),axis=None)
            # paso vi -- Si w(s A + ai) ??? 2 para alguna fila ai de la matriz A, entonces el vector error es e = (ui,s A + ai).
            else:
                num_fila = -1
                fila = None
                for i in range(len(A[0])):  # A[0] -> numero de filas
                    if peso_palabra(trunca_binario(s+A[i])) <= 2:
                        num_fila = i
                        fila = A[i]
                        break
                # paso vii -- Si todav??a no se ha determinado el vector error e, solicitar una retransmisi??n pues se han producido m??s de tres errores.
                if e is None:
                    print("Se ha recibido mas de tres errores")
                else:
                    e = np.concatenate((trunca_binario(fila+s),I[num_fila]),axis=None)
        else:
            e = np.concatenate((trunca_binario(fila+s),I[num_fila]),axis=None)

    if e is not None:
        palabra_origen = palabra_original(e,r)
    return palabra_origen

palabra3 = np.array([1,1,1,1,1,1,0,0,0,0,0,0])

print("Palabra origen:", palabra3)
print("Palabra codificada de 23 bits:", codificar_palabra_23(palabra3))
print("\nVamos a a??adir 3 errores a la anterior palabra en el primer, tercer y ultimo bit")
palabra_codificada = np.array([0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1]) # Error en el primer,tercer y ultimo bit

print("Palabra codificada con 3 errores:", palabra_codificada)
print("\nA??adimos un bit a la palabra de 23 bits")
palabra_codificada_24 = a??adir_bit(palabra_codificada)
print("Palabra codificada de 24 bits:", palabra_codificada_24)

palabra_descodificada = descodificar(palabra_codificada_24)
print("Palabra descodificada de 24 bits: ", palabra_descodificada)
palabra_descodificada_23 = eliminar_bit_final(palabra_descodificada)
print("Palabra decodificada de 23 bits: ", palabra_descodificada_23)

palabra_fuente = simbolo_fuente(palabra_descodificada)
print("Palabra fuente", palabra_fuente)

####################################################################################################################
print("Palabra origen:", palabra3)
print("Palabra codificada de 23 bits:", codificar_palabra_23(palabra3))
print("\nVamos a a??adir 4 errores a la anterior palabra en el primer, tercer y ultimo bit")
palabra_codificada = np.array([0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1]) # Error en el primer,tercer y ultimo bit

print("Palabra codificada con 4 errores:", palabra_codificada)
print("\nA??adimos un bit a la palabra de 23 bits")
palabra_codificada_24 = a??adir_bit(palabra_codificada)
print("Palabra codificada de 24 bits:", palabra_codificada_24)

palabra_descodificada = descodificar(palabra_codificada_24)
