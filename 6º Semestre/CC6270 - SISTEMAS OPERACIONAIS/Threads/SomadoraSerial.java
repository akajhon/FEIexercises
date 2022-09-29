public class SomadoraSerial implements Runnable {

  public int linha;
  public Matriz ma;
  public int soma;

  public SomadoraSerial(int linha, Matriz ma) {
    this.linha = linha;
    this.ma = ma;
  }

  public void run() {
    for(int i = 0; i < ma.linhas; i++){
      for(int j = 0; j < ma.colunas; j++){
        this.soma += ma.dados[i][j];
        JobUtil.atrasar(1);
      }
    }
  }
}
