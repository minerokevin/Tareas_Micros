# Programa que contiene una serie de errores detectables con flake8.

def ParImpar(ent):#Func. determina si el núm es par o impar.
    if ent % int(2)==0:#Se verifica si el residuo es cero.
        print("El número es par.")#Se le indica al usuario que el valor es par.
    else: 
        print("El número es impar.")#De otra forma es impar
ent=int(input("Digite un número:"))#Se solicita el input al ususario.
ParImpar(ent)#Se llama la función

#############################LISTADO DE ERRORES#################################
# 1)Deben dejarse dos espacios antes de cada comentario. 
# 2)Después del numeral debe dejarse un espacio en cada comentario.
# 3)En cada operador matemático se debe dejar espacios por ejemplo: "a = c"
# 4)Se deben dejar dos líneas en blanco después de la definición de la función.
