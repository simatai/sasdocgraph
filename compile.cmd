
SET PATH=.;%PATH%;C:\Program Files\Java\jdk1.8.0_92\bin;D:\programming\graphviz\release\bin;D:\programming\antlr;

antlr4 -Dlanguage=Python3 ./grammar/SAS.g4 -o ./saspyparser

