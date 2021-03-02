import Métodos  # Se importa el archivo donde están las funciones a testear
import string  # Se importa la librería string
AB_min = list(string.ascii_lowercase)  # Se crea lista del abecedario minúscula
AB_may = list(string.ascii_uppercase)  # Se crea lista del abecedario mayúscula
AB_mix = AB_may + AB_min  # Se crea lista del abecedario en mayúsc. y minúsc.


# Func. que verifica que al ingresar un caracter entre la A-Z a la función
# check_char()ya sea mayúscula o minúscula se obtenga un "0" como resultado.


def test_check_char_a():
    i = 0  # Variable que recorre todas las posiciones de la lista
    while i <= 51:  # Ciclo que permite reccorer toda la lista AB_mix
        retorno = Métodos.check_char(AB_mix[i])  # Evalúan todos los caracteres
        assert retorno == "0"  # Valor esperado de la variable "retorno".
        i = i+1  # Se repite el ciclo con el próximo elemento de la lista.


# Func. que verifica que al ingresar un caracter entre la A-Z a la función
# caps_switch() ya sea mayúscula o minúscula se obtenga un esa misma letra en
# minúscula o mayúscula respectivamente.


def test_caps_switch():
    i = 0  # Variable que recorre todas las posiciones de la lista
    while i <= 51:  # Ciclo que permite recorrer toda la lista AB_mix
        if i <= 25:  # Se analizan inicialmente las letras mayúsculas.
            retorno = Métodos.caps_switch(AB_mix[i])  # Evalúa todas mayúsc.
            assert retorno == AB_min[i]  # Esperado:misma letra pero en minúsc.

        elif i > 25:  # Se analizan ahora las letras minúsculas.
            retorno = Métodos.caps_switch(AB_mix[i])  # Evalúa todas minúsc.
            assert retorno == AB_may[i-26]  # Espera misma letra pero mayúsc.
        i = i+1  # Se repite el ciclo con el próximo elemento de la lista.


# Func. que verifica que al ingresar más de un caracter entre la A-Z la función
# check_char() devuelve el código de error "1" definido por los programadores.


def test_check_char_b():
    retorno = Métodos.check_char("aB")  # Evalúa más de un caracter entre A-Z
    assert retorno == "1"  # El valor esperado es el código de error "1".


# Func. que verifica que al ingresar uno o más caracteres alfanuméricos o
# especiales (que no se encuentran entre A-Z) a check_char() esta devuelve
# el código de error "2" definido para el caso.


def test_check_char_c():
    retorno = Métodos.check_char("@]")  # Se ingresa expresión fuera de A-Z.
    assert retorno == "2"  # El valor esperado es el código de error "2".


# Func. que verifica que al ingresar uno o más elementos que no sean ni
# caracteres ni strings a check_char() esta devuelve el código de error "404"


def test_check_char_d():
    retorno = Métodos.check_char(" ")  # Se evalúa con un espacio vacío.
    assert retorno == "404"  # El valor esperado es el código de error "404".
