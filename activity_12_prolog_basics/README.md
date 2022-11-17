# Example 1

Consider a college scenario where faculty, students, and visitors have controlled access to a lab during week and weekend days to encode the following facts in Prolog:  

```
Xavier and Brandi are faculty
Harvey, Ariel, Charlie, and Dan are students 
Laverne and Ramon are visitors
Dan is advised by Xavier while Ariel is advised by Brandi
```
faculty(Xavier) 
faculty(Brandi) 

student(Harvey)
student(Ariel)
student(Charlie)
student(Dan)

visitor(Laverne) 
visitor(Ramon) 


advisor(xavier , dan) :- faculty(xavier), stundent(dan).
advisor(brandi , ariel) :- faculty(brandi), stundent(ariel).

Next, encode the following rules: 

```
faculty and students have access to the lab during business days (Monday-Friday); 
only faculty or students currently being advised by faculty have access to the lab during the weekends.  
```
-questions is about who has access
business(mon) 
business(tue) 
business(wed) 
business(thu) 
business(fri) 
weekend(sat) 
weekend(sun) 

- uppercase variables because they are variables 
- create a geeneral rule ( x is a faculty, , d is a student, and the day is a business day) 
access(X, D ) :- (faculty (X) ; student(X)), business(D).
-business is a constant taht wll help when creating queries 
access(X, business) :- faculty(X) ;student(X).
-rule for weekend day : x has to be a faculty or x is a student advised by a faculty ( _ is an unamed variable) 
access(X, D ) :- (faculty (X) ; advisor(_,X)), weekend(D).
access(X, weekend ) :- faculty (X) ; advisor(_,X)).


Finally, have Prolog answer the following queries:  

```
Is Xavier a student?  
% student(xavier) 
% false 
Is Dan a student?  
% student(Dan) 
% true
Is Brandi a faculty?  
% faculty(Brandi) 
Is Ariel a visitor?  
Does Xavier have access to the lab during business days?  
Does Harvey have access to the lab during business days?  
Does Laverne have access to the lab during business days?  
Does Xavier have access to the lab during the weekend?  
Does Harvey have access to the lab during the weekend?  
Does Dan have access to the lab during the weekends?  
Does Laverne have access to the lab during the weekends?   
Who is Ariel’s advisor?  
-using variables (which values of x will make this predicate true) 
% advisor(X, ariel) 
% Brandi 

Who has access to the lab during business days?  
%access(X, businees)
Who has access to the lab during the weekends?  
%access( X, weekend)
```



# Example 2

Using Prolog, encode the following facts about students enrolled in classes:  

```
* Grace, Omar, Pablo, Molly, and Anthony are students
David is a faculty that is enrolled in CHE3190 to help on his research
Grace and Omar are CS majors
Pablo is a chemistry major
Molly is a history major
Anthony is a biology major
Grace is enrolled in CS3210 and CS3600
Omar is enrolled in CS3600
Pablo is enrolled in CHE3190 and CHE3200
Molly is enrolled in BIO1080
Anthony is enrolled in BIO1080
```
student(Grace) 
student(Omar) 
student(Pablo) 
student(Molly) 
student(Anthony) 

//Generic Rule
faculty(David).
enroll(X, C) :-  (studnet(X) ; facultyX)), course(C). 
enroll(david, che3190) :- (studnet(david) ; faculty(david)), course(

//Majors 

major(cs)
major(che)
major(his) 
major(bio) 

// G and O cs majors 
major(grace, CS
majors(computerScience , Omar) :- major(ComputerScience, stundent(Omar).
compscience(Omar)  
compscience(Grace) 

chemistry(Pablo)

history(Molly)

biology(Anthony)

course(CS3210)
course(CHE319)
CHE319
CHE319(David) 

CS3210(Grace)
CS3600(Grace)

CS3600(Omar)

CHE3190(Pablo)
CHE3200(Pablo)

BIO1080(Molly)

BIO1080(Anthony)



A biotech company is willing to hire student interns for the summer IF the student is:  

```
a CS major and is currently taking CS3210; OR  
currently taking CHE3190 (regardless of their major); OR 
a biology major
```
//X = cs major 
//majors checks for undrade viwers 
hire(X) :-  major(x, cs), enroll( X, Cs3210) 
hire(X) :-  stundet(X), enroll( X, Csche3190).
hire(X) :-  major(x, bio.

Have Prolog answer which student(s) should be hired.   
