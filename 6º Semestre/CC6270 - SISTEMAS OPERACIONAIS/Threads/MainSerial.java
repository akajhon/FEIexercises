public class MainSerial {

  public static void main(String[] args) {
    //use Scanner se preferir
    int tamanho = Integer.parseInt(args[0]);
    Matriz ma = new Matriz(tamanho);
    ma.imprimeDados();

    int somatoria = 0;
    for(int i = 0; i < ma.linhas; i++){
      for(int j = 0; j < ma.colunas; j++){
        somatoria += ma.dados[i][j];
        JobUtil.atrasar(1);//atrasar o calculo
      }
    }
    System.out.println(somatoria);
  }
}

