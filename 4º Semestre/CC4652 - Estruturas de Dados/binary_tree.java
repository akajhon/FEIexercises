/**
 * @author      : lopespt (lopespt@$HOSTNAME)
 * @file        : main
 * @created     : quinta out 21, 2021 08:54:56 -03
 */

class No {
    public No(int valor) {
        this.valor = valor;
        this.esq = null;
        this.dir = null;
        this.pai = null;
    }
    public int valor;
    public No esq;
    public No dir;
    public No pai;
}

interface ArvBin {
    boolean insere(int valor);
    boolean remove(int valor);
    boolean busca(int valor);
    void imprime();
}

class ArvBinBusca implements ArvBin {
    public No raiz = null;
    private int n = 0;
    private void imprimeErd(No a) {
        if(a != null) {
            imprimeErd(a.esq);
            System.out.print(a.valor + "  ");
            imprimeErd(a.dir);
        }
    }

    public boolean insere(int valor) {
      No novo = new No(valor);

      No anterior = null;
      No atual = raiz;
      while(atual != null){
        anterior = atual;
        if(valor <= atual.valor)
          atual = atual.esq;
        else
          atual = atual.dir;
      }

      novo.pai = anterior;
      if(anterior != null){
        if(valor <= anterior.valor){
          anterior.esq = novo;
        }
        else{
          anterior.dir = novo;
        }
      }
      else{
        raiz = novo;
      }
      n++;

      return true;
    }
    public int getN() {
        return n;
    }

    public boolean remove(int valor) {
        return false;
    }

    public boolean busca(int valor) {
      No atual = raiz;
      while(atual!=null){
        
        if(valor <= atual.valor && valor != atual.valor){
          if(atual.esq==null)
            return false;
          atual=atual.esq;
        }
        else if(valor >= atual.valor && valor != atual.valor){
          if(atual.dir==null)
            return false;
          atual=atual.dir;
        }
        else
          return true;
        

      } 
      return false;     
    }
    

    public void imprime() {
        imprimeErd(raiz);
        System.out.println();
    }

}

public class Main {
    private static void testeBusca(ArvBinBusca a, int valor) {
        if (a.busca(valor)) {
            System.out.println("valor " + valor + " encontrado na arvore");
        } else {
            System.out.println("valor " + valor + " NAO encontrado na arvore");
        }
    }
    private static void testeInsere(ArvBinBusca a, int valor) {
        if (a.insere(valor)) {
            System.out.println("valor " + valor + " inserido na arvore");
            a.imprime();
            System.out.println("======== Total: " + a.getN() + " nos ===========\n");
        }
    }
    public static void main(String[] args) {
        ArvBinBusca a = new ArvBinBusca();
        testeInsere(a, 51);
        testeInsere(a, 43);
        testeInsere(a, 5);
        testeInsere(a, 53);
        testeInsere(a, -15);
        testeInsere(a, 36);
        testeInsere(a, 17);
        testeInsere(a, 56);
        testeInsere(a, 55);
        testeInsere(a, 74);
        testeBusca(a, 55);
        testeBusca(a, 2);
        testeBusca(a, 15);
        testeBusca(a, 36);
        testeBusca(a, 22);
        testeBusca(a, -5);
        testeBusca(a, 55);
        testeBusca(a, 74);
    }
}