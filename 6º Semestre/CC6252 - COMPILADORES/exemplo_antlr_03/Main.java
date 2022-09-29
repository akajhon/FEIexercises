import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import java.io.IOException;

public class Main{

  public static void main(String[] args) throws IOException {
    System.out.println("[+] Digite o seu codigo: ");

    //Fazer leitura do codigo do usuario
    CharStream input = CharStreams.fromStream(System.in);

    //instanciar analizador lexico
    atribuicaoLexer lexer = new atribuicaoLexer(input);

    //Gerar os tokens
    CommonTokenStream tokens = new CommonTokenStream(lexer);

    //Instanciar o Analizador Sintatico
    atribuicaoParser parser = new atribuicaoParser(tokens);

    //Comeca a fazer a analise a partir do init
    ParseTree tree = parser.init();
  
    //Andar sobre a arvore de derivacao
    ParseTreeWalker walker = new ParseTreeWalker();
  
    Tradutor tr = new Tradutor();

    walker.walk(tr, tree);
  }
}
