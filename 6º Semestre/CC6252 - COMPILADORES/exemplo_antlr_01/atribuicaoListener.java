// Generated from atribuicao.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link atribuicaoParser}.
 */
public interface atribuicaoListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#init}.
	 * @param ctx the parse tree
	 */
	void enterInit(atribuicaoParser.InitContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#init}.
	 * @param ctx the parse tree
	 */
	void exitInit(atribuicaoParser.InitContext ctx);
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(atribuicaoParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(atribuicaoParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(atribuicaoParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(atribuicaoParser.TipoContext ctx);
}