#include <iostream> //Se importan librerías utilizadas.
#include <iomanip>
#include <thread>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>

/*Función capaz de calcular la potecia de todos
los valores dentro de un array. Recibe el array,
el valor de la posición de inicio dentro del
array y el valor de la posición final para el recorrido
y calcula la potencia de cada uno de los valores
en ese rango.*/

void Potencia(int arr[], int start, int end) {
    for (int i = start; i < end ; i++) {
        int pot = pow(arr[i], 2);
    }
}

int main(void)
{
    clock_t start, end; //Variables que almacenan valores devuelto por clock ()
    srand(time(NULL)); //Permite que en cada compilación rand() genere # distintos.
    const unsigned int size = 100000; //Se define el tamaño del array.
    int randArray[size]{}; //Se declara el array.
    for (int i = 0;i < size; i++) {
        randArray[i] = rand() % 100; //Genera # entre 0 y 99 y los coloca en array.
    }

    start = clock(); //Se guarda variable de tiempo al inicio de ejecución.

    std::thread t1 (Potencia,randArray,0,100000); //Se corre potencia con un solo hilo.
    
    t1.join(); //Hace que el main espere hasta que la operación del hilo termine.

    end = clock(); //Se guarda variable de tiempo al final de ejecución.

    double time_taken = double(end - start) / double(CLOCKS_PER_SEC); //Se pasa de tiempo de procesador a segundos.
   std::cout << "Time taken by program with 1 thread is: " << std::fixed
        << time_taken << std::setprecision(5); //Se muestra el tiempo que tarda la ejecución de la operación.
   std:: cout << " sec " << std::endl;
    return 0; //Se pone pues el main es del tipo int.
}