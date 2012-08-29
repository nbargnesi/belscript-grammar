# $ANTLR 3.4 BELScript_Python_v1.g 2012-08-28 20:03:51

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__64=64
T__65=65
T__66=66
T__67=67
T__68=68
T__69=69
T__70=70
T__71=71
T__72=72
T__73=73
T__74=74
T__75=75
T__76=76
T__77=77
T__78=78
T__79=79
T__80=80
T__81=81
T__82=82
T__83=83
T__84=84
T__85=85
T__86=86
T__87=87
T__88=88
T__89=89
T__90=90
T__91=91
T__92=92
T__93=93
T__94=94
T__95=95
T__96=96
T__97=97
T__98=98
T__99=99
T__100=100
T__101=101
T__102=102
T__103=103
T__104=104
T__105=105
T__106=106
T__107=107
T__108=108
T__109=109
T__110=110
T__111=111
T__112=112
T__113=113
T__114=114
T__115=115
T__116=116
T__117=117
T__118=118
T__119=119
T__120=120
T__121=121
T__122=122
T__123=123
T__124=124
T__125=125
T__126=126
T__127=127
T__128=128
T__129=129
T__130=130
T__131=131
T__132=132
T__133=133
T__134=134
T__135=135
T__136=136
T__137=137
T__138=138
T__139=139
T__140=140
T__141=141
T__142=142
T__143=143
T__144=144
T__145=145
T__146=146
T__147=147
T__148=148
T__149=149
T__150=150
ANNO_DEF_LIST=4
ANNO_DEF_PTRN=5
ANNO_DEF_URL=6
ANNO_SET_ID=7
ANNO_SET_LIST=8
ANNO_SET_QV=9
COLON=10
COMMA=11
DFLT_NSDEF=12
DIGIT=13
DOCDEF=14
DOCSET_ID=15
DOCSET_LIST=16
DOCSET_QV=17
DOCUMENT_COMMENT=18
EQ=19
ESCAPE_SEQUENCE=20
HEX_DIGIT=21
IDENT_LIST=22
KWRD_ANNO=23
KWRD_AS=24
KWRD_AUTHORS=25
KWRD_CONTACTINFO=26
KWRD_COPYRIGHT=27
KWRD_DEFINE=28
KWRD_DESC=29
KWRD_DFLT=30
KWRD_DISCLAIMER=31
KWRD_DOCUMENT=32
KWRD_LICENSES=33
KWRD_LIST=34
KWRD_NAME=35
KWRD_NS=36
KWRD_PATTERN=37
KWRD_SET=38
KWRD_STMT_GROUP=39
KWRD_UNSET=40
KWRD_URL=41
KWRD_VERSION=42
LETTER=43
LP=44
NEWLINE=45
NSDEF=46
OBJECT_IDENT=47
OCTAL_ESCAPE=48
PARAM_DEF_ID=49
PARAM_DEF_QV=50
QUOTED_VALUE=51
RP=52
SG_SET_ID=53
SG_SET_QV=54
STATEMENT_COMMENT=55
STMTDEF=56
TERMDEF=57
UNICODE_ESCAPE=58
UNSET_ID=59
UNSET_ID_LIST=60
UNSET_SG=61
VALUE_LIST=62
WS=63

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ANNO_DEF_LIST", "ANNO_DEF_PTRN", "ANNO_DEF_URL", "ANNO_SET_ID", "ANNO_SET_LIST",
    "ANNO_SET_QV", "COLON", "COMMA", "DFLT_NSDEF", "DIGIT", "DOCDEF", "DOCSET_ID",
    "DOCSET_LIST", "DOCSET_QV", "DOCUMENT_COMMENT", "EQ", "ESCAPE_SEQUENCE",
    "HEX_DIGIT", "IDENT_LIST", "KWRD_ANNO", "KWRD_AS", "KWRD_AUTHORS", "KWRD_CONTACTINFO",
    "KWRD_COPYRIGHT", "KWRD_DEFINE", "KWRD_DESC", "KWRD_DFLT", "KWRD_DISCLAIMER",
    "KWRD_DOCUMENT", "KWRD_LICENSES", "KWRD_LIST", "KWRD_NAME", "KWRD_NS",
    "KWRD_PATTERN", "KWRD_SET", "KWRD_STMT_GROUP", "KWRD_UNSET", "KWRD_URL",
    "KWRD_VERSION", "LETTER", "LP", "NEWLINE", "NSDEF", "OBJECT_IDENT",
    "OCTAL_ESCAPE", "PARAM_DEF_ID", "PARAM_DEF_QV", "QUOTED_VALUE", "RP",
    "SG_SET_ID", "SG_SET_QV", "STATEMENT_COMMENT", "STMTDEF", "TERMDEF",
    "UNICODE_ESCAPE", "UNSET_ID", "UNSET_ID_LIST", "UNSET_SG", "VALUE_LIST",
    "WS", "'--'", "'->'", "'-|'", "':>'", "'=>'", "'=|'", "'>>'", "'a'",
    "'abundance'", "'act'", "'analogous'", "'association'", "'biologicalProcess'",
    "'biomarkerFor'", "'bp'", "'cat'", "'catalyticActivity'", "'causesNoChange'",
    "'cellSecretion'", "'cellSurfaceExpression'", "'chap'", "'chaperoneActivity'",
    "'complex'", "'complexAbundance'", "'composite'", "'compositeAbundance'",
    "'decreases'", "'deg'", "'degradation'", "'directlyDecreases'", "'directlyIncreases'",
    "'fus'", "'fusion'", "'g'", "'geneAbundance'", "'gtp'", "'gtpBoundActivity'",
    "'hasComponent'", "'hasComponents'", "'hasMember'", "'hasMembers'",
    "'increases'", "'isA'", "'kin'", "'kinaseActivity'", "'list'", "'m'",
    "'microRNAAbundance'", "'molecularActivity'", "'negativeCorrelation'",
    "'orthologous'", "'p'", "'path'", "'pathology'", "'pep'", "'peptidaseActivity'",
    "'phos'", "'phosphataseActivity'", "'pmod'", "'positiveCorrelation'",
    "'products'", "'prognosticBiomarkerFor'", "'proteinAbundance'", "'proteinModification'",
    "'r'", "'rateLimitingStepOf'", "'reactants'", "'reaction'", "'ribo'",
    "'ribosylationActivity'", "'rnaAbundance'", "'rxn'", "'sec'", "'sub'",
    "'subProcessOf'", "'substitution'", "'surf'", "'tloc'", "'tport'", "'transcribedTo'",
    "'transcriptionalActivity'", "'translatedTo'", "'translocation'", "'transportActivity'",
    "'trunc'", "'truncation'", "'tscript'"
]




class BELScript_Python_v1Parser(Parser):
    grammarFileName = "BELScript_Python_v1.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(BELScript_Python_v1Parser, self).__init__(input, state, *args, **kwargs)

        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )

        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )




        self.delegates = []

    self._adaptor = None
    self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class document_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.document_return, self).__init__()

            self.tree = None





    # $ANTLR start "document"
    # BELScript_Python_v1.g:67:1: document : ( NEWLINE | DOCUMENT_COMMENT | record )+ EOF -> ^( DOCDEF ( record )+ ) ;
    def document(self, ):
        retval = self.document_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE1 = None
        DOCUMENT_COMMENT2 = None
        EOF4 = None
        record3 = None


        NEWLINE1_tree = None
        DOCUMENT_COMMENT2_tree = None
        EOF4_tree = None
        stream_DOCUMENT_COMMENT = RewriteRuleTokenStream(self._adaptor, "token DOCUMENT_COMMENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_record = RewriteRuleSubtreeStream(self._adaptor, "rule record")
        try:
            try:
                # BELScript_Python_v1.g:68:5: ( ( NEWLINE | DOCUMENT_COMMENT | record )+ EOF -> ^( DOCDEF ( record )+ ) )
                # BELScript_Python_v1.g:68:9: ( NEWLINE | DOCUMENT_COMMENT | record )+ EOF
                pass
                # BELScript_Python_v1.g:68:9: ( NEWLINE | DOCUMENT_COMMENT | record )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 4
                    LA1 = self.input.LA(1)
                    if LA1 == NEWLINE:
                        alt1 = 1
                    elif LA1 == DOCUMENT_COMMENT:
                        alt1 = 2
                    elif LA1 == KWRD_DEFINE or LA1 == KWRD_SET or LA1 == KWRD_UNSET or LA1 == 71 or LA1 == 72 or LA1 == 73 or LA1 == 76 or LA1 == 78 or LA1 == 79 or LA1 == 80 or LA1 == 82 or LA1 == 83 or LA1 == 84 or LA1 == 85 or LA1 == 86 or LA1 == 87 or LA1 == 88 or LA1 == 89 or LA1 == 91 or LA1 == 92 or LA1 == 95 or LA1 == 96 or LA1 == 97 or LA1 == 98 or LA1 == 99 or LA1 == 100 or LA1 == 107 or LA1 == 108 or LA1 == 109 or LA1 == 110 or LA1 == 111 or LA1 == 112 or LA1 == 115 or LA1 == 116 or LA1 == 117 or LA1 == 118 or LA1 == 119 or LA1 == 120 or LA1 == 121 or LA1 == 122 or LA1 == 124 or LA1 == 126 or LA1 == 127 or LA1 == 128 or LA1 == 130 or LA1 == 131 or LA1 == 132 or LA1 == 133 or LA1 == 134 or LA1 == 135 or LA1 == 136 or LA1 == 137 or LA1 == 139 or LA1 == 140 or LA1 == 141 or LA1 == 142 or LA1 == 144 or LA1 == 146 or LA1 == 147 or LA1 == 148 or LA1 == 149 or LA1 == 150:
                        alt1 = 3

                    if alt1 == 1:
                        # BELScript_Python_v1.g:68:10: NEWLINE
                        pass
                        NEWLINE1 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_document327)
                        stream_NEWLINE.add(NEWLINE1)



                    elif alt1 == 2:
                        # BELScript_Python_v1.g:68:20: DOCUMENT_COMMENT
                        pass
                        DOCUMENT_COMMENT2 = self.match(self.input, DOCUMENT_COMMENT, self.FOLLOW_DOCUMENT_COMMENT_in_document331)
                        stream_DOCUMENT_COMMENT.add(DOCUMENT_COMMENT2)



                    elif alt1 == 3:
                        # BELScript_Python_v1.g:68:39: record
                        pass
                        self._state.following.append(self.FOLLOW_record_in_document335)
                        record3 = self.record()

                        self._state.following.pop()
                        stream_record.add(record3.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_document339)
                stream_EOF.add(EOF4)


                # AST Rewrite
                # elements: record
                # token labels:
                # rule labels: retval
                # token list labels:
                # rule list labels:
                # wildcard labels:
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 68:52: -> ^( DOCDEF ( record )+ )
                # BELScript_Python_v1.g:69:9: ^( DOCDEF ( record )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DOCDEF, "DOCDEF")
                , root_1)

                # BELScript_Python_v1.g:69:18: ( record )+
                if not (stream_record.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_record.hasNext():
                    self._adaptor.addChild(root_1, stream_record.nextTree())


                stream_record.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "document"


    class record_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.record_return, self).__init__()

            self.tree = None





    # $ANTLR start "record"
    # BELScript_Python_v1.g:72:1: record : ( define_namespace | define_annotation | set_annotation | set_document | set_statement_group | unset_statement_group | unset | statement );
    def record(self, ):
        retval = self.record_return()
        retval.start = self.input.LT(1)


        root_0 = None

        define_namespace5 = None

        define_annotation6 = None

        set_annotation7 = None

        set_document8 = None

        set_statement_group9 = None

        unset_statement_group10 = None

        unset11 = None

        statement12 = None



        try:
            try:
                # BELScript_Python_v1.g:73:5: ( define_namespace | define_annotation | set_annotation | set_document | set_statement_group | unset_statement_group | unset | statement )
                alt2 = 8
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # BELScript_Python_v1.g:73:9: define_namespace
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_define_namespace_in_record375)
                    define_namespace5 = self.define_namespace()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, define_namespace5.tree)



                elif alt2 == 2:
                    # BELScript_Python_v1.g:74:9: define_annotation
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_define_annotation_in_record385)
                    define_annotation6 = self.define_annotation()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, define_annotation6.tree)



                elif alt2 == 3:
                    # BELScript_Python_v1.g:75:9: set_annotation
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_annotation_in_record395)
                    set_annotation7 = self.set_annotation()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_annotation7.tree)



                elif alt2 == 4:
                    # BELScript_Python_v1.g:76:9: set_document
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_document_in_record405)
                    set_document8 = self.set_document()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_document8.tree)



                elif alt2 == 5:
                    # BELScript_Python_v1.g:77:9: set_statement_group
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_statement_group_in_record415)
                    set_statement_group9 = self.set_statement_group()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_statement_group9.tree)



                elif alt2 == 6:
                    # BELScript_Python_v1.g:78:9: unset_statement_group
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unset_statement_group_in_record425)
                    unset_statement_group10 = self.unset_statement_group()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unset_statement_group10.tree)



                elif alt2 == 7:
                    # BELScript_Python_v1.g:79:9: unset
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unset_in_record435)
                    unset11 = self.unset()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unset11.tree)



                elif alt2 == 8:
                    # BELScript_Python_v1.g:80:9: statement
                    pass
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_in_record445)
                    statement12 = self.statement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement12.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "record"


    class set_doc_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.set_doc_expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "set_doc_expr"
    # BELScript_Python_v1.g:83:1: set_doc_expr : KWRD_SET ( WS )* KWRD_DOCUMENT ( WS )* ;
    def set_doc_expr(self, ):
        retval = self.set_doc_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        KWRD_SET13 = None
        WS14 = None
        KWRD_DOCUMENT15 = None
        WS16 = None

        KWRD_SET13_tree = None
        WS14_tree = None
        KWRD_DOCUMENT15_tree = None
        WS16_tree = None

        try:
            try:
                # BELScript_Python_v1.g:84:5: ( KWRD_SET ( WS )* KWRD_DOCUMENT ( WS )* )
                # BELScript_Python_v1.g:84:9: KWRD_SET ( WS )* KWRD_DOCUMENT ( WS )*
                pass
                root_0 = self._adaptor.nil()


                KWRD_SET13 = self.match(self.input, KWRD_SET, self.FOLLOW_KWRD_SET_in_set_doc_expr464)
                KWRD_SET13_tree = self._adaptor.createWithPayload(KWRD_SET13)
                self._adaptor.addChild(root_0, KWRD_SET13_tree)



                # BELScript_Python_v1.g:84:18: ( WS )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == WS) :
                        alt3 = 1


                    if alt3 == 1:
                        # BELScript_Python_v1.g:84:18: WS
                        pass
                        WS14 = self.match(self.input, WS, self.FOLLOW_WS_in_set_doc_expr466)
                        WS14_tree = self._adaptor.createWithPayload(WS14)
                        self._adaptor.addChild(root_0, WS14_tree)




                    else:
                        break #loop3


                KWRD_DOCUMENT15 = self.match(self.input, KWRD_DOCUMENT, self.FOLLOW_KWRD_DOCUMENT_in_set_doc_expr469)
                KWRD_DOCUMENT15_tree = self._adaptor.createWithPayload(KWRD_DOCUMENT15)
                self._adaptor.addChild(root_0, KWRD_DOCUMENT15_tree)



                # BELScript_Python_v1.g:84:36: ( WS )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == WS) :
                        alt4 = 1


                    if alt4 == 1:
                        # BELScript_Python_v1.g:84:36: WS
                        pass
                        WS16 = self.match(self.input, WS, self.FOLLOW_WS_in_set_doc_expr471)
                        WS16_tree = self._adaptor.createWithPayload(WS16)
                        self._adaptor.addChild(root_0, WS16_tree)




                    else:
                        break #loop4




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_doc_expr"


    class set_document_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.set_document_return, self).__init__()

            self.tree = None





    # $ANTLR start "set_document"
    # BELScript_Python_v1.g:87:1: set_document : ( set_doc_expr document_property eq_clause val= QUOTED_VALUE -> ^( DOCSET_QV document_property $val) | set_doc_expr document_property eq_clause val= VALUE_LIST -> ^( DOCSET_LIST document_property $val) | set_doc_expr document_property eq_clause val= OBJECT_IDENT -> ^( DOCSET_ID document_property $val) );
    def set_document(self, ):
        retval = self.set_document_return()
        retval.start = self.input.LT(1)


        root_0 = None

        val = None
        set_doc_expr17 = None

        document_property18 = None

        eq_clause19 = None

        set_doc_expr20 = None

        document_property21 = None

        eq_clause22 = None

        set_doc_expr23 = None

        document_property24 = None

        eq_clause25 = None


        val_tree = None
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_QUOTED_VALUE = RewriteRuleTokenStream(self._adaptor, "token QUOTED_VALUE")
        stream_VALUE_LIST = RewriteRuleTokenStream(self._adaptor, "token VALUE_LIST")
        stream_set_doc_expr = RewriteRuleSubtreeStream(self._adaptor, "rule set_doc_expr")
        stream_eq_clause = RewriteRuleSubtreeStream(self._adaptor, "rule eq_clause")
        stream_document_property = RewriteRuleSubtreeStream(self._adaptor, "rule document_property")
        try:
            try:
                # BELScript_Python_v1.g:88:5: ( set_doc_expr document_property eq_clause val= QUOTED_VALUE -> ^( DOCSET_QV document_property $val) | set_doc_expr document_property eq_clause val= VALUE_LIST -> ^( DOCSET_LIST document_property $val) | set_doc_expr document_property eq_clause val= OBJECT_IDENT -> ^( DOCSET_ID document_property $val) )
                alt5 = 3
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # BELScript_Python_v1.g:88:9: set_doc_expr document_property eq_clause val= QUOTED_VALUE
                    pass
                    self._state.following.append(self.FOLLOW_set_doc_expr_in_set_document491)
                    set_doc_expr17 = self.set_doc_expr()

                    self._state.following.pop()
                    stream_set_doc_expr.add(set_doc_expr17.tree)


                    self._state.following.append(self.FOLLOW_document_property_in_set_document493)
                    document_property18 = self.document_property()

                    self._state.following.pop()
                    stream_document_property.add(document_property18.tree)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_document495)
                    eq_clause19 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause19.tree)


                    val = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_set_document499)
                    stream_QUOTED_VALUE.add(val)


                    # AST Rewrite
                    # elements: val, document_property
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 88:67: -> ^( DOCSET_QV document_property $val)
                    # BELScript_Python_v1.g:89:9: ^( DOCSET_QV document_property $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DOCSET_QV, "DOCSET_QV")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_document_property.nextTree())

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt5 == 2:
                    # BELScript_Python_v1.g:90:9: set_doc_expr document_property eq_clause val= VALUE_LIST
                    pass
                    self._state.following.append(self.FOLLOW_set_doc_expr_in_set_document528)
                    set_doc_expr20 = self.set_doc_expr()

                    self._state.following.pop()
                    stream_set_doc_expr.add(set_doc_expr20.tree)


                    self._state.following.append(self.FOLLOW_document_property_in_set_document530)
                    document_property21 = self.document_property()

                    self._state.following.pop()
                    stream_document_property.add(document_property21.tree)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_document532)
                    eq_clause22 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause22.tree)


                    val = self.match(self.input, VALUE_LIST, self.FOLLOW_VALUE_LIST_in_set_document536)
                    stream_VALUE_LIST.add(val)


                    # AST Rewrite
                    # elements: document_property, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 90:65: -> ^( DOCSET_LIST document_property $val)
                    # BELScript_Python_v1.g:91:9: ^( DOCSET_LIST document_property $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DOCSET_LIST, "DOCSET_LIST")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_document_property.nextTree())

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt5 == 3:
                    # BELScript_Python_v1.g:92:9: set_doc_expr document_property eq_clause val= OBJECT_IDENT
                    pass
                    self._state.following.append(self.FOLLOW_set_doc_expr_in_set_document565)
                    set_doc_expr23 = self.set_doc_expr()

                    self._state.following.pop()
                    stream_set_doc_expr.add(set_doc_expr23.tree)


                    self._state.following.append(self.FOLLOW_document_property_in_set_document567)
                    document_property24 = self.document_property()

                    self._state.following.pop()
                    stream_document_property.add(document_property24.tree)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_document569)
                    eq_clause25 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause25.tree)


                    val = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_set_document573)
                    stream_OBJECT_IDENT.add(val)


                    # AST Rewrite
                    # elements: document_property, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 92:67: -> ^( DOCSET_ID document_property $val)
                    # BELScript_Python_v1.g:93:9: ^( DOCSET_ID document_property $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DOCSET_ID, "DOCSET_ID")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_document_property.nextTree())

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_document"


    class set_sg_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.set_sg_expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "set_sg_expr"
    # BELScript_Python_v1.g:96:1: set_sg_expr : KWRD_SET ( WS )* KWRD_STMT_GROUP ;
    def set_sg_expr(self, ):
        retval = self.set_sg_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        KWRD_SET26 = None
        WS27 = None
        KWRD_STMT_GROUP28 = None

        KWRD_SET26_tree = None
        WS27_tree = None
        KWRD_STMT_GROUP28_tree = None

        try:
            try:
                # BELScript_Python_v1.g:97:5: ( KWRD_SET ( WS )* KWRD_STMT_GROUP )
                # BELScript_Python_v1.g:97:9: KWRD_SET ( WS )* KWRD_STMT_GROUP
                pass
                root_0 = self._adaptor.nil()


                KWRD_SET26 = self.match(self.input, KWRD_SET, self.FOLLOW_KWRD_SET_in_set_sg_expr611)
                KWRD_SET26_tree = self._adaptor.createWithPayload(KWRD_SET26)
                self._adaptor.addChild(root_0, KWRD_SET26_tree)



                # BELScript_Python_v1.g:97:18: ( WS )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == WS) :
                        alt6 = 1


                    if alt6 == 1:
                        # BELScript_Python_v1.g:97:18: WS
                        pass
                        WS27 = self.match(self.input, WS, self.FOLLOW_WS_in_set_sg_expr613)
                        WS27_tree = self._adaptor.createWithPayload(WS27)
                        self._adaptor.addChild(root_0, WS27_tree)




                    else:
                        break #loop6


                KWRD_STMT_GROUP28 = self.match(self.input, KWRD_STMT_GROUP, self.FOLLOW_KWRD_STMT_GROUP_in_set_sg_expr616)
                KWRD_STMT_GROUP28_tree = self._adaptor.createWithPayload(KWRD_STMT_GROUP28)
                self._adaptor.addChild(root_0, KWRD_STMT_GROUP28_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_sg_expr"


    class set_statement_group_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.set_statement_group_return, self).__init__()

            self.tree = None





    # $ANTLR start "set_statement_group"
    # BELScript_Python_v1.g:100:1: set_statement_group : ( set_sg_expr eq_clause val= QUOTED_VALUE -> ^( SG_SET_QV $val) | set_sg_expr eq_clause val= OBJECT_IDENT -> ^( SG_SET_ID $val) );
    def set_statement_group(self, ):
        retval = self.set_statement_group_return()
        retval.start = self.input.LT(1)


        root_0 = None

        val = None
        set_sg_expr29 = None

        eq_clause30 = None

        set_sg_expr31 = None

        eq_clause32 = None


        val_tree = None
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_QUOTED_VALUE = RewriteRuleTokenStream(self._adaptor, "token QUOTED_VALUE")
        stream_eq_clause = RewriteRuleSubtreeStream(self._adaptor, "rule eq_clause")
        stream_set_sg_expr = RewriteRuleSubtreeStream(self._adaptor, "rule set_sg_expr")
        try:
            try:
                # BELScript_Python_v1.g:101:5: ( set_sg_expr eq_clause val= QUOTED_VALUE -> ^( SG_SET_QV $val) | set_sg_expr eq_clause val= OBJECT_IDENT -> ^( SG_SET_ID $val) )
                alt7 = 2
                alt7 = self.dfa7.predict(self.input)
                if alt7 == 1:
                    # BELScript_Python_v1.g:101:9: set_sg_expr eq_clause val= QUOTED_VALUE
                    pass
                    self._state.following.append(self.FOLLOW_set_sg_expr_in_set_statement_group635)
                    set_sg_expr29 = self.set_sg_expr()

                    self._state.following.pop()
                    stream_set_sg_expr.add(set_sg_expr29.tree)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_statement_group637)
                    eq_clause30 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause30.tree)


                    val = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_set_statement_group641)
                    stream_QUOTED_VALUE.add(val)


                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 101:48: -> ^( SG_SET_QV $val)
                    # BELScript_Python_v1.g:101:51: ^( SG_SET_QV $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(SG_SET_QV, "SG_SET_QV")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt7 == 2:
                    # BELScript_Python_v1.g:102:9: set_sg_expr eq_clause val= OBJECT_IDENT
                    pass
                    self._state.following.append(self.FOLLOW_set_sg_expr_in_set_statement_group660)
                    set_sg_expr31 = self.set_sg_expr()

                    self._state.following.pop()
                    stream_set_sg_expr.add(set_sg_expr31.tree)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_statement_group662)
                    eq_clause32 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause32.tree)


                    val = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_set_statement_group666)
                    stream_OBJECT_IDENT.add(val)


                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 102:48: -> ^( SG_SET_ID $val)
                    # BELScript_Python_v1.g:102:51: ^( SG_SET_ID $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(SG_SET_ID, "SG_SET_ID")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_statement_group"


    class set_annotation_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.set_annotation_return, self).__init__()

            self.tree = None





    # $ANTLR start "set_annotation"
    # BELScript_Python_v1.g:105:1: set_annotation : ( KWRD_SET OBJECT_IDENT eq_clause val= QUOTED_VALUE -> ^( ANNO_SET_QV OBJECT_IDENT $val) | KWRD_SET OBJECT_IDENT eq_clause val= VALUE_LIST -> ^( ANNO_SET_LIST OBJECT_IDENT $val) | KWRD_SET OBJECT_IDENT eq_clause val= OBJECT_IDENT -> ^( ANNO_SET_ID OBJECT_IDENT $val) );
    def set_annotation(self, ):
        retval = self.set_annotation_return()
        retval.start = self.input.LT(1)


        root_0 = None

        val = None
        KWRD_SET33 = None
        OBJECT_IDENT34 = None
        KWRD_SET36 = None
        OBJECT_IDENT37 = None
        KWRD_SET39 = None
        OBJECT_IDENT40 = None
        eq_clause35 = None

        eq_clause38 = None

        eq_clause41 = None


        val_tree = None
        KWRD_SET33_tree = None
        OBJECT_IDENT34_tree = None
        KWRD_SET36_tree = None
        OBJECT_IDENT37_tree = None
        KWRD_SET39_tree = None
        OBJECT_IDENT40_tree = None
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_QUOTED_VALUE = RewriteRuleTokenStream(self._adaptor, "token QUOTED_VALUE")
        stream_VALUE_LIST = RewriteRuleTokenStream(self._adaptor, "token VALUE_LIST")
        stream_KWRD_SET = RewriteRuleTokenStream(self._adaptor, "token KWRD_SET")
        stream_eq_clause = RewriteRuleSubtreeStream(self._adaptor, "rule eq_clause")
        try:
            try:
                # BELScript_Python_v1.g:106:5: ( KWRD_SET OBJECT_IDENT eq_clause val= QUOTED_VALUE -> ^( ANNO_SET_QV OBJECT_IDENT $val) | KWRD_SET OBJECT_IDENT eq_clause val= VALUE_LIST -> ^( ANNO_SET_LIST OBJECT_IDENT $val) | KWRD_SET OBJECT_IDENT eq_clause val= OBJECT_IDENT -> ^( ANNO_SET_ID OBJECT_IDENT $val) )
                alt8 = 3
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # BELScript_Python_v1.g:106:9: KWRD_SET OBJECT_IDENT eq_clause val= QUOTED_VALUE
                    pass
                    KWRD_SET33 = self.match(self.input, KWRD_SET, self.FOLLOW_KWRD_SET_in_set_annotation694)
                    stream_KWRD_SET.add(KWRD_SET33)


                    OBJECT_IDENT34 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_set_annotation696)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT34)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_annotation698)
                    eq_clause35 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause35.tree)


                    val = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_set_annotation702)
                    stream_QUOTED_VALUE.add(val)


                    # AST Rewrite
                    # elements: val, OBJECT_IDENT
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 106:58: -> ^( ANNO_SET_QV OBJECT_IDENT $val)
                    # BELScript_Python_v1.g:107:9: ^( ANNO_SET_QV OBJECT_IDENT $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNO_SET_QV, "ANNO_SET_QV")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt8 == 2:
                    # BELScript_Python_v1.g:108:9: KWRD_SET OBJECT_IDENT eq_clause val= VALUE_LIST
                    pass
                    KWRD_SET36 = self.match(self.input, KWRD_SET, self.FOLLOW_KWRD_SET_in_set_annotation731)
                    stream_KWRD_SET.add(KWRD_SET36)


                    OBJECT_IDENT37 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_set_annotation733)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT37)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_annotation735)
                    eq_clause38 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause38.tree)


                    val = self.match(self.input, VALUE_LIST, self.FOLLOW_VALUE_LIST_in_set_annotation739)
                    stream_VALUE_LIST.add(val)


                    # AST Rewrite
                    # elements: OBJECT_IDENT, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 108:56: -> ^( ANNO_SET_LIST OBJECT_IDENT $val)
                    # BELScript_Python_v1.g:109:9: ^( ANNO_SET_LIST OBJECT_IDENT $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNO_SET_LIST, "ANNO_SET_LIST")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt8 == 3:
                    # BELScript_Python_v1.g:110:9: KWRD_SET OBJECT_IDENT eq_clause val= OBJECT_IDENT
                    pass
                    KWRD_SET39 = self.match(self.input, KWRD_SET, self.FOLLOW_KWRD_SET_in_set_annotation768)
                    stream_KWRD_SET.add(KWRD_SET39)


                    OBJECT_IDENT40 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_set_annotation770)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT40)


                    self._state.following.append(self.FOLLOW_eq_clause_in_set_annotation772)
                    eq_clause41 = self.eq_clause()

                    self._state.following.pop()
                    stream_eq_clause.add(eq_clause41.tree)


                    val = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_set_annotation776)
                    stream_OBJECT_IDENT.add(val)


                    # AST Rewrite
                    # elements: OBJECT_IDENT, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 110:58: -> ^( ANNO_SET_ID OBJECT_IDENT $val)
                    # BELScript_Python_v1.g:111:9: ^( ANNO_SET_ID OBJECT_IDENT $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNO_SET_ID, "ANNO_SET_ID")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_annotation"


    class unset_statement_group_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.unset_statement_group_return, self).__init__()

            self.tree = None





    # $ANTLR start "unset_statement_group"
    # BELScript_Python_v1.g:114:1: unset_statement_group : KWRD_UNSET KWRD_STMT_GROUP -> ^( UNSET_SG ) ;
    def unset_statement_group(self, ):
        retval = self.unset_statement_group_return()
        retval.start = self.input.LT(1)


        root_0 = None

        KWRD_UNSET42 = None
        KWRD_STMT_GROUP43 = None

        KWRD_UNSET42_tree = None
        KWRD_STMT_GROUP43_tree = None
        stream_KWRD_UNSET = RewriteRuleTokenStream(self._adaptor, "token KWRD_UNSET")
        stream_KWRD_STMT_GROUP = RewriteRuleTokenStream(self._adaptor, "token KWRD_STMT_GROUP")

        try:
            try:
                # BELScript_Python_v1.g:115:5: ( KWRD_UNSET KWRD_STMT_GROUP -> ^( UNSET_SG ) )
                # BELScript_Python_v1.g:115:9: KWRD_UNSET KWRD_STMT_GROUP
                pass
                KWRD_UNSET42 = self.match(self.input, KWRD_UNSET, self.FOLLOW_KWRD_UNSET_in_unset_statement_group814)
                stream_KWRD_UNSET.add(KWRD_UNSET42)


                KWRD_STMT_GROUP43 = self.match(self.input, KWRD_STMT_GROUP, self.FOLLOW_KWRD_STMT_GROUP_in_unset_statement_group816)
                stream_KWRD_STMT_GROUP.add(KWRD_STMT_GROUP43)


                # AST Rewrite
                # elements:
                # token labels:
                # rule labels: retval
                # token list labels:
                # rule list labels:
                # wildcard labels:
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 115:36: -> ^( UNSET_SG )
                # BELScript_Python_v1.g:115:39: ^( UNSET_SG )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(UNSET_SG, "UNSET_SG")
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unset_statement_group"


    class unset_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.unset_return, self).__init__()

            self.tree = None





    # $ANTLR start "unset"
    # BELScript_Python_v1.g:118:1: unset : ( KWRD_UNSET val= OBJECT_IDENT -> ^( UNSET_ID $val) | KWRD_UNSET val= IDENT_LIST -> ^( UNSET_ID_LIST $val) );
    def unset(self, ):
        retval = self.unset_return()
        retval.start = self.input.LT(1)


        root_0 = None

        val = None
        KWRD_UNSET44 = None
        KWRD_UNSET45 = None

        val_tree = None
        KWRD_UNSET44_tree = None
        KWRD_UNSET45_tree = None
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_KWRD_UNSET = RewriteRuleTokenStream(self._adaptor, "token KWRD_UNSET")
        stream_IDENT_LIST = RewriteRuleTokenStream(self._adaptor, "token IDENT_LIST")

        try:
            try:
                # BELScript_Python_v1.g:119:5: ( KWRD_UNSET val= OBJECT_IDENT -> ^( UNSET_ID $val) | KWRD_UNSET val= IDENT_LIST -> ^( UNSET_ID_LIST $val) )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == KWRD_UNSET) :
                    LA9_1 = self.input.LA(2)

                    if (LA9_1 == OBJECT_IDENT) :
                        alt9 = 1
                    elif (LA9_1 == IDENT_LIST) :
                        alt9 = 2
                    else:
                        nvae = NoViableAltException("", 9, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # BELScript_Python_v1.g:119:9: KWRD_UNSET val= OBJECT_IDENT
                    pass
                    KWRD_UNSET44 = self.match(self.input, KWRD_UNSET, self.FOLLOW_KWRD_UNSET_in_unset841)
                    stream_KWRD_UNSET.add(KWRD_UNSET44)


                    val = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_unset845)
                    stream_OBJECT_IDENT.add(val)


                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 119:37: -> ^( UNSET_ID $val)
                    # BELScript_Python_v1.g:119:40: ^( UNSET_ID $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(UNSET_ID, "UNSET_ID")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt9 == 2:
                    # BELScript_Python_v1.g:120:9: KWRD_UNSET val= IDENT_LIST
                    pass
                    KWRD_UNSET45 = self.match(self.input, KWRD_UNSET, self.FOLLOW_KWRD_UNSET_in_unset864)
                    stream_KWRD_UNSET.add(KWRD_UNSET45)


                    val = self.match(self.input, IDENT_LIST, self.FOLLOW_IDENT_LIST_in_unset868)
                    stream_IDENT_LIST.add(val)


                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 120:35: -> ^( UNSET_ID_LIST $val)
                    # BELScript_Python_v1.g:120:38: ^( UNSET_ID_LIST $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(UNSET_ID_LIST, "UNSET_ID_LIST")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unset"


    class define_namespace_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.define_namespace_return, self).__init__()

            self.tree = None





    # $ANTLR start "define_namespace"
    # BELScript_Python_v1.g:123:1: define_namespace : ( KWRD_DEFINE KWRD_DFLT KWRD_NS OBJECT_IDENT KWRD_AS KWRD_URL QUOTED_VALUE -> ^( DFLT_NSDEF OBJECT_IDENT QUOTED_VALUE ) | KWRD_DEFINE KWRD_NS OBJECT_IDENT KWRD_AS KWRD_URL QUOTED_VALUE -> ^( NSDEF OBJECT_IDENT QUOTED_VALUE ) );
    def define_namespace(self, ):
        retval = self.define_namespace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        KWRD_DEFINE46 = None
        KWRD_DFLT47 = None
        KWRD_NS48 = None
        OBJECT_IDENT49 = None
        KWRD_AS50 = None
        KWRD_URL51 = None
        QUOTED_VALUE52 = None
        KWRD_DEFINE53 = None
        KWRD_NS54 = None
        OBJECT_IDENT55 = None
        KWRD_AS56 = None
        KWRD_URL57 = None
        QUOTED_VALUE58 = None

        KWRD_DEFINE46_tree = None
        KWRD_DFLT47_tree = None
        KWRD_NS48_tree = None
        OBJECT_IDENT49_tree = None
        KWRD_AS50_tree = None
        KWRD_URL51_tree = None
        QUOTED_VALUE52_tree = None
        KWRD_DEFINE53_tree = None
        KWRD_NS54_tree = None
        OBJECT_IDENT55_tree = None
        KWRD_AS56_tree = None
        KWRD_URL57_tree = None
        QUOTED_VALUE58_tree = None
        stream_KWRD_DFLT = RewriteRuleTokenStream(self._adaptor, "token KWRD_DFLT")
        stream_KWRD_DEFINE = RewriteRuleTokenStream(self._adaptor, "token KWRD_DEFINE")
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_QUOTED_VALUE = RewriteRuleTokenStream(self._adaptor, "token QUOTED_VALUE")
        stream_KWRD_NS = RewriteRuleTokenStream(self._adaptor, "token KWRD_NS")
        stream_KWRD_URL = RewriteRuleTokenStream(self._adaptor, "token KWRD_URL")
        stream_KWRD_AS = RewriteRuleTokenStream(self._adaptor, "token KWRD_AS")

        try:
            try:
                # BELScript_Python_v1.g:124:5: ( KWRD_DEFINE KWRD_DFLT KWRD_NS OBJECT_IDENT KWRD_AS KWRD_URL QUOTED_VALUE -> ^( DFLT_NSDEF OBJECT_IDENT QUOTED_VALUE ) | KWRD_DEFINE KWRD_NS OBJECT_IDENT KWRD_AS KWRD_URL QUOTED_VALUE -> ^( NSDEF OBJECT_IDENT QUOTED_VALUE ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == KWRD_DEFINE) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == KWRD_DFLT) :
                        alt10 = 1
                    elif (LA10_1 == KWRD_NS) :
                        alt10 = 2
                    else:
                        nvae = NoViableAltException("", 10, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # BELScript_Python_v1.g:124:9: KWRD_DEFINE KWRD_DFLT KWRD_NS OBJECT_IDENT KWRD_AS KWRD_URL QUOTED_VALUE
                    pass
                    KWRD_DEFINE46 = self.match(self.input, KWRD_DEFINE, self.FOLLOW_KWRD_DEFINE_in_define_namespace896)
                    stream_KWRD_DEFINE.add(KWRD_DEFINE46)


                    KWRD_DFLT47 = self.match(self.input, KWRD_DFLT, self.FOLLOW_KWRD_DFLT_in_define_namespace898)
                    stream_KWRD_DFLT.add(KWRD_DFLT47)


                    KWRD_NS48 = self.match(self.input, KWRD_NS, self.FOLLOW_KWRD_NS_in_define_namespace900)
                    stream_KWRD_NS.add(KWRD_NS48)


                    OBJECT_IDENT49 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_define_namespace902)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT49)


                    KWRD_AS50 = self.match(self.input, KWRD_AS, self.FOLLOW_KWRD_AS_in_define_namespace904)
                    stream_KWRD_AS.add(KWRD_AS50)


                    KWRD_URL51 = self.match(self.input, KWRD_URL, self.FOLLOW_KWRD_URL_in_define_namespace906)
                    stream_KWRD_URL.add(KWRD_URL51)


                    QUOTED_VALUE52 = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_define_namespace908)
                    stream_QUOTED_VALUE.add(QUOTED_VALUE52)


                    # AST Rewrite
                    # elements: QUOTED_VALUE, OBJECT_IDENT
                    # token labels:
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 124:82: -> ^( DFLT_NSDEF OBJECT_IDENT QUOTED_VALUE )
                    # BELScript_Python_v1.g:125:9: ^( DFLT_NSDEF OBJECT_IDENT QUOTED_VALUE )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DFLT_NSDEF, "DFLT_NSDEF")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1,
                    stream_QUOTED_VALUE.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt10 == 2:
                    # BELScript_Python_v1.g:126:9: KWRD_DEFINE KWRD_NS OBJECT_IDENT KWRD_AS KWRD_URL QUOTED_VALUE
                    pass
                    KWRD_DEFINE53 = self.match(self.input, KWRD_DEFINE, self.FOLLOW_KWRD_DEFINE_in_define_namespace936)
                    stream_KWRD_DEFINE.add(KWRD_DEFINE53)


                    KWRD_NS54 = self.match(self.input, KWRD_NS, self.FOLLOW_KWRD_NS_in_define_namespace938)
                    stream_KWRD_NS.add(KWRD_NS54)


                    OBJECT_IDENT55 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_define_namespace940)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT55)


                    KWRD_AS56 = self.match(self.input, KWRD_AS, self.FOLLOW_KWRD_AS_in_define_namespace942)
                    stream_KWRD_AS.add(KWRD_AS56)


                    KWRD_URL57 = self.match(self.input, KWRD_URL, self.FOLLOW_KWRD_URL_in_define_namespace944)
                    stream_KWRD_URL.add(KWRD_URL57)


                    QUOTED_VALUE58 = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_define_namespace946)
                    stream_QUOTED_VALUE.add(QUOTED_VALUE58)


                    # AST Rewrite
                    # elements: OBJECT_IDENT, QUOTED_VALUE
                    # token labels:
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 126:72: -> ^( NSDEF OBJECT_IDENT QUOTED_VALUE )
                    # BELScript_Python_v1.g:127:9: ^( NSDEF OBJECT_IDENT QUOTED_VALUE )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NSDEF, "NSDEF")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1,
                    stream_QUOTED_VALUE.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "define_namespace"


    class define_anno_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.define_anno_expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "define_anno_expr"
    # BELScript_Python_v1.g:130:1: define_anno_expr : KWRD_DEFINE ( WS )* KWRD_ANNO ( WS )* ;
    def define_anno_expr(self, ):
        retval = self.define_anno_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        KWRD_DEFINE59 = None
        WS60 = None
        KWRD_ANNO61 = None
        WS62 = None

        KWRD_DEFINE59_tree = None
        WS60_tree = None
        KWRD_ANNO61_tree = None
        WS62_tree = None

        try:
            try:
                # BELScript_Python_v1.g:131:5: ( KWRD_DEFINE ( WS )* KWRD_ANNO ( WS )* )
                # BELScript_Python_v1.g:131:9: KWRD_DEFINE ( WS )* KWRD_ANNO ( WS )*
                pass
                root_0 = self._adaptor.nil()


                KWRD_DEFINE59 = self.match(self.input, KWRD_DEFINE, self.FOLLOW_KWRD_DEFINE_in_define_anno_expr983)
                KWRD_DEFINE59_tree = self._adaptor.createWithPayload(KWRD_DEFINE59)
                self._adaptor.addChild(root_0, KWRD_DEFINE59_tree)



                # BELScript_Python_v1.g:131:21: ( WS )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == WS) :
                        alt11 = 1


                    if alt11 == 1:
                        # BELScript_Python_v1.g:131:21: WS
                        pass
                        WS60 = self.match(self.input, WS, self.FOLLOW_WS_in_define_anno_expr985)
                        WS60_tree = self._adaptor.createWithPayload(WS60)
                        self._adaptor.addChild(root_0, WS60_tree)




                    else:
                        break #loop11


                KWRD_ANNO61 = self.match(self.input, KWRD_ANNO, self.FOLLOW_KWRD_ANNO_in_define_anno_expr988)
                KWRD_ANNO61_tree = self._adaptor.createWithPayload(KWRD_ANNO61)
                self._adaptor.addChild(root_0, KWRD_ANNO61_tree)



                # BELScript_Python_v1.g:131:35: ( WS )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == WS) :
                        alt12 = 1


                    if alt12 == 1:
                        # BELScript_Python_v1.g:131:35: WS
                        pass
                        WS62 = self.match(self.input, WS, self.FOLLOW_WS_in_define_anno_expr990)
                        WS62_tree = self._adaptor.createWithPayload(WS62)
                        self._adaptor.addChild(root_0, WS62_tree)




                    else:
                        break #loop12




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "define_anno_expr"


    class define_annotation_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.define_annotation_return, self).__init__()

            self.tree = None





    # $ANTLR start "define_annotation"
    # BELScript_Python_v1.g:134:1: define_annotation : ( define_anno_expr OBJECT_IDENT KWRD_AS KWRD_LIST val= VALUE_LIST -> ^( ANNO_DEF_LIST OBJECT_IDENT $val) | define_anno_expr OBJECT_IDENT KWRD_AS KWRD_URL val= QUOTED_VALUE -> ^( ANNO_DEF_URL OBJECT_IDENT $val) | define_anno_expr OBJECT_IDENT KWRD_AS KWRD_PATTERN val= QUOTED_VALUE -> ^( ANNO_DEF_PTRN OBJECT_IDENT $val) );
    def define_annotation(self, ):
        retval = self.define_annotation_return()
        retval.start = self.input.LT(1)


        root_0 = None

        val = None
        OBJECT_IDENT64 = None
        KWRD_AS65 = None
        KWRD_LIST66 = None
        OBJECT_IDENT68 = None
        KWRD_AS69 = None
        KWRD_URL70 = None
        OBJECT_IDENT72 = None
        KWRD_AS73 = None
        KWRD_PATTERN74 = None
        define_anno_expr63 = None

        define_anno_expr67 = None

        define_anno_expr71 = None


        val_tree = None
        OBJECT_IDENT64_tree = None
        KWRD_AS65_tree = None
        KWRD_LIST66_tree = None
        OBJECT_IDENT68_tree = None
        KWRD_AS69_tree = None
        KWRD_URL70_tree = None
        OBJECT_IDENT72_tree = None
        KWRD_AS73_tree = None
        KWRD_PATTERN74_tree = None
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_KWRD_LIST = RewriteRuleTokenStream(self._adaptor, "token KWRD_LIST")
        stream_KWRD_PATTERN = RewriteRuleTokenStream(self._adaptor, "token KWRD_PATTERN")
        stream_QUOTED_VALUE = RewriteRuleTokenStream(self._adaptor, "token QUOTED_VALUE")
        stream_KWRD_URL = RewriteRuleTokenStream(self._adaptor, "token KWRD_URL")
        stream_KWRD_AS = RewriteRuleTokenStream(self._adaptor, "token KWRD_AS")
        stream_VALUE_LIST = RewriteRuleTokenStream(self._adaptor, "token VALUE_LIST")
        stream_define_anno_expr = RewriteRuleSubtreeStream(self._adaptor, "rule define_anno_expr")
        try:
            try:
                # BELScript_Python_v1.g:135:5: ( define_anno_expr OBJECT_IDENT KWRD_AS KWRD_LIST val= VALUE_LIST -> ^( ANNO_DEF_LIST OBJECT_IDENT $val) | define_anno_expr OBJECT_IDENT KWRD_AS KWRD_URL val= QUOTED_VALUE -> ^( ANNO_DEF_URL OBJECT_IDENT $val) | define_anno_expr OBJECT_IDENT KWRD_AS KWRD_PATTERN val= QUOTED_VALUE -> ^( ANNO_DEF_PTRN OBJECT_IDENT $val) )
                alt13 = 3
                alt13 = self.dfa13.predict(self.input)
                if alt13 == 1:
                    # BELScript_Python_v1.g:135:9: define_anno_expr OBJECT_IDENT KWRD_AS KWRD_LIST val= VALUE_LIST
                    pass
                    self._state.following.append(self.FOLLOW_define_anno_expr_in_define_annotation1010)
                    define_anno_expr63 = self.define_anno_expr()

                    self._state.following.pop()
                    stream_define_anno_expr.add(define_anno_expr63.tree)


                    OBJECT_IDENT64 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_define_annotation1012)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT64)


                    KWRD_AS65 = self.match(self.input, KWRD_AS, self.FOLLOW_KWRD_AS_in_define_annotation1014)
                    stream_KWRD_AS.add(KWRD_AS65)


                    KWRD_LIST66 = self.match(self.input, KWRD_LIST, self.FOLLOW_KWRD_LIST_in_define_annotation1016)
                    stream_KWRD_LIST.add(KWRD_LIST66)


                    val = self.match(self.input, VALUE_LIST, self.FOLLOW_VALUE_LIST_in_define_annotation1020)
                    stream_VALUE_LIST.add(val)


                    # AST Rewrite
                    # elements: OBJECT_IDENT, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 135:72: -> ^( ANNO_DEF_LIST OBJECT_IDENT $val)
                    # BELScript_Python_v1.g:136:9: ^( ANNO_DEF_LIST OBJECT_IDENT $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNO_DEF_LIST, "ANNO_DEF_LIST")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 2:
                    # BELScript_Python_v1.g:137:9: define_anno_expr OBJECT_IDENT KWRD_AS KWRD_URL val= QUOTED_VALUE
                    pass
                    self._state.following.append(self.FOLLOW_define_anno_expr_in_define_annotation1049)
                    define_anno_expr67 = self.define_anno_expr()

                    self._state.following.pop()
                    stream_define_anno_expr.add(define_anno_expr67.tree)


                    OBJECT_IDENT68 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_define_annotation1051)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT68)


                    KWRD_AS69 = self.match(self.input, KWRD_AS, self.FOLLOW_KWRD_AS_in_define_annotation1053)
                    stream_KWRD_AS.add(KWRD_AS69)


                    KWRD_URL70 = self.match(self.input, KWRD_URL, self.FOLLOW_KWRD_URL_in_define_annotation1055)
                    stream_KWRD_URL.add(KWRD_URL70)


                    val = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_define_annotation1059)
                    stream_QUOTED_VALUE.add(val)


                    # AST Rewrite
                    # elements: OBJECT_IDENT, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 137:73: -> ^( ANNO_DEF_URL OBJECT_IDENT $val)
                    # BELScript_Python_v1.g:138:9: ^( ANNO_DEF_URL OBJECT_IDENT $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNO_DEF_URL, "ANNO_DEF_URL")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 3:
                    # BELScript_Python_v1.g:139:9: define_anno_expr OBJECT_IDENT KWRD_AS KWRD_PATTERN val= QUOTED_VALUE
                    pass
                    self._state.following.append(self.FOLLOW_define_anno_expr_in_define_annotation1088)
                    define_anno_expr71 = self.define_anno_expr()

                    self._state.following.pop()
                    stream_define_anno_expr.add(define_anno_expr71.tree)


                    OBJECT_IDENT72 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_define_annotation1090)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT72)


                    KWRD_AS73 = self.match(self.input, KWRD_AS, self.FOLLOW_KWRD_AS_in_define_annotation1092)
                    stream_KWRD_AS.add(KWRD_AS73)


                    KWRD_PATTERN74 = self.match(self.input, KWRD_PATTERN, self.FOLLOW_KWRD_PATTERN_in_define_annotation1094)
                    stream_KWRD_PATTERN.add(KWRD_PATTERN74)


                    val = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_define_annotation1098)
                    stream_QUOTED_VALUE.add(val)


                    # AST Rewrite
                    # elements: val, OBJECT_IDENT
                    # token labels: val
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 139:77: -> ^( ANNO_DEF_PTRN OBJECT_IDENT $val)
                    # BELScript_Python_v1.g:140:9: ^( ANNO_DEF_PTRN OBJECT_IDENT $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNO_DEF_PTRN, "ANNO_DEF_PTRN")
                    , root_1)

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "define_annotation"


    class document_property_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.document_property_return, self).__init__()

            self.tree = None





    # $ANTLR start "document_property"
    # BELScript_Python_v1.g:143:1: document_property : ( KWRD_AUTHORS | KWRD_CONTACTINFO | KWRD_COPYRIGHT | KWRD_DESC | KWRD_DISCLAIMER | KWRD_LICENSES | KWRD_NAME | KWRD_VERSION );
    def document_property(self, ):
        retval = self.document_property_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set75 = None

        set75_tree = None

        try:
            try:
                # BELScript_Python_v1.g:144:5: ( KWRD_AUTHORS | KWRD_CONTACTINFO | KWRD_COPYRIGHT | KWRD_DESC | KWRD_DISCLAIMER | KWRD_LICENSES | KWRD_NAME | KWRD_VERSION )
                # BELScript_Python_v1.g:
                pass
                root_0 = self._adaptor.nil()


                set75 = self.input.LT(1)

                if (KWRD_AUTHORS <= self.input.LA(1) <= KWRD_COPYRIGHT) or self.input.LA(1) == KWRD_DESC or self.input.LA(1) == KWRD_DISCLAIMER or self.input.LA(1) == KWRD_LICENSES or self.input.LA(1) == KWRD_NAME or self.input.LA(1) == KWRD_VERSION:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set75))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "document_property"


    class argument_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.argument_return, self).__init__()

            self.tree = None





    # $ANTLR start "argument"
    # BELScript_Python_v1.g:154:1: argument : ( ( COMMA )? term -> term | ( COMMA )? param -> param );
    def argument(self, ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA76 = None
        COMMA78 = None
        term77 = None

        param79 = None


        COMMA76_tree = None
        COMMA78_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_param = RewriteRuleSubtreeStream(self._adaptor, "rule param")
        stream_term = RewriteRuleSubtreeStream(self._adaptor, "rule term")
        try:
            try:
                # BELScript_Python_v1.g:155:5: ( ( COMMA )? term -> term | ( COMMA )? param -> param )
                alt16 = 2
                LA16 = self.input.LA(1)
                if LA16 == COMMA:
                    LA16_1 = self.input.LA(2)

                    if ((71 <= LA16_1 <= 73) or LA16_1 == 76 or (78 <= LA16_1 <= 80) or (82 <= LA16_1 <= 89) or (91 <= LA16_1 <= 92) or (95 <= LA16_1 <= 100) or (107 <= LA16_1 <= 112) or (115 <= LA16_1 <= 122) or LA16_1 == 124 or (126 <= LA16_1 <= 128) or (130 <= LA16_1 <= 137) or (139 <= LA16_1 <= 142) or LA16_1 == 144 or (146 <= LA16_1 <= 150)) :
                        alt16 = 1
                    elif (LA16_1 == OBJECT_IDENT or LA16_1 == QUOTED_VALUE) :
                        alt16 = 2
                    else:
                        nvae = NoViableAltException("", 16, 1, self.input)

                        raise nvae


                elif LA16 == 71 or LA16 == 72 or LA16 == 73 or LA16 == 76 or LA16 == 78 or LA16 == 79 or LA16 == 80 or LA16 == 82 or LA16 == 83 or LA16 == 84 or LA16 == 85 or LA16 == 86 or LA16 == 87 or LA16 == 88 or LA16 == 89 or LA16 == 91 or LA16 == 92 or LA16 == 95 or LA16 == 96 or LA16 == 97 or LA16 == 98 or LA16 == 99 or LA16 == 100 or LA16 == 107 or LA16 == 108 or LA16 == 109 or LA16 == 110 or LA16 == 111 or LA16 == 112 or LA16 == 115 or LA16 == 116 or LA16 == 117 or LA16 == 118 or LA16 == 119 or LA16 == 120 or LA16 == 121 or LA16 == 122 or LA16 == 124 or LA16 == 126 or LA16 == 127 or LA16 == 128 or LA16 == 130 or LA16 == 131 or LA16 == 132 or LA16 == 133 or LA16 == 134 or LA16 == 135 or LA16 == 136 or LA16 == 137 or LA16 == 139 or LA16 == 140 or LA16 == 141 or LA16 == 142 or LA16 == 144 or LA16 == 146 or LA16 == 147 or LA16 == 148 or LA16 == 149 or LA16 == 150:
                    alt16 = 1
                elif LA16 == OBJECT_IDENT or LA16 == QUOTED_VALUE:
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # BELScript_Python_v1.g:155:9: ( COMMA )? term
                    pass
                    # BELScript_Python_v1.g:155:9: ( COMMA )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1
                    if alt14 == 1:
                        # BELScript_Python_v1.g:155:9: COMMA
                        pass
                        COMMA76 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argument1225)
                        stream_COMMA.add(COMMA76)





                    self._state.following.append(self.FOLLOW_term_in_argument1228)
                    term77 = self.term()

                    self._state.following.pop()
                    stream_term.add(term77.tree)


                    # AST Rewrite
                    # elements: term
                    # token labels:
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 155:21: -> term
                    self._adaptor.addChild(root_0, stream_term.nextTree())




                    retval.tree = root_0




                elif alt16 == 2:
                    # BELScript_Python_v1.g:156:9: ( COMMA )? param
                    pass
                    # BELScript_Python_v1.g:156:9: ( COMMA )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == COMMA) :
                        alt15 = 1
                    if alt15 == 1:
                        # BELScript_Python_v1.g:156:9: COMMA
                        pass
                        COMMA78 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argument1242)
                        stream_COMMA.add(COMMA78)





                    self._state.following.append(self.FOLLOW_param_in_argument1245)
                    param79 = self.param()

                    self._state.following.pop()
                    stream_param.add(param79.tree)


                    # AST Rewrite
                    # elements: param
                    # token labels:
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 156:22: -> param
                    self._adaptor.addChild(root_0, stream_param.nextTree())




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "argument"


    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.term_return, self).__init__()

            self.tree = None





    # $ANTLR start "term"
    # BELScript_Python_v1.g:159:1: term : function LP ( argument )* RP -> ^( TERMDEF function ( argument )* ) ;
    def term(self, ):
        retval = self.term_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LP81 = None
        RP83 = None
        function80 = None

        argument82 = None


        LP81_tree = None
        RP83_tree = None
        stream_RP = RewriteRuleTokenStream(self._adaptor, "token RP")
        stream_LP = RewriteRuleTokenStream(self._adaptor, "token LP")
        stream_argument = RewriteRuleSubtreeStream(self._adaptor, "rule argument")
        stream_function = RewriteRuleSubtreeStream(self._adaptor, "rule function")
        try:
            try:
                # BELScript_Python_v1.g:160:5: ( function LP ( argument )* RP -> ^( TERMDEF function ( argument )* ) )
                # BELScript_Python_v1.g:160:9: function LP ( argument )* RP
                pass
                self._state.following.append(self.FOLLOW_function_in_term1268)
                function80 = self.function()

                self._state.following.pop()
                stream_function.add(function80.tree)


                LP81 = self.match(self.input, LP, self.FOLLOW_LP_in_term1270)
                stream_LP.add(LP81)


                # BELScript_Python_v1.g:160:21: ( argument )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == COMMA or LA17_0 == OBJECT_IDENT or LA17_0 == QUOTED_VALUE or (71 <= LA17_0 <= 73) or LA17_0 == 76 or (78 <= LA17_0 <= 80) or (82 <= LA17_0 <= 89) or (91 <= LA17_0 <= 92) or (95 <= LA17_0 <= 100) or (107 <= LA17_0 <= 112) or (115 <= LA17_0 <= 122) or LA17_0 == 124 or (126 <= LA17_0 <= 128) or (130 <= LA17_0 <= 137) or (139 <= LA17_0 <= 142) or LA17_0 == 144 or (146 <= LA17_0 <= 150)) :
                        alt17 = 1


                    if alt17 == 1:
                        # BELScript_Python_v1.g:160:22: argument
                        pass
                        self._state.following.append(self.FOLLOW_argument_in_term1273)
                        argument82 = self.argument()

                        self._state.following.pop()
                        stream_argument.add(argument82.tree)



                    else:
                        break #loop17


                RP83 = self.match(self.input, RP, self.FOLLOW_RP_in_term1277)
                stream_RP.add(RP83)


                # AST Rewrite
                # elements: argument, function
                # token labels:
                # rule labels: retval
                # token list labels:
                # rule list labels:
                # wildcard labels:
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 160:36: -> ^( TERMDEF function ( argument )* )
                # BELScript_Python_v1.g:161:9: ^( TERMDEF function ( argument )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TERMDEF, "TERMDEF")
                , root_1)

                self._adaptor.addChild(root_1, stream_function.nextTree())

                # BELScript_Python_v1.g:161:28: ( argument )*
                while stream_argument.hasNext():
                    self._adaptor.addChild(root_1, stream_argument.nextTree())


                stream_argument.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "term"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.statement_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement"
    # BELScript_Python_v1.g:166:1: statement : subject= term (rel= relationship ( LP obj_sub= term obj_rel= relationship obj_obj= term RP |obj= term ) )? (comment= STATEMENT_COMMENT )? -> ^( STMTDEF ( $comment)? $subject ( $rel)? ( $obj)? ( $obj_sub)? ( $obj_rel)? ( $obj_obj)? ) ;
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        comment = None
        LP84 = None
        RP85 = None
        subject = None

        rel = None

        obj_sub = None

        obj_rel = None

        obj_obj = None

        obj = None


        comment_tree = None
        LP84_tree = None
        RP85_tree = None
        stream_RP = RewriteRuleTokenStream(self._adaptor, "token RP")
        stream_STATEMENT_COMMENT = RewriteRuleTokenStream(self._adaptor, "token STATEMENT_COMMENT")
        stream_LP = RewriteRuleTokenStream(self._adaptor, "token LP")
        stream_relationship = RewriteRuleSubtreeStream(self._adaptor, "rule relationship")
        stream_term = RewriteRuleSubtreeStream(self._adaptor, "rule term")
        try:
            try:
                # BELScript_Python_v1.g:167:5: (subject= term (rel= relationship ( LP obj_sub= term obj_rel= relationship obj_obj= term RP |obj= term ) )? (comment= STATEMENT_COMMENT )? -> ^( STMTDEF ( $comment)? $subject ( $rel)? ( $obj)? ( $obj_sub)? ( $obj_rel)? ( $obj_obj)? ) )
                # BELScript_Python_v1.g:167:9: subject= term (rel= relationship ( LP obj_sub= term obj_rel= relationship obj_obj= term RP |obj= term ) )? (comment= STATEMENT_COMMENT )?
                pass
                self._state.following.append(self.FOLLOW_term_in_statement1319)
                subject = self.term()

                self._state.following.pop()
                stream_term.add(subject.tree)


                # BELScript_Python_v1.g:167:22: (rel= relationship ( LP obj_sub= term obj_rel= relationship obj_obj= term RP |obj= term ) )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((64 <= LA19_0 <= 70) or (74 <= LA19_0 <= 75) or LA19_0 == 77 or LA19_0 == 81 or LA19_0 == 90 or (93 <= LA19_0 <= 94) or (101 <= LA19_0 <= 106) or (113 <= LA19_0 <= 114) or LA19_0 == 123 or LA19_0 == 125 or LA19_0 == 129 or LA19_0 == 138 or LA19_0 == 143 or LA19_0 == 145) :
                    alt19 = 1
                if alt19 == 1:
                    # BELScript_Python_v1.g:167:23: rel= relationship ( LP obj_sub= term obj_rel= relationship obj_obj= term RP |obj= term )
                    pass
                    self._state.following.append(self.FOLLOW_relationship_in_statement1324)
                    rel = self.relationship()

                    self._state.following.pop()
                    stream_relationship.add(rel.tree)


                    # BELScript_Python_v1.g:167:40: ( LP obj_sub= term obj_rel= relationship obj_obj= term RP |obj= term )
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == LP) :
                        alt18 = 1
                    elif ((71 <= LA18_0 <= 73) or LA18_0 == 76 or (78 <= LA18_0 <= 80) or (82 <= LA18_0 <= 89) or (91 <= LA18_0 <= 92) or (95 <= LA18_0 <= 100) or (107 <= LA18_0 <= 112) or (115 <= LA18_0 <= 122) or LA18_0 == 124 or (126 <= LA18_0 <= 128) or (130 <= LA18_0 <= 137) or (139 <= LA18_0 <= 142) or LA18_0 == 144 or (146 <= LA18_0 <= 150)) :
                        alt18 = 2
                    else:
                        nvae = NoViableAltException("", 18, 0, self.input)

                        raise nvae


                    if alt18 == 1:
                        # BELScript_Python_v1.g:167:41: LP obj_sub= term obj_rel= relationship obj_obj= term RP
                        pass
                        LP84 = self.match(self.input, LP, self.FOLLOW_LP_in_statement1327)
                        stream_LP.add(LP84)


                        self._state.following.append(self.FOLLOW_term_in_statement1331)
                        obj_sub = self.term()

                        self._state.following.pop()
                        stream_term.add(obj_sub.tree)


                        self._state.following.append(self.FOLLOW_relationship_in_statement1335)
                        obj_rel = self.relationship()

                        self._state.following.pop()
                        stream_relationship.add(obj_rel.tree)


                        self._state.following.append(self.FOLLOW_term_in_statement1339)
                        obj_obj = self.term()

                        self._state.following.pop()
                        stream_term.add(obj_obj.tree)


                        RP85 = self.match(self.input, RP, self.FOLLOW_RP_in_statement1341)
                        stream_RP.add(RP85)



                    elif alt18 == 2:
                        # BELScript_Python_v1.g:167:96: obj= term
                        pass
                        self._state.following.append(self.FOLLOW_term_in_statement1347)
                        obj = self.term()

                        self._state.following.pop()
                        stream_term.add(obj.tree)








                # BELScript_Python_v1.g:167:115: (comment= STATEMENT_COMMENT )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == STATEMENT_COMMENT) :
                    alt20 = 1
                if alt20 == 1:
                    # BELScript_Python_v1.g:167:115: comment= STATEMENT_COMMENT
                    pass
                    comment = self.match(self.input, STATEMENT_COMMENT, self.FOLLOW_STATEMENT_COMMENT_in_statement1354)
                    stream_STATEMENT_COMMENT.add(comment)





                # AST Rewrite
                # elements: obj_rel, obj_obj, subject, obj, rel, comment, obj_sub
                # token labels: comment
                # rule labels: obj_obj, retval, obj_sub, subject, obj, rel, obj_rel
                # token list labels:
                # rule list labels:
                # wildcard labels:
                retval.tree = root_0
                stream_comment = RewriteRuleTokenStream(self._adaptor, "token comment", comment)
                if obj_obj is not None:
                    stream_obj_obj = RewriteRuleSubtreeStream(self._adaptor, "rule obj_obj", obj_obj.tree)
                else:
                    stream_obj_obj = RewriteRuleSubtreeStream(self._adaptor, "token obj_obj", None)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                if obj_sub is not None:
                    stream_obj_sub = RewriteRuleSubtreeStream(self._adaptor, "rule obj_sub", obj_sub.tree)
                else:
                    stream_obj_sub = RewriteRuleSubtreeStream(self._adaptor, "token obj_sub", None)

                if subject is not None:
                    stream_subject = RewriteRuleSubtreeStream(self._adaptor, "rule subject", subject.tree)
                else:
                    stream_subject = RewriteRuleSubtreeStream(self._adaptor, "token subject", None)

                if obj is not None:
                    stream_obj = RewriteRuleSubtreeStream(self._adaptor, "rule obj", obj.tree)
                else:
                    stream_obj = RewriteRuleSubtreeStream(self._adaptor, "token obj", None)

                if rel is not None:
                    stream_rel = RewriteRuleSubtreeStream(self._adaptor, "rule rel", rel.tree)
                else:
                    stream_rel = RewriteRuleSubtreeStream(self._adaptor, "token rel", None)

                if obj_rel is not None:
                    stream_obj_rel = RewriteRuleSubtreeStream(self._adaptor, "rule obj_rel", obj_rel.tree)
                else:
                    stream_obj_rel = RewriteRuleSubtreeStream(self._adaptor, "token obj_rel", None)


                root_0 = self._adaptor.nil()
                # 167:135: -> ^( STMTDEF ( $comment)? $subject ( $rel)? ( $obj)? ( $obj_sub)? ( $obj_rel)? ( $obj_obj)? )
                # BELScript_Python_v1.g:168:9: ^( STMTDEF ( $comment)? $subject ( $rel)? ( $obj)? ( $obj_sub)? ( $obj_rel)? ( $obj_obj)? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STMTDEF, "STMTDEF")
                , root_1)

                # BELScript_Python_v1.g:168:20: ( $comment)?
                if stream_comment.hasNext():
                    self._adaptor.addChild(root_1, stream_comment.nextNode())


                stream_comment.reset();

                self._adaptor.addChild(root_1, stream_subject.nextTree())

                # BELScript_Python_v1.g:168:39: ( $rel)?
                if stream_rel.hasNext():
                    self._adaptor.addChild(root_1, stream_rel.nextTree())


                stream_rel.reset();

                # BELScript_Python_v1.g:168:45: ( $obj)?
                if stream_obj.hasNext():
                    self._adaptor.addChild(root_1, stream_obj.nextTree())


                stream_obj.reset();

                # BELScript_Python_v1.g:168:51: ( $obj_sub)?
                if stream_obj_sub.hasNext():
                    self._adaptor.addChild(root_1, stream_obj_sub.nextTree())


                stream_obj_sub.reset();

                # BELScript_Python_v1.g:168:61: ( $obj_rel)?
                if stream_obj_rel.hasNext():
                    self._adaptor.addChild(root_1, stream_obj_rel.nextTree())


                stream_obj_rel.reset();

                # BELScript_Python_v1.g:168:71: ( $obj_obj)?
                if stream_obj_obj.hasNext():
                    self._adaptor.addChild(root_1, stream_obj_obj.nextTree())


                stream_obj_obj.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "statement"


    class ns_prefix_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.ns_prefix_return, self).__init__()

            self.tree = None





    # $ANTLR start "ns_prefix"
    # BELScript_Python_v1.g:171:1: ns_prefix : OBJECT_IDENT COLON !;
    def ns_prefix(self, ):
        retval = self.ns_prefix_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBJECT_IDENT86 = None
        COLON87 = None

        OBJECT_IDENT86_tree = None
        COLON87_tree = None

        try:
            try:
                # BELScript_Python_v1.g:172:5: ( OBJECT_IDENT COLON !)
                # BELScript_Python_v1.g:172:9: OBJECT_IDENT COLON !
                pass
                root_0 = self._adaptor.nil()


                OBJECT_IDENT86 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_ns_prefix1415)
                OBJECT_IDENT86_tree = self._adaptor.createWithPayload(OBJECT_IDENT86)
                self._adaptor.addChild(root_0, OBJECT_IDENT86_tree)



                COLON87 = self.match(self.input, COLON, self.FOLLOW_COLON_in_ns_prefix1417)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "ns_prefix"


    class param_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.param_return, self).__init__()

            self.tree = None





    # $ANTLR start "param"
    # BELScript_Python_v1.g:175:1: param : ( ( ns_prefix )? OBJECT_IDENT -> ^( PARAM_DEF_ID ( ns_prefix )? OBJECT_IDENT ) | ( ns_prefix )? QUOTED_VALUE -> ^( PARAM_DEF_QV ( ns_prefix )? QUOTED_VALUE ) );
    def param(self, ):
        retval = self.param_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBJECT_IDENT89 = None
        QUOTED_VALUE91 = None
        ns_prefix88 = None

        ns_prefix90 = None


        OBJECT_IDENT89_tree = None
        QUOTED_VALUE91_tree = None
        stream_OBJECT_IDENT = RewriteRuleTokenStream(self._adaptor, "token OBJECT_IDENT")
        stream_QUOTED_VALUE = RewriteRuleTokenStream(self._adaptor, "token QUOTED_VALUE")
        stream_ns_prefix = RewriteRuleSubtreeStream(self._adaptor, "rule ns_prefix")
        try:
            try:
                # BELScript_Python_v1.g:176:5: ( ( ns_prefix )? OBJECT_IDENT -> ^( PARAM_DEF_ID ( ns_prefix )? OBJECT_IDENT ) | ( ns_prefix )? QUOTED_VALUE -> ^( PARAM_DEF_QV ( ns_prefix )? QUOTED_VALUE ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == OBJECT_IDENT) :
                    LA23_1 = self.input.LA(2)

                    if (LA23_1 == COLON) :
                        LA23_3 = self.input.LA(3)

                        if (LA23_3 == OBJECT_IDENT) :
                            alt23 = 1
                        elif (LA23_3 == QUOTED_VALUE) :
                            alt23 = 2
                        else:
                            nvae = NoViableAltException("", 23, 3, self.input)

                            raise nvae


                    elif (LA23_1 == COMMA or LA23_1 == OBJECT_IDENT or (QUOTED_VALUE <= LA23_1 <= RP) or (71 <= LA23_1 <= 73) or LA23_1 == 76 or (78 <= LA23_1 <= 80) or (82 <= LA23_1 <= 89) or (91 <= LA23_1 <= 92) or (95 <= LA23_1 <= 100) or (107 <= LA23_1 <= 112) or (115 <= LA23_1 <= 122) or LA23_1 == 124 or (126 <= LA23_1 <= 128) or (130 <= LA23_1 <= 137) or (139 <= LA23_1 <= 142) or LA23_1 == 144 or (146 <= LA23_1 <= 150)) :
                        alt23 = 1
                    else:
                        nvae = NoViableAltException("", 23, 1, self.input)

                        raise nvae


                elif (LA23_0 == QUOTED_VALUE) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # BELScript_Python_v1.g:176:9: ( ns_prefix )? OBJECT_IDENT
                    pass
                    # BELScript_Python_v1.g:176:9: ( ns_prefix )?
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == OBJECT_IDENT) :
                        LA21_1 = self.input.LA(2)

                        if (LA21_1 == COLON) :
                            alt21 = 1
                    if alt21 == 1:
                        # BELScript_Python_v1.g:176:9: ns_prefix
                        pass
                        self._state.following.append(self.FOLLOW_ns_prefix_in_param1437)
                        ns_prefix88 = self.ns_prefix()

                        self._state.following.pop()
                        stream_ns_prefix.add(ns_prefix88.tree)





                    OBJECT_IDENT89 = self.match(self.input, OBJECT_IDENT, self.FOLLOW_OBJECT_IDENT_in_param1440)
                    stream_OBJECT_IDENT.add(OBJECT_IDENT89)


                    # AST Rewrite
                    # elements: OBJECT_IDENT, ns_prefix
                    # token labels:
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 176:33: -> ^( PARAM_DEF_ID ( ns_prefix )? OBJECT_IDENT )
                    # BELScript_Python_v1.g:176:36: ^( PARAM_DEF_ID ( ns_prefix )? OBJECT_IDENT )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(PARAM_DEF_ID, "PARAM_DEF_ID")
                    , root_1)

                    # BELScript_Python_v1.g:176:51: ( ns_prefix )?
                    if stream_ns_prefix.hasNext():
                        self._adaptor.addChild(root_1, stream_ns_prefix.nextTree())


                    stream_ns_prefix.reset();

                    self._adaptor.addChild(root_1,
                    stream_OBJECT_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt23 == 2:
                    # BELScript_Python_v1.g:177:9: ( ns_prefix )? QUOTED_VALUE
                    pass
                    # BELScript_Python_v1.g:177:9: ( ns_prefix )?
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == OBJECT_IDENT) :
                        alt22 = 1
                    if alt22 == 1:
                        # BELScript_Python_v1.g:177:9: ns_prefix
                        pass
                        self._state.following.append(self.FOLLOW_ns_prefix_in_param1461)
                        ns_prefix90 = self.ns_prefix()

                        self._state.following.pop()
                        stream_ns_prefix.add(ns_prefix90.tree)





                    QUOTED_VALUE91 = self.match(self.input, QUOTED_VALUE, self.FOLLOW_QUOTED_VALUE_in_param1464)
                    stream_QUOTED_VALUE.add(QUOTED_VALUE91)


                    # AST Rewrite
                    # elements: QUOTED_VALUE, ns_prefix
                    # token labels:
                    # rule labels: retval
                    # token list labels:
                    # rule list labels:
                    # wildcard labels:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 177:33: -> ^( PARAM_DEF_QV ( ns_prefix )? QUOTED_VALUE )
                    # BELScript_Python_v1.g:177:36: ^( PARAM_DEF_QV ( ns_prefix )? QUOTED_VALUE )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(PARAM_DEF_QV, "PARAM_DEF_QV")
                    , root_1)

                    # BELScript_Python_v1.g:177:51: ( ns_prefix )?
                    if stream_ns_prefix.hasNext():
                        self._adaptor.addChild(root_1, stream_ns_prefix.nextTree())


                    stream_ns_prefix.reset();

                    self._adaptor.addChild(root_1,
                    stream_QUOTED_VALUE.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "param"


    class function_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.function_return, self).__init__()

            self.r = None
            self.tree = None





    # $ANTLR start "function"
    # BELScript_Python_v1.g:180:1: function returns [r] : (fv= 'proteinAbundance' |fv= 'p' |fv= 'rnaAbundance' |fv= 'r' |fv= 'abundance' |fv= 'a' |fv= 'microRNAAbundance' |fv= 'm' |fv= 'geneAbundance' |fv= 'g' |fv= 'biologicalProcess' |fv= 'bp' |fv= 'pathology' |fv= 'path' |fv= 'complexAbundance' |fv= 'complex' |fv= 'translocation' |fv= 'tloc' |fv= 'cellSecretion' |fv= 'sec' |fv= 'cellSurfaceExpression' |fv= 'surf' |fv= 'reaction' |fv= 'rxn' |fv= 'compositeAbundance' |fv= 'composite' |fv= 'fusion' |fv= 'fus' |fv= 'degradation' |fv= 'deg' |fv= 'molecularActivity' |fv= 'act' |fv= 'catalyticActivity' |fv= 'cat' |fv= 'kinaseActivity' |fv= 'kin' |fv= 'phosphataseActivity' |fv= 'phos' |fv= 'peptidaseActivity' |fv= 'pep' |fv= 'ribosylationActivity' |fv= 'ribo' |fv= 'transcriptionalActivity' |fv= 'tscript' |fv= 'transportActivity' |fv= 'tport' |fv= 'gtpBoundActivity' |fv= 'gtp' |fv= 'chaperoneActivity' |fv= 'chap' |fv= 'proteinModification' |fv= 'pmod' |fv= 'substitution' |fv= 'sub' |fv= 'truncation' |fv= 'trunc' |fv= 'reactants' |fv= 'products' |fv= 'list' );
    def function(self, ):
        retval = self.function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        fv = None

        fv_tree = None

        try:
            try:
                # BELScript_Python_v1.g:181:5: (fv= 'proteinAbundance' |fv= 'p' |fv= 'rnaAbundance' |fv= 'r' |fv= 'abundance' |fv= 'a' |fv= 'microRNAAbundance' |fv= 'm' |fv= 'geneAbundance' |fv= 'g' |fv= 'biologicalProcess' |fv= 'bp' |fv= 'pathology' |fv= 'path' |fv= 'complexAbundance' |fv= 'complex' |fv= 'translocation' |fv= 'tloc' |fv= 'cellSecretion' |fv= 'sec' |fv= 'cellSurfaceExpression' |fv= 'surf' |fv= 'reaction' |fv= 'rxn' |fv= 'compositeAbundance' |fv= 'composite' |fv= 'fusion' |fv= 'fus' |fv= 'degradation' |fv= 'deg' |fv= 'molecularActivity' |fv= 'act' |fv= 'catalyticActivity' |fv= 'cat' |fv= 'kinaseActivity' |fv= 'kin' |fv= 'phosphataseActivity' |fv= 'phos' |fv= 'peptidaseActivity' |fv= 'pep' |fv= 'ribosylationActivity' |fv= 'ribo' |fv= 'transcriptionalActivity' |fv= 'tscript' |fv= 'transportActivity' |fv= 'tport' |fv= 'gtpBoundActivity' |fv= 'gtp' |fv= 'chaperoneActivity' |fv= 'chap' |fv= 'proteinModification' |fv= 'pmod' |fv= 'substitution' |fv= 'sub' |fv= 'truncation' |fv= 'trunc' |fv= 'reactants' |fv= 'products' |fv= 'list' )
                alt24 = 59
                LA24 = self.input.LA(1)
                if LA24 == 126:
                    alt24 = 1
                elif LA24 == 115:
                    alt24 = 2
                elif LA24 == 134:
                    alt24 = 3
                elif LA24 == 128:
                    alt24 = 4
                elif LA24 == 72:
                    alt24 = 5
                elif LA24 == 71:
                    alt24 = 6
                elif LA24 == 111:
                    alt24 = 7
                elif LA24 == 110:
                    alt24 = 8
                elif LA24 == 98:
                    alt24 = 9
                elif LA24 == 97:
                    alt24 = 10
                elif LA24 == 76:
                    alt24 = 11
                elif LA24 == 78:
                    alt24 = 12
                elif LA24 == 117:
                    alt24 = 13
                elif LA24 == 116:
                    alt24 = 14
                elif LA24 == 87:
                    alt24 = 15
                elif LA24 == 86:
                    alt24 = 16
                elif LA24 == 146:
                    alt24 = 17
                elif LA24 == 141:
                    alt24 = 18
                elif LA24 == 82:
                    alt24 = 19
                elif LA24 == 136:
                    alt24 = 20
                elif LA24 == 83:
                    alt24 = 21
                elif LA24 == 140:
                    alt24 = 22
                elif LA24 == 131:
                    alt24 = 23
                elif LA24 == 135:
                    alt24 = 24
                elif LA24 == 89:
                    alt24 = 25
                elif LA24 == 88:
                    alt24 = 26
                elif LA24 == 96:
                    alt24 = 27
                elif LA24 == 95:
                    alt24 = 28
                elif LA24 == 92:
                    alt24 = 29
                elif LA24 == 91:
                    alt24 = 30
                elif LA24 == 112:
                    alt24 = 31
                elif LA24 == 73:
                    alt24 = 32
                elif LA24 == 80:
                    alt24 = 33
                elif LA24 == 79:
                    alt24 = 34
                elif LA24 == 108:
                    alt24 = 35
                elif LA24 == 107:
                    alt24 = 36
                elif LA24 == 121:
                    alt24 = 37
                elif LA24 == 120:
                    alt24 = 38
                elif LA24 == 119:
                    alt24 = 39
                elif LA24 == 118:
                    alt24 = 40
                elif LA24 == 133:
                    alt24 = 41
                elif LA24 == 132:
                    alt24 = 42
                elif LA24 == 144:
                    alt24 = 43
                elif LA24 == 150:
                    alt24 = 44
                elif LA24 == 147:
                    alt24 = 45
                elif LA24 == 142:
                    alt24 = 46
                elif LA24 == 100:
                    alt24 = 47
                elif LA24 == 99:
                    alt24 = 48
                elif LA24 == 85:
                    alt24 = 49
                elif LA24 == 84:
                    alt24 = 50
                elif LA24 == 127:
                    alt24 = 51
                elif LA24 == 122:
                    alt24 = 52
                elif LA24 == 139:
                    alt24 = 53
                elif LA24 == 137:
                    alt24 = 54
                elif LA24 == 149:
                    alt24 = 55
                elif LA24 == 148:
                    alt24 = 56
                elif LA24 == 130:
                    alt24 = 57
                elif LA24 == 124:
                    alt24 = 58
                elif LA24 == 109:
                    alt24 = 59
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # BELScript_Python_v1.g:181:9: fv= 'proteinAbundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 126, self.FOLLOW_126_in_function1500)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "p"
                    #action end



                elif alt24 == 2:
                    # BELScript_Python_v1.g:182:9: fv= 'p'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 115, self.FOLLOW_115_in_function1524)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "p"
                    #action end



                elif alt24 == 3:
                    # BELScript_Python_v1.g:183:9: fv= 'rnaAbundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 134, self.FOLLOW_134_in_function1563)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "r"
                    #action end



                elif alt24 == 4:
                    # BELScript_Python_v1.g:184:9: fv= 'r'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 128, self.FOLLOW_128_in_function1591)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "r"
                    #action end



                elif alt24 == 5:
                    # BELScript_Python_v1.g:185:9: fv= 'abundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 72, self.FOLLOW_72_in_function1630)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "a"
                    #action end



                elif alt24 == 6:
                    # BELScript_Python_v1.g:186:9: fv= 'a'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 71, self.FOLLOW_71_in_function1661)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "a"
                    #action end



                elif alt24 == 7:
                    # BELScript_Python_v1.g:187:9: fv= 'microRNAAbundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 111, self.FOLLOW_111_in_function1700)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "m"
                    #action end



                elif alt24 == 8:
                    # BELScript_Python_v1.g:188:9: fv= 'm'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 110, self.FOLLOW_110_in_function1723)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "m"
                    #action end



                elif alt24 == 9:
                    # BELScript_Python_v1.g:189:9: fv= 'geneAbundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 98, self.FOLLOW_98_in_function1762)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "g"
                    #action end



                elif alt24 == 10:
                    # BELScript_Python_v1.g:190:9: fv= 'g'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 97, self.FOLLOW_97_in_function1789)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "g"
                    #action end



                elif alt24 == 11:
                    # BELScript_Python_v1.g:191:9: fv= 'biologicalProcess'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 76, self.FOLLOW_76_in_function1828)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "bp"
                    #action end



                elif alt24 == 12:
                    # BELScript_Python_v1.g:192:9: fv= 'bp'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 78, self.FOLLOW_78_in_function1851)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "bp"
                    #action end



                elif alt24 == 13:
                    # BELScript_Python_v1.g:193:9: fv= 'pathology'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 117, self.FOLLOW_117_in_function1889)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "path"
                    #action end



                elif alt24 == 14:
                    # BELScript_Python_v1.g:194:9: fv= 'path'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 116, self.FOLLOW_116_in_function1920)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "path"
                    #action end



                elif alt24 == 15:
                    # BELScript_Python_v1.g:195:9: fv= 'complexAbundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 87, self.FOLLOW_87_in_function1956)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "complex"
                    #action end



                elif alt24 == 16:
                    # BELScript_Python_v1.g:196:9: fv= 'complex'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 86, self.FOLLOW_86_in_function1980)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "complex"
                    #action end



                elif alt24 == 17:
                    # BELScript_Python_v1.g:197:9: fv= 'translocation'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 146, self.FOLLOW_146_in_function2013)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "tloc"
                    #action end



                elif alt24 == 18:
                    # BELScript_Python_v1.g:198:9: fv= 'tloc'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 141, self.FOLLOW_141_in_function2040)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "tloc"
                    #action end



                elif alt24 == 19:
                    # BELScript_Python_v1.g:199:9: fv= 'cellSecretion'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 82, self.FOLLOW_82_in_function2076)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "sec"
                    #action end



                elif alt24 == 20:
                    # BELScript_Python_v1.g:200:9: fv= 'sec'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 136, self.FOLLOW_136_in_function2103)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "sec"
                    #action end



                elif alt24 == 21:
                    # BELScript_Python_v1.g:201:9: fv= 'cellSurfaceExpression'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 83, self.FOLLOW_83_in_function2140)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "surf"
                    #action end



                elif alt24 == 22:
                    # BELScript_Python_v1.g:202:9: fv= 'surf'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 140, self.FOLLOW_140_in_function2159)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "surf"
                    #action end



                elif alt24 == 23:
                    # BELScript_Python_v1.g:203:9: fv= 'reaction'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 131, self.FOLLOW_131_in_function2195)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "rxn"
                    #action end



                elif alt24 == 24:
                    # BELScript_Python_v1.g:204:9: fv= 'rxn'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 135, self.FOLLOW_135_in_function2227)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "rxn"
                    #action end



                elif alt24 == 25:
                    # BELScript_Python_v1.g:205:9: fv= 'compositeAbundance'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 89, self.FOLLOW_89_in_function2264)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "composite"
                    #action end



                elif alt24 == 26:
                    # BELScript_Python_v1.g:206:9: fv= 'composite'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 88, self.FOLLOW_88_in_function2286)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "composite"
                    #action end



                elif alt24 == 27:
                    # BELScript_Python_v1.g:207:9: fv= 'fusion'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 96, self.FOLLOW_96_in_function2317)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "fus"
                    #action end



                elif alt24 == 28:
                    # BELScript_Python_v1.g:208:9: fv= 'fus'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 95, self.FOLLOW_95_in_function2351)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "fus"
                    #action end



                elif alt24 == 29:
                    # BELScript_Python_v1.g:209:9: fv= 'degradation'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 92, self.FOLLOW_92_in_function2388)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "deg"
                    #action end



                elif alt24 == 30:
                    # BELScript_Python_v1.g:210:9: fv= 'deg'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 91, self.FOLLOW_91_in_function2417)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "deg"
                    #action end



                elif alt24 == 31:
                    # BELScript_Python_v1.g:211:9: fv= 'molecularActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 112, self.FOLLOW_112_in_function2454)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "act"
                    #action end



                elif alt24 == 32:
                    # BELScript_Python_v1.g:212:9: fv= 'act'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 73, self.FOLLOW_73_in_function2477)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "act"
                    #action end



                elif alt24 == 33:
                    # BELScript_Python_v1.g:213:9: fv= 'catalyticActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 80, self.FOLLOW_80_in_function2514)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "cat"
                    #action end



                elif alt24 == 34:
                    # BELScript_Python_v1.g:214:9: fv= 'cat'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 79, self.FOLLOW_79_in_function2537)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "cat"
                    #action end



                elif alt24 == 35:
                    # BELScript_Python_v1.g:215:9: fv= 'kinaseActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 108, self.FOLLOW_108_in_function2574)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "kin"
                    #action end



                elif alt24 == 36:
                    # BELScript_Python_v1.g:216:9: fv= 'kin'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 107, self.FOLLOW_107_in_function2600)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "kin"
                    #action end



                elif alt24 == 37:
                    # BELScript_Python_v1.g:217:9: fv= 'phosphataseActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 121, self.FOLLOW_121_in_function2637)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "phos"
                    #action end



                elif alt24 == 38:
                    # BELScript_Python_v1.g:218:9: fv= 'phos'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 120, self.FOLLOW_120_in_function2658)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "phos"
                    #action end



                elif alt24 == 39:
                    # BELScript_Python_v1.g:219:9: fv= 'peptidaseActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 119, self.FOLLOW_119_in_function2694)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "pep"
                    #action end



                elif alt24 == 40:
                    # BELScript_Python_v1.g:220:9: fv= 'pep'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 118, self.FOLLOW_118_in_function2717)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "pep"
                    #action end



                elif alt24 == 41:
                    # BELScript_Python_v1.g:221:9: fv= 'ribosylationActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 133, self.FOLLOW_133_in_function2754)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "ribo"
                    #action end



                elif alt24 == 42:
                    # BELScript_Python_v1.g:222:9: fv= 'ribo'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 132, self.FOLLOW_132_in_function2774)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "ribo"
                    #action end



                elif alt24 == 43:
                    # BELScript_Python_v1.g:223:9: fv= 'transcriptionalActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 144, self.FOLLOW_144_in_function2810)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "tscript"
                    #action end



                elif alt24 == 44:
                    # BELScript_Python_v1.g:224:9: fv= 'tscript'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 150, self.FOLLOW_150_in_function2827)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "tscript"
                    #action end



                elif alt24 == 45:
                    # BELScript_Python_v1.g:225:9: fv= 'transportActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 147, self.FOLLOW_147_in_function2860)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "tport"
                    #action end



                elif alt24 == 46:
                    # BELScript_Python_v1.g:226:9: fv= 'tport'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 142, self.FOLLOW_142_in_function2883)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "tport"
                    #action end



                elif alt24 == 47:
                    # BELScript_Python_v1.g:227:9: fv= 'gtpBoundActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 100, self.FOLLOW_100_in_function2918)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "gtp"
                    #action end



                elif alt24 == 48:
                    # BELScript_Python_v1.g:228:9: fv= 'gtp'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 99, self.FOLLOW_99_in_function2942)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "gtp"
                    #action end



                elif alt24 == 49:
                    # BELScript_Python_v1.g:229:9: fv= 'chaperoneActivity'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 85, self.FOLLOW_85_in_function2979)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "chap"
                    #action end



                elif alt24 == 50:
                    # BELScript_Python_v1.g:230:9: fv= 'chap'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 84, self.FOLLOW_84_in_function3002)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "chap"
                    #action end



                elif alt24 == 51:
                    # BELScript_Python_v1.g:231:9: fv= 'proteinModification'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 127, self.FOLLOW_127_in_function3038)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "pmod"
                    #action end



                elif alt24 == 52:
                    # BELScript_Python_v1.g:232:9: fv= 'pmod'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 122, self.FOLLOW_122_in_function3059)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "pmod"
                    #action end



                elif alt24 == 53:
                    # BELScript_Python_v1.g:233:9: fv= 'substitution'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 139, self.FOLLOW_139_in_function3095)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "sub"
                    #action end



                elif alt24 == 54:
                    # BELScript_Python_v1.g:234:9: fv= 'sub'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 137, self.FOLLOW_137_in_function3123)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "sub"
                    #action end



                elif alt24 == 55:
                    # BELScript_Python_v1.g:235:9: fv= 'truncation'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 149, self.FOLLOW_149_in_function3160)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "trunc"
                    #action end



                elif alt24 == 56:
                    # BELScript_Python_v1.g:236:9: fv= 'trunc'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 148, self.FOLLOW_148_in_function3190)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "trunc"
                    #action end



                elif alt24 == 57:
                    # BELScript_Python_v1.g:237:9: fv= 'reactants'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 130, self.FOLLOW_130_in_function3225)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "reactants"
                    #action end



                elif alt24 == 58:
                    # BELScript_Python_v1.g:238:9: fv= 'products'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 124, self.FOLLOW_124_in_function3256)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "products"
                    #action end



                elif alt24 == 59:
                    # BELScript_Python_v1.g:239:9: fv= 'list'
                    pass
                    root_0 = self._adaptor.nil()


                    fv = self.match(self.input, 109, self.FOLLOW_109_in_function3288)
                    fv_tree = self._adaptor.createWithPayload(fv)
                    self._adaptor.addChild(root_0, fv_tree)



                    #action start
                    retval.r =  "list"
                    #action end



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "function"


    class relationship_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.relationship_return, self).__init__()

            self.r = None
            self.tree = None





    # $ANTLR start "relationship"
    # BELScript_Python_v1.g:242:1: relationship returns [r] : (rv= 'increases' |rv= '->' |rv= 'decreases' |rv= '-|' |rv= 'directlyIncreases' |rv= '=>' |rv= 'directlyDecreases' |rv= '=|' |rv= 'causesNoChange' |rv= 'positiveCorrelation' |rv= 'negativeCorrelation' |rv= 'translatedTo' |rv= '>>' |rv= 'transcribedTo' |rv= ':>' |rv= 'isA' |rv= 'subProcessOf' |rv= 'rateLimitingStepOf' |rv= 'biomarkerFor' |rv= 'prognosticBiomarkerFor' |rv= 'orthologous' |rv= 'analogous' |rv= 'association' |rv= '--' |rv= 'hasMembers' |rv= 'hasComponents' |rv= 'hasMember' |rv= 'hasComponent' );
    def relationship(self, ):
        retval = self.relationship_return()
        retval.start = self.input.LT(1)


        root_0 = None

        rv = None

        rv_tree = None

        try:
            try:
                # BELScript_Python_v1.g:243:5: (rv= 'increases' |rv= '->' |rv= 'decreases' |rv= '-|' |rv= 'directlyIncreases' |rv= '=>' |rv= 'directlyDecreases' |rv= '=|' |rv= 'causesNoChange' |rv= 'positiveCorrelation' |rv= 'negativeCorrelation' |rv= 'translatedTo' |rv= '>>' |rv= 'transcribedTo' |rv= ':>' |rv= 'isA' |rv= 'subProcessOf' |rv= 'rateLimitingStepOf' |rv= 'biomarkerFor' |rv= 'prognosticBiomarkerFor' |rv= 'orthologous' |rv= 'analogous' |rv= 'association' |rv= '--' |rv= 'hasMembers' |rv= 'hasComponents' |rv= 'hasMember' |rv= 'hasComponent' )
                alt25 = 28
                LA25 = self.input.LA(1)
                if LA25 == 105:
                    alt25 = 1
                elif LA25 == 65:
                    alt25 = 2
                elif LA25 == 90:
                    alt25 = 3
                elif LA25 == 66:
                    alt25 = 4
                elif LA25 == 94:
                    alt25 = 5
                elif LA25 == 68:
                    alt25 = 6
                elif LA25 == 93:
                    alt25 = 7
                elif LA25 == 69:
                    alt25 = 8
                elif LA25 == 81:
                    alt25 = 9
                elif LA25 == 123:
                    alt25 = 10
                elif LA25 == 113:
                    alt25 = 11
                elif LA25 == 145:
                    alt25 = 12
                elif LA25 == 70:
                    alt25 = 13
                elif LA25 == 143:
                    alt25 = 14
                elif LA25 == 67:
                    alt25 = 15
                elif LA25 == 106:
                    alt25 = 16
                elif LA25 == 138:
                    alt25 = 17
                elif LA25 == 129:
                    alt25 = 18
                elif LA25 == 77:
                    alt25 = 19
                elif LA25 == 125:
                    alt25 = 20
                elif LA25 == 114:
                    alt25 = 21
                elif LA25 == 74:
                    alt25 = 22
                elif LA25 == 75:
                    alt25 = 23
                elif LA25 == 64:
                    alt25 = 24
                elif LA25 == 104:
                    alt25 = 25
                elif LA25 == 102:
                    alt25 = 26
                elif LA25 == 103:
                    alt25 = 27
                elif LA25 == 101:
                    alt25 = 28
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # BELScript_Python_v1.g:243:9: rv= 'increases'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 105, self.FOLLOW_105_in_relationship3337)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "increases"
                    #action end



                elif alt25 == 2:
                    # BELScript_Python_v1.g:244:9: rv= '->'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 65, self.FOLLOW_65_in_relationship3368)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "increases"
                    #action end



                elif alt25 == 3:
                    # BELScript_Python_v1.g:245:9: rv= 'decreases'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 90, self.FOLLOW_90_in_relationship3406)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "decreases"
                    #action end



                elif alt25 == 4:
                    # BELScript_Python_v1.g:246:9: rv= '-|'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 66, self.FOLLOW_66_in_relationship3437)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "decreases"
                    #action end



                elif alt25 == 5:
                    # BELScript_Python_v1.g:247:9: rv= 'directlyIncreases'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 94, self.FOLLOW_94_in_relationship3475)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "directlyIncreases"
                    #action end



                elif alt25 == 6:
                    # BELScript_Python_v1.g:248:9: rv= '=>'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 68, self.FOLLOW_68_in_relationship3498)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "directlyIncreases"
                    #action end



                elif alt25 == 7:
                    # BELScript_Python_v1.g:249:9: rv= 'directlyDecreases'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 93, self.FOLLOW_93_in_relationship3536)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "directlyDecreases"
                    #action end



                elif alt25 == 8:
                    # BELScript_Python_v1.g:250:9: rv= '=|'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 69, self.FOLLOW_69_in_relationship3559)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "directlyDecreases"
                    #action end



                elif alt25 == 9:
                    # BELScript_Python_v1.g:251:9: rv= 'causesNoChange'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 81, self.FOLLOW_81_in_relationship3597)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "causesNoChange"
                    #action end



                elif alt25 == 10:
                    # BELScript_Python_v1.g:252:9: rv= 'positiveCorrelation'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 123, self.FOLLOW_123_in_relationship3623)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "positiveCorrelation"
                    #action end



                elif alt25 == 11:
                    # BELScript_Python_v1.g:253:9: rv= 'negativeCorrelation'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 113, self.FOLLOW_113_in_relationship3644)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "negativeCorrelation"
                    #action end



                elif alt25 == 12:
                    # BELScript_Python_v1.g:254:9: rv= 'translatedTo'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 145, self.FOLLOW_145_in_relationship3665)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "translatedTo"
                    #action end



                elif alt25 == 13:
                    # BELScript_Python_v1.g:255:9: rv= '>>'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 70, self.FOLLOW_70_in_relationship3693)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "translatedTo"
                    #action end



                elif alt25 == 14:
                    # BELScript_Python_v1.g:256:9: rv= 'transcribedTo'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 143, self.FOLLOW_143_in_relationship3731)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "transcribedTo"
                    #action end



                elif alt25 == 15:
                    # BELScript_Python_v1.g:257:9: rv= ':>'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 67, self.FOLLOW_67_in_relationship3758)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "transcribedTo"
                    #action end



                elif alt25 == 16:
                    # BELScript_Python_v1.g:258:9: rv= 'isA'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 106, self.FOLLOW_106_in_relationship3796)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "isA"
                    #action end



                elif alt25 == 17:
                    # BELScript_Python_v1.g:259:9: rv= 'subProcessOf'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 138, self.FOLLOW_138_in_relationship3833)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "subProcessOf"
                    #action end



                elif alt25 == 18:
                    # BELScript_Python_v1.g:260:9: rv= 'rateLimitingStepOf'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 129, self.FOLLOW_129_in_relationship3861)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "rateLimitingStepOf"
                    #action end



                elif alt25 == 19:
                    # BELScript_Python_v1.g:261:9: rv= 'biomarkerFor'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 77, self.FOLLOW_77_in_relationship3883)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "biomarkerFor"
                    #action end



                elif alt25 == 20:
                    # BELScript_Python_v1.g:262:9: rv= 'prognosticBiomarkerFor'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 125, self.FOLLOW_125_in_relationship3911)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "prognosticBiomarkerFor"
                    #action end



                elif alt25 == 21:
                    # BELScript_Python_v1.g:263:9: rv= 'orthologous'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 114, self.FOLLOW_114_in_relationship3929)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "orthologous"
                    #action end



                elif alt25 == 22:
                    # BELScript_Python_v1.g:264:9: rv= 'analogous'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 74, self.FOLLOW_74_in_relationship3958)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "analogous"
                    #action end



                elif alt25 == 23:
                    # BELScript_Python_v1.g:265:9: rv= 'association'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 75, self.FOLLOW_75_in_relationship3989)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "association"
                    #action end



                elif alt25 == 24:
                    # BELScript_Python_v1.g:266:9: rv= '--'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 64, self.FOLLOW_64_in_relationship4018)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "association"
                    #action end



                elif alt25 == 25:
                    # BELScript_Python_v1.g:267:9: rv= 'hasMembers'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 104, self.FOLLOW_104_in_relationship4056)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "hasMembers"
                    #action end



                elif alt25 == 26:
                    # BELScript_Python_v1.g:268:9: rv= 'hasComponents'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 102, self.FOLLOW_102_in_relationship4086)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "hasComponents"
                    #action end



                elif alt25 == 27:
                    # BELScript_Python_v1.g:269:9: rv= 'hasMember'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 103, self.FOLLOW_103_in_relationship4113)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "hasMember"
                    #action end



                elif alt25 == 28:
                    # BELScript_Python_v1.g:270:9: rv= 'hasComponent'
                    pass
                    root_0 = self._adaptor.nil()


                    rv = self.match(self.input, 101, self.FOLLOW_101_in_relationship4144)
                    rv_tree = self._adaptor.createWithPayload(rv)
                    self._adaptor.addChild(root_0, rv_tree)



                    #action start
                    retval.r =  "hasComponent"
                    #action end



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "relationship"


    class eq_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(BELScript_Python_v1Parser.eq_clause_return, self).__init__()

            self.tree = None





    # $ANTLR start "eq_clause"
    # BELScript_Python_v1.g:273:1: eq_clause : ( WS )* EQ ( WS )* ;
    def eq_clause(self, ):
        retval = self.eq_clause_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WS92 = None
        EQ93 = None
        WS94 = None

        WS92_tree = None
        EQ93_tree = None
        WS94_tree = None

        try:
            try:
                # BELScript_Python_v1.g:274:5: ( ( WS )* EQ ( WS )* )
                # BELScript_Python_v1.g:274:9: ( WS )* EQ ( WS )*
                pass
                root_0 = self._adaptor.nil()


                # BELScript_Python_v1.g:274:9: ( WS )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == WS) :
                        alt26 = 1


                    if alt26 == 1:
                        # BELScript_Python_v1.g:274:9: WS
                        pass
                        WS92 = self.match(self.input, WS, self.FOLLOW_WS_in_eq_clause4179)
                        WS92_tree = self._adaptor.createWithPayload(WS92)
                        self._adaptor.addChild(root_0, WS92_tree)




                    else:
                        break #loop26


                EQ93 = self.match(self.input, EQ, self.FOLLOW_EQ_in_eq_clause4182)
                EQ93_tree = self._adaptor.createWithPayload(EQ93)
                self._adaptor.addChild(root_0, EQ93_tree)



                # BELScript_Python_v1.g:274:16: ( WS )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == WS) :
                        alt27 = 1


                    if alt27 == 1:
                        # BELScript_Python_v1.g:274:16: WS
                        pass
                        WS94 = self.match(self.input, WS, self.FOLLOW_WS_in_eq_clause4184)
                        WS94_tree = self._adaptor.createWithPayload(WS94)
                        self._adaptor.addChild(root_0, WS94_tree)




                    else:
                        break #loop27




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "eq_clause"



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\34\1\27\1\40\1\26\4\uffff\1\40\4\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\u0096\2\77\1\57\4\uffff\1\77\4\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\4\uffff\1\10\1\1\1\2\1\3\1\uffff\1\4\1\5\1\6\1\7"
        )

    DFA2_special = DFA.unpack(
        u"\15\uffff"
        )


    DFA2_transition = [
        DFA.unpack(u"\1\1\11\uffff\1\2\1\uffff\1\3\36\uffff\3\4\2\uffff\1"
        u"\4\1\uffff\3\4\1\uffff\10\4\1\uffff\2\4\2\uffff\6\4\6\uffff\6\4"
        u"\2\uffff\10\4\1\uffff\1\4\1\uffff\3\4\1\uffff\10\4\1\uffff\4\4"
        u"\1\uffff\1\4\1\uffff\5\4"),
        DFA.unpack(u"\1\6\6\uffff\1\5\5\uffff\1\5\32\uffff\1\6"),
        DFA.unpack(u"\1\11\6\uffff\1\12\7\uffff\1\7\17\uffff\1\10"),
        DFA.unpack(u"\1\14\20\uffff\1\13\7\uffff\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\6\uffff\1\12\27\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    class DFA2(DFA):
        pass


    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\46\2\40\2\31\2\23\2\57\3\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\46\10\77\3\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\11\uffff\1\1\1\2\1\3"
        )

    DFA5_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA5_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\36\uffff\1\2"),
        DFA.unpack(u"\1\3\36\uffff\1\2"),
        DFA.unpack(u"\3\5\1\uffff\1\5\1\uffff\1\5\1\uffff\1\5\1\uffff\1"
        u"\5\6\uffff\1\5\24\uffff\1\4"),
        DFA.unpack(u"\3\5\1\uffff\1\5\1\uffff\1\5\1\uffff\1\5\1\uffff\1"
        u"\5\6\uffff\1\5\24\uffff\1\4"),
        DFA.unpack(u"\1\7\53\uffff\1\6"),
        DFA.unpack(u"\1\7\53\uffff\1\6"),
        DFA.unpack(u"\1\13\3\uffff\1\11\12\uffff\1\12\1\10"),
        DFA.unpack(u"\1\13\3\uffff\1\11\12\uffff\1\12\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\46\2\47\2\23\2\57\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\46\6\77\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\7\uffff\1\1\1\2"
        )

    DFA7_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA7_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\27\uffff\1\2"),
        DFA.unpack(u"\1\3\27\uffff\1\2"),
        DFA.unpack(u"\1\5\53\uffff\1\4"),
        DFA.unpack(u"\1\5\53\uffff\1\4"),
        DFA.unpack(u"\1\10\3\uffff\1\7\13\uffff\1\6"),
        DFA.unpack(u"\1\10\3\uffff\1\7\13\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\46\1\57\2\23\2\57\3\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\46\1\57\4\77\3\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\6\uffff\1\1\1\2\1\3"
        )

    DFA8_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\4\53\uffff\1\3"),
        DFA.unpack(u"\1\4\53\uffff\1\3"),
        DFA.unpack(u"\1\10\3\uffff\1\6\12\uffff\1\7\1\5"),
        DFA.unpack(u"\1\10\3\uffff\1\6\12\uffff\1\7\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\34\2\27\2\57\1\30\1\42\3\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\34\4\77\1\30\1\51\3\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\7\uffff\1\1\1\2\1\3"
        )

    DFA13_special = DFA.unpack(
        u"\12\uffff"
        )


    DFA13_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\47\uffff\1\2"),
        DFA.unpack(u"\1\3\47\uffff\1\2"),
        DFA.unpack(u"\1\5\17\uffff\1\4"),
        DFA.unpack(u"\1\5\17\uffff\1\4"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\7\2\uffff\1\11\3\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #13

    class DFA13(DFA):
        pass




    FOLLOW_NEWLINE_in_document327 = frozenset([18, 28, 38, 40, 45, 71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_DOCUMENT_COMMENT_in_document331 = frozenset([18, 28, 38, 40, 45, 71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_record_in_document335 = frozenset([18, 28, 38, 40, 45, 71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_EOF_in_document339 = frozenset([1])
    FOLLOW_define_namespace_in_record375 = frozenset([1])
    FOLLOW_define_annotation_in_record385 = frozenset([1])
    FOLLOW_set_annotation_in_record395 = frozenset([1])
    FOLLOW_set_document_in_record405 = frozenset([1])
    FOLLOW_set_statement_group_in_record415 = frozenset([1])
    FOLLOW_unset_statement_group_in_record425 = frozenset([1])
    FOLLOW_unset_in_record435 = frozenset([1])
    FOLLOW_statement_in_record445 = frozenset([1])
    FOLLOW_KWRD_SET_in_set_doc_expr464 = frozenset([32, 63])
    FOLLOW_WS_in_set_doc_expr466 = frozenset([32, 63])
    FOLLOW_KWRD_DOCUMENT_in_set_doc_expr469 = frozenset([1, 63])
    FOLLOW_WS_in_set_doc_expr471 = frozenset([1, 63])
    FOLLOW_set_doc_expr_in_set_document491 = frozenset([25, 26, 27, 29, 31, 33, 35, 42])
    FOLLOW_document_property_in_set_document493 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_document495 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_set_document499 = frozenset([1])
    FOLLOW_set_doc_expr_in_set_document528 = frozenset([25, 26, 27, 29, 31, 33, 35, 42])
    FOLLOW_document_property_in_set_document530 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_document532 = frozenset([62])
    FOLLOW_VALUE_LIST_in_set_document536 = frozenset([1])
    FOLLOW_set_doc_expr_in_set_document565 = frozenset([25, 26, 27, 29, 31, 33, 35, 42])
    FOLLOW_document_property_in_set_document567 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_document569 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_set_document573 = frozenset([1])
    FOLLOW_KWRD_SET_in_set_sg_expr611 = frozenset([39, 63])
    FOLLOW_WS_in_set_sg_expr613 = frozenset([39, 63])
    FOLLOW_KWRD_STMT_GROUP_in_set_sg_expr616 = frozenset([1])
    FOLLOW_set_sg_expr_in_set_statement_group635 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_statement_group637 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_set_statement_group641 = frozenset([1])
    FOLLOW_set_sg_expr_in_set_statement_group660 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_statement_group662 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_set_statement_group666 = frozenset([1])
    FOLLOW_KWRD_SET_in_set_annotation694 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_set_annotation696 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_annotation698 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_set_annotation702 = frozenset([1])
    FOLLOW_KWRD_SET_in_set_annotation731 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_set_annotation733 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_annotation735 = frozenset([62])
    FOLLOW_VALUE_LIST_in_set_annotation739 = frozenset([1])
    FOLLOW_KWRD_SET_in_set_annotation768 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_set_annotation770 = frozenset([19, 63])
    FOLLOW_eq_clause_in_set_annotation772 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_set_annotation776 = frozenset([1])
    FOLLOW_KWRD_UNSET_in_unset_statement_group814 = frozenset([39])
    FOLLOW_KWRD_STMT_GROUP_in_unset_statement_group816 = frozenset([1])
    FOLLOW_KWRD_UNSET_in_unset841 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_unset845 = frozenset([1])
    FOLLOW_KWRD_UNSET_in_unset864 = frozenset([22])
    FOLLOW_IDENT_LIST_in_unset868 = frozenset([1])
    FOLLOW_KWRD_DEFINE_in_define_namespace896 = frozenset([30])
    FOLLOW_KWRD_DFLT_in_define_namespace898 = frozenset([36])
    FOLLOW_KWRD_NS_in_define_namespace900 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_define_namespace902 = frozenset([24])
    FOLLOW_KWRD_AS_in_define_namespace904 = frozenset([41])
    FOLLOW_KWRD_URL_in_define_namespace906 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_define_namespace908 = frozenset([1])
    FOLLOW_KWRD_DEFINE_in_define_namespace936 = frozenset([36])
    FOLLOW_KWRD_NS_in_define_namespace938 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_define_namespace940 = frozenset([24])
    FOLLOW_KWRD_AS_in_define_namespace942 = frozenset([41])
    FOLLOW_KWRD_URL_in_define_namespace944 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_define_namespace946 = frozenset([1])
    FOLLOW_KWRD_DEFINE_in_define_anno_expr983 = frozenset([23, 63])
    FOLLOW_WS_in_define_anno_expr985 = frozenset([23, 63])
    FOLLOW_KWRD_ANNO_in_define_anno_expr988 = frozenset([1, 63])
    FOLLOW_WS_in_define_anno_expr990 = frozenset([1, 63])
    FOLLOW_define_anno_expr_in_define_annotation1010 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_define_annotation1012 = frozenset([24])
    FOLLOW_KWRD_AS_in_define_annotation1014 = frozenset([34])
    FOLLOW_KWRD_LIST_in_define_annotation1016 = frozenset([62])
    FOLLOW_VALUE_LIST_in_define_annotation1020 = frozenset([1])
    FOLLOW_define_anno_expr_in_define_annotation1049 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_define_annotation1051 = frozenset([24])
    FOLLOW_KWRD_AS_in_define_annotation1053 = frozenset([41])
    FOLLOW_KWRD_URL_in_define_annotation1055 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_define_annotation1059 = frozenset([1])
    FOLLOW_define_anno_expr_in_define_annotation1088 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_define_annotation1090 = frozenset([24])
    FOLLOW_KWRD_AS_in_define_annotation1092 = frozenset([37])
    FOLLOW_KWRD_PATTERN_in_define_annotation1094 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_define_annotation1098 = frozenset([1])
    FOLLOW_COMMA_in_argument1225 = frozenset([71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_term_in_argument1228 = frozenset([1])
    FOLLOW_COMMA_in_argument1242 = frozenset([47, 51])
    FOLLOW_param_in_argument1245 = frozenset([1])
    FOLLOW_function_in_term1268 = frozenset([44])
    FOLLOW_LP_in_term1270 = frozenset([11, 47, 51, 52, 71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_argument_in_term1273 = frozenset([11, 47, 51, 52, 71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_RP_in_term1277 = frozenset([1])
    FOLLOW_term_in_statement1319 = frozenset([1, 55, 64, 65, 66, 67, 68, 69, 70, 74, 75, 77, 81, 90, 93, 94, 101, 102, 103, 104, 105, 106, 113, 114, 123, 125, 129, 138, 143, 145])
    FOLLOW_relationship_in_statement1324 = frozenset([44, 71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_LP_in_statement1327 = frozenset([71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_term_in_statement1331 = frozenset([64, 65, 66, 67, 68, 69, 70, 74, 75, 77, 81, 90, 93, 94, 101, 102, 103, 104, 105, 106, 113, 114, 123, 125, 129, 138, 143, 145])
    FOLLOW_relationship_in_statement1335 = frozenset([71, 72, 73, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 95, 96, 97, 98, 99, 100, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 144, 146, 147, 148, 149, 150])
    FOLLOW_term_in_statement1339 = frozenset([52])
    FOLLOW_RP_in_statement1341 = frozenset([1, 55])
    FOLLOW_term_in_statement1347 = frozenset([1, 55])
    FOLLOW_STATEMENT_COMMENT_in_statement1354 = frozenset([1])
    FOLLOW_OBJECT_IDENT_in_ns_prefix1415 = frozenset([10])
    FOLLOW_COLON_in_ns_prefix1417 = frozenset([1])
    FOLLOW_ns_prefix_in_param1437 = frozenset([47])
    FOLLOW_OBJECT_IDENT_in_param1440 = frozenset([1])
    FOLLOW_ns_prefix_in_param1461 = frozenset([51])
    FOLLOW_QUOTED_VALUE_in_param1464 = frozenset([1])
    FOLLOW_126_in_function1500 = frozenset([1])
    FOLLOW_115_in_function1524 = frozenset([1])
    FOLLOW_134_in_function1563 = frozenset([1])
    FOLLOW_128_in_function1591 = frozenset([1])
    FOLLOW_72_in_function1630 = frozenset([1])
    FOLLOW_71_in_function1661 = frozenset([1])
    FOLLOW_111_in_function1700 = frozenset([1])
    FOLLOW_110_in_function1723 = frozenset([1])
    FOLLOW_98_in_function1762 = frozenset([1])
    FOLLOW_97_in_function1789 = frozenset([1])
    FOLLOW_76_in_function1828 = frozenset([1])
    FOLLOW_78_in_function1851 = frozenset([1])
    FOLLOW_117_in_function1889 = frozenset([1])
    FOLLOW_116_in_function1920 = frozenset([1])
    FOLLOW_87_in_function1956 = frozenset([1])
    FOLLOW_86_in_function1980 = frozenset([1])
    FOLLOW_146_in_function2013 = frozenset([1])
    FOLLOW_141_in_function2040 = frozenset([1])
    FOLLOW_82_in_function2076 = frozenset([1])
    FOLLOW_136_in_function2103 = frozenset([1])
    FOLLOW_83_in_function2140 = frozenset([1])
    FOLLOW_140_in_function2159 = frozenset([1])
    FOLLOW_131_in_function2195 = frozenset([1])
    FOLLOW_135_in_function2227 = frozenset([1])
    FOLLOW_89_in_function2264 = frozenset([1])
    FOLLOW_88_in_function2286 = frozenset([1])
    FOLLOW_96_in_function2317 = frozenset([1])
    FOLLOW_95_in_function2351 = frozenset([1])
    FOLLOW_92_in_function2388 = frozenset([1])
    FOLLOW_91_in_function2417 = frozenset([1])
    FOLLOW_112_in_function2454 = frozenset([1])
    FOLLOW_73_in_function2477 = frozenset([1])
    FOLLOW_80_in_function2514 = frozenset([1])
    FOLLOW_79_in_function2537 = frozenset([1])
    FOLLOW_108_in_function2574 = frozenset([1])
    FOLLOW_107_in_function2600 = frozenset([1])
    FOLLOW_121_in_function2637 = frozenset([1])
    FOLLOW_120_in_function2658 = frozenset([1])
    FOLLOW_119_in_function2694 = frozenset([1])
    FOLLOW_118_in_function2717 = frozenset([1])
    FOLLOW_133_in_function2754 = frozenset([1])
    FOLLOW_132_in_function2774 = frozenset([1])
    FOLLOW_144_in_function2810 = frozenset([1])
    FOLLOW_150_in_function2827 = frozenset([1])
    FOLLOW_147_in_function2860 = frozenset([1])
    FOLLOW_142_in_function2883 = frozenset([1])
    FOLLOW_100_in_function2918 = frozenset([1])
    FOLLOW_99_in_function2942 = frozenset([1])
    FOLLOW_85_in_function2979 = frozenset([1])
    FOLLOW_84_in_function3002 = frozenset([1])
    FOLLOW_127_in_function3038 = frozenset([1])
    FOLLOW_122_in_function3059 = frozenset([1])
    FOLLOW_139_in_function3095 = frozenset([1])
    FOLLOW_137_in_function3123 = frozenset([1])
    FOLLOW_149_in_function3160 = frozenset([1])
    FOLLOW_148_in_function3190 = frozenset([1])
    FOLLOW_130_in_function3225 = frozenset([1])
    FOLLOW_124_in_function3256 = frozenset([1])
    FOLLOW_109_in_function3288 = frozenset([1])
    FOLLOW_105_in_relationship3337 = frozenset([1])
    FOLLOW_65_in_relationship3368 = frozenset([1])
    FOLLOW_90_in_relationship3406 = frozenset([1])
    FOLLOW_66_in_relationship3437 = frozenset([1])
    FOLLOW_94_in_relationship3475 = frozenset([1])
    FOLLOW_68_in_relationship3498 = frozenset([1])
    FOLLOW_93_in_relationship3536 = frozenset([1])
    FOLLOW_69_in_relationship3559 = frozenset([1])
    FOLLOW_81_in_relationship3597 = frozenset([1])
    FOLLOW_123_in_relationship3623 = frozenset([1])
    FOLLOW_113_in_relationship3644 = frozenset([1])
    FOLLOW_145_in_relationship3665 = frozenset([1])
    FOLLOW_70_in_relationship3693 = frozenset([1])
    FOLLOW_143_in_relationship3731 = frozenset([1])
    FOLLOW_67_in_relationship3758 = frozenset([1])
    FOLLOW_106_in_relationship3796 = frozenset([1])
    FOLLOW_138_in_relationship3833 = frozenset([1])
    FOLLOW_129_in_relationship3861 = frozenset([1])
    FOLLOW_77_in_relationship3883 = frozenset([1])
    FOLLOW_125_in_relationship3911 = frozenset([1])
    FOLLOW_114_in_relationship3929 = frozenset([1])
    FOLLOW_74_in_relationship3958 = frozenset([1])
    FOLLOW_75_in_relationship3989 = frozenset([1])
    FOLLOW_64_in_relationship4018 = frozenset([1])
    FOLLOW_104_in_relationship4056 = frozenset([1])
    FOLLOW_102_in_relationship4086 = frozenset([1])
    FOLLOW_103_in_relationship4113 = frozenset([1])
    FOLLOW_101_in_relationship4144 = frozenset([1])
    FOLLOW_WS_in_eq_clause4179 = frozenset([19, 63])
    FOLLOW_EQ_in_eq_clause4182 = frozenset([1, 63])
    FOLLOW_WS_in_eq_clause4184 = frozenset([1, 63])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("BELScript_Python_v1Lexer", BELScript_Python_v1Parser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
