% CS3210 - Principles of Programming Languages - Fall 2022
% Instructor: Thyago Mota
% Description: Homework 11 - Prolog Lists
% Student Name: Emily Carrillo 

% Sum Predicate

sum([],X):- X is 0.
sum([H|T],X):- sum(T, X1), X is X1 + H.


%Tests: 
%sum([], 0). 
%output: true
%sum([1, 2, 5], 8). 
%output: true
%sum([1, 2, 5], X). 
%output: X = 8 

% Max Predicate

max([X],X).
max([H|T],Z) :- max(T,Ts),(H>=Ts,Z=H,!;Z=Ts,!).

%Tests: 
%max([1, 2, 5], 5). 
%output: true

%max([1, 2, 5], X). 
%output: X=5
