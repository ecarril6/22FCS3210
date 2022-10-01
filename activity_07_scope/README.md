# Question 1

Consider the following JavaScript-like program to answer the items below.  

```
var x;

function sub1() {
    document.write("x = " + x);
}

function sub2() {
    var x;
    x = 10;
    sub1();
}

x = 5;
sub2();
```

a) What value of x is displayed in function **sub1** IF **static-scoping** rules are applied?  


b) What value of x is displayed in function **sub1** IF **dynamic-scoping** rules are applied?  

'''
main:
x = 5
sub 2: 
    x = 10 
        sub 1:
        //satic scoping x = 5
        // static look locally then look outer scope
        //dynamic scope x = 10 
        // dynamic look locally the who called 
 
'''
# Question 2

Consider the following program, written in JavaScript-like syntax:  

```
// main program
var x, y, z;

function sub1() {
    var a, y, z;
    // ... 
}

function sub2() {
    var a, b, z;
    // ...
}

function sub3() {
    var a, x, w;
    // ...
}
```

Given the following calling sequences and assuming that dynamic scoping is used, what variables are visible during execution of the last subprogram activated? Include with each visible variable the name of the unit where it is declared.  

a) main calls sub1; sub1 calls sub2; sub2 calls sub3.  
'''
main: 
x, y, z
    sub 1:
    a, y , z
    : y sub 1 
     sub 2:
     a , b, c 
     : a sub  1, b sub 2, c sub sub 2
      sub 3: 
      a ,x, w
      : a sub 3, x sub 3, w sub 3
      
a: sub 3
b: sub 2
x: sub 3 
y: sub 1
z: sub 1
w: sub 3
      
'''  
b) main calls sub1; sub1 calls sub3.  

''' 
a: sub 3
b: not visible 
x: sub 3 
y: sub 1
z: sub 1
w: sub 3

''' 
c) main calls sub2; sub2 calls sub3; sub3 calls sub1.  

''' 
main: 
x, y, z
 sub 2: 
 a , b, c 
  sub 3: 
  a, x, w
    sub 1: 
    a, y , z 
    

a: sub 1
b: sub 2
c: sub 2
x: sub 3
y: sub 1
z: sub 1
w: sub 3

''' 
d) main calls sub3; sub3 calls sub1.  

''' 
a: sub 1 
x: sub 3
y: sub 1
z: sub 1
w: sub 3
b: not visible 
c: not visible 
''' 

e) main calls sub1; sub1 calls sub3; sub3 calls sub2.  

''' 
a: sub 2
x: sub 3
y: sub 1
z: sub 1
w: sub 3
b: sub 2
c: sub 2
''' 

 
f) main calls sub3; sub3 calls sub2; sub2 calls sub1.  

''' 
a: sub 1
x: sub 3
y: sub 1
z: sub 1
w: sub 3
b: sub 2
c: sub 2
'''

# Question 3

When the code below is interpreted using static scoping it outputs 0.25 and 0.25. However, if the same code is interpreted using dynamic scoping it outputs 0.25 and 0.125. Explain why the difference. 

```
program dynamic(in, out):

var r: real;

procedure show:
begin
    writeln(r)
end; 

procedure small:
var r: real;
begin
    r := 0.125; 
    show
end;

begin
    r := 0.25;
    show; small
end.
```

        // static look locally then look outer scope
Static :

```
program dynamic(in, out):

var r: real;

procedure show:        // procedure show look locally the outer - prints 0.25 
begin
    writeln(r)
end; 

procedure small:        // procedure small 
var r: real;            // defines r 
begin
    r := 0.125;         //r = 0.125        
    show                  // show is called by small - look locally - prints 0.125 
end;

begin
    r := 0.25;
    show; small
end.
```

       // dynamic look locally the who called 
Dynamic: 

```
program dynamic(in, out):

var r: real;

procedure show:
begin
    writeln(r) 
end; 

procedure small:
var r: real;
begin
    r := 0.125; 
    show
end;

begin
    r := 0.25;
    show; small
end.
```

