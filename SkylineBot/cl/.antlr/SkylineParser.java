// Generated from /home/hammer/fib-upc/lp/TelegramBot/SkylineBot/cl/Skyline.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, MUL=8, DIV=9, 
		ADD=10, SUB=11, POW=12, ASSIGN=13, NUM=14, ID=15, WS=16;
	public static final int
		RULE_root = 0, RULE_statement = 1, RULE_expr = 2, RULE_city = 3, RULE_building = 4;
	public static final String[] ruleNames = {
		"root", "statement", "expr", "city", "building"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "'['", "','", "']'", "'{'", "'}'", "'*'", "'/'", "'+'", 
		"'-'", "'**'", "':='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, "MUL", "DIV", "ADD", "SUB", 
		"POW", "ASSIGN", "NUM", "ID", "WS"
	};
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
	public String getGrammarFileName() { return "Skyline.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SkylineParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SkylineParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			statement();
			setState(11);
			match(EOF);
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

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExprStmtContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprStmtContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class AssignStmtContext extends StatementContext {
		public TerminalNode ID() { return getToken(SkylineParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(SkylineParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignStmtContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(17);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				_localctx = new AssignStmtContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(13);
				match(ID);
				setState(14);
				match(ASSIGN);
				setState(15);
				expr(0);
				}
				break;
			case 2:
				_localctx = new ExprStmtContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(16);
				expr(0);
				}
				break;
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

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MirrorContext extends ExprContext {
		public TerminalNode SUB() { return getToken(SkylineParser.SUB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MirrorContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ExprIdentContext extends ExprContext {
		public TerminalNode ID() { return getToken(SkylineParser.ID, 0); }
		public ExprIdentContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ArithmeticContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode POW() { return getToken(SkylineParser.POW, 0); }
		public TerminalNode MUL() { return getToken(SkylineParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(SkylineParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(SkylineParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(SkylineParser.SUB, 0); }
		public ArithmeticContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ParenthesisContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParenthesisContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ValueContext extends ExprContext {
		public BuildingContext building() {
			return getRuleContext(BuildingContext.class,0);
		}
		public CityContext city() {
			return getRuleContext(CityContext.class,0);
		}
		public TerminalNode NUM() { return getToken(SkylineParser.NUM, 0); }
		public ValueContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				_localctx = new ParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(20);
				match(T__0);
				setState(21);
				expr(0);
				setState(22);
				match(T__1);
				}
				break;
			case 2:
				{
				_localctx = new MirrorContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(24);
				match(SUB);
				setState(25);
				expr(6);
				}
				break;
			case 3:
				{
				_localctx = new ValueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(29);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(26);
					building();
					}
					break;
				case T__2:
				case T__5:
					{
					setState(27);
					city();
					}
					break;
				case NUM:
					{
					setState(28);
					match(NUM);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 4:
				{
				_localctx = new ExprIdentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(31);
				match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(45);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(43);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ArithmeticContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(34);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(35);
						((ArithmeticContext)_localctx).op = match(POW);
						setState(36);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new ArithmeticContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(37);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(38);
						((ArithmeticContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((ArithmeticContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(39);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ArithmeticContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(40);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(41);
						((ArithmeticContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((ArithmeticContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(42);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(47);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class CityContext extends ParserRuleContext {
		public CityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_city; }
	 
		public CityContext() { }
		public void copyFrom(CityContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class RandomContext extends CityContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RandomContext(CityContext ctx) { copyFrom(ctx); }
	}
	public static class MultipleContext extends CityContext {
		public List<BuildingContext> building() {
			return getRuleContexts(BuildingContext.class);
		}
		public BuildingContext building(int i) {
			return getRuleContext(BuildingContext.class,i);
		}
		public MultipleContext(CityContext ctx) { copyFrom(ctx); }
	}

	public final CityContext city() throws RecognitionException {
		CityContext _localctx = new CityContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_city);
		int _la;
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				_localctx = new MultipleContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				match(T__2);
				setState(49);
				building();
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(50);
					match(T__3);
					setState(51);
					building();
					}
					}
					setState(56);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(57);
				match(T__4);
				}
				break;
			case T__5:
				_localctx = new RandomContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				match(T__5);
				setState(60);
				expr(0);
				setState(61);
				match(T__3);
				setState(62);
				expr(0);
				setState(63);
				match(T__3);
				setState(64);
				expr(0);
				setState(65);
				match(T__3);
				setState(66);
				expr(0);
				setState(67);
				match(T__3);
				setState(68);
				expr(0);
				setState(69);
				match(T__6);
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

	public static class BuildingContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BuildingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_building; }
	}

	public final BuildingContext building() throws RecognitionException {
		BuildingContext _localctx = new BuildingContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_building);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(T__0);
			setState(74);
			expr(0);
			setState(75);
			match(T__3);
			setState(76);
			expr(0);
			setState(77);
			match(T__3);
			setState(78);
			expr(0);
			setState(79);
			match(T__1);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22T\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4 \n\4\3\4\5\4#\n\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\5\3\5\3\5\3\5\7\5"+
		"\67\n\5\f\5\16\5:\13\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\5\5J\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b"+
		"\n\2\4\3\2\n\13\3\2\f\r\2Y\2\f\3\2\2\2\4\23\3\2\2\2\6\"\3\2\2\2\bI\3\2"+
		"\2\2\nK\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\7\21\2\2\20"+
		"\21\7\17\2\2\21\24\5\6\4\2\22\24\5\6\4\2\23\17\3\2\2\2\23\22\3\2\2\2\24"+
		"\5\3\2\2\2\25\26\b\4\1\2\26\27\7\3\2\2\27\30\5\6\4\2\30\31\7\4\2\2\31"+
		"#\3\2\2\2\32\33\7\r\2\2\33#\5\6\4\b\34 \5\n\6\2\35 \5\b\5\2\36 \7\20\2"+
		"\2\37\34\3\2\2\2\37\35\3\2\2\2\37\36\3\2\2\2 #\3\2\2\2!#\7\21\2\2\"\25"+
		"\3\2\2\2\"\32\3\2\2\2\"\37\3\2\2\2\"!\3\2\2\2#/\3\2\2\2$%\f\7\2\2%&\7"+
		"\16\2\2&.\5\6\4\7\'(\f\6\2\2()\t\2\2\2).\5\6\4\7*+\f\5\2\2+,\t\3\2\2,"+
		".\5\6\4\6-$\3\2\2\2-\'\3\2\2\2-*\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2"+
		"\2\2\60\7\3\2\2\2\61/\3\2\2\2\62\63\7\5\2\2\638\5\n\6\2\64\65\7\6\2\2"+
		"\65\67\5\n\6\2\66\64\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2"+
		"\2:8\3\2\2\2;<\7\7\2\2<J\3\2\2\2=>\7\b\2\2>?\5\6\4\2?@\7\6\2\2@A\5\6\4"+
		"\2AB\7\6\2\2BC\5\6\4\2CD\7\6\2\2DE\5\6\4\2EF\7\6\2\2FG\5\6\4\2GH\7\t\2"+
		"\2HJ\3\2\2\2I\62\3\2\2\2I=\3\2\2\2J\t\3\2\2\2KL\7\3\2\2LM\5\6\4\2MN\7"+
		"\6\2\2NO\5\6\4\2OP\7\6\2\2PQ\5\6\4\2QR\7\4\2\2R\13\3\2\2\2\t\23\37\"-"+
		"/8I";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}