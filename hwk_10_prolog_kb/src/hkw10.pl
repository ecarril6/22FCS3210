% CS3210 - Principles of Programming Languages - Fall 2022
% Instructor: Thyago Mota
% Description: Homework 10 - A KB in Prolog with queries
% Student Name: Emily Carrillo


%% Name of mountain 
mountain(mteverest).
mountain(aconcagua).
mountain(mtmckinley).
mountain(kilimanjaro).
mountain(mtelbrus).
mountain(mtvinson).
mountain(puncakjaya).

%% mountain locations
location(mteverest, asia).
location(aconcagua, southamerica).
location(mtmckinley, northamerica).
location(kilimanjaro, africa).
location(mtelbrus, europe).
location(mtvinson, antartica).
location(puncakjaya, australia).

%% Height of peaks
peak(mteverest, 29029).
peak(aconcagua, 22841).
peak(mtmckinley, 20312).
peak(kilimanjaro, 19340).
peak(mtelbrus, 18510).
peak(mtvinson, 16050).
peak(puncakjaya, 16023).


higher(X,Y) :-
    peak(X,H),
    (H>Y).
    
question('Is Mt. Everest one of the highest peaks in the world?'):- true.

% Climbers and status of certification

climber(john).
climber(kelly).
climber(maria).
climber(derek).
climber(thyago).

certified(john).
certified(kelly).
certified(maria).
certified(derek).
not(certified(thyago)).

climb(john,X) :-
    mountain(X),
    certified(john),
    location(X,northamerica).

climb(kelly,X) :-
    mountain(X),
    certified(kelly),
    peak(X,Y),
    Y >= 20000.

climb(maria,X) :-
    mountain(X),
    certified(maria).

climb(derek,X) :-
    mountain(X),
    certified(john),
    (location(X,europe);
    location(X,africa);
    location(X,australia)),
    peak(X,Y),
    Y =< 19000.

climb(thyago, _) :- 
    false.

% Queries

%Is Mt. Everest one of the highest peaks in the world? true 
%question('Is Mt. Everest one of the highest peaks in the world?').

%Is the Kilimanjaro located in Africa? true 
%location(kilimanjaro, africa).

%Is Mt. Elbrus more than 18K feet? true 
%higher(mtelbrus, 18000).

%Is Thyago a certified climber? false 
%certified(thyago).

%Is John a certified climber? true 
%certified(john).

%All certified climbers? John, Kelly, Maria, and Derek 
%certified(X).

%All peaks that John would climb?  Mt. McKinley 
%climb(john, X).

%All peaks that Kelly would climb? Mt. Everest, the Aconcagua, and Mt. McKinley
%climb(kelly, X).

%All peaks that Maria would climb? all of the 7 peaks! 
%climb(maria, X).

%All peaks that Derek would climb? Mt. Elbrus and the Puncak Jaya 
%climb(derek, X).

%All peaks that Thyago would climb? none (or false) 
%climb(thyago, X).
