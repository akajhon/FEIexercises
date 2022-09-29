public class SomadoraSerial implements Runnable {

  public Matriz ma;
  public int soma;

  public SomadoraSerial(Matriz ma) {
    this.ma = ma;
  }

  public void run() {
    System.out.println("Executando a soma");
    for(int i = 0; i < ma.linhas; i++){
      for(int j = 0; j < ma.colunas; j++){
        this.soma += ma.dados[i][j];	
        JobUtil.atrasar(1);
      }
    }
  }
}
