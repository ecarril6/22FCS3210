% CS3210 - Principles of Programming Languages - Fall 2022
% Instructor: Thyago Mota
% Description: Homework 11 - Prolog Lists
% Student Name: Emily Carrillo 



sum([],X):- X is 0.
sum([H|T],X):- sum(T, X1), X is X1 + H.

Tests: 

sum([], 0). 

sum([1, 2, 5], 8). 

sum([1, 2, 5], X). 

max([X,Y|[]],Z):- X > Y, !, Z is X.
max([X,Y|[]],Z):- Z is Y.

max([X|Y],Z):- max(Y,Z2), X > Z2, Z is X, !. 
max([X|Y],Z):- max(Y,Z2), Z is Z2, !. 

Tests: 

max([1, 2, 5], 5). 

max([1, 2, 5], X). 
