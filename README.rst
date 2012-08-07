BEL Script grammar and interpreter utilities.

Use
===

Interpreter
-----------

To use this as a BEL Script interpreter::

    ./build.sh && ./run.sh
    Expecting BEL Script on stdin...
    + java -cp antlr-3.4.jar:. Main

Enter BEL Script text, EOF when finished.

BEL Script Files
----------------

To use this on BEL Script files::

    ./build.sh && ./run.sh < /path/to/file.bel
    Expecting BEL Script on stdin...
    + java -cp antlr-3.4.jar:. Main

For example::

    ./build.sh && ./run.sh < /path/to/small_corpus.bel
    Expecting BEL Script on stdin...
    + java -cp antlr-3.4.jar:. Main
    DOCDEF
    DOWN
    DOCSET_QV
    DOWN
    Name
    "BEL Framework Small Corpus Document"
    UP
    DOCSET_QV
    DOWN

