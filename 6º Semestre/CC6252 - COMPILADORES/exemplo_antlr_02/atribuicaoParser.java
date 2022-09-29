// Generated from atribuicao.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class atribuicaoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, ID=6, NUM=7, Ws=8;
	public static final int
		RULE_init = 0, RULE_tipo = 1, RULE_op = 2, RULE_id = 3, RULE_num = 4, 
		RULE_repeticao = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"init", "tipo", "op", "id", "num", "repeticao"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'inteiro'", "'decimal'", "'palavra'", "'<-'", "'loop'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "ID", "NUM", "Ws"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "atribuicao.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public atribuicaoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class InitContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public List<IdContext> id() {
			return getRuleContexts(IdContext.class);
		}
		public IdContext id(int i) {
			return getRuleContext(IdContext.class,i);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public NumContext num() {
			return getRuleContext(NumContext.class,0);
		}
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).enterInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).exitInit(this);
		}
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			tipo();
			setState(13);
			id();
			setState(14);
			op();
			setState(17);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				{
				setState(15);
				num();
				}
				break;
			case ID:
				{
				setState(16);
				id();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TipoContext extends ParserRuleContext {
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_tipo);
		try {
			setState(25);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				match(T__0);
				System.out.print("int ");
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(21);
				match(T__1);
				System.out.print("double ");
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 3);
				{
				setState(23);
				match(T__2);
				System.out.print("String ");
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OpContext extends ParserRuleContext {
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).enterOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).exitOp(this);
		}
	}

	public final OpContext op() throws RecognitionException {
		OpContext _localctx = new OpContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			match(T__3);
			System.out.print(" = ");
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdContext extends ParserRuleContext {
		public Token ID;
		public TerminalNode ID() { return getToken(atribuicaoParser.ID, 0); }
		public IdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).enterId(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).exitId(this);
		}
	}

	public final IdContext id() throws RecognitionException {
		IdContext _localctx = new IdContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			((IdContext)_localctx).ID = match(ID);
			System.out.print((((IdContext)_localctx).ID!=null?((IdContext)_localctx).ID.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumContext extends ParserRuleContext {
		public Token NUM;
		public TerminalNode NUM() { return getToken(atribuicaoParser.NUM, 0); }
		public NumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).enterNum(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).exitNum(this);
		}
	}

	public final NumContext num() throws RecognitionException {
		NumContext _localctx = new NumContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_num);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			((NumContext)_localctx).NUM = match(NUM);
			System.out.print((((NumContext)_localctx).NUM!=null?((NumContext)_localctx).NUM.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RepeticaoContext extends ParserRuleContext {
		public RepeticaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeticao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).enterRepeticao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof atribuicaoListener ) ((atribuicaoListener)listener).exitRepeticao(this);
		}
	}

	public final RepeticaoContext repeticao() throws RecognitionException {
		RepeticaoContext _localctx = new RepeticaoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_repeticao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(T__4);
			System.out.println("for");
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\b(\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0003\u0000\u0012\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001a\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0000"+
		"\u0000\u0006\u0000\u0002\u0004\u0006\b\n\u0000\u0000$\u0000\f\u0001\u0000"+
		"\u0000\u0000\u0002\u0019\u0001\u0000\u0000\u0000\u0004\u001b\u0001\u0000"+
		"\u0000\u0000\u0006\u001e\u0001\u0000\u0000\u0000\b!\u0001\u0000\u0000"+
		"\u0000\n$\u0001\u0000\u0000\u0000\f\r\u0003\u0002\u0001\u0000\r\u000e"+
		"\u0003\u0006\u0003\u0000\u000e\u0011\u0003\u0004\u0002\u0000\u000f\u0012"+
		"\u0003\b\u0004\u0000\u0010\u0012\u0003\u0006\u0003\u0000\u0011\u000f\u0001"+
		"\u0000\u0000\u0000\u0011\u0010\u0001\u0000\u0000\u0000\u0012\u0001\u0001"+
		"\u0000\u0000\u0000\u0013\u0014\u0005\u0001\u0000\u0000\u0014\u001a\u0006"+
		"\u0001\uffff\uffff\u0000\u0015\u0016\u0005\u0002\u0000\u0000\u0016\u001a"+
		"\u0006\u0001\uffff\uffff\u0000\u0017\u0018\u0005\u0003\u0000\u0000\u0018"+
		"\u001a\u0006\u0001\uffff\uffff\u0000\u0019\u0013\u0001\u0000\u0000\u0000"+
		"\u0019\u0015\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000"+
		"\u001a\u0003\u0001\u0000\u0000\u0000\u001b\u001c\u0005\u0004\u0000\u0000"+
		"\u001c\u001d\u0006\u0002\uffff\uffff\u0000\u001d\u0005\u0001\u0000\u0000"+
		"\u0000\u001e\u001f\u0005\u0006\u0000\u0000\u001f \u0006\u0003\uffff\uffff"+
		"\u0000 \u0007\u0001\u0000\u0000\u0000!\"\u0005\u0007\u0000\u0000\"#\u0006"+
		"\u0004\uffff\uffff\u0000#\t\u0001\u0000\u0000\u0000$%\u0005\u0005\u0000"+
		"\u0000%&\u0006\u0005\uffff\uffff\u0000&\u000b\u0001\u0000\u0000\u0000"+
		"\u0002\u0011\u0019";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}