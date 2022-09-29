#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int valor = 5;

int main(){
  pid_t pid;

  pid = fork();
  if(pid == 0){
    valor+=15;
    printf("Filho: valor = %d\n", valor);
    return 0;
  }
  else if (pid > 0){
    wait(NULL);
    printf("Pai: valor = %d\n", valor);
    return 0;
  }
}
