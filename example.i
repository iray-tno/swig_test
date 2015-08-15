/* example.i */
%module example
%{
/* Put header files here or function declarations like below */
#include <iostream>
extern void unko();
%}

#include <iostream>
extern void unko();
