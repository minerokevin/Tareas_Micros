def check_char(x):  #Función que evalúa si un parámetro está entre A-Z y si es un solo carácter
    if x.isalpha() and len(x)==1:  #x se encuentra entre A-Z y es un solo carácter
        return "0"  #Se retorna 0 en caso de que cumpla las condiciones
    elif x.isalpha() and len(x)>1:
        return "1"  #x se encuentra entre A-Z, pero contiene más de un carácter
    elif x.isalnum():
        return "2"  #x es alfanumérico
    else:  
        return "404"  #Cualquier caso adicional entra en este error. 

def caps_switch(x):  #Función capaz de invertir entre mayúscula o minúscula si check_char retornó un cero
    y=check_char()  #Se inicia una variable y igual al retorno de check_char
    if y=="0":  #Si el retorno de check_char indica que se tiene un cáracter entre A-Z
        return x.swapcase()  #Se invierte de minúsculas a mayúsculas o viceversa
    else:  #Cualquier otro caso entra en el else
        return y   #Se retorna el error respectivo según sea el caso

    

