public class MainPseudoParalelo{

  public static void main(String[] args){

    int nrColunas = 0;
    if(args.length != 0) // checa se tem args
      nrColunas = Integer.parseInt(args[0]);
    else
      nrColunas = 10; // tamanho fixo
                      
    Matriz ma = new Matriz(nrColunas);
    ma.imprimeDados();

    SomadoraSerial s1 = new SomadoraSerial(ma);
    Thread t1 = new Thread(s1);

    t1.start();
    try {
      t1.join();
    } catch (InterruptedException ie) {
      System.out.println("algo de errado");
    }
    System.out.println(s1.soma);
  }
}
