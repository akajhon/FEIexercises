#include <sys/types.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
  pid_t pid;

  pid = fork();
  printf("Meu pid: %d\n", pid);

  if (pid < 0){
    fprintf(stderr, "Fork Falhou...");
    return 1;
  }

  else if (pid == 0){
    execlp("/bin/ls","ls", NULL);
  }

  else{
    wait(NULL);
    printf("Filhoi Completo");
  }
  return 0;
}
