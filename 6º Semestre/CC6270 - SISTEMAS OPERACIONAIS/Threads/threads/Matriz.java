public class Matriz {

  public int[][] dados;
  public int linhas;    
  public int colunas;

  public Matriz(int nrColunas) {
    dados = new int[2][nrColunas];
    this.linhas = dados.length;
    this.colunas = dados[0].length;
    inicializa();
  }

  public void inicializa(){
    for(int i = 0; i < linhas; i++){
      for(int j = 0; j < colunas; j++){
        dados[i][j] = 1;	
      }
    }
  }

  public void imprimeDados() {
    System.out.println("imprimindo a matriz");
    for(int i = 0; i < linhas; i++){
      for(int j = 0; j < colunas; j++){
        System.out.print(dados[i][j]);	
      }
      System.out.println("");
    }
  }
}
