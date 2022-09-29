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
    execlp("./script01.sh", "", NULL);
  }

  else{
    wait(NULL);
    execlp("./script02.sh", "", NULL);
  }
  return 0;
}
