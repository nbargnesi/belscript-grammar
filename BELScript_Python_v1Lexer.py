# $ANTLR 3.4 BELScript_Python_v1.g 2012-08-13 14:39:17

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



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


class BELScript_Python_v1Lexer(Lexer):

    grammarFileName = "BELScript_Python_v1.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(BELScript_Python_v1Lexer, self).__init__(input, state)

        self.delegates = []

        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
            )






    # $ANTLR start "T__64"
    def mT__64(self, ):
        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:7:7: ( '--' )
            # BELScript_Python_v1.g:7:9: '--'
            pass 
            self.match("--")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):
        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:8:7: ( '->' )
            # BELScript_Python_v1.g:8:9: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):
        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:9:7: ( '-|' )
            # BELScript_Python_v1.g:9:9: '-|'
            pass 
            self.match("-|")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):
        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:10:7: ( ':>' )
            # BELScript_Python_v1.g:10:9: ':>'
            pass 
            self.match(":>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):
        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:11:7: ( '=>' )
            # BELScript_Python_v1.g:11:9: '=>'
            pass 
            self.match("=>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):
        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:12:7: ( '=|' )
            # BELScript_Python_v1.g:12:9: '=|'
            pass 
            self.match("=|")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):
        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:13:7: ( '>>' )
            # BELScript_Python_v1.g:13:9: '>>'
            pass 
            self.match(">>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):
        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:14:7: ( 'a' )
            # BELScript_Python_v1.g:14:9: 'a'
            pass 
            self.match(97)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):
        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:15:7: ( 'abundance' )
            # BELScript_Python_v1.g:15:9: 'abundance'
            pass 
            self.match("abundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):
        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:16:7: ( 'act' )
            # BELScript_Python_v1.g:16:9: 'act'
            pass 
            self.match("act")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):
        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:17:7: ( 'analogous' )
            # BELScript_Python_v1.g:17:9: 'analogous'
            pass 
            self.match("analogous")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):
        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:18:7: ( 'association' )
            # BELScript_Python_v1.g:18:9: 'association'
            pass 
            self.match("association")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):
        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:19:7: ( 'biologicalProcess' )
            # BELScript_Python_v1.g:19:9: 'biologicalProcess'
            pass 
            self.match("biologicalProcess")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):
        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:20:7: ( 'biomarkerFor' )
            # BELScript_Python_v1.g:20:9: 'biomarkerFor'
            pass 
            self.match("biomarkerFor")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):
        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:21:7: ( 'bp' )
            # BELScript_Python_v1.g:21:9: 'bp'
            pass 
            self.match("bp")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):
        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:22:7: ( 'cat' )
            # BELScript_Python_v1.g:22:9: 'cat'
            pass 
            self.match("cat")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__79"



    # $ANTLR start "T__80"
    def mT__80(self, ):
        try:
            _type = T__80
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:23:7: ( 'catalyticActivity' )
            # BELScript_Python_v1.g:23:9: 'catalyticActivity'
            pass 
            self.match("catalyticActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__80"



    # $ANTLR start "T__81"
    def mT__81(self, ):
        try:
            _type = T__81
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:24:7: ( 'causesNoChange' )
            # BELScript_Python_v1.g:24:9: 'causesNoChange'
            pass 
            self.match("causesNoChange")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__81"



    # $ANTLR start "T__82"
    def mT__82(self, ):
        try:
            _type = T__82
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:25:7: ( 'cellSecretion' )
            # BELScript_Python_v1.g:25:9: 'cellSecretion'
            pass 
            self.match("cellSecretion")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__82"



    # $ANTLR start "T__83"
    def mT__83(self, ):
        try:
            _type = T__83
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:26:7: ( 'cellSurfaceExpression' )
            # BELScript_Python_v1.g:26:9: 'cellSurfaceExpression'
            pass 
            self.match("cellSurfaceExpression")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__83"



    # $ANTLR start "T__84"
    def mT__84(self, ):
        try:
            _type = T__84
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:27:7: ( 'chap' )
            # BELScript_Python_v1.g:27:9: 'chap'
            pass 
            self.match("chap")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__84"



    # $ANTLR start "T__85"
    def mT__85(self, ):
        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:28:7: ( 'chaperoneActivity' )
            # BELScript_Python_v1.g:28:9: 'chaperoneActivity'
            pass 
            self.match("chaperoneActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):
        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:29:7: ( 'complex' )
            # BELScript_Python_v1.g:29:9: 'complex'
            pass 
            self.match("complex")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):
        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:30:7: ( 'complexAbundance' )
            # BELScript_Python_v1.g:30:9: 'complexAbundance'
            pass 
            self.match("complexAbundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):
        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:31:7: ( 'composite' )
            # BELScript_Python_v1.g:31:9: 'composite'
            pass 
            self.match("composite")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):
        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:32:7: ( 'compositeAbundance' )
            # BELScript_Python_v1.g:32:9: 'compositeAbundance'
            pass 
            self.match("compositeAbundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):
        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:33:7: ( 'decreases' )
            # BELScript_Python_v1.g:33:9: 'decreases'
            pass 
            self.match("decreases")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):
        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:34:7: ( 'deg' )
            # BELScript_Python_v1.g:34:9: 'deg'
            pass 
            self.match("deg")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__91"



    # $ANTLR start "T__92"
    def mT__92(self, ):
        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:35:7: ( 'degradation' )
            # BELScript_Python_v1.g:35:9: 'degradation'
            pass 
            self.match("degradation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):
        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:36:7: ( 'directlyDecreases' )
            # BELScript_Python_v1.g:36:9: 'directlyDecreases'
            pass 
            self.match("directlyDecreases")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):
        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:37:7: ( 'directlyIncreases' )
            # BELScript_Python_v1.g:37:9: 'directlyIncreases'
            pass 
            self.match("directlyIncreases")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):
        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:38:7: ( 'fus' )
            # BELScript_Python_v1.g:38:9: 'fus'
            pass 
            self.match("fus")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):
        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:39:7: ( 'fusion' )
            # BELScript_Python_v1.g:39:9: 'fusion'
            pass 
            self.match("fusion")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):
        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:40:7: ( 'g' )
            # BELScript_Python_v1.g:40:9: 'g'
            pass 
            self.match(103)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):
        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:41:7: ( 'geneAbundance' )
            # BELScript_Python_v1.g:41:9: 'geneAbundance'
            pass 
            self.match("geneAbundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):
        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:42:7: ( 'gtp' )
            # BELScript_Python_v1.g:42:9: 'gtp'
            pass 
            self.match("gtp")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):
        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:43:8: ( 'gtpBoundActivity' )
            # BELScript_Python_v1.g:43:10: 'gtpBoundActivity'
            pass 
            self.match("gtpBoundActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):
        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:44:8: ( 'hasComponent' )
            # BELScript_Python_v1.g:44:10: 'hasComponent'
            pass 
            self.match("hasComponent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):
        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:45:8: ( 'hasComponents' )
            # BELScript_Python_v1.g:45:10: 'hasComponents'
            pass 
            self.match("hasComponents")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):
        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:46:8: ( 'hasMember' )
            # BELScript_Python_v1.g:46:10: 'hasMember'
            pass 
            self.match("hasMember")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__103"



    # $ANTLR start "T__104"
    def mT__104(self, ):
        try:
            _type = T__104
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:47:8: ( 'hasMembers' )
            # BELScript_Python_v1.g:47:10: 'hasMembers'
            pass 
            self.match("hasMembers")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__104"



    # $ANTLR start "T__105"
    def mT__105(self, ):
        try:
            _type = T__105
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:48:8: ( 'increases' )
            # BELScript_Python_v1.g:48:10: 'increases'
            pass 
            self.match("increases")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__105"



    # $ANTLR start "T__106"
    def mT__106(self, ):
        try:
            _type = T__106
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:49:8: ( 'isA' )
            # BELScript_Python_v1.g:49:10: 'isA'
            pass 
            self.match("isA")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__106"



    # $ANTLR start "T__107"
    def mT__107(self, ):
        try:
            _type = T__107
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:50:8: ( 'kin' )
            # BELScript_Python_v1.g:50:10: 'kin'
            pass 
            self.match("kin")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__107"



    # $ANTLR start "T__108"
    def mT__108(self, ):
        try:
            _type = T__108
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:51:8: ( 'kinaseActivity' )
            # BELScript_Python_v1.g:51:10: 'kinaseActivity'
            pass 
            self.match("kinaseActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__108"



    # $ANTLR start "T__109"
    def mT__109(self, ):
        try:
            _type = T__109
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:52:8: ( 'list' )
            # BELScript_Python_v1.g:52:10: 'list'
            pass 
            self.match("list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__109"



    # $ANTLR start "T__110"
    def mT__110(self, ):
        try:
            _type = T__110
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:53:8: ( 'm' )
            # BELScript_Python_v1.g:53:10: 'm'
            pass 
            self.match(109)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__110"



    # $ANTLR start "T__111"
    def mT__111(self, ):
        try:
            _type = T__111
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:54:8: ( 'microRNAAbundance' )
            # BELScript_Python_v1.g:54:10: 'microRNAAbundance'
            pass 
            self.match("microRNAAbundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__111"



    # $ANTLR start "T__112"
    def mT__112(self, ):
        try:
            _type = T__112
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:55:8: ( 'molecularActivity' )
            # BELScript_Python_v1.g:55:10: 'molecularActivity'
            pass 
            self.match("molecularActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__112"



    # $ANTLR start "T__113"
    def mT__113(self, ):
        try:
            _type = T__113
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:56:8: ( 'negativeCorrelation' )
            # BELScript_Python_v1.g:56:10: 'negativeCorrelation'
            pass 
            self.match("negativeCorrelation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__113"



    # $ANTLR start "T__114"
    def mT__114(self, ):
        try:
            _type = T__114
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:57:8: ( 'orthologous' )
            # BELScript_Python_v1.g:57:10: 'orthologous'
            pass 
            self.match("orthologous")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__114"



    # $ANTLR start "T__115"
    def mT__115(self, ):
        try:
            _type = T__115
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:58:8: ( 'p' )
            # BELScript_Python_v1.g:58:10: 'p'
            pass 
            self.match(112)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__115"



    # $ANTLR start "T__116"
    def mT__116(self, ):
        try:
            _type = T__116
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:59:8: ( 'path' )
            # BELScript_Python_v1.g:59:10: 'path'
            pass 
            self.match("path")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__116"



    # $ANTLR start "T__117"
    def mT__117(self, ):
        try:
            _type = T__117
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:60:8: ( 'pathology' )
            # BELScript_Python_v1.g:60:10: 'pathology'
            pass 
            self.match("pathology")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__117"



    # $ANTLR start "T__118"
    def mT__118(self, ):
        try:
            _type = T__118
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:61:8: ( 'pep' )
            # BELScript_Python_v1.g:61:10: 'pep'
            pass 
            self.match("pep")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__118"



    # $ANTLR start "T__119"
    def mT__119(self, ):
        try:
            _type = T__119
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:62:8: ( 'peptidaseActivity' )
            # BELScript_Python_v1.g:62:10: 'peptidaseActivity'
            pass 
            self.match("peptidaseActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__119"



    # $ANTLR start "T__120"
    def mT__120(self, ):
        try:
            _type = T__120
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:63:8: ( 'phos' )
            # BELScript_Python_v1.g:63:10: 'phos'
            pass 
            self.match("phos")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__120"



    # $ANTLR start "T__121"
    def mT__121(self, ):
        try:
            _type = T__121
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:64:8: ( 'phosphataseActivity' )
            # BELScript_Python_v1.g:64:10: 'phosphataseActivity'
            pass 
            self.match("phosphataseActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__121"



    # $ANTLR start "T__122"
    def mT__122(self, ):
        try:
            _type = T__122
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:65:8: ( 'pmod' )
            # BELScript_Python_v1.g:65:10: 'pmod'
            pass 
            self.match("pmod")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__122"



    # $ANTLR start "T__123"
    def mT__123(self, ):
        try:
            _type = T__123
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:66:8: ( 'positiveCorrelation' )
            # BELScript_Python_v1.g:66:10: 'positiveCorrelation'
            pass 
            self.match("positiveCorrelation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__123"



    # $ANTLR start "T__124"
    def mT__124(self, ):
        try:
            _type = T__124
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:67:8: ( 'products' )
            # BELScript_Python_v1.g:67:10: 'products'
            pass 
            self.match("products")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__124"



    # $ANTLR start "T__125"
    def mT__125(self, ):
        try:
            _type = T__125
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:68:8: ( 'prognosticBiomarkerFor' )
            # BELScript_Python_v1.g:68:10: 'prognosticBiomarkerFor'
            pass 
            self.match("prognosticBiomarkerFor")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__125"



    # $ANTLR start "T__126"
    def mT__126(self, ):
        try:
            _type = T__126
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:69:8: ( 'proteinAbundance' )
            # BELScript_Python_v1.g:69:10: 'proteinAbundance'
            pass 
            self.match("proteinAbundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__126"



    # $ANTLR start "T__127"
    def mT__127(self, ):
        try:
            _type = T__127
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:70:8: ( 'proteinModification' )
            # BELScript_Python_v1.g:70:10: 'proteinModification'
            pass 
            self.match("proteinModification")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__127"



    # $ANTLR start "T__128"
    def mT__128(self, ):
        try:
            _type = T__128
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:71:8: ( 'r' )
            # BELScript_Python_v1.g:71:10: 'r'
            pass 
            self.match(114)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__128"



    # $ANTLR start "T__129"
    def mT__129(self, ):
        try:
            _type = T__129
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:72:8: ( 'rateLimitingStepOf' )
            # BELScript_Python_v1.g:72:10: 'rateLimitingStepOf'
            pass 
            self.match("rateLimitingStepOf")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__129"



    # $ANTLR start "T__130"
    def mT__130(self, ):
        try:
            _type = T__130
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:73:8: ( 'reactants' )
            # BELScript_Python_v1.g:73:10: 'reactants'
            pass 
            self.match("reactants")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__130"



    # $ANTLR start "T__131"
    def mT__131(self, ):
        try:
            _type = T__131
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:74:8: ( 'reaction' )
            # BELScript_Python_v1.g:74:10: 'reaction'
            pass 
            self.match("reaction")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__131"



    # $ANTLR start "T__132"
    def mT__132(self, ):
        try:
            _type = T__132
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:75:8: ( 'ribo' )
            # BELScript_Python_v1.g:75:10: 'ribo'
            pass 
            self.match("ribo")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__132"



    # $ANTLR start "T__133"
    def mT__133(self, ):
        try:
            _type = T__133
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:76:8: ( 'ribosylationActivity' )
            # BELScript_Python_v1.g:76:10: 'ribosylationActivity'
            pass 
            self.match("ribosylationActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__133"



    # $ANTLR start "T__134"
    def mT__134(self, ):
        try:
            _type = T__134
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:77:8: ( 'rnaAbundance' )
            # BELScript_Python_v1.g:77:10: 'rnaAbundance'
            pass 
            self.match("rnaAbundance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__134"



    # $ANTLR start "T__135"
    def mT__135(self, ):
        try:
            _type = T__135
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:78:8: ( 'rxn' )
            # BELScript_Python_v1.g:78:10: 'rxn'
            pass 
            self.match("rxn")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__135"



    # $ANTLR start "T__136"
    def mT__136(self, ):
        try:
            _type = T__136
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:79:8: ( 'sec' )
            # BELScript_Python_v1.g:79:10: 'sec'
            pass 
            self.match("sec")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__136"



    # $ANTLR start "T__137"
    def mT__137(self, ):
        try:
            _type = T__137
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:80:8: ( 'sub' )
            # BELScript_Python_v1.g:80:10: 'sub'
            pass 
            self.match("sub")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__137"



    # $ANTLR start "T__138"
    def mT__138(self, ):
        try:
            _type = T__138
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:81:8: ( 'subProcessOf' )
            # BELScript_Python_v1.g:81:10: 'subProcessOf'
            pass 
            self.match("subProcessOf")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__138"



    # $ANTLR start "T__139"
    def mT__139(self, ):
        try:
            _type = T__139
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:82:8: ( 'substitution' )
            # BELScript_Python_v1.g:82:10: 'substitution'
            pass 
            self.match("substitution")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__139"



    # $ANTLR start "T__140"
    def mT__140(self, ):
        try:
            _type = T__140
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:83:8: ( 'surf' )
            # BELScript_Python_v1.g:83:10: 'surf'
            pass 
            self.match("surf")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__140"



    # $ANTLR start "T__141"
    def mT__141(self, ):
        try:
            _type = T__141
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:84:8: ( 'tloc' )
            # BELScript_Python_v1.g:84:10: 'tloc'
            pass 
            self.match("tloc")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__141"



    # $ANTLR start "T__142"
    def mT__142(self, ):
        try:
            _type = T__142
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:85:8: ( 'tport' )
            # BELScript_Python_v1.g:85:10: 'tport'
            pass 
            self.match("tport")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__142"



    # $ANTLR start "T__143"
    def mT__143(self, ):
        try:
            _type = T__143
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:86:8: ( 'transcribedTo' )
            # BELScript_Python_v1.g:86:10: 'transcribedTo'
            pass 
            self.match("transcribedTo")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__143"



    # $ANTLR start "T__144"
    def mT__144(self, ):
        try:
            _type = T__144
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:87:8: ( 'transcriptionalActivity' )
            # BELScript_Python_v1.g:87:10: 'transcriptionalActivity'
            pass 
            self.match("transcriptionalActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__144"



    # $ANTLR start "T__145"
    def mT__145(self, ):
        try:
            _type = T__145
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:88:8: ( 'translatedTo' )
            # BELScript_Python_v1.g:88:10: 'translatedTo'
            pass 
            self.match("translatedTo")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__145"



    # $ANTLR start "T__146"
    def mT__146(self, ):
        try:
            _type = T__146
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:89:8: ( 'translocation' )
            # BELScript_Python_v1.g:89:10: 'translocation'
            pass 
            self.match("translocation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__146"



    # $ANTLR start "T__147"
    def mT__147(self, ):
        try:
            _type = T__147
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:90:8: ( 'transportActivity' )
            # BELScript_Python_v1.g:90:10: 'transportActivity'
            pass 
            self.match("transportActivity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__147"



    # $ANTLR start "T__148"
    def mT__148(self, ):
        try:
            _type = T__148
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:91:8: ( 'trunc' )
            # BELScript_Python_v1.g:91:10: 'trunc'
            pass 
            self.match("trunc")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__148"



    # $ANTLR start "T__149"
    def mT__149(self, ):
        try:
            _type = T__149
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:92:8: ( 'truncation' )
            # BELScript_Python_v1.g:92:10: 'truncation'
            pass 
            self.match("truncation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__149"



    # $ANTLR start "T__150"
    def mT__150(self, ):
        try:
            _type = T__150
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:93:8: ( 'tscript' )
            # BELScript_Python_v1.g:93:10: 'tscript'
            pass 
            self.match("tscript")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__150"



    # $ANTLR start "DOCUMENT_COMMENT"
    def mDOCUMENT_COMMENT(self, ):
        try:
            _type = DOCUMENT_COMMENT
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:278:5: ( '#' (~ ( '\\n' | '\\r' ) )* )
            # BELScript_Python_v1.g:278:9: '#' (~ ( '\\n' | '\\r' ) )*
            pass 
            self.match(35)

            # BELScript_Python_v1.g:278:13: (~ ( '\\n' | '\\r' ) )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 12) or (14 <= LA1_0 <= 65535)) :
                    alt1 = 1


                if alt1 == 1:
                    # BELScript_Python_v1.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOCUMENT_COMMENT"



    # $ANTLR start "STATEMENT_COMMENT"
    def mSTATEMENT_COMMENT(self, ):
        try:
            _type = STATEMENT_COMMENT
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:282:5: ( '//' ( ( '\\\\\\n' ) | ( '\\\\\\r\\n' ) |~ ( '\\n' | '\\r' ) )* )
            # BELScript_Python_v1.g:282:9: '//' ( ( '\\\\\\n' ) | ( '\\\\\\r\\n' ) |~ ( '\\n' | '\\r' ) )*
            pass 
            self.match("//")


            # BELScript_Python_v1.g:282:14: ( ( '\\\\\\n' ) | ( '\\\\\\r\\n' ) |~ ( '\\n' | '\\r' ) )*
            while True: #loop2
                alt2 = 4
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 92) :
                    LA2 = self.input.LA(2)
                    if LA2 == 10:
                        alt2 = 1
                    elif LA2 == 13:
                        alt2 = 2
                    else:
                        alt2 = 3

                elif ((0 <= LA2_0 <= 9) or (11 <= LA2_0 <= 12) or (14 <= LA2_0 <= 91) or (93 <= LA2_0 <= 65535)) :
                    alt2 = 3


                if alt2 == 1:
                    # BELScript_Python_v1.g:282:15: ( '\\\\\\n' )
                    pass 
                    # BELScript_Python_v1.g:282:15: ( '\\\\\\n' )
                    # BELScript_Python_v1.g:282:16: '\\\\\\n'
                    pass 
                    self.match("\\\n")






                elif alt2 == 2:
                    # BELScript_Python_v1.g:282:26: ( '\\\\\\r\\n' )
                    pass 
                    # BELScript_Python_v1.g:282:26: ( '\\\\\\r\\n' )
                    # BELScript_Python_v1.g:282:27: '\\\\\\r\\n'
                    pass 
                    self.match("\\\r\n")






                elif alt2 == 3:
                    # BELScript_Python_v1.g:282:39: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATEMENT_COMMENT"



    # $ANTLR start "IDENT_LIST"
    def mIDENT_LIST(self, ):
        try:
            _type = IDENT_LIST
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:286:5: ( '{' OBJECT_IDENT ( COMMA OBJECT_IDENT )* '}' )
            # BELScript_Python_v1.g:286:9: '{' OBJECT_IDENT ( COMMA OBJECT_IDENT )* '}'
            pass 
            self.match(123)

            self.mOBJECT_IDENT()


            # BELScript_Python_v1.g:286:26: ( COMMA OBJECT_IDENT )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 44) :
                    alt3 = 1


                if alt3 == 1:
                    # BELScript_Python_v1.g:286:27: COMMA OBJECT_IDENT
                    pass 
                    self.mCOMMA()


                    self.mOBJECT_IDENT()



                else:
                    break #loop3


            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDENT_LIST"



    # $ANTLR start "VALUE_LIST"
    def mVALUE_LIST(self, ):
        try:
            _type = VALUE_LIST
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:290:5: ( '{' ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )? ( COMMA ( ' ' )* ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )? )* '}' )
            # BELScript_Python_v1.g:290:9: '{' ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )? ( COMMA ( ' ' )* ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )? )* '}'
            pass 
            self.match(123)

            # BELScript_Python_v1.g:290:13: ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )?
            alt4 = 4
            LA4 = self.input.LA(1)
            if LA4 == 48 or LA4 == 49 or LA4 == 50 or LA4 == 51 or LA4 == 52 or LA4 == 53 or LA4 == 54 or LA4 == 55 or LA4 == 56 or LA4 == 57 or LA4 == 65 or LA4 == 66 or LA4 == 67 or LA4 == 68 or LA4 == 69 or LA4 == 70 or LA4 == 71 or LA4 == 72 or LA4 == 73 or LA4 == 74 or LA4 == 75 or LA4 == 76 or LA4 == 77 or LA4 == 78 or LA4 == 79 or LA4 == 80 or LA4 == 81 or LA4 == 82 or LA4 == 83 or LA4 == 84 or LA4 == 85 or LA4 == 86 or LA4 == 87 or LA4 == 88 or LA4 == 89 or LA4 == 90 or LA4 == 95 or LA4 == 97 or LA4 == 98 or LA4 == 99 or LA4 == 100 or LA4 == 101 or LA4 == 102 or LA4 == 103 or LA4 == 104 or LA4 == 105 or LA4 == 106 or LA4 == 107 or LA4 == 108 or LA4 == 109 or LA4 == 110 or LA4 == 111 or LA4 == 112 or LA4 == 113 or LA4 == 114 or LA4 == 115 or LA4 == 116 or LA4 == 117 or LA4 == 118 or LA4 == 119 or LA4 == 120 or LA4 == 121 or LA4 == 122:
                alt4 = 1
            elif LA4 == 34:
                alt4 = 2
            elif LA4 == 123:
                alt4 = 3
            if alt4 == 1:
                # BELScript_Python_v1.g:290:14: OBJECT_IDENT
                pass 
                self.mOBJECT_IDENT()



            elif alt4 == 2:
                # BELScript_Python_v1.g:290:29: QUOTED_VALUE
                pass 
                self.mQUOTED_VALUE()



            elif alt4 == 3:
                # BELScript_Python_v1.g:290:44: VALUE_LIST
                pass 
                self.mVALUE_LIST()





            # BELScript_Python_v1.g:290:57: ( COMMA ( ' ' )* ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )? )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 44) :
                    alt7 = 1


                if alt7 == 1:
                    # BELScript_Python_v1.g:290:58: COMMA ( ' ' )* ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )?
                    pass 
                    self.mCOMMA()


                    # BELScript_Python_v1.g:290:64: ( ' ' )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == 32) :
                            alt5 = 1


                        if alt5 == 1:
                            # BELScript_Python_v1.g:290:65: ' '
                            pass 
                            self.match(32)


                        else:
                            break #loop5


                    # BELScript_Python_v1.g:290:71: ( OBJECT_IDENT | QUOTED_VALUE | VALUE_LIST )?
                    alt6 = 4
                    LA6 = self.input.LA(1)
                    if LA6 == 48 or LA6 == 49 or LA6 == 50 or LA6 == 51 or LA6 == 52 or LA6 == 53 or LA6 == 54 or LA6 == 55 or LA6 == 56 or LA6 == 57 or LA6 == 65 or LA6 == 66 or LA6 == 67 or LA6 == 68 or LA6 == 69 or LA6 == 70 or LA6 == 71 or LA6 == 72 or LA6 == 73 or LA6 == 74 or LA6 == 75 or LA6 == 76 or LA6 == 77 or LA6 == 78 or LA6 == 79 or LA6 == 80 or LA6 == 81 or LA6 == 82 or LA6 == 83 or LA6 == 84 or LA6 == 85 or LA6 == 86 or LA6 == 87 or LA6 == 88 or LA6 == 89 or LA6 == 90 or LA6 == 95 or LA6 == 97 or LA6 == 98 or LA6 == 99 or LA6 == 100 or LA6 == 101 or LA6 == 102 or LA6 == 103 or LA6 == 104 or LA6 == 105 or LA6 == 106 or LA6 == 107 or LA6 == 108 or LA6 == 109 or LA6 == 110 or LA6 == 111 or LA6 == 112 or LA6 == 113 or LA6 == 114 or LA6 == 115 or LA6 == 116 or LA6 == 117 or LA6 == 118 or LA6 == 119 or LA6 == 120 or LA6 == 121 or LA6 == 122:
                        alt6 = 1
                    elif LA6 == 34:
                        alt6 = 2
                    elif LA6 == 123:
                        alt6 = 3
                    if alt6 == 1:
                        # BELScript_Python_v1.g:290:72: OBJECT_IDENT
                        pass 
                        self.mOBJECT_IDENT()



                    elif alt6 == 2:
                        # BELScript_Python_v1.g:290:87: QUOTED_VALUE
                        pass 
                        self.mQUOTED_VALUE()



                    elif alt6 == 3:
                        # BELScript_Python_v1.g:290:102: VALUE_LIST
                        pass 
                        self.mVALUE_LIST()






                else:
                    break #loop7


            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VALUE_LIST"



    # $ANTLR start "QUOTED_VALUE"
    def mQUOTED_VALUE(self, ):
        try:
            _type = QUOTED_VALUE
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:294:5: ( '\"' ( ESCAPE_SEQUENCE | '\\\\\\n' | '\\\\\\r\\n' |~ ( '\\\\' | '\"' ) )* '\"' )
            # BELScript_Python_v1.g:294:9: '\"' ( ESCAPE_SEQUENCE | '\\\\\\n' | '\\\\\\r\\n' |~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)

            # BELScript_Python_v1.g:294:13: ( ESCAPE_SEQUENCE | '\\\\\\n' | '\\\\\\r\\n' |~ ( '\\\\' | '\"' ) )*
            while True: #loop8
                alt8 = 5
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 92) :
                    LA8 = self.input.LA(2)
                    if LA8 == 34 or LA8 == 39 or LA8 == 48 or LA8 == 49 or LA8 == 50 or LA8 == 51 or LA8 == 52 or LA8 == 53 or LA8 == 54 or LA8 == 55 or LA8 == 92 or LA8 == 98 or LA8 == 102 or LA8 == 110 or LA8 == 114 or LA8 == 116 or LA8 == 117:
                        alt8 = 1
                    elif LA8 == 10:
                        alt8 = 2
                    elif LA8 == 13:
                        alt8 = 3

                elif ((0 <= LA8_0 <= 33) or (35 <= LA8_0 <= 91) or (93 <= LA8_0 <= 65535)) :
                    alt8 = 4


                if alt8 == 1:
                    # BELScript_Python_v1.g:294:15: ESCAPE_SEQUENCE
                    pass 
                    self.mESCAPE_SEQUENCE()



                elif alt8 == 2:
                    # BELScript_Python_v1.g:294:33: '\\\\\\n'
                    pass 
                    self.match("\\\n")



                elif alt8 == 3:
                    # BELScript_Python_v1.g:294:42: '\\\\\\r\\n'
                    pass 
                    self.match("\\\r\n")



                elif alt8 == 4:
                    # BELScript_Python_v1.g:294:53: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop8


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QUOTED_VALUE"



    # $ANTLR start "LP"
    def mLP(self, ):
        try:
            _type = LP
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:297:3: ( '(' )
            # BELScript_Python_v1.g:297:5: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LP"



    # $ANTLR start "RP"
    def mRP(self, ):
        try:
            _type = RP
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:298:3: ( ')' )
            # BELScript_Python_v1.g:298:5: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RP"



    # $ANTLR start "EQ"
    def mEQ(self, ):
        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:299:3: ( '=' )
            # BELScript_Python_v1.g:299:5: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQ"



    # $ANTLR start "COLON"
    def mCOLON(self, ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:300:6: ( ':' )
            # BELScript_Python_v1.g:300:8: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:301:6: ( ',' )
            # BELScript_Python_v1.g:301:8: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:304:5: ( ( '\\u000d' )? '\\u000a' | '\\u000d' )
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 13) :
                LA10_1 = self.input.LA(2)

                if (LA10_1 == 10) :
                    alt10 = 1
                else:
                    alt10 = 2

            elif (LA10_0 == 10) :
                alt10 = 1
            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae


            if alt10 == 1:
                # BELScript_Python_v1.g:304:9: ( '\\u000d' )? '\\u000a'
                pass 
                # BELScript_Python_v1.g:304:9: ( '\\u000d' )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 13) :
                    alt9 = 1
                if alt9 == 1:
                    # BELScript_Python_v1.g:304:9: '\\u000d'
                    pass 
                    self.match(13)




                self.match(10)


            elif alt10 == 2:
                # BELScript_Python_v1.g:304:30: '\\u000d'
                pass 
                self.match(13)


            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:307:3: ( ( ' ' | '\\t' | '\\n' | '\\r' | '\\f' | '\\\\\\n' | '\\\\\\r\\n' )+ )
            # BELScript_Python_v1.g:307:5: ( ' ' | '\\t' | '\\n' | '\\r' | '\\f' | '\\\\\\n' | '\\\\\\r\\n' )+
            pass 
            # BELScript_Python_v1.g:307:5: ( ' ' | '\\t' | '\\n' | '\\r' | '\\f' | '\\\\\\n' | '\\\\\\r\\n' )+
            cnt11 = 0
            while True: #loop11
                alt11 = 8
                LA11 = self.input.LA(1)
                if LA11 == 32:
                    alt11 = 1
                elif LA11 == 9:
                    alt11 = 2
                elif LA11 == 10:
                    alt11 = 3
                elif LA11 == 13:
                    alt11 = 4
                elif LA11 == 12:
                    alt11 = 5
                elif LA11 == 92:
                    LA11_7 = self.input.LA(2)

                    if (LA11_7 == 10) :
                        alt11 = 6
                    elif (LA11_7 == 13) :
                        alt11 = 7



                if alt11 == 1:
                    # BELScript_Python_v1.g:307:6: ' '
                    pass 
                    self.match(32)


                elif alt11 == 2:
                    # BELScript_Python_v1.g:307:12: '\\t'
                    pass 
                    self.match(9)


                elif alt11 == 3:
                    # BELScript_Python_v1.g:307:19: '\\n'
                    pass 
                    self.match(10)


                elif alt11 == 4:
                    # BELScript_Python_v1.g:307:26: '\\r'
                    pass 
                    self.match(13)


                elif alt11 == 5:
                    # BELScript_Python_v1.g:307:32: '\\f'
                    pass 
                    self.match(12)


                elif alt11 == 6:
                    # BELScript_Python_v1.g:307:39: '\\\\\\n'
                    pass 
                    self.match("\\\n")



                elif alt11 == 7:
                    # BELScript_Python_v1.g:307:48: '\\\\\\r\\n'
                    pass 
                    self.match("\\\r\n")



                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1


            #action start
            skip() 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "KWRD_ANNO"
    def mKWRD_ANNO(self, ):
        try:
            _type = KWRD_ANNO
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:312:5: ( ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'N' | 'n' ) ( 'O' | 'o' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) )
            # BELScript_Python_v1.g:312:9: ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'N' | 'n' ) ( 'O' | 'o' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_ANNO"



    # $ANTLR start "KWRD_AS"
    def mKWRD_AS(self, ):
        try:
            _type = KWRD_AS
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:316:5: ( ( 'A' | 'a' ) ( 'S' | 's' ) )
            # BELScript_Python_v1.g:316:9: ( 'A' | 'a' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_AS"



    # $ANTLR start "KWRD_AUTHORS"
    def mKWRD_AUTHORS(self, ):
        try:
            _type = KWRD_AUTHORS
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:320:5: ( ( 'A' | 'a' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'H' | 'h' ) ( 'O' | 'o' ) ( 'R' | 'r' ) ( 'S' | 's' ) )
            # BELScript_Python_v1.g:320:9: ( 'A' | 'a' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'H' | 'h' ) ( 'O' | 'o' ) ( 'R' | 'r' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_AUTHORS"



    # $ANTLR start "KWRD_CONTACTINFO"
    def mKWRD_CONTACTINFO(self, ):
        try:
            _type = KWRD_CONTACTINFO
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:324:5: ( ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'C' | 'c' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'F' | 'f' ) ( 'O' | 'o' ) )
            # BELScript_Python_v1.g:324:9: ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'C' | 'c' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'F' | 'f' ) ( 'O' | 'o' )
            pass 
            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_CONTACTINFO"



    # $ANTLR start "KWRD_COPYRIGHT"
    def mKWRD_COPYRIGHT(self, ):
        try:
            _type = KWRD_COPYRIGHT
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:328:5: ( ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'P' | 'p' ) ( 'Y' | 'y' ) ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'G' | 'g' ) ( 'H' | 'h' ) ( 'T' | 't' ) )
            # BELScript_Python_v1.g:328:9: ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'P' | 'p' ) ( 'Y' | 'y' ) ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'G' | 'g' ) ( 'H' | 'h' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_COPYRIGHT"



    # $ANTLR start "KWRD_DFLT"
    def mKWRD_DFLT(self, ):
        try:
            _type = KWRD_DFLT
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:332:5: ( ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'U' | 'u' ) ( 'L' | 'l' ) ( 'T' | 't' ) )
            # BELScript_Python_v1.g:332:9: ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'U' | 'u' ) ( 'L' | 'l' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_DFLT"



    # $ANTLR start "KWRD_DEFINE"
    def mKWRD_DEFINE(self, ):
        try:
            _type = KWRD_DEFINE
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:336:5: ( ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'E' | 'e' ) )
            # BELScript_Python_v1.g:336:9: ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_DEFINE"



    # $ANTLR start "KWRD_DESC"
    def mKWRD_DESC(self, ):
        try:
            _type = KWRD_DESC
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:340:5: ( ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'C' | 'c' ) ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'P' | 'p' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) )
            # BELScript_Python_v1.g:340:9: ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'C' | 'c' ) ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'P' | 'p' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_DESC"



    # $ANTLR start "KWRD_DISCLAIMER"
    def mKWRD_DISCLAIMER(self, ):
        try:
            _type = KWRD_DISCLAIMER
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:344:5: ( ( 'D' | 'd' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'C' | 'c' ) ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'I' | 'i' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'R' | 'r' ) )
            # BELScript_Python_v1.g:344:9: ( 'D' | 'd' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'C' | 'c' ) ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'I' | 'i' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_DISCLAIMER"



    # $ANTLR start "KWRD_DOCUMENT"
    def mKWRD_DOCUMENT(self, ):
        try:
            _type = KWRD_DOCUMENT
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:348:5: ( ( 'D' | 'd' ) ( 'O' | 'o' ) ( 'C' | 'c' ) ( 'U' | 'u' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'N' | 'n' ) ( 'T' | 't' ) )
            # BELScript_Python_v1.g:348:9: ( 'D' | 'd' ) ( 'O' | 'o' ) ( 'C' | 'c' ) ( 'U' | 'u' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'N' | 'n' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_DOCUMENT"



    # $ANTLR start "KWRD_LICENSES"
    def mKWRD_LICENSES(self, ):
        try:
            _type = KWRD_LICENSES
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:352:5: ( ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'C' | 'c' ) ( 'E' | 'e' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'S' | 's' ) )
            # BELScript_Python_v1.g:352:9: ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'C' | 'c' ) ( 'E' | 'e' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_LICENSES"



    # $ANTLR start "KWRD_LIST"
    def mKWRD_LIST(self, ):
        try:
            _type = KWRD_LIST
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:356:5: ( ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) )
            # BELScript_Python_v1.g:356:9: ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_LIST"



    # $ANTLR start "KWRD_NAME"
    def mKWRD_NAME(self, ):
        try:
            _type = KWRD_NAME
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:360:5: ( ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) )
            # BELScript_Python_v1.g:360:9: ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_NAME"



    # $ANTLR start "KWRD_NS"
    def mKWRD_NS(self, ):
        try:
            _type = KWRD_NS
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:364:5: ( ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'P' | 'p' ) ( 'A' | 'a' ) ( 'C' | 'c' ) ( 'E' | 'e' ) )
            # BELScript_Python_v1.g:364:9: ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'P' | 'p' ) ( 'A' | 'a' ) ( 'C' | 'c' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_NS"



    # $ANTLR start "KWRD_PATTERN"
    def mKWRD_PATTERN(self, ):
        try:
            _type = KWRD_PATTERN
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:368:5: ( ( 'P' | 'p' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'N' | 'n' ) )
            # BELScript_Python_v1.g:368:9: ( 'P' | 'p' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_PATTERN"



    # $ANTLR start "KWRD_SET"
    def mKWRD_SET(self, ):
        try:
            _type = KWRD_SET
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:372:5: ( ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' ) )
            # BELScript_Python_v1.g:372:9: ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_SET"



    # $ANTLR start "KWRD_STMT_GROUP"
    def mKWRD_STMT_GROUP(self, ):
        try:
            _type = KWRD_STMT_GROUP
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:376:5: ( ( 'S' | 's' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'N' | 'n' ) ( 'T' | 't' ) ( '_' ) ( 'G' | 'g' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'P' | 'p' ) )
            # BELScript_Python_v1.g:376:9: ( 'S' | 's' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'N' | 'n' ) ( 'T' | 't' ) ( '_' ) ( 'G' | 'g' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'P' | 'p' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # BELScript_Python_v1.g:376:90: ( '_' )
            # BELScript_Python_v1.g:376:91: '_'
            pass 
            self.match(95)




            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_STMT_GROUP"



    # $ANTLR start "KWRD_UNSET"
    def mKWRD_UNSET(self, ):
        try:
            _type = KWRD_UNSET
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:380:5: ( ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' ) )
            # BELScript_Python_v1.g:380:9: ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_UNSET"



    # $ANTLR start "KWRD_URL"
    def mKWRD_URL(self, ):
        try:
            _type = KWRD_URL
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:384:5: ( ( 'U' | 'u' ) ( 'R' | 'r' ) ( 'L' | 'l' ) )
            # BELScript_Python_v1.g:384:9: ( 'U' | 'u' ) ( 'R' | 'r' ) ( 'L' | 'l' )
            pass 
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_URL"



    # $ANTLR start "KWRD_VERSION"
    def mKWRD_VERSION(self, ):
        try:
            _type = KWRD_VERSION
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:388:5: ( ( 'V' | 'v' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'S' | 's' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) )
            # BELScript_Python_v1.g:388:9: ( 'V' | 'v' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'S' | 's' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 86 or self.input.LA(1) == 118:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KWRD_VERSION"



    # $ANTLR start "OBJECT_IDENT"
    def mOBJECT_IDENT(self, ):
        try:
            _type = OBJECT_IDENT
            _channel = DEFAULT_CHANNEL

            # BELScript_Python_v1.g:392:5: ( ( '_' | LETTER | DIGIT )+ )
            # BELScript_Python_v1.g:392:9: ( '_' | LETTER | DIGIT )+
            pass 
            # BELScript_Python_v1.g:392:9: ( '_' | LETTER | DIGIT )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57) or (65 <= LA12_0 <= 90) or LA12_0 == 95 or (97 <= LA12_0 <= 122)) :
                    alt12 = 1


                if alt12 == 1:
                    # BELScript_Python_v1.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OBJECT_IDENT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):
        try:
            # BELScript_Python_v1.g:400:5: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # BELScript_Python_v1.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):
        try:
            # BELScript_Python_v1.g:404:5: ( '0' .. '9' )
            # BELScript_Python_v1.g:
            pass 
            if (48 <= self.input.LA(1) <= 57):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "ESCAPE_SEQUENCE"
    def mESCAPE_SEQUENCE(self, ):
        try:
            # BELScript_Python_v1.g:408:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESCAPE | OCTAL_ESCAPE )
            alt13 = 3
            LA13_0 = self.input.LA(1)

            if (LA13_0 == 92) :
                LA13 = self.input.LA(2)
                if LA13 == 34 or LA13 == 39 or LA13 == 92 or LA13 == 98 or LA13 == 102 or LA13 == 110 or LA13 == 114 or LA13 == 116:
                    alt13 = 1
                elif LA13 == 117:
                    alt13 = 2
                elif LA13 == 48 or LA13 == 49 or LA13 == 50 or LA13 == 51 or LA13 == 52 or LA13 == 53 or LA13 == 54 or LA13 == 55:
                    alt13 = 3
                else:
                    nvae = NoViableAltException("", 13, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 13, 0, self.input)

                raise nvae


            if alt13 == 1:
                # BELScript_Python_v1.g:408:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)

                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt13 == 2:
                # BELScript_Python_v1.g:409:9: UNICODE_ESCAPE
                pass 
                self.mUNICODE_ESCAPE()



            elif alt13 == 3:
                # BELScript_Python_v1.g:410:9: OCTAL_ESCAPE
                pass 
                self.mOCTAL_ESCAPE()




        finally:
            pass

    # $ANTLR end "ESCAPE_SEQUENCE"



    # $ANTLR start "OCTAL_ESCAPE"
    def mOCTAL_ESCAPE(self, ):
        try:
            # BELScript_Python_v1.g:414:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt14 = 3
            LA14_0 = self.input.LA(1)

            if (LA14_0 == 92) :
                LA14_1 = self.input.LA(2)

                if ((48 <= LA14_1 <= 51)) :
                    LA14_2 = self.input.LA(3)

                    if ((48 <= LA14_2 <= 55)) :
                        LA14_4 = self.input.LA(4)

                        if ((48 <= LA14_4 <= 55)) :
                            alt14 = 1
                        else:
                            alt14 = 2

                    else:
                        alt14 = 3

                elif ((52 <= LA14_1 <= 55)) :
                    LA14_3 = self.input.LA(3)

                    if ((48 <= LA14_3 <= 55)) :
                        alt14 = 2
                    else:
                        alt14 = 3

                else:
                    nvae = NoViableAltException("", 14, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 14, 0, self.input)

                raise nvae


            if alt14 == 1:
                # BELScript_Python_v1.g:414:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 51):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt14 == 2:
                # BELScript_Python_v1.g:415:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt14 == 3:
                # BELScript_Python_v1.g:416:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





        finally:
            pass

    # $ANTLR end "OCTAL_ESCAPE"



    # $ANTLR start "UNICODE_ESCAPE"
    def mUNICODE_ESCAPE(self, ):
        try:
            # BELScript_Python_v1.g:420:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # BELScript_Python_v1.g:420:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)

            self.match(117)

            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()





        finally:
            pass

    # $ANTLR end "UNICODE_ESCAPE"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):
        try:
            # BELScript_Python_v1.g:424:5: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # BELScript_Python_v1.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HEX_DIGIT"



    def mTokens(self):
        # BELScript_Python_v1.g:1:8: ( T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | T__104 | T__105 | T__106 | T__107 | T__108 | T__109 | T__110 | T__111 | T__112 | T__113 | T__114 | T__115 | T__116 | T__117 | T__118 | T__119 | T__120 | T__121 | T__122 | T__123 | T__124 | T__125 | T__126 | T__127 | T__128 | T__129 | T__130 | T__131 | T__132 | T__133 | T__134 | T__135 | T__136 | T__137 | T__138 | T__139 | T__140 | T__141 | T__142 | T__143 | T__144 | T__145 | T__146 | T__147 | T__148 | T__149 | T__150 | DOCUMENT_COMMENT | STATEMENT_COMMENT | IDENT_LIST | VALUE_LIST | QUOTED_VALUE | LP | RP | EQ | COLON | COMMA | NEWLINE | WS | KWRD_ANNO | KWRD_AS | KWRD_AUTHORS | KWRD_CONTACTINFO | KWRD_COPYRIGHT | KWRD_DFLT | KWRD_DEFINE | KWRD_DESC | KWRD_DISCLAIMER | KWRD_DOCUMENT | KWRD_LICENSES | KWRD_LIST | KWRD_NAME | KWRD_NS | KWRD_PATTERN | KWRD_SET | KWRD_STMT_GROUP | KWRD_UNSET | KWRD_URL | KWRD_VERSION | OBJECT_IDENT )
        alt15 = 120
        alt15 = self.dfa15.predict(self.input)
        if alt15 == 1:
            # BELScript_Python_v1.g:1:10: T__64
            pass 
            self.mT__64()



        elif alt15 == 2:
            # BELScript_Python_v1.g:1:16: T__65
            pass 
            self.mT__65()



        elif alt15 == 3:
            # BELScript_Python_v1.g:1:22: T__66
            pass 
            self.mT__66()



        elif alt15 == 4:
            # BELScript_Python_v1.g:1:28: T__67
            pass 
            self.mT__67()



        elif alt15 == 5:
            # BELScript_Python_v1.g:1:34: T__68
            pass 
            self.mT__68()



        elif alt15 == 6:
            # BELScript_Python_v1.g:1:40: T__69
            pass 
            self.mT__69()



        elif alt15 == 7:
            # BELScript_Python_v1.g:1:46: T__70
            pass 
            self.mT__70()



        elif alt15 == 8:
            # BELScript_Python_v1.g:1:52: T__71
            pass 
            self.mT__71()



        elif alt15 == 9:
            # BELScript_Python_v1.g:1:58: T__72
            pass 
            self.mT__72()



        elif alt15 == 10:
            # BELScript_Python_v1.g:1:64: T__73
            pass 
            self.mT__73()



        elif alt15 == 11:
            # BELScript_Python_v1.g:1:70: T__74
            pass 
            self.mT__74()



        elif alt15 == 12:
            # BELScript_Python_v1.g:1:76: T__75
            pass 
            self.mT__75()



        elif alt15 == 13:
            # BELScript_Python_v1.g:1:82: T__76
            pass 
            self.mT__76()



        elif alt15 == 14:
            # BELScript_Python_v1.g:1:88: T__77
            pass 
            self.mT__77()



        elif alt15 == 15:
            # BELScript_Python_v1.g:1:94: T__78
            pass 
            self.mT__78()



        elif alt15 == 16:
            # BELScript_Python_v1.g:1:100: T__79
            pass 
            self.mT__79()



        elif alt15 == 17:
            # BELScript_Python_v1.g:1:106: T__80
            pass 
            self.mT__80()



        elif alt15 == 18:
            # BELScript_Python_v1.g:1:112: T__81
            pass 
            self.mT__81()



        elif alt15 == 19:
            # BELScript_Python_v1.g:1:118: T__82
            pass 
            self.mT__82()



        elif alt15 == 20:
            # BELScript_Python_v1.g:1:124: T__83
            pass 
            self.mT__83()



        elif alt15 == 21:
            # BELScript_Python_v1.g:1:130: T__84
            pass 
            self.mT__84()



        elif alt15 == 22:
            # BELScript_Python_v1.g:1:136: T__85
            pass 
            self.mT__85()



        elif alt15 == 23:
            # BELScript_Python_v1.g:1:142: T__86
            pass 
            self.mT__86()



        elif alt15 == 24:
            # BELScript_Python_v1.g:1:148: T__87
            pass 
            self.mT__87()



        elif alt15 == 25:
            # BELScript_Python_v1.g:1:154: T__88
            pass 
            self.mT__88()



        elif alt15 == 26:
            # BELScript_Python_v1.g:1:160: T__89
            pass 
            self.mT__89()



        elif alt15 == 27:
            # BELScript_Python_v1.g:1:166: T__90
            pass 
            self.mT__90()



        elif alt15 == 28:
            # BELScript_Python_v1.g:1:172: T__91
            pass 
            self.mT__91()



        elif alt15 == 29:
            # BELScript_Python_v1.g:1:178: T__92
            pass 
            self.mT__92()



        elif alt15 == 30:
            # BELScript_Python_v1.g:1:184: T__93
            pass 
            self.mT__93()



        elif alt15 == 31:
            # BELScript_Python_v1.g:1:190: T__94
            pass 
            self.mT__94()



        elif alt15 == 32:
            # BELScript_Python_v1.g:1:196: T__95
            pass 
            self.mT__95()



        elif alt15 == 33:
            # BELScript_Python_v1.g:1:202: T__96
            pass 
            self.mT__96()



        elif alt15 == 34:
            # BELScript_Python_v1.g:1:208: T__97
            pass 
            self.mT__97()



        elif alt15 == 35:
            # BELScript_Python_v1.g:1:214: T__98
            pass 
            self.mT__98()



        elif alt15 == 36:
            # BELScript_Python_v1.g:1:220: T__99
            pass 
            self.mT__99()



        elif alt15 == 37:
            # BELScript_Python_v1.g:1:226: T__100
            pass 
            self.mT__100()



        elif alt15 == 38:
            # BELScript_Python_v1.g:1:233: T__101
            pass 
            self.mT__101()



        elif alt15 == 39:
            # BELScript_Python_v1.g:1:240: T__102
            pass 
            self.mT__102()



        elif alt15 == 40:
            # BELScript_Python_v1.g:1:247: T__103
            pass 
            self.mT__103()



        elif alt15 == 41:
            # BELScript_Python_v1.g:1:254: T__104
            pass 
            self.mT__104()



        elif alt15 == 42:
            # BELScript_Python_v1.g:1:261: T__105
            pass 
            self.mT__105()



        elif alt15 == 43:
            # BELScript_Python_v1.g:1:268: T__106
            pass 
            self.mT__106()



        elif alt15 == 44:
            # BELScript_Python_v1.g:1:275: T__107
            pass 
            self.mT__107()



        elif alt15 == 45:
            # BELScript_Python_v1.g:1:282: T__108
            pass 
            self.mT__108()



        elif alt15 == 46:
            # BELScript_Python_v1.g:1:289: T__109
            pass 
            self.mT__109()



        elif alt15 == 47:
            # BELScript_Python_v1.g:1:296: T__110
            pass 
            self.mT__110()



        elif alt15 == 48:
            # BELScript_Python_v1.g:1:303: T__111
            pass 
            self.mT__111()



        elif alt15 == 49:
            # BELScript_Python_v1.g:1:310: T__112
            pass 
            self.mT__112()



        elif alt15 == 50:
            # BELScript_Python_v1.g:1:317: T__113
            pass 
            self.mT__113()



        elif alt15 == 51:
            # BELScript_Python_v1.g:1:324: T__114
            pass 
            self.mT__114()



        elif alt15 == 52:
            # BELScript_Python_v1.g:1:331: T__115
            pass 
            self.mT__115()



        elif alt15 == 53:
            # BELScript_Python_v1.g:1:338: T__116
            pass 
            self.mT__116()



        elif alt15 == 54:
            # BELScript_Python_v1.g:1:345: T__117
            pass 
            self.mT__117()



        elif alt15 == 55:
            # BELScript_Python_v1.g:1:352: T__118
            pass 
            self.mT__118()



        elif alt15 == 56:
            # BELScript_Python_v1.g:1:359: T__119
            pass 
            self.mT__119()



        elif alt15 == 57:
            # BELScript_Python_v1.g:1:366: T__120
            pass 
            self.mT__120()



        elif alt15 == 58:
            # BELScript_Python_v1.g:1:373: T__121
            pass 
            self.mT__121()



        elif alt15 == 59:
            # BELScript_Python_v1.g:1:380: T__122
            pass 
            self.mT__122()



        elif alt15 == 60:
            # BELScript_Python_v1.g:1:387: T__123
            pass 
            self.mT__123()



        elif alt15 == 61:
            # BELScript_Python_v1.g:1:394: T__124
            pass 
            self.mT__124()



        elif alt15 == 62:
            # BELScript_Python_v1.g:1:401: T__125
            pass 
            self.mT__125()



        elif alt15 == 63:
            # BELScript_Python_v1.g:1:408: T__126
            pass 
            self.mT__126()



        elif alt15 == 64:
            # BELScript_Python_v1.g:1:415: T__127
            pass 
            self.mT__127()



        elif alt15 == 65:
            # BELScript_Python_v1.g:1:422: T__128
            pass 
            self.mT__128()



        elif alt15 == 66:
            # BELScript_Python_v1.g:1:429: T__129
            pass 
            self.mT__129()



        elif alt15 == 67:
            # BELScript_Python_v1.g:1:436: T__130
            pass 
            self.mT__130()



        elif alt15 == 68:
            # BELScript_Python_v1.g:1:443: T__131
            pass 
            self.mT__131()



        elif alt15 == 69:
            # BELScript_Python_v1.g:1:450: T__132
            pass 
            self.mT__132()



        elif alt15 == 70:
            # BELScript_Python_v1.g:1:457: T__133
            pass 
            self.mT__133()



        elif alt15 == 71:
            # BELScript_Python_v1.g:1:464: T__134
            pass 
            self.mT__134()



        elif alt15 == 72:
            # BELScript_Python_v1.g:1:471: T__135
            pass 
            self.mT__135()



        elif alt15 == 73:
            # BELScript_Python_v1.g:1:478: T__136
            pass 
            self.mT__136()



        elif alt15 == 74:
            # BELScript_Python_v1.g:1:485: T__137
            pass 
            self.mT__137()



        elif alt15 == 75:
            # BELScript_Python_v1.g:1:492: T__138
            pass 
            self.mT__138()



        elif alt15 == 76:
            # BELScript_Python_v1.g:1:499: T__139
            pass 
            self.mT__139()



        elif alt15 == 77:
            # BELScript_Python_v1.g:1:506: T__140
            pass 
            self.mT__140()



        elif alt15 == 78:
            # BELScript_Python_v1.g:1:513: T__141
            pass 
            self.mT__141()



        elif alt15 == 79:
            # BELScript_Python_v1.g:1:520: T__142
            pass 
            self.mT__142()



        elif alt15 == 80:
            # BELScript_Python_v1.g:1:527: T__143
            pass 
            self.mT__143()



        elif alt15 == 81:
            # BELScript_Python_v1.g:1:534: T__144
            pass 
            self.mT__144()



        elif alt15 == 82:
            # BELScript_Python_v1.g:1:541: T__145
            pass 
            self.mT__145()



        elif alt15 == 83:
            # BELScript_Python_v1.g:1:548: T__146
            pass 
            self.mT__146()



        elif alt15 == 84:
            # BELScript_Python_v1.g:1:555: T__147
            pass 
            self.mT__147()



        elif alt15 == 85:
            # BELScript_Python_v1.g:1:562: T__148
            pass 
            self.mT__148()



        elif alt15 == 86:
            # BELScript_Python_v1.g:1:569: T__149
            pass 
            self.mT__149()



        elif alt15 == 87:
            # BELScript_Python_v1.g:1:576: T__150
            pass 
            self.mT__150()



        elif alt15 == 88:
            # BELScript_Python_v1.g:1:583: DOCUMENT_COMMENT
            pass 
            self.mDOCUMENT_COMMENT()



        elif alt15 == 89:
            # BELScript_Python_v1.g:1:600: STATEMENT_COMMENT
            pass 
            self.mSTATEMENT_COMMENT()



        elif alt15 == 90:
            # BELScript_Python_v1.g:1:618: IDENT_LIST
            pass 
            self.mIDENT_LIST()



        elif alt15 == 91:
            # BELScript_Python_v1.g:1:629: VALUE_LIST
            pass 
            self.mVALUE_LIST()



        elif alt15 == 92:
            # BELScript_Python_v1.g:1:640: QUOTED_VALUE
            pass 
            self.mQUOTED_VALUE()



        elif alt15 == 93:
            # BELScript_Python_v1.g:1:653: LP
            pass 
            self.mLP()



        elif alt15 == 94:
            # BELScript_Python_v1.g:1:656: RP
            pass 
            self.mRP()



        elif alt15 == 95:
            # BELScript_Python_v1.g:1:659: EQ
            pass 
            self.mEQ()



        elif alt15 == 96:
            # BELScript_Python_v1.g:1:662: COLON
            pass 
            self.mCOLON()



        elif alt15 == 97:
            # BELScript_Python_v1.g:1:668: COMMA
            pass 
            self.mCOMMA()



        elif alt15 == 98:
            # BELScript_Python_v1.g:1:674: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt15 == 99:
            # BELScript_Python_v1.g:1:682: WS
            pass 
            self.mWS()



        elif alt15 == 100:
            # BELScript_Python_v1.g:1:685: KWRD_ANNO
            pass 
            self.mKWRD_ANNO()



        elif alt15 == 101:
            # BELScript_Python_v1.g:1:695: KWRD_AS
            pass 
            self.mKWRD_AS()



        elif alt15 == 102:
            # BELScript_Python_v1.g:1:703: KWRD_AUTHORS
            pass 
            self.mKWRD_AUTHORS()



        elif alt15 == 103:
            # BELScript_Python_v1.g:1:716: KWRD_CONTACTINFO
            pass 
            self.mKWRD_CONTACTINFO()



        elif alt15 == 104:
            # BELScript_Python_v1.g:1:733: KWRD_COPYRIGHT
            pass 
            self.mKWRD_COPYRIGHT()



        elif alt15 == 105:
            # BELScript_Python_v1.g:1:748: KWRD_DFLT
            pass 
            self.mKWRD_DFLT()



        elif alt15 == 106:
            # BELScript_Python_v1.g:1:758: KWRD_DEFINE
            pass 
            self.mKWRD_DEFINE()



        elif alt15 == 107:
            # BELScript_Python_v1.g:1:770: KWRD_DESC
            pass 
            self.mKWRD_DESC()



        elif alt15 == 108:
            # BELScript_Python_v1.g:1:780: KWRD_DISCLAIMER
            pass 
            self.mKWRD_DISCLAIMER()



        elif alt15 == 109:
            # BELScript_Python_v1.g:1:796: KWRD_DOCUMENT
            pass 
            self.mKWRD_DOCUMENT()



        elif alt15 == 110:
            # BELScript_Python_v1.g:1:810: KWRD_LICENSES
            pass 
            self.mKWRD_LICENSES()



        elif alt15 == 111:
            # BELScript_Python_v1.g:1:824: KWRD_LIST
            pass 
            self.mKWRD_LIST()



        elif alt15 == 112:
            # BELScript_Python_v1.g:1:834: KWRD_NAME
            pass 
            self.mKWRD_NAME()



        elif alt15 == 113:
            # BELScript_Python_v1.g:1:844: KWRD_NS
            pass 
            self.mKWRD_NS()



        elif alt15 == 114:
            # BELScript_Python_v1.g:1:852: KWRD_PATTERN
            pass 
            self.mKWRD_PATTERN()



        elif alt15 == 115:
            # BELScript_Python_v1.g:1:865: KWRD_SET
            pass 
            self.mKWRD_SET()



        elif alt15 == 116:
            # BELScript_Python_v1.g:1:874: KWRD_STMT_GROUP
            pass 
            self.mKWRD_STMT_GROUP()



        elif alt15 == 117:
            # BELScript_Python_v1.g:1:890: KWRD_UNSET
            pass 
            self.mKWRD_UNSET()



        elif alt15 == 118:
            # BELScript_Python_v1.g:1:901: KWRD_URL
            pass 
            self.mKWRD_URL()



        elif alt15 == 119:
            # BELScript_Python_v1.g:1:910: KWRD_VERSION
            pass 
            self.mKWRD_VERSION()



        elif alt15 == 120:
            # BELScript_Python_v1.g:1:923: OBJECT_IDENT
            pass 
            self.mOBJECT_IDENT()








    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\2\uffff\1\56\1\61\1\uffff\1\71\4\51\1\111\4\51\1\122\2\51\1\135"
        u"\1\143\2\51\7\uffff\2\156\1\uffff\11\51\11\uffff\3\51\1\167\1\51"
        u"\1\167\1\51\1\uffff\1\51\1\172\15\51\1\uffff\10\51\1\uffff\12\51"
        u"\1\uffff\5\51\1\uffff\10\51\3\uffff\4\51\1\u00b4\3\51\1\uffff\2"
        u"\51\1\uffff\1\u00bc\7\51\1\u00c5\5\51\1\u00cd\1\51\1\u00d0\2\51"
        u"\1\u00d4\1\u00d6\12\51\1\u00e2\10\51\1\u00ed\1\u00ee\1\u00ef\1"
        u"\u00f2\7\51\2\uffff\1\51\1\u00fd\2\51\1\uffff\7\51\1\uffff\2\51"
        u"\1\u010a\5\51\1\uffff\7\51\1\uffff\2\51\1\uffff\3\51\1\uffff\1"
        u"\51\1\uffff\1\u011e\1\u011f\4\51\1\u0125\1\51\1\u0128\2\51\1\uffff"
        u"\1\u012c\1\u012d\6\51\1\u0135\1\51\3\uffff\2\51\1\uffff\1\u0139"
        u"\1\51\1\u013b\4\51\2\uffff\1\51\1\uffff\14\51\1\uffff\23\51\2\uffff"
        u"\5\51\1\uffff\2\51\1\uffff\3\51\2\uffff\7\51\1\uffff\3\51\1\uffff"
        u"\1\51\1\uffff\1\u0177\1\51\1\u017c\1\51\1\u017e\24\51\1\u0193\4"
        u"\51\1\u0198\34\51\1\uffff\4\51\1\uffff\1\51\1\uffff\5\51\1\u01c0"
        u"\7\51\1\u01c9\5\51\1\u01cf\1\uffff\4\51\1\uffff\15\51\1\u01e1\23"
        u"\51\1\u01f6\1\u01f7\4\51\1\uffff\10\51\1\uffff\5\51\1\uffff\3\51"
        u"\1\u020d\6\51\1\u0214\6\51\1\uffff\3\51\1\u021e\5\51\1\u0224\12"
        u"\51\2\uffff\1\u0230\1\u0231\12\51\1\u023d\1\51\1\u023f\1\u0240"
        u"\5\51\1\uffff\3\51\1\u024a\1\u024b\1\51\1\uffff\3\51\1\u0250\1"
        u"\51\1\u0252\3\51\1\uffff\4\51\1\u025a\1\uffff\13\51\2\uffff\1\u0266"
        u"\12\51\1\uffff\1\51\2\uffff\4\51\1\u0276\3\51\1\u027a\2\uffff\4"
        u"\51\1\uffff\1\51\1\uffff\7\51\1\uffff\12\51\1\u0291\1\uffff\1\u0292"
        u"\11\51\1\u029c\1\u029d\1\u029e\2\51\1\uffff\3\51\1\uffff\4\51\1"
        u"\u02a8\21\51\2\uffff\1\51\1\u02bb\7\51\3\uffff\4\51\1\u02c8\4\51"
        u"\1\uffff\10\51\1\u02d5\1\u02d6\1\u02d7\3\51\1\u02db\3\51\1\uffff"
        u"\2\51\1\u02e1\6\51\1\u02e8\1\51\1\u02ea\1\uffff\14\51\3\uffff\1"
        u"\51\1\u02f8\1\51\1\uffff\1\u02fa\3\51\1\u02fe\1\uffff\6\51\1\uffff"
        u"\1\51\1\uffff\1\u0306\14\51\1\uffff\1\51\1\uffff\3\51\1\uffff\7"
        u"\51\1\uffff\13\51\1\u0329\6\51\1\u0330\3\51\1\u0334\7\51\1\u033c"
        u"\3\51\1\uffff\2\51\1\u0342\1\u0343\1\51\1\u0345\1\uffff\1\51\1"
        u"\u0347\1\u0348\1\uffff\1\u0349\1\u034a\1\51\1\u034c\3\51\1\uffff"
        u"\4\51\1\u0354\2\uffff\1\51\1\uffff\1\u0356\4\uffff\1\51\1\uffff"
        u"\4\51\1\u035c\2\51\1\uffff\1\51\1\uffff\1\u0360\1\u0361\1\u0362"
        u"\1\51\1\u0364\1\uffff\3\51\3\uffff\1\51\1\uffff\1\u0369\1\51\1"
        u"\u036b\1\51\1\uffff\1\51\1\uffff\1\u036e\1\51\1\uffff\1\u0370\1"
        u"\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\u0371\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\11\1\55\2\76\1\uffff\1\60\1\151\1\117\1\105\1\165\1\60\1\141"
        u"\1\156\1\151\1\111\1\60\1\101\1\162\2\60\1\105\1\154\2\uffff\1"
        u"\42\4\uffff\2\11\1\uffff\1\116\1\117\1\105\1\111\2\101\1\105\1"
        u"\116\1\105\11\uffff\1\165\1\164\1\116\1\60\1\116\1\60\1\124\1\uffff"
        u"\1\157\1\60\1\164\1\154\1\141\2\116\1\106\1\123\1\106\1\123\1\103"
        u"\1\163\1\156\1\160\1\uffff\1\163\1\143\1\101\1\156\2\103\1\143"
        u"\1\154\1\uffff\1\147\1\115\1\164\1\124\1\160\2\157\1\163\1\157"
        u"\1\124\1\uffff\1\164\1\141\1\142\1\141\1\156\1\uffff\1\124\1\142"
        u"\1\124\1\101\2\157\1\141\1\143\1\54\2\uffff\1\123\1\114\1\122\1"
        u"\156\1\60\1\154\1\117\1\157\1\uffff\1\110\1\154\1\uffff\1\60\1"
        u"\163\1\154\2\160\1\124\1\131\1\162\1\60\1\101\1\103\1\145\1\103"
        u"\1\125\1\60\1\145\1\60\1\103\1\162\2\60\1\124\1\105\1\124\1\162"
        u"\1\145\1\141\1\105\1\150\2\124\1\60\1\163\1\144\1\151\1\144\1\145"
        u"\1\143\1\157\1\101\4\60\1\146\1\124\1\143\1\162\2\156\1\162\1\40"
        u"\1\uffff\1\105\1\60\1\123\1\144\1\uffff\1\157\1\124\1\143\1\117"
        u"\1\157\1\141\1\154\1\uffff\1\145\1\123\1\60\1\154\1\101\1\122\1"
        u"\145\1\141\1\uffff\1\125\1\116\1\122\1\143\1\114\1\115\1\157\1"
        u"\uffff\1\101\1\157\1\uffff\1\157\2\145\1\uffff\1\163\1\uffff\2"
        u"\60\1\116\1\157\1\143\1\164\1\60\1\157\1\60\1\105\1\151\1\uffff"
        u"\2\60\1\164\1\165\1\156\1\145\1\114\1\164\1\60\1\142\3\uffff\1"
        u"\162\1\164\1\uffff\1\60\1\105\1\60\1\164\1\163\1\143\1\151\1\54"
        u"\1\uffff\1\124\1\uffff\1\111\1\141\1\147\1\101\1\151\1\122\1\147"
        u"\1\162\1\171\1\163\1\145\1\162\1\uffff\1\145\1\163\1\103\1\111"
        u"\1\141\1\144\1\114\1\105\1\111\1\164\1\101\1\105\1\156\1\142\1"
        u"\165\2\155\1\141\1\145\2\uffff\1\123\1\122\1\165\1\151\1\120\1"
        u"\uffff\2\154\1\uffff\1\122\1\144\1\150\2\uffff\1\151\1\143\1\157"
        u"\2\151\1\141\1\171\1\uffff\1\165\1\157\1\151\1\uffff\1\115\1\uffff"
        u"\1\60\1\143\1\60\1\160\1\60\1\117\1\156\1\157\1\124\1\141\1\123"
        u"\1\151\1\153\1\164\1\116\1\143\1\162\1\157\1\170\1\151\1\124\1"
        u"\107\1\163\1\141\1\124\1\60\1\120\1\154\1\111\1\116\1\60\1\165"
        u"\1\156\1\160\1\142\1\163\1\101\1\105\1\116\1\154\1\166\1\101\2"
        u"\157\1\116\2\141\1\166\1\164\1\163\1\156\1\155\1\156\1\157\1\154"
        u"\1\156\1\143\1\164\1\105\1\uffff\1\162\1\141\1\157\1\164\1\uffff"
        u"\1\164\1\uffff\1\116\1\143\1\165\1\111\1\164\1\60\1\143\1\145\1"
        u"\151\1\157\1\162\1\146\1\156\1\60\1\164\1\111\1\110\1\145\1\164"
        u"\1\60\1\uffff\1\124\1\171\1\115\1\124\1\uffff\1\156\1\144\1\157"
        u"\2\145\1\143\1\123\1\101\1\141\1\145\1\103\2\147\1\60\1\163\1\164"
        u"\1\145\1\163\1\164\1\101\1\151\1\164\1\156\1\141\1\144\1\145\1"
        u"\165\1\116\1\151\1\164\1\143\1\162\1\151\2\60\1\145\1\163\1\117"
        u"\1\151\1\uffff\1\141\1\162\1\143\1\103\1\145\1\141\1\145\1\142"
        u"\1\uffff\1\145\1\116\1\124\1\163\1\151\1\uffff\1\111\1\104\1\105"
        u"\1\60\1\144\1\101\1\156\1\162\1\163\1\164\1\60\1\101\1\162\1\103"
        u"\1\105\1\157\1\171\1\uffff\1\145\1\141\1\103\1\60\1\151\1\142\1"
        u"\157\1\164\1\163\1\60\1\164\1\141\1\163\1\164\1\124\1\142\1\145"
        u"\1\141\1\164\1\157\2\uffff\2\60\1\116\1\157\1\154\1\106\1\101\1"
        u"\150\1\164\1\143\1\101\1\165\1\60\1\106\2\60\1\157\1\117\1\145"
        u"\1\156\1\122\1\uffff\1\141\1\143\1\145\2\60\1\151\1\uffff\1\142"
        u"\1\101\1\157\1\60\1\165\1\60\1\101\1\163\1\157\1\uffff\1\143\1"
        u"\165\1\144\1\151\1\60\1\uffff\1\151\1\156\1\163\1\151\1\137\1\145"
        u"\1\164\1\144\1\164\1\101\1\156\2\uffff\1\60\1\156\1\120\1\157\1"
        u"\143\1\141\1\151\1\145\1\143\1\156\1\142\1\uffff\1\117\2\uffff"
        u"\1\156\1\116\2\143\1\60\1\156\1\164\1\156\1\60\2\uffff\1\166\1"
        u"\165\1\143\1\162\1\uffff\1\163\1\uffff\1\143\1\145\1\162\1\102"
        u"\1\156\1\151\1\156\1\uffff\1\157\1\143\1\117\1\157\1\107\1\144"
        u"\1\151\1\124\1\151\1\143\1\60\1\uffff\1\60\2\162\1\164\1\156\1"
        u"\157\1\105\1\164\1\144\1\165\3\60\2\162\1\uffff\1\143\1\151\1\164"
        u"\1\uffff\1\151\1\156\1\164\1\162\1\60\1\164\1\101\1\162\1\151\1"
        u"\144\1\146\1\147\1\156\1\145\1\146\1\156\1\122\1\124\3\157\1\164"
        u"\2\uffff\1\157\1\60\1\151\1\147\1\156\1\170\1\151\1\141\1\156\3"
        u"\uffff\3\145\1\166\1\60\1\164\1\144\1\151\1\145\1\uffff\1\151\1"
        u"\143\1\145\1\157\1\141\1\151\1\123\1\101\3\60\1\117\1\157\1\156"
        u"\1\60\1\156\1\151\1\143\1\uffff\1\166\1\145\1\60\1\160\1\166\1"
        u"\156\1\144\2\141\1\60\1\151\1\60\1\uffff\1\171\1\141\1\166\1\154"
        u"\1\166\1\164\1\154\1\155\1\156\1\143\1\164\1\143\3\uffff\1\125"
        u"\1\60\1\141\1\uffff\1\60\1\166\1\145\1\151\1\60\1\uffff\1\162\1"
        u"\151\1\143\1\141\2\163\1\uffff\1\164\1\uffff\1\60\1\156\1\151\1"
        u"\141\2\151\2\141\1\143\1\141\1\145\1\164\1\120\1\uffff\1\154\1"
        u"\uffff\1\151\1\163\1\164\1\uffff\1\145\1\164\1\145\1\156\2\145"
        u"\1\171\1\uffff\1\143\3\164\1\166\1\164\1\162\1\145\1\164\1\160"
        u"\1\151\1\60\1\101\1\164\1\163\1\171\1\163\1\171\1\60\1\143\2\163"
        u"\1\60\1\145\1\171\1\151\1\171\2\151\1\153\1\60\1\151\1\117\1\166"
        u"\1\uffff\1\143\1\171\2\60\1\163\1\60\1\uffff\1\145\2\60\1\uffff"
        u"\2\60\1\157\1\60\1\164\1\157\1\145\1\uffff\1\157\1\146\1\151\1"
        u"\164\1\60\2\uffff\1\151\1\uffff\1\60\4\uffff\1\156\1\uffff\1\171"
        u"\1\156\1\162\1\156\1\60\1\164\1\151\1\uffff\1\157\1\uffff\3\60"
        u"\1\106\1\60\1\uffff\1\171\1\166\1\156\3\uffff\1\157\1\uffff\1\60"
        u"\1\151\1\60\1\162\1\uffff\1\164\1\uffff\1\60\1\171\1\uffff\1\60"
        u"\1\uffff"
        )

    DFA15_max = DFA.unpack(
        u"\1\173\1\174\1\76\1\174\1\uffff\1\172\1\160\2\157\1\165\1\172\1"
        u"\141\1\163\2\151\1\172\1\145\1\162\2\172\1\165\1\163\2\uffff\1"
        u"\175\4\uffff\2\134\1\uffff\1\165\2\157\1\151\2\141\1\164\1\162"
        u"\1\145\11\uffff\1\165\1\164\1\156\1\172\1\156\1\172\1\164\1\uffff"
        u"\1\157\1\172\1\165\1\154\1\141\2\160\4\163\1\143\1\163\1\156\1"
        u"\160\1\uffff\1\163\1\143\1\101\1\156\2\163\1\143\1\154\1\uffff"
        u"\1\147\1\155\2\164\1\160\2\157\1\163\1\157\1\164\1\uffff\1\164"
        u"\1\141\1\142\1\141\1\156\1\uffff\1\164\1\162\1\164\1\141\2\157"
        u"\1\165\1\143\1\175\2\uffff\1\163\1\154\1\162\1\156\1\172\1\154"
        u"\2\157\1\uffff\1\150\1\155\1\uffff\1\172\1\163\1\154\2\160\1\164"
        u"\1\171\1\162\1\172\1\151\1\143\1\145\1\143\1\165\1\172\1\145\1"
        u"\172\1\115\1\162\2\172\1\164\1\145\1\164\1\162\1\145\1\141\1\145"
        u"\1\150\2\164\1\172\1\163\1\144\1\151\1\164\1\145\1\143\1\157\1"
        u"\101\4\172\1\146\1\164\1\143\1\162\2\156\1\162\1\175\1\uffff\1"
        u"\145\1\172\1\163\1\144\1\uffff\1\157\1\164\1\143\2\157\1\141\1"
        u"\154\1\uffff\1\145\1\123\1\172\1\157\1\141\1\162\1\145\1\141\1"
        u"\uffff\1\165\1\156\1\162\1\143\1\154\1\155\1\157\1\uffff\1\101"
        u"\1\157\1\uffff\1\157\2\145\1\uffff\1\163\1\uffff\2\172\1\156\1"
        u"\157\1\143\1\164\1\172\1\157\1\172\1\145\1\151\1\uffff\2\172\1"
        u"\164\1\165\1\156\1\145\1\114\1\164\1\172\1\142\3\uffff\1\162\1"
        u"\164\1\uffff\1\172\1\145\1\172\1\164\1\163\1\143\1\151\1\175\1"
        u"\uffff\1\164\1\uffff\1\151\1\141\1\147\1\141\1\151\1\162\1\147"
        u"\1\162\1\171\1\163\1\165\1\162\1\uffff\1\145\1\163\1\143\1\151"
        u"\1\141\1\144\1\154\1\145\1\151\1\164\1\141\1\145\1\156\1\142\1"
        u"\165\2\155\1\141\1\145\2\uffff\1\163\1\122\1\165\1\151\1\160\1"
        u"\uffff\2\154\1\uffff\1\162\1\144\1\150\2\uffff\1\151\1\143\1\157"
        u"\3\151\1\171\1\uffff\1\165\1\157\1\151\1\uffff\1\155\1\uffff\1"
        u"\172\1\160\1\172\1\160\1\172\1\157\1\156\1\157\1\164\1\141\1\163"
        u"\1\151\1\153\1\164\1\116\1\143\1\162\1\157\1\170\1\151\1\164\1"
        u"\147\1\163\1\141\1\164\1\172\1\160\1\154\1\151\1\156\1\172\1\165"
        u"\1\156\1\160\1\142\1\163\1\101\1\145\1\116\1\154\1\166\1\141\2"
        u"\157\1\156\2\141\1\166\1\164\1\163\1\156\1\155\1\156\1\157\1\154"
        u"\1\156\1\143\1\164\1\145\1\uffff\1\162\2\157\1\164\1\uffff\1\164"
        u"\1\uffff\1\156\1\143\1\165\1\151\1\164\1\172\1\143\1\145\1\151"
        u"\1\157\1\162\1\146\1\156\1\172\1\164\1\151\1\150\1\145\1\164\1"
        u"\172\1\uffff\1\164\1\171\1\155\1\164\1\uffff\1\156\1\144\1\157"
        u"\2\145\1\143\1\163\1\101\1\141\1\145\1\143\2\147\1\172\1\163\1"
        u"\164\1\145\1\163\1\164\1\115\1\151\1\164\1\156\1\141\1\144\1\145"
        u"\1\165\1\156\1\151\1\164\1\143\1\162\1\151\2\172\1\145\1\163\1"
        u"\157\1\151\1\uffff\1\141\1\162\1\143\1\103\1\145\1\141\1\145\1"
        u"\142\1\uffff\1\145\1\156\1\164\1\163\1\151\1\uffff\1\151\1\111"
        u"\1\145\1\172\1\144\1\101\1\156\1\162\1\163\1\164\1\172\1\101\1"
        u"\162\1\103\1\145\1\157\1\171\1\uffff\1\145\1\141\1\103\1\172\1"
        u"\151\1\142\1\157\1\164\1\163\1\172\1\164\1\141\1\163\2\164\1\160"
        u"\1\145\1\141\1\164\1\157\2\uffff\2\172\1\156\1\157\1\154\1\106"
        u"\1\101\1\150\1\164\1\143\1\101\1\165\1\172\1\146\2\172\2\157\1"
        u"\145\1\156\1\162\1\uffff\1\141\1\143\1\145\2\172\1\151\1\uffff"
        u"\1\142\1\101\1\157\1\172\1\165\1\172\1\101\1\163\1\157\1\uffff"
        u"\1\143\1\165\1\144\1\151\1\172\1\uffff\1\151\1\156\1\163\1\151"
        u"\1\137\1\145\1\164\1\144\1\164\1\101\1\156\2\uffff\1\172\1\156"
        u"\1\120\1\157\1\143\1\141\1\151\1\145\1\143\1\156\1\142\1\uffff"
        u"\1\157\2\uffff\2\156\2\143\1\172\1\156\1\164\1\156\1\172\2\uffff"
        u"\1\166\1\165\1\143\1\162\1\uffff\1\163\1\uffff\1\143\1\145\1\162"
        u"\1\102\1\156\1\151\1\156\1\uffff\1\157\1\143\1\117\1\157\1\147"
        u"\1\144\1\151\1\124\1\151\1\143\1\172\1\uffff\1\172\2\162\1\164"
        u"\1\156\1\157\1\105\1\164\1\144\1\165\3\172\2\162\1\uffff\1\143"
        u"\1\151\1\164\1\uffff\1\151\1\156\1\164\1\162\1\172\1\164\1\101"
        u"\1\162\1\151\1\144\1\146\1\147\1\156\1\145\1\146\1\156\1\162\1"
        u"\124\3\157\1\164\2\uffff\1\157\1\172\1\151\1\147\1\156\1\170\1"
        u"\151\1\141\1\156\3\uffff\3\145\1\166\1\172\1\164\1\144\1\151\1"
        u"\145\1\uffff\1\151\1\143\1\145\1\157\1\141\1\151\1\123\1\101\3"
        u"\172\2\157\1\156\1\172\1\156\1\151\1\143\1\uffff\1\166\1\145\1"
        u"\172\1\160\1\166\1\156\1\144\2\141\1\172\1\151\1\172\1\uffff\1"
        u"\171\1\141\1\166\1\154\1\166\1\164\1\154\1\155\1\156\1\143\1\164"
        u"\1\143\3\uffff\1\165\1\172\1\141\1\uffff\1\172\1\166\1\145\1\151"
        u"\1\172\1\uffff\1\162\1\151\1\143\1\141\2\163\1\uffff\1\164\1\uffff"
        u"\1\172\1\156\1\151\1\141\2\151\2\141\1\143\1\141\1\145\1\164\1"
        u"\160\1\uffff\1\154\1\uffff\1\151\1\163\1\164\1\uffff\1\145\1\164"
        u"\1\145\1\156\2\145\1\171\1\uffff\1\143\3\164\1\166\1\164\1\162"
        u"\1\145\1\164\1\160\1\151\1\172\1\101\1\164\1\163\1\171\1\163\1"
        u"\171\1\172\1\143\2\163\1\172\1\145\1\171\1\151\1\171\2\151\1\153"
        u"\1\172\1\151\1\117\1\166\1\uffff\1\143\1\171\2\172\1\163\1\172"
        u"\1\uffff\1\145\2\172\1\uffff\2\172\1\157\1\172\1\164\1\157\1\145"
        u"\1\uffff\1\157\1\146\1\151\1\164\1\172\2\uffff\1\151\1\uffff\1"
        u"\172\4\uffff\1\156\1\uffff\1\171\1\156\1\162\1\156\1\172\1\164"
        u"\1\151\1\uffff\1\157\1\uffff\3\172\1\106\1\172\1\uffff\1\171\1"
        u"\166\1\156\3\uffff\1\157\1\uffff\1\172\1\151\1\172\1\162\1\uffff"
        u"\1\164\1\uffff\1\172\1\171\1\uffff\1\172\1\uffff"
        )

    DFA15_accept = DFA.unpack(
        u"\4\uffff\1\7\21\uffff\1\130\1\131\1\uffff\1\134\1\135\1\136\1\141"
        u"\2\uffff\1\143\11\uffff\1\170\1\1\1\2\1\3\1\4\1\140\1\5\1\6\1\137"
        u"\7\uffff\1\10\17\uffff\1\42\10\uffff\1\57\12\uffff\1\64\5\uffff"
        u"\1\101\11\uffff\1\133\1\142\10\uffff\1\145\2\uffff\1\17\64\uffff"
        u"\1\132\4\uffff\1\12\7\uffff\1\20\10\uffff\1\34\7\uffff\1\40\2\uffff"
        u"\1\44\3\uffff\1\53\1\uffff\1\54\13\uffff\1\67\12\uffff\1\110\1"
        u"\111\1\163\2\uffff\1\112\10\uffff\1\132\1\uffff\1\166\14\uffff"
        u"\1\25\23\uffff\1\56\1\157\5\uffff\1\160\2\uffff\1\65\3\uffff\1"
        u"\71\1\73\7\uffff\1\105\3\uffff\1\115\1\uffff\1\116\73\uffff\1\117"
        u"\4\uffff\1\125\1\uffff\1\165\24\uffff\1\152\4\uffff\1\41\47\uffff"
        u"\1\146\10\uffff\1\27\5\uffff\1\151\21\uffff\1\162\24\uffff\1\127"
        u"\1\167\25\uffff\1\155\6\uffff\1\156\11\uffff\1\75\5\uffff\1\104"
        u"\13\uffff\1\11\1\13\13\uffff\1\31\1\uffff\1\150\1\33\11\uffff\1"
        u"\50\1\52\4\uffff\1\161\1\uffff\1\66\7\uffff\1\103\13\uffff\1\144"
        u"\17\uffff\1\154\3\uffff\1\51\26\uffff\1\126\1\14\11\uffff\1\147"
        u"\1\35\1\153\11\uffff\1\63\22\uffff\1\16\14\uffff\1\46\14\uffff"
        u"\1\107\1\113\1\114\3\uffff\1\122\5\uffff\1\23\6\uffff\1\43\1\uffff"
        u"\1\47\15\uffff\1\120\1\uffff\1\123\3\uffff\1\22\7\uffff\1\55\42"
        u"\uffff\1\164\6\uffff\1\30\3\uffff\1\45\7\uffff\1\77\5\uffff\1\15"
        u"\1\21\1\uffff\1\26\1\uffff\1\36\1\37\1\60\1\61\1\uffff\1\70\7\uffff"
        u"\1\124\1\uffff\1\32\5\uffff\1\102\3\uffff\1\62\1\72\1\74\1\uffff"
        u"\1\100\4\uffff\1\106\1\uffff\1\24\2\uffff\1\76\1\uffff\1\121"
        )

    DFA15_special = DFA.unpack(
        u"\u0371\uffff"
        )


    DFA15_transition = [
        DFA.unpack(u"\1\37\1\36\1\uffff\1\37\1\35\22\uffff\1\37\1\uffff\1"
        u"\31\1\26\4\uffff\1\32\1\33\2\uffff\1\34\1\1\1\uffff\1\27\12\51"
        u"\1\2\2\uffff\1\3\1\4\2\uffff\1\40\1\51\1\41\1\42\7\51\1\43\1\51"
        u"\1\44\1\51\1\45\2\51\1\46\1\51\1\47\1\50\4\51\1\uffff\1\37\2\uffff"
        u"\1\51\1\uffff\1\5\1\6\1\7\1\10\1\51\1\11\1\12\1\13\1\14\1\51\1"
        u"\15\1\16\1\17\1\20\1\21\1\22\1\51\1\23\1\24\1\25\1\47\1\50\4\51"
        u"\1\30"),
        DFA.unpack(u"\1\52\20\uffff\1\53\75\uffff\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\57\75\uffff\1\60"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\15\51\1\66\4\51\1\67\1\51\1\70\5\51"
        u"\4\uffff\1\51\1\uffff\1\51\1\62\1\63\12\51\1\64\4\51\1\65\1\51"
        u"\1\70\5\51"),
        DFA.unpack(u"\1\72\6\uffff\1\73"),
        DFA.unpack(u"\1\100\21\uffff\1\74\3\uffff\1\75\2\uffff\1\76\6\uffff"
        u"\1\77"),
        DFA.unpack(u"\1\103\3\uffff\1\104\5\uffff\1\105\25\uffff\1\101\3"
        u"\uffff\1\102\5\uffff\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\4\51\1\107"
        u"\16\51\1\110\6\51"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113\4\uffff\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\117\37\uffff\1\116"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\10\51\1\120"
        u"\5\51\1\121\13\51"),
        DFA.unpack(u"\1\124\37\uffff\1\124\3\uffff\1\123"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\12\51\7\uffff\1\134\31\51\4\uffff\1\51\1\uffff\1\126"
        u"\3\51\1\127\2\51\1\130\4\51\1\131\1\51\1\132\2\51\1\133\10\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\1\136\3\51"
        u"\1\137\3\51\1\140\4\51\1\141\11\51\1\142\2\51"),
        DFA.unpack(u"\1\146\16\uffff\1\147\20\uffff\1\144\16\uffff\1\147"
        u"\1\145"),
        DFA.unpack(u"\1\150\3\uffff\1\151\1\uffff\1\152\1\153"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\155\11\uffff\1\155\3\uffff\12\154\7\uffff\32\154"
        u"\4\uffff\1\154\1\uffff\32\154\1\155\1\uffff\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\1\36\1\uffff\2\37\22\uffff\1\37\73\uffff\1\37"),
        DFA.unpack(u"\2\37\1\uffff\2\37\22\uffff\1\37\73\uffff\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\4\uffff\1\67\1\uffff\1\70\30\uffff\1\66\4\uffff"
        u"\1\67\1\uffff\1\70"),
        DFA.unpack(u"\1\100\37\uffff\1\100"),
        DFA.unpack(u"\1\103\3\uffff\1\104\5\uffff\1\105\25\uffff\1\103\3"
        u"\uffff\1\104\5\uffff\1\105"),
        DFA.unpack(u"\1\117\37\uffff\1\117"),
        DFA.unpack(u"\1\124\37\uffff\1\124"),
        DFA.unpack(u"\1\134\37\uffff\1\134"),
        DFA.unpack(u"\1\146\16\uffff\1\147\20\uffff\1\146\16\uffff\1\147"),
        DFA.unpack(u"\1\157\3\uffff\1\160\33\uffff\1\157\3\uffff\1\160"),
        DFA.unpack(u"\1\161\37\uffff\1\161"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\165\22\uffff\1\164\14\uffff\1\165"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\22\51\1\166"
        u"\7\51"),
        DFA.unpack(u"\1\165\37\uffff\1\165"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\170\37\uffff\1\170"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\173\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\u0080\1\uffff\1\u0081\34\uffff\1\177\1\u0080\1\uffff"
        u"\1\u0081"),
        DFA.unpack(u"\1\u0080\1\uffff\1\u0081\35\uffff\1\u0080\1\uffff\1"
        u"\u0081"),
        DFA.unpack(u"\1\u0084\14\uffff\1\u0085\17\uffff\1\u0082\2\uffff"
        u"\1\u0084\1\u0083\13\uffff\1\u0085"),
        DFA.unpack(u"\1\u0087\36\uffff\1\u0086\1\u0087"),
        DFA.unpack(u"\1\u0084\14\uffff\1\u0085\22\uffff\1\u0084\14\uffff"
        u"\1\u0085"),
        DFA.unpack(u"\1\u0087\37\uffff\1\u0087"),
        DFA.unpack(u"\1\u0088\37\uffff\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0091\17\uffff\1\u0092\17\uffff\1\u0091\17\uffff"
        u"\1\u0090"),
        DFA.unpack(u"\1\u0091\17\uffff\1\u0092\17\uffff\1\u0091\17\uffff"
        u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096\37\uffff\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0099\37\uffff\1\u0098"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u0099\37\uffff\1\u0099"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a5\16\uffff\1\u00a4\20\uffff\1\u00a5"),
        DFA.unpack(u"\1\u00a6\17\uffff\1\u00a7"),
        DFA.unpack(u"\1\u00a5\37\uffff\1\u00a5"),
        DFA.unpack(u"\1\u00a8\37\uffff\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\1\u00ab\23\uffff\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae\3\uffff\12\154\7\uffff\32\154\4\uffff\1\154"
        u"\1\uffff\32\154\2\uffff\1\u00af"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b0\37\uffff\1\u00b0"),
        DFA.unpack(u"\1\u00b1\37\uffff\1\u00b1"),
        DFA.unpack(u"\1\u00b2\37\uffff\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6\37\uffff\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b8\37\uffff\1\u00b8"),
        DFA.unpack(u"\1\u00b9\1\u00ba"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\1\u00bb\31"
        u"\51"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1\37\uffff\1\u00c1"),
        DFA.unpack(u"\1\u00c2\37\uffff\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\21\51\1\u00c4"
        u"\10\51"),
        DFA.unpack(u"\1\u00c6\7\uffff\1\u00c7\27\uffff\1\u00c6\7\uffff\1"
        u"\u00c7"),
        DFA.unpack(u"\1\u00c8\37\uffff\1\u00c8"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca\37\uffff\1\u00ca"),
        DFA.unpack(u"\1\u00cb\37\uffff\1\u00cb"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\10\51\1\u00cc"
        u"\21\51"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u"\12\51\7\uffff\1\51\1\u00cf\30\51\4\uffff\1\51\1\uffff"
        u"\32\51"),
        DFA.unpack(u"\1\u00d1\11\uffff\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\1\u00d5\31"
        u"\51"),
        DFA.unpack(u"\1\u00d8\37\uffff\1\u00d7"),
        DFA.unpack(u"\1\u00d9\37\uffff\1\u00d9"),
        DFA.unpack(u"\1\u00d8\37\uffff\1\u00d8"),
        DFA.unpack(u"\1\u00da"),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\1\u00dd\37\uffff\1\u00dd"),
        DFA.unpack(u"\1\u00de"),
        DFA.unpack(u"\1\u00e0\23\uffff\1\u00df\13\uffff\1\u00e0"),
        DFA.unpack(u"\1\u00e0\37\uffff\1\u00e0"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\23\51\1\u00e1"
        u"\6\51"),
        DFA.unpack(u"\1\u00e3"),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u"\1\u00e6\2\uffff\1\u00e7\14\uffff\1\u00e8"),
        DFA.unpack(u"\1\u00e9"),
        DFA.unpack(u"\1\u00ea"),
        DFA.unpack(u"\1\u00eb"),
        DFA.unpack(u"\1\u00ec"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\17\51\1\u00f0\12\51\4\uffff\1\51\1\uffff"
        u"\22\51\1\u00f1\7\51"),
        DFA.unpack(u"\1\u00f3"),
        DFA.unpack(u"\1\u00f4\37\uffff\1\u00f4"),
        DFA.unpack(u"\1\u00f5"),
        DFA.unpack(u"\1\u00f6"),
        DFA.unpack(u"\1\u00f7"),
        DFA.unpack(u"\1\u00f8"),
        DFA.unpack(u"\1\u00f9"),
        DFA.unpack(u"\1\155\1\uffff\1\155\11\uffff\1\155\3\uffff\12\u00fa"
        u"\7\uffff\32\u00fa\4\uffff\1\u00fa\1\uffff\32\u00fa\1\155\1\uffff"
        u"\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fc\37\uffff\1\u00fc"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u00fe\37\uffff\1\u00fe"),
        DFA.unpack(u"\1\u00ff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0100"),
        DFA.unpack(u"\1\u0101\37\uffff\1\u0101"),
        DFA.unpack(u"\1\u0102"),
        DFA.unpack(u"\1\u0103\37\uffff\1\u0103"),
        DFA.unpack(u"\1\u0104"),
        DFA.unpack(u"\1\u0105"),
        DFA.unpack(u"\1\u0106"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0107"),
        DFA.unpack(u"\1\u0108"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\4\51\1\u0109"
        u"\25\51"),
        DFA.unpack(u"\1\u010b\2\uffff\1\u010c"),
        DFA.unpack(u"\1\u010d\37\uffff\1\u010d"),
        DFA.unpack(u"\1\u010e\37\uffff\1\u010e"),
        DFA.unpack(u"\1\u010f"),
        DFA.unpack(u"\1\u0110"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0111\37\uffff\1\u0111"),
        DFA.unpack(u"\1\u0112\37\uffff\1\u0112"),
        DFA.unpack(u"\1\u0113\37\uffff\1\u0113"),
        DFA.unpack(u"\1\u0114"),
        DFA.unpack(u"\1\u0115\37\uffff\1\u0115"),
        DFA.unpack(u"\1\u0116\37\uffff\1\u0116"),
        DFA.unpack(u"\1\u0117"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0118"),
        DFA.unpack(u"\1\u0119"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u011a"),
        DFA.unpack(u"\1\u011b"),
        DFA.unpack(u"\1\u011c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u011d"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0120\37\uffff\1\u0120"),
        DFA.unpack(u"\1\u0121"),
        DFA.unpack(u"\1\u0122"),
        DFA.unpack(u"\1\u0123"),
        DFA.unpack(u"\12\51\7\uffff\22\51\1\u0124\7\51\4\uffff\1\51\1\uffff"
        u"\22\51\1\u0124\7\51"),
        DFA.unpack(u"\1\u0126"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\16\51\1\u0127"
        u"\13\51"),
        DFA.unpack(u"\1\u0129\37\uffff\1\u0129"),
        DFA.unpack(u"\1\u012a"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\17\51\1\u012b"
        u"\12\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u012e"),
        DFA.unpack(u"\1\u012f"),
        DFA.unpack(u"\1\u0130"),
        DFA.unpack(u"\1\u0131"),
        DFA.unpack(u"\1\u0132"),
        DFA.unpack(u"\1\u0133"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\22\51\1\u0134"
        u"\7\51"),
        DFA.unpack(u"\1\u0136"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0137"),
        DFA.unpack(u"\1\u0138"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u013a\37\uffff\1\u013a"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u013c"),
        DFA.unpack(u"\1\u013d"),
        DFA.unpack(u"\1\u013e"),
        DFA.unpack(u"\1\u013f"),
        DFA.unpack(u"\1\u00ae\3\uffff\12\u00fa\7\uffff\32\u00fa\4\uffff"
        u"\1\u00fa\1\uffff\32\u00fa\2\uffff\1\u00af"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0140\37\uffff\1\u0140"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0141\37\uffff\1\u0141"),
        DFA.unpack(u"\1\u0142"),
        DFA.unpack(u"\1\u0143"),
        DFA.unpack(u"\1\u0144\37\uffff\1\u0144"),
        DFA.unpack(u"\1\u0145"),
        DFA.unpack(u"\1\u0146\37\uffff\1\u0146"),
        DFA.unpack(u"\1\u0147"),
        DFA.unpack(u"\1\u0148"),
        DFA.unpack(u"\1\u0149"),
        DFA.unpack(u"\1\u014a"),
        DFA.unpack(u"\1\u014b\17\uffff\1\u014c"),
        DFA.unpack(u"\1\u014d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u014e"),
        DFA.unpack(u"\1\u014f"),
        DFA.unpack(u"\1\u0150\37\uffff\1\u0150"),
        DFA.unpack(u"\1\u0151\37\uffff\1\u0151"),
        DFA.unpack(u"\1\u0152"),
        DFA.unpack(u"\1\u0153"),
        DFA.unpack(u"\1\u0154\37\uffff\1\u0154"),
        DFA.unpack(u"\1\u0155\37\uffff\1\u0155"),
        DFA.unpack(u"\1\u0156\37\uffff\1\u0156"),
        DFA.unpack(u"\1\u0157"),
        DFA.unpack(u"\1\u0158\37\uffff\1\u0158"),
        DFA.unpack(u"\1\u0159\37\uffff\1\u0159"),
        DFA.unpack(u"\1\u015a"),
        DFA.unpack(u"\1\u015b"),
        DFA.unpack(u"\1\u015c"),
        DFA.unpack(u"\1\u015d"),
        DFA.unpack(u"\1\u015e"),
        DFA.unpack(u"\1\u015f"),
        DFA.unpack(u"\1\u0160"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0161\37\uffff\1\u0161"),
        DFA.unpack(u"\1\u0162"),
        DFA.unpack(u"\1\u0163"),
        DFA.unpack(u"\1\u0164"),
        DFA.unpack(u"\1\u0165\37\uffff\1\u0165"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0166"),
        DFA.unpack(u"\1\u0167"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0168\37\uffff\1\u0168"),
        DFA.unpack(u"\1\u0169"),
        DFA.unpack(u"\1\u016a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u016b"),
        DFA.unpack(u"\1\u016c"),
        DFA.unpack(u"\1\u016d"),
        DFA.unpack(u"\1\u016e"),
        DFA.unpack(u"\1\u016f"),
        DFA.unpack(u"\1\u0170\7\uffff\1\u0171"),
        DFA.unpack(u"\1\u0172"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0173"),
        DFA.unpack(u"\1\u0174"),
        DFA.unpack(u"\1\u0175"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0176\37\uffff\1\u0176"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0178\10\uffff\1\u0179\3\uffff\1\u017a"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\1\u017b\31"
        u"\51"),
        DFA.unpack(u"\1\u017d"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u017f\37\uffff\1\u017f"),
        DFA.unpack(u"\1\u0180"),
        DFA.unpack(u"\1\u0181"),
        DFA.unpack(u"\1\u0182\37\uffff\1\u0182"),
        DFA.unpack(u"\1\u0183"),
        DFA.unpack(u"\1\u0184\37\uffff\1\u0184"),
        DFA.unpack(u"\1\u0185"),
        DFA.unpack(u"\1\u0186"),
        DFA.unpack(u"\1\u0187"),
        DFA.unpack(u"\1\u0188"),
        DFA.unpack(u"\1\u0189"),
        DFA.unpack(u"\1\u018a"),
        DFA.unpack(u"\1\u018b"),
        DFA.unpack(u"\1\u018c"),
        DFA.unpack(u"\1\u018d"),
        DFA.unpack(u"\1\u018e\37\uffff\1\u018e"),
        DFA.unpack(u"\1\u018f\37\uffff\1\u018f"),
        DFA.unpack(u"\1\u0190"),
        DFA.unpack(u"\1\u0191"),
        DFA.unpack(u"\1\u0192\37\uffff\1\u0192"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0194\37\uffff\1\u0194"),
        DFA.unpack(u"\1\u0195"),
        DFA.unpack(u"\1\u0196\37\uffff\1\u0196"),
        DFA.unpack(u"\1\u0197\37\uffff\1\u0197"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0199"),
        DFA.unpack(u"\1\u019a"),
        DFA.unpack(u"\1\u019b"),
        DFA.unpack(u"\1\u019c"),
        DFA.unpack(u"\1\u019d"),
        DFA.unpack(u"\1\u019e"),
        DFA.unpack(u"\1\u019f\37\uffff\1\u019f"),
        DFA.unpack(u"\1\u01a0"),
        DFA.unpack(u"\1\u01a1"),
        DFA.unpack(u"\1\u01a2"),
        DFA.unpack(u"\1\u01a3\37\uffff\1\u01a3"),
        DFA.unpack(u"\1\u01a4"),
        DFA.unpack(u"\1\u01a5"),
        DFA.unpack(u"\1\u01a6\37\uffff\1\u01a6"),
        DFA.unpack(u"\1\u01a7"),
        DFA.unpack(u"\1\u01a8"),
        DFA.unpack(u"\1\u01a9"),
        DFA.unpack(u"\1\u01aa"),
        DFA.unpack(u"\1\u01ab"),
        DFA.unpack(u"\1\u01ac"),
        DFA.unpack(u"\1\u01ad"),
        DFA.unpack(u"\1\u01ae"),
        DFA.unpack(u"\1\u01af"),
        DFA.unpack(u"\1\u01b0"),
        DFA.unpack(u"\1\u01b1"),
        DFA.unpack(u"\1\u01b2"),
        DFA.unpack(u"\1\u01b3"),
        DFA.unpack(u"\1\u01b4\37\uffff\1\u01b4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01b5"),
        DFA.unpack(u"\1\u01b6\15\uffff\1\u01b7"),
        DFA.unpack(u"\1\u01b8"),
        DFA.unpack(u"\1\u01b9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01ba"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01bb\37\uffff\1\u01bb"),
        DFA.unpack(u"\1\u01bc"),
        DFA.unpack(u"\1\u01bd"),
        DFA.unpack(u"\1\u01be\37\uffff\1\u01be"),
        DFA.unpack(u"\1\u01bf"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u01c1"),
        DFA.unpack(u"\1\u01c2"),
        DFA.unpack(u"\1\u01c3"),
        DFA.unpack(u"\1\u01c4"),
        DFA.unpack(u"\1\u01c5"),
        DFA.unpack(u"\1\u01c6"),
        DFA.unpack(u"\1\u01c7"),
        DFA.unpack(u"\12\51\7\uffff\1\u01c8\31\51\4\uffff\1\51\1\uffff\32"
        u"\51"),
        DFA.unpack(u"\1\u01ca"),
        DFA.unpack(u"\1\u01cb\37\uffff\1\u01cb"),
        DFA.unpack(u"\1\u01cc\37\uffff\1\u01cc"),
        DFA.unpack(u"\1\u01cd"),
        DFA.unpack(u"\1\u01ce"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d0\37\uffff\1\u01d0"),
        DFA.unpack(u"\1\u01d1"),
        DFA.unpack(u"\1\u01d2\37\uffff\1\u01d2"),
        DFA.unpack(u"\1\u01d3\37\uffff\1\u01d3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d4"),
        DFA.unpack(u"\1\u01d5"),
        DFA.unpack(u"\1\u01d6"),
        DFA.unpack(u"\1\u01d7"),
        DFA.unpack(u"\1\u01d8"),
        DFA.unpack(u"\1\u01d9"),
        DFA.unpack(u"\1\u01da\37\uffff\1\u01da"),
        DFA.unpack(u"\1\u01db"),
        DFA.unpack(u"\1\u01dc"),
        DFA.unpack(u"\1\u01dd"),
        DFA.unpack(u"\1\u01de\37\uffff\1\u01de"),
        DFA.unpack(u"\1\u01df"),
        DFA.unpack(u"\1\u01e0"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u01e2"),
        DFA.unpack(u"\1\u01e3"),
        DFA.unpack(u"\1\u01e4"),
        DFA.unpack(u"\1\u01e5"),
        DFA.unpack(u"\1\u01e6"),
        DFA.unpack(u"\1\u01e7\13\uffff\1\u01e8"),
        DFA.unpack(u"\1\u01e9"),
        DFA.unpack(u"\1\u01ea"),
        DFA.unpack(u"\1\u01eb"),
        DFA.unpack(u"\1\u01ec"),
        DFA.unpack(u"\1\u01ed"),
        DFA.unpack(u"\1\u01ee"),
        DFA.unpack(u"\1\u01ef"),
        DFA.unpack(u"\1\u01f0\37\uffff\1\u01f0"),
        DFA.unpack(u"\1\u01f1"),
        DFA.unpack(u"\1\u01f2"),
        DFA.unpack(u"\1\u01f3"),
        DFA.unpack(u"\1\u01f4"),
        DFA.unpack(u"\1\u01f5"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u01f8"),
        DFA.unpack(u"\1\u01f9"),
        DFA.unpack(u"\1\u01fa\37\uffff\1\u01fa"),
        DFA.unpack(u"\1\u01fb"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01fc"),
        DFA.unpack(u"\1\u01fd"),
        DFA.unpack(u"\1\u01fe"),
        DFA.unpack(u"\1\u01ff"),
        DFA.unpack(u"\1\u0200"),
        DFA.unpack(u"\1\u0201"),
        DFA.unpack(u"\1\u0202"),
        DFA.unpack(u"\1\u0203"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0204"),
        DFA.unpack(u"\1\u0205\37\uffff\1\u0205"),
        DFA.unpack(u"\1\u0206\37\uffff\1\u0206"),
        DFA.unpack(u"\1\u0207"),
        DFA.unpack(u"\1\u0208"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0209\37\uffff\1\u0209"),
        DFA.unpack(u"\1\u020a\4\uffff\1\u020b"),
        DFA.unpack(u"\1\u020c\37\uffff\1\u020c"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u020e"),
        DFA.unpack(u"\1\u020f"),
        DFA.unpack(u"\1\u0210"),
        DFA.unpack(u"\1\u0211"),
        DFA.unpack(u"\1\u0212"),
        DFA.unpack(u"\1\u0213"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0215"),
        DFA.unpack(u"\1\u0216"),
        DFA.unpack(u"\1\u0217"),
        DFA.unpack(u"\1\u0218\37\uffff\1\u0218"),
        DFA.unpack(u"\1\u0219"),
        DFA.unpack(u"\1\u021a"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u021b"),
        DFA.unpack(u"\1\u021c"),
        DFA.unpack(u"\1\u021d"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u021f"),
        DFA.unpack(u"\1\u0220"),
        DFA.unpack(u"\1\u0221"),
        DFA.unpack(u"\1\u0222"),
        DFA.unpack(u"\1\u0223"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0225"),
        DFA.unpack(u"\1\u0226"),
        DFA.unpack(u"\1\u0227"),
        DFA.unpack(u"\1\u0228"),
        DFA.unpack(u"\1\u0229\37\uffff\1\u0229"),
        DFA.unpack(u"\1\u022a\15\uffff\1\u022b"),
        DFA.unpack(u"\1\u022c"),
        DFA.unpack(u"\1\u022d"),
        DFA.unpack(u"\1\u022e"),
        DFA.unpack(u"\1\u022f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0232\37\uffff\1\u0232"),
        DFA.unpack(u"\1\u0233"),
        DFA.unpack(u"\1\u0234"),
        DFA.unpack(u"\1\u0235"),
        DFA.unpack(u"\1\u0236"),
        DFA.unpack(u"\1\u0237"),
        DFA.unpack(u"\1\u0238"),
        DFA.unpack(u"\1\u0239"),
        DFA.unpack(u"\1\u023a"),
        DFA.unpack(u"\1\u023b"),
        DFA.unpack(u"\12\51\7\uffff\1\u023c\31\51\4\uffff\1\51\1\uffff\32"
        u"\51"),
        DFA.unpack(u"\1\u023e\37\uffff\1\u023e"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0241"),
        DFA.unpack(u"\1\u0242\37\uffff\1\u0242"),
        DFA.unpack(u"\1\u0243"),
        DFA.unpack(u"\1\u0244"),
        DFA.unpack(u"\1\u0245\37\uffff\1\u0245"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0246"),
        DFA.unpack(u"\1\u0247"),
        DFA.unpack(u"\1\u0248"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\22\51\1\u0249"
        u"\7\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u024c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u024d"),
        DFA.unpack(u"\1\u024e"),
        DFA.unpack(u"\1\u024f"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0251"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0253"),
        DFA.unpack(u"\1\u0254"),
        DFA.unpack(u"\1\u0255"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0256"),
        DFA.unpack(u"\1\u0257"),
        DFA.unpack(u"\1\u0258"),
        DFA.unpack(u"\1\u0259"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u025b"),
        DFA.unpack(u"\1\u025c"),
        DFA.unpack(u"\1\u025d"),
        DFA.unpack(u"\1\u025e"),
        DFA.unpack(u"\1\u025f"),
        DFA.unpack(u"\1\u0260"),
        DFA.unpack(u"\1\u0261"),
        DFA.unpack(u"\1\u0262"),
        DFA.unpack(u"\1\u0263"),
        DFA.unpack(u"\1\u0264"),
        DFA.unpack(u"\1\u0265"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0267"),
        DFA.unpack(u"\1\u0268"),
        DFA.unpack(u"\1\u0269"),
        DFA.unpack(u"\1\u026a"),
        DFA.unpack(u"\1\u026b"),
        DFA.unpack(u"\1\u026c"),
        DFA.unpack(u"\1\u026d"),
        DFA.unpack(u"\1\u026e"),
        DFA.unpack(u"\1\u026f"),
        DFA.unpack(u"\1\u0270"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0271\37\uffff\1\u0271"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0272"),
        DFA.unpack(u"\1\u0273\37\uffff\1\u0273"),
        DFA.unpack(u"\1\u0274"),
        DFA.unpack(u"\1\u0275"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0277"),
        DFA.unpack(u"\1\u0278"),
        DFA.unpack(u"\1\u0279"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u027b"),
        DFA.unpack(u"\1\u027c"),
        DFA.unpack(u"\1\u027d"),
        DFA.unpack(u"\1\u027e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u027f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0280"),
        DFA.unpack(u"\1\u0281"),
        DFA.unpack(u"\1\u0282"),
        DFA.unpack(u"\1\u0283"),
        DFA.unpack(u"\1\u0284"),
        DFA.unpack(u"\1\u0285"),
        DFA.unpack(u"\1\u0286"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0287"),
        DFA.unpack(u"\1\u0288"),
        DFA.unpack(u"\1\u0289"),
        DFA.unpack(u"\1\u028a"),
        DFA.unpack(u"\1\u028b\37\uffff\1\u028b"),
        DFA.unpack(u"\1\u028c"),
        DFA.unpack(u"\1\u028d"),
        DFA.unpack(u"\1\u028e"),
        DFA.unpack(u"\1\u028f"),
        DFA.unpack(u"\1\u0290"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0293"),
        DFA.unpack(u"\1\u0294"),
        DFA.unpack(u"\1\u0295"),
        DFA.unpack(u"\1\u0296"),
        DFA.unpack(u"\1\u0297"),
        DFA.unpack(u"\1\u0298"),
        DFA.unpack(u"\1\u0299"),
        DFA.unpack(u"\1\u029a"),
        DFA.unpack(u"\1\u029b"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u029f"),
        DFA.unpack(u"\1\u02a0"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02a1"),
        DFA.unpack(u"\1\u02a2"),
        DFA.unpack(u"\1\u02a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02a4"),
        DFA.unpack(u"\1\u02a5"),
        DFA.unpack(u"\1\u02a6"),
        DFA.unpack(u"\1\u02a7"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02a9"),
        DFA.unpack(u"\1\u02aa"),
        DFA.unpack(u"\1\u02ab"),
        DFA.unpack(u"\1\u02ac"),
        DFA.unpack(u"\1\u02ad"),
        DFA.unpack(u"\1\u02ae"),
        DFA.unpack(u"\1\u02af"),
        DFA.unpack(u"\1\u02b0"),
        DFA.unpack(u"\1\u02b1"),
        DFA.unpack(u"\1\u02b2"),
        DFA.unpack(u"\1\u02b3"),
        DFA.unpack(u"\1\u02b4\37\uffff\1\u02b4"),
        DFA.unpack(u"\1\u02b5"),
        DFA.unpack(u"\1\u02b6"),
        DFA.unpack(u"\1\u02b7"),
        DFA.unpack(u"\1\u02b8"),
        DFA.unpack(u"\1\u02b9"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02ba"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02bc"),
        DFA.unpack(u"\1\u02bd"),
        DFA.unpack(u"\1\u02be"),
        DFA.unpack(u"\1\u02bf"),
        DFA.unpack(u"\1\u02c0"),
        DFA.unpack(u"\1\u02c1"),
        DFA.unpack(u"\1\u02c2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02c3"),
        DFA.unpack(u"\1\u02c4"),
        DFA.unpack(u"\1\u02c5"),
        DFA.unpack(u"\1\u02c6"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\22\51\1\u02c7"
        u"\7\51"),
        DFA.unpack(u"\1\u02c9"),
        DFA.unpack(u"\1\u02ca"),
        DFA.unpack(u"\1\u02cb"),
        DFA.unpack(u"\1\u02cc"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02cd"),
        DFA.unpack(u"\1\u02ce"),
        DFA.unpack(u"\1\u02cf"),
        DFA.unpack(u"\1\u02d0"),
        DFA.unpack(u"\1\u02d1"),
        DFA.unpack(u"\1\u02d2"),
        DFA.unpack(u"\1\u02d3"),
        DFA.unpack(u"\1\u02d4"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02d8\37\uffff\1\u02d8"),
        DFA.unpack(u"\1\u02d9"),
        DFA.unpack(u"\1\u02da"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02dc"),
        DFA.unpack(u"\1\u02dd"),
        DFA.unpack(u"\1\u02de"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02df"),
        DFA.unpack(u"\1\u02e0"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02e2"),
        DFA.unpack(u"\1\u02e3"),
        DFA.unpack(u"\1\u02e4"),
        DFA.unpack(u"\1\u02e5"),
        DFA.unpack(u"\1\u02e6"),
        DFA.unpack(u"\1\u02e7"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02e9"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02eb"),
        DFA.unpack(u"\1\u02ec"),
        DFA.unpack(u"\1\u02ed"),
        DFA.unpack(u"\1\u02ee"),
        DFA.unpack(u"\1\u02ef"),
        DFA.unpack(u"\1\u02f0"),
        DFA.unpack(u"\1\u02f1"),
        DFA.unpack(u"\1\u02f2"),
        DFA.unpack(u"\1\u02f3"),
        DFA.unpack(u"\1\u02f4"),
        DFA.unpack(u"\1\u02f5"),
        DFA.unpack(u"\1\u02f6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02f7\37\uffff\1\u02f7"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02f9"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u02fb"),
        DFA.unpack(u"\1\u02fc"),
        DFA.unpack(u"\1\u02fd"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u02ff"),
        DFA.unpack(u"\1\u0300"),
        DFA.unpack(u"\1\u0301"),
        DFA.unpack(u"\1\u0302"),
        DFA.unpack(u"\1\u0303"),
        DFA.unpack(u"\1\u0304"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0305"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0307"),
        DFA.unpack(u"\1\u0308"),
        DFA.unpack(u"\1\u0309"),
        DFA.unpack(u"\1\u030a"),
        DFA.unpack(u"\1\u030b"),
        DFA.unpack(u"\1\u030c"),
        DFA.unpack(u"\1\u030d"),
        DFA.unpack(u"\1\u030e"),
        DFA.unpack(u"\1\u030f"),
        DFA.unpack(u"\1\u0310"),
        DFA.unpack(u"\1\u0311"),
        DFA.unpack(u"\1\u0312\37\uffff\1\u0312"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0313"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0314"),
        DFA.unpack(u"\1\u0315"),
        DFA.unpack(u"\1\u0316"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0317"),
        DFA.unpack(u"\1\u0318"),
        DFA.unpack(u"\1\u0319"),
        DFA.unpack(u"\1\u031a"),
        DFA.unpack(u"\1\u031b"),
        DFA.unpack(u"\1\u031c"),
        DFA.unpack(u"\1\u031d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u031e"),
        DFA.unpack(u"\1\u031f"),
        DFA.unpack(u"\1\u0320"),
        DFA.unpack(u"\1\u0321"),
        DFA.unpack(u"\1\u0322"),
        DFA.unpack(u"\1\u0323"),
        DFA.unpack(u"\1\u0324"),
        DFA.unpack(u"\1\u0325"),
        DFA.unpack(u"\1\u0326"),
        DFA.unpack(u"\1\u0327"),
        DFA.unpack(u"\1\u0328"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u032a"),
        DFA.unpack(u"\1\u032b"),
        DFA.unpack(u"\1\u032c"),
        DFA.unpack(u"\1\u032d"),
        DFA.unpack(u"\1\u032e"),
        DFA.unpack(u"\1\u032f"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0331"),
        DFA.unpack(u"\1\u0332"),
        DFA.unpack(u"\1\u0333"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0335"),
        DFA.unpack(u"\1\u0336"),
        DFA.unpack(u"\1\u0337"),
        DFA.unpack(u"\1\u0338"),
        DFA.unpack(u"\1\u0339"),
        DFA.unpack(u"\1\u033a"),
        DFA.unpack(u"\1\u033b"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u033d"),
        DFA.unpack(u"\1\u033e"),
        DFA.unpack(u"\1\u033f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0340"),
        DFA.unpack(u"\1\u0341"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0344"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0346"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u034b"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u034d"),
        DFA.unpack(u"\1\u034e"),
        DFA.unpack(u"\1\u034f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0350"),
        DFA.unpack(u"\1\u0351"),
        DFA.unpack(u"\1\u0352"),
        DFA.unpack(u"\1\u0353"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0355"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0357"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0358"),
        DFA.unpack(u"\1\u0359"),
        DFA.unpack(u"\1\u035a"),
        DFA.unpack(u"\1\u035b"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u035d"),
        DFA.unpack(u"\1\u035e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u035f"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u0363"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0365"),
        DFA.unpack(u"\1\u0366"),
        DFA.unpack(u"\1\u0367"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0368"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u036a"),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u036c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u036d"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"\1\u036f"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff\32\51"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(BELScript_Python_v1Lexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
