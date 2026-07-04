### Infix: 

**Order of Operations (Only Infix):**  
Grouping (e.g. (), [], {}, ``, Numerator and Denominator of Fractions)  
Exponents and Roots  
Multiplication & Division (Left to Right)  
Addition & Subtraction (Left to Right)  

**Infix Examples:**  
(AB + (C/D))^E  
A + B - C * \[D / E] ^ (F / G)

### Prefix

* No order of operations
* Operator Operand Operand

**Example**  
^ + * A B / C D E
\- (+ A B) (* C ^ (/ D E) (/ F G))

### Postfix

* No order of operations
* Operand Operand Operator

**Examples:**  
A B * C D / + E ^  
A B + C D E / F G / ^ -


### Increments / Decrements

**Prefix:**  
* Example: ++a; --a;
* First we increment/decrement the variable, then if needed, perform the operation

**Postfix:**  
* Example: a++; a--;
* First we perform the operation if needed, then we increment/decrement the variable
