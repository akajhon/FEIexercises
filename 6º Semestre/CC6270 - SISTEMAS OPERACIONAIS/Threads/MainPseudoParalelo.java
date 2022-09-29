public class MainPseudoParalelo{

  public static void main(String[] args){

    int tamanho = Integer.parseInt(args[0]);
    Matriz ma = new Matriz(tamanho);
    ma.imprimeDados();
    SomadoraSerial s1 = new SomadoraSerial(0,ma);
    Thread t1 = new Thread(s1);
    t1.start();
    try {
      t1.join();
    }catch (InterruptedException ie) {
      System.out.println("algo de errado");
    }
    System.out.println(s1.soma);
  }
}
