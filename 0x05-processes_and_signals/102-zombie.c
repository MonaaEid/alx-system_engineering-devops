#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++) {
		pid = fork();

		if (pid == 0) {
			exit(0);
		} else if (pid > 0) {
			printf("Zombie process created, PID: %d\n", pid);
		} else {
			printf("Fork failed\n");
			exit(1);
		}
	}

	infinite_while();

	return 0;
}
