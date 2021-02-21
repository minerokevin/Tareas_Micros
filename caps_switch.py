from check_char import * #Se importan las funciones del archivo check_char.py

def caps_switch():#Función capaz de invertir entre mayúscula o minúscula (o viceversa) si check_char retornó un cero
    x=check_char()#Se inicia una variable x igual al retorno de check_char
    y=char()#Se inicia una variable y igual al retorno de char
    
    if x=="0":#Se evalúa si x es igual a 0, es decir, si el retorno de check_char indica que se tiene un cáracter entre A-Z
        return y.swapcase()#En caso de que se cumpla, se invierte de minúsculas a mayúsculas (o viceversa)
    else:#Cualquier otro caso entra en el else
        return x #Se retorna el error respectivo según sea el caso

