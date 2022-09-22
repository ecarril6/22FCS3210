# Left Recursion Elimination

Eliminate any left-recursive productions (including indirect ones). When you are done, submit this README.md file with your answers on Canvas. 

## Q1

```
X -> XYz | Xw | w
Y -> Yp | q
```
```
X -> XYz | Xw | w

X -> wX'
X' -> YzX' | wX' | epsilon
```

```
Y -> Yp | q
Y -> q | Y'
Y' -> pY' | epsilon
```

## Q2

```
S -> aA | Sd
A -> b
```
```
S -> aA | Sd

S -> aA | S'
S' -> dS' | epsilon
```
```
A -> b
```

## Q3

```
A -> Bxy | x
B -> CD
C -> A | c
D -> d           
```

```

B -> CD 
B -> Ad | cd



A -> Bxy | x
A -> Adxy | cdxy| x

A -> cdxy | x | A'
A' -> dxyA' | epsilon



```
