# python-learning

clone the repo into local, update in jupyter notebook.
cmd prompt
jupyter notebook

Generator expressions vs List Comprehension 

squares = ( x*x for x in range(100000))
Generator expression wont use any memory when declared.
in above squares Generator object is created but it wont contain any data.

while similar list Comprehension creates a list with complete data so uses lot of memory.

Generator expressions are lazy in nature. 
memory efficient.

you can use next , sum , list(),for ... to materialise Generator object.

exampe : v1 = next(squares)
v1 holds 0 

vs = sum(sqaures) memory is used for one vslue at a time as sum iterates .
 