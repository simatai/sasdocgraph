
@ECHO OFF
call sasdocgraph ./tests/test-grammar.sas > "test-grammar.txt"
call dot test-grammar.txt