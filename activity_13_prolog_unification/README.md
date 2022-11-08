# Instructions

Consider the following knowledge base: 

```
elf(bing). 
elf(penny). 

elf('Gabriel'). 

elf(trixie). 
wizard(merlin). 
wizard(gandalf). 
witch(jadis). 
-- rules on seperat lines works as OR 
magic(X) :- elf(X). 
magic(X) :- wizard(X). 
magic(X) :- witch(X). 
--This can only be true if X is a wizard
freeze(X,Y) :- wizard(X), elf(Y). 
```

Which of the following queries are satisfied?  Where relevant, give all the variable instantiations that lead to success. 

```
- 'Gabirel' does not equal gabriel 
elf(gabriel).  
false 

wizard('Merlin').  
false 

wizard(X).  
works! 
-bind X to all the possible sollutioms 
X = merlin 
X= gandalf 

magic(X).   

X = bing
X = penny
X = 'Gabriel'
X = trixie
X = merlin
X = gandalf
X = jadis

witch(Jadis).  
-works!
Jadis = jadis

freeze(merlin, Y).  

Y = bing
Y = penny
Y = 'Gabriel'
Y = trixie

freeze(X, merlin).   
-false 
```
