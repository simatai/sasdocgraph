data water;                      
  set water2;
  run;
  
data water;
set somemore;
run;

proc sort data=water;
by water;
run;
