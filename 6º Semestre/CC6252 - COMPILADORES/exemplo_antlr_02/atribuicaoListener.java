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
	 * Enter a parse tree produced by {@link atribuicaoParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(atribuicaoParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(atribuicaoParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(atribuicaoParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(atribuicaoParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#id}.
	 * @param ctx the parse tree
	 */
	void enterId(atribuicaoParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#id}.
	 * @param ctx the parse tree
	 */
	void exitId(atribuicaoParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#num}.
	 * @param ctx the parse tree
	 */
	void enterNum(atribuicaoParser.NumContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#num}.
	 * @param ctx the parse tree
	 */
	void exitNum(atribuicaoParser.NumContext ctx);
	/**
	 * Enter a parse tree produced by {@link atribuicaoParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void enterRepeticao(atribuicaoParser.RepeticaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link atribuicaoParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void exitRepeticao(atribuicaoParser.RepeticaoContext ctx);
}