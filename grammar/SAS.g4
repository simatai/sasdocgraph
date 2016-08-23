grammar SAS;
import CommonGrammar;

parse
 : (sas_stmt_list)* EOF
 ;

sas_stmt_list
 : data_stmt
 | proc_stmt
 | any_stmt
 ;

set_stmt
 : SET dataset_name ';' 
 ;

run_stmt
 : RUN ';'
 ;
 
data_stmt
 : DATA dataset_name ';' set_stmt run_stmt
 ;
 
dataset_name : variables; 
 
proc_stmt
 : PROC ';'
 ; 
 
any_stmt
 : any_text
 ;
 
any_text : .;