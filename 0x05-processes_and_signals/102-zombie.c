#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - an infinite loop that simlates interaction
 * Return: 0 if success
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - is the program that creates 5 zombie processes.It displays Zombie process created, PID: ZOMBIE_PID
 * Return: 0 if success.
 */

int main(void)
{
	pid_t zombie;
	int zmbieLoop;

	for (zmbieLoop = 0; zmbieLoop < 5; zmbieLoop++)
	{
		zombie = fork();
		if (zombie == 0)
			exit(EXIT_FAILURE);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
