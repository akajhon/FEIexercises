#include <stdio.h>
#include <unistd.h>

int main(){
  int i;
  int p;
  int max = 4;

  for (i = 0; i < max; i++)
    p = fork();
  printf("%d\n", p);
  return 0;
}
