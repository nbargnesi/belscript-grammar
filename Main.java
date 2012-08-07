import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;

public class Main {
    public static void main(String... args) throws Exception {
        ANTLRInputStream is = new ANTLRInputStream(System.in);
        BELScript_v1Lexer lexer = new BELScript_v1Lexer(is);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        BELScript_v1Parser parser = new BELScript_v1Parser(tokens);
        CommonTree t = (CommonTree) parser.document().getTree();

        CommonTreeNodeStream nodes = new CommonTreeNodeStream(t);

        Object o = nodes.nextElement();
        String token = o.toString();
        while (!"EOF".equals(token)) {
            System.out.println(token);
            o = nodes.nextElement();
            token = o.toString();
        }
        System.out.println(token);
    }
}

