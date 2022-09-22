# Left Recursion Elimination

Eliminate any left-recursive productions (including indirect ones). When you are done, submit this README.md file with your answers on Canvas. 

## Q1

```
X -> XYz | Xw | w
Y -> Yp | q
```
X -> Xqz | Xw | w

X -> Xqz | Xw | w

X -> wX'
X'-> qzX' | wX' | epsilon

## Q2

```
S -> aA | Sd
A -> b
```

S -> aA | Sd
S -> ab | Sd

S -> abS'
S' -> dS' | epsilon


## Q3

```
A -> Bxy | x
B -> CD
C -> A | c
D -> d           
```

