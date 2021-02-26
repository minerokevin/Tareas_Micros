#Función que evalúa si un parámetro está entre A-Z y si es un solo carácter
def check_char(x):  
    if x.isalpha() and len(x)==1:  #x entre A-Z y es un solo carácter
        return "0"  #Se retorna 0 en caso de que cumpla las condiciones
    elif x.isalpha() and len(x)>1:
        return "1"  #x entre A-Z, pero contiene más de un carácter
    elif x.isalnum():
        return "2"  #x es alfanumérico
    else:  
        return "404"  #Cualquier caso adicional entra en este error. 

#Función que cambia entre mayúscula o minúscula si check_char retornó un cero
def caps_switch(x):  
    y=check_char()  #Se inicia una variable y igual al retorno de check_char
    if y=="0":  #check_char indica que se tiene un cáracter entre A-Z
        return x.swapcase()  #invierte de minúsculas a mayúsculas o viceversa
    else:  #Cualquier otro caso entra en el else
        return y   #Se retorna el error respectivo según sea el caso

    

