public class MainSerial {

  public static void main(String[] args) {
    int nrColunas = 0;
    if(args.length != 0) // checa se tem args
      nrColunas = Integer.parseInt(args[0]);
    else
      nrColunas = 10; // tamanho fixo

    Matriz ma = new Matriz(nrColunas);
    ma.imprimeDados();

    System.out.println("Executando a soma");
    int somatoria = 0;
    for(int i = 0; i < ma.linhas; i++){
      for(int j = 0; j < ma.colunas; j++){
        somatoria += ma.dados[i][j];	
        JobUtil.atrasar(1);//atrasar o calculo
      }
    }
    System.out.println("Soma: " + somatoria);
  }
}
