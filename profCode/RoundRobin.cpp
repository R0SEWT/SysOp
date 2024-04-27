#include <stdio.h>

int main(int n, char **args)
{

    printf("Round Robin");

    int np = 11, procesos[10], quantum = 0, nq = 0;

    double tp = 0; // tiempo promedio.

    int finalizado = 0;

    while (np > 10 || np <= 0)
    {

        printf("\nNumero de procesos [0-10](%d): ", np);

        scanf("%d", &np);
    }

    // para i=0, mientras i<np, hacer:...

    // pedimos el tamaño de cada proceso.

    for (int i = 0; i < np; i++)
    {

        printf("\nInserte el valor CPU Burst del proceso %d :", i + 1);

        scanf("%d", &procesos[i]);
    }

    while (quantum <= 0)
    {

        printf("Tamaño de quantum:");

        scanf("%d", &quantum);
    }

    // Algoritmo RR

    while (finalizado == 0)
    {

        finalizado = 1; // Sí finalizado

        for (int i = 0; i < np; i++)
        {

            if (procesos[i] > 0)
            {

                procesos[i] -= quantum;

                nq++;

                printf("\nQuantum[%d] proceso %d", nq, i + 1);

                if (procesos[i] > 0)
                {

                    finalizado = 0; // No finalizado
                }
                else
                {

                    tp += nq * quantum;
                }
            }
        }
    }

    tp = tp / np;

    printf("\nTiempo promedio RR %f:", tp);

    return 0;
}