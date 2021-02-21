def char():#Se define una función encargada de devolver el/los carácteres que se envalúan en la siguiente función.
    return "A"#la función retorna lo que se evalúa en check_char

def check_char():#Función que evalúa si un parámetro está entre A-Z y si es un solo carácter
    x=char()#Se inicializa una variable x igual a la función char() para un manejo más sencillo
    
    if x.isalpha() and len(x)==1:#Se evalúa si x se encuentra entre A-Z y si es un solo carácter
        return "0"#Se retorna 0 en caso de que cumpla las condiciones
    elif x.isalpha() and len(x)>1:#Se evalúa si x se encuentra entre A-Z, pero contiene más de un carácter
        return "¡Oh no! La entrada recibió más de un carácter."#Se retorna un error único en caso de que cumpla las condiciones
    elif x.isalnum():#Se evalúa si x es alfanumérico
        return "¡Oh no! La entrada recibió un carácter fuera del rango A-Z."#Se retorna un error único en caso de que cumpla las condiciones
    else:#Cualquier caso adicional entra en este else
        return "Ha ocurrido un error, inténtelo de nuevo."#Se retorna un error único en caso de que cumpla las condiciones
--------------------------------------------------------------------------------------------------------------------------------------------
def caps_switch():#Función capaz de invertir entre mayúscula o minúscula (o viceversa) si check_char retornó un cero
    y=check_char()#Se inicia una variable y igual al retorno de check_char
    z=char()#Se inicia una variable z igual al retorno de char
    
    if y=="0":#Se evalúa si y es igual a 0, es decir, si el retorno de check_char indica que se tiene un cáracter entre A-Z
        return z.swapcase()#En caso de que se cumpla, se invierte de minúsculas a mayúsculas (o viceversa)
    else:#Cualquier otro caso entra en el else
        return y #Se retorna el error respectivo según sea el caso

    

