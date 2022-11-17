# Instructions

Use Python's list comprehension feature to generate the following lists. 

```
[3, 4, 5, 6, 7, 8, 9, 10]

target = list(range(3, 11))

#alternatively 
target = [x for x in range (3, 11)] 
print(target) 
```

```
[10, 8, 6, 4, 2]

target = list(range(10 , 1, -2))
prnt(target)
```

```
[1, 16, 49, 100]
7 + 3 = 10 ^ 2
- start at theone with steps of 3 

target = [x**2 fro x in range(11) if x % 3 == 1]
print(target)

# alternatively 
target[ x**2 fo rx in range(1,11, 3) 
```

```
# only integers from 
source = [ 2, 3.75, .04, 59, .3, 6, 7, 8.5, 9, 10 ]

target = [ x for x in source if type(x) == int ]

#alternatively 
target = [ x for x in source if instance == int ]
```

```
1-1000 divisible by 7

# number 1-1000 divisible by 7 
div7 = [n for n in range(1,1000) if n % 7 == 0] 
print(div7)

```

```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [2, 7, 1, 12]
# tuples (x, y), x from a, y from b, x + y > 10

target = [ (x, y) for x in a for y in b if x + y > 10]
print(target)

```
