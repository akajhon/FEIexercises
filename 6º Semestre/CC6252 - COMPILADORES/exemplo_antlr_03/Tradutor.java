public class Tradutor extends atribuicaoBaseListener{

  @Override
  public void exitOperador(atribuicaoParser.OperadorContext ctx){
    System.out.println(" = ");
  }

}
