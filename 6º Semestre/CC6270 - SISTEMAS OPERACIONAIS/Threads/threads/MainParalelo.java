public class MainParalelo {

  public static void main(String[] args) {

    int nrColunas = 0;
    if(args.length != 0) // checa se tem args
      nrColunas = Integer.parseInt(args[0]);
    else
      nrColunas = 10; // tamanho fixo
                      
    Matriz ma = new Matriz(nrColunas);
    ma.imprimeDados();

    Somadora s1 = new Somadora(0,ma);
    Somadora s2 = new Somadora(1,ma);

    Thread t1 = new Thread(s1);
    Thread t2 = new Thread(s2);

    t1.start();
    t2.start();

    try {
      t1.join();
      t2.join();
    } catch (InterruptedException ie) {
      System.out.println("do nothing");
    }
    System.out.println(s1.soma + s2.soma);
  }
}
