/* Nome: João Pedro Rosa Cezarino */
/* RA: 22.120.021-5 */
/* MergeSort */

import java.util.Scanner;
import java.util.ArrayList; 

class MergeSort{

    void juntar(int lista[], int esq, int meio, int dir){
      int tamanhoLado1 = meio - esq + 1;
      int tamanhoLado2 = dir - meio;
  
      int Esquerda[] = new int[tamanhoLado1];
      int Direita[] = new int[tamanhoLado2];

      for (int i = 0; i < tamanhoLado1; ++i)
        Esquerda[i] = lista[esq + i];
      
      for (int j = 0; j < tamanhoLado2; ++j)
        Direita[j] = lista[meio + 1 + j];
      
      int i = 0, j = 0;
      int k = esq;
      
      while (i < tamanhoLado1 && j < tamanhoLado2){
        if (Esquerda[i] <= Direita[j]){
          lista[k] = Esquerda[i];
          i++;}
        else{
          lista[k] = Direita[j];
          j++;}
        k++;
      }
      
      while (i < tamanhoLado1) {
        lista[k] = Esquerda[i];
        i++;
        k++;
      }
      
      while (j < tamanhoLado2) {
        lista[k] = Direita[j];
        j++;
        k++;
      }
      }
  
    void organiza(int lista[], int esq, int dir){
      if (esq < dir){
        int meio = esq + (dir - esq)/2;
        organiza(lista, esq, meio);
        organiza(lista, meio + 1, dir);
        juntar(lista, esq, meio, dir);
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
      MergeSort newordenation = new MergeSort();
      newordenation.organiza(lista, 0, lista.length - 1);
      
      System.out.println("\nSaída:");
      for (int i = 0; i < n; ++i)
          System.out.print(lista[i] + "\n");
      System.out.println();
      }
}