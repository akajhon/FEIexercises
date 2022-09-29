/* Nome: João Pedro Rosa Cezarino */
/* RA: 22.120.021-5 */
/* QuickSort*/

import java.util.Scanner;
import java.util.ArrayList;

class QuickSort{

  int divisao(int list[], int inicio, int fim){
      int pivo = list[fim]; 
      int i = (inicio-1);
      for (int j = inicio; j < fim; j++){
        if (list[j] <= pivo){
            i++;
            int tmp = list[i];
            list[i] = list[j];
            list[j] = tmp;
          }
        }
      int tmp = list[i+1];
      list[i+1] = list[fim];
      list[fim] = tmp;
      return i+1;
    }

  void organiza(int list[], int inicio, int fim){
    if (inicio < fim){
      int pi = divisao(list, inicio, fim);
      organiza(list, inicio, pi-1);
      organiza(list, pi+1, fim);
      }
    }
  
  public static int[] InputLista(){
      int num = 0;
      ArrayList<Integer> listInt = new ArrayList<>();
      Scanner entrada = new Scanner(System.in);
      while (num != -1){
        num = entrada.nextInt();
        if (num == -1){
          break;
        }
        listInt.add(num);}
      entrada.close();
      int[] lista = new int[listInt.size()];
      for (int x = 0; x < listInt.size(); x++){
        lista[x] = listInt.get(x);
      }
      return lista;
    }

  public static void main(String args[]){
      int[] lista = InputLista();
      
      int n = lista.length;
      QuickSort newordenation = new QuickSort();
      newordenation.organiza(lista, 0, n-1);
      
      System.out.println("\nSaída:");
      for (int i = 0; i < n; ++i)
          System.out.print(lista[i] + "\n");
      System.out.println();
      }
}
