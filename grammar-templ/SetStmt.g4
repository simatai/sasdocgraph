grammar SetStmt;
import CommonGrammar ;

set_main
 : (set_stmt)* EOF
 ;

set_stmt
 : SET dataset_name ';'
 ;