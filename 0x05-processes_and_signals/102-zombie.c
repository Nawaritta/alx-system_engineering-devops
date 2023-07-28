#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * create_zombie_process - Create a zombie process by forking a child process
 *                         and then exiting it immediately.
 *
 */
void create_zombie_process(void)
{
	pid_t pid = fork();

	if (pid == 0)
	{

		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * infinite_while - Runs an infinite loop with 1sec delay between iterations.
 *
 * Return: Always returns 0.
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
 * main - Entry point of the program
 *        creates 5 zombie processes
 *
 * Return: Always returns 0.
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		create_zombie_process();
	}

	infinite_while();

	return (0);
}
