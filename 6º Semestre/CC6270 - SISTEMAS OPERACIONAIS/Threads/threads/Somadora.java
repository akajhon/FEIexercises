public class Somadora implements Runnable {

  public int linha;
  public Matriz ma;
  public int soma;

  public Somadora(int linha, Matriz ma) {
    this.linha = linha;
    this.ma = ma;
  }

  public void run() {
    System.out.println("Executando a soma");
    for (int j = 0; j < this.ma.colunas; j++) {
      this.soma += this.ma.dados[linha][j];
      JobUtil.atrasar(1);
    }
  }
}
