### Lesson 1: Number Systems

**Decimal (Base 10) \[0 1 2 3 4 5 6 7 8 9]**

* 70932 = 7(10<sup>4</sup>) + 0(10<sup>3</sup>) + 9(10<sup>2</sup>) + 3(10<sup>1</sup>) + 2(10<sup>0</sup>)
* 1e4 = 1\*(10<sup>4</sup>); 3e-8 = 3\*(10<sup>-8</sup>) = 3/(10<sup>8</sup>)

**Binary (Base 2) \[0 1]**

* Most computer use the binary number system because it is made of electrical signals that can be on (1) or off (0)
* When there is no base, it must be decimal
* Represented as N<sub>2</sub> or 0bN
* 1010<sub>2</sub> = 1(2<sup>3</sup>) + 0(2<sup>2</sup>) + 1(2<sup>1</sup>) + 0(2<sup>0</sup>)

**How to count in Binary**

| Decimal | Binary | | Decimal | Binary | | Decimal | Binary | | Decimal | Binary | | Decimal | Binary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | | 8 | 1000 | | 16 | 10000 | | 24 | 11000 | | 32 | 100000 |
| 1 | 1 | | 9 | 1001 | | 17 | 10001 | | 25 | 11001 | | | |
| 2 | 10 | | 10 | 1010 | | 18 | 10010 | | 26 | 11010 | | | |
| 3 | 11 | | 11 | 1011 | | 19 | 10011 | | 27 | 11011 | | | |
| 4 | 100 | | 12 | 1100 | | 20 | 10100 | | 28 | 11100 | | | |
| 5 | 101 | | 13 | 1101 | | 21 | 10101 | | 29 | 11101 | | | |
| 6 | 110 | | 14 | 1110 | | 22 | 10110 | | 30 | 11110 | | | |
| 7 | 111 | | 15 | 1111 | | 23 | 10111 | | 31 | 11111 | | | |

* For being proficient in Binary, we must know the powers of 2 from at least 0 to 10 (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)

**Binary to Decimal**

* 1010<sub>2</sub> = 1(2<sup>3</sup>) + 0(2<sup>2</sup>) + 1(2<sup>1</sup>) + 0(2<sup>0</sup>)

**Decimal to Binary (Proper)**

* x = 2<sup>n</sup>(?<sub>0</sub>) + 2<sup>n-1</sup>(?<sub>1</sub>) + ... + 2<sup>0</sup>(?<sub>n-1</sub>)
* Take the greatest power of 2 possible without going over and keep doing this from left to right
* EXAMPLE: 37 = 2<sup>5</sup>(1) + 2<sup>4</sup>(0) + 2<sup>3</sup>(0) + 2<sup>2</sup>(1) + 2<sup>1</sup>(0) + 2<sup>0</sup>(1) = 100101<sub>2</sub>

**Decimal to Binary (Shortcut)**

* Keep dividing number n by 2 until you get to 1/2=0R1 (take the rounded down integer of the division). Make a list of all the remainders from left to right (starting with n%2). Reverse the list to get the final number. 
* EXAMPLE: 37/2=18R1; 18/2=9R0; 9/2=4R1; 4/2=2R0; 2/2=1R0; 1/2=0R1 -> List of remainders from left to right: \[1 0 1 0 0 1] -> Reverse the list \[1 0 0 1 0 1] -> Final Binary Number: 100101<sub>2</sub>

**Hexadecimal (Base 16) \[0 1 2 3 4 5 6 7 8 9 A B C D E F]**

* Used by some computers to shorten binary numbers
* After 0 through 9, A is 10, B is 11, C is 12, D is 13, E is 14, F is 15
* Most programmers use hexadecimal

**How to count in Hexadecimal**

| Decimal | Hexadecimal | | Decimal | Hexadecimal | | Decimal | Hexadecimal | | Decimal | Hexadecimal | | Decimal | Hexadecimal | | Decimal | Hexadecimal | | Decimal | Hexadecimal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | | 8 | 8 | | 16 | 10 | | 24 | 18 | | 32 | 20 | | 40 | 28 | | 48 | 30 |
| 1 | 1 | | 9 | 9 | | 17 | 11 | | 25 | 19 | | 33 | 21 | | 41 | 29 | | | |
| 2 | 2 | | 10 | A | | 18 | 12 | | 26 | 1A | | 34 | 22 | | 42 | 2A | | | |
| 3 | 3 | | 11 | B | | 19 | 13 | | 27 | 1B | | 35 | 23 | | 43 | 2B | | | |
| 4 | 4 | | 12 | C | | 20 | 14 | | 28 | 1C | | 36 | 24 | | 44 | 2C | | | |
| 5 | 5 | | 13 | D | | 21 | 15 | | 29 | 1D | | 37 | 25 | | 45 | 2D | | | |
| 6 | 6 | | 14 | E | | 22 | 16 | | 30 | 1E | | 38 | 26 | | 46 | 2E | | | |
| 7 | 7 | | 15 | F | | 23 | 17 | | 31 | 1F | | 39 | 27 | | 47 | 2F | | | |

**Hexadecimal to Decimal**

* 2E5<sub>16</sub> = 2(16<sup>2</sup>) + 14(16<sup>1</sup> + 5(16<sup>0</sup>) = 741

**Decimal to Hexadecimal**

* Proper: Same as binary (using the maximum power of 16 & multiplying it)
* Shortcut: Keep dividing number n by 16 until you get a result of 0/16=0Ry (take the rounded down integer of the division). Make a list of all the remainders from left to right (starting with n%16). Reverse the list to get the final number.
* EXAMPLE: 741/16=46R5; 46/16=2R14; 2/16=0R2; 0/16=0 -> List of remainders from left to right: \[5 14 2] -> Reverse the list \[2 14 5] -> Replace numbers greater than 9 with the corresponding letter \[2 E 5] -> Final Hexadecimal Number: 2E5<sub>16</sub>

**Octal (Base 8) \[0 1 2 3 4 5 6 7]**

* Some programmers use octal
* Once you go beyond 7, carry over

**How to count in Octal**
| Decimal | Octal | | Decimal | Octal | | Decimal | Octal | | Decimal | Octal | | Decimal | Octal | | Decimal | Octal | | Decimal | Octal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | | 8 | 10 | | 16 | 20 | | 24 | 30 | | 32 | 40 | | 40 | 50 | | 48 | 60 |
| 1 | 1 | | 9 | 11 | | 17 | 21 | | 25 | 31 | | 33 | 41 | | 41 | 51 | | | |
| 2 | 2 | | 10 | 12 | | 18 | 22 | | 26 | 32 | | 34 | 42 | | 42 | 52 | | | |
| 3 | 3 | | 11 | 13 | | 19 | 23 | | 27 | 33 | | 35 | 43 | | 43 | 53 | | | |
| 4 | 4 | | 12 | 14 | | 20 | 24 | | 28 | 34 | | 36 | 44 | | 44 | 54 | | | |
| 5 | 5 | | 13 | 15 | | 21 | 25 | | 29 | 35 | | 37 | 45 | | 45 | 55 | | | |
| 6 | 6 | | 14 | 16 | | 22 | 26 | | 30 | 36 | | 38 | 46 | | 46 | 56 | | | |
| 7 | 7 | | 15 | 17 | | 23 | 27 | | 31 | 37 | | 39 | 47 | | 47 | 57 | | | |

**Octal to Decimal**

* 37<sub>8</sub> = 3(8<sup>1</sup>) + 7(8<sup>0</sup> = 31

**Decimal to Octal**

* Proper: Same as binary (using the maximum power of 8 & multiplying it)
* Shortcut: Keep dividing number n by 8 until you get a result of 0/8=0Ry (take the rounded down integer of the division). Make a list of all the remainders from left to right (starting with n%16). Reverse the list to get the final number.
* EXAMPLE: 47/8=5R7; 5/8=0R5; 0/8=0R0 -> List of remainders from left to right: \[7 5] -> Reverse the list \[5 7] -> Final Octal Number: 57<sub>8</sub>

**Binary to Octal & Octal to Binary**

* Observation: 8<sup>1</sup> = 2<sup>3</sup> -> Every 1 octal digit corresponds to 3 binary digits
* Binary to Octal:
  * Split the binary number into groups of 3 from right to left (use leading zeros to finish the leftmost group) then convert each group into an octal digit
  * EXAMPLE: 001010000100111101<sub>2</sub> -> 001 010 000 100 111 101<sub>2</sub> -> 1 2 0 4 7 5<sub>8</sub> -> 120475<sub>8</sub>
* Octal to Binary:
  * Take each digit in the octal number and convert to a 3 digit group in binary
  * EXAMPLE: 120475<sub>8</sub> -> 1 2 0 4 7 5<sub>8</sub> -> 001 010 000 100 111 101<sub>2</sub> -> 001010000100111101<sub>2</sub> -> 1010000100111101<sub>2</sub>
* When grouping always start from the right side and if the group is not even on the leftmost one, use leading zeros

**Binary to Hexadecimal & Vice Versa**

* 16<sup>1</sup> = 2<sup>4</sup> -> Every 1 hex digit corresponds to 4 binary digits
* Binary to Hex: 1010000100111101<sub>2</sub> ->1010 0001 0011 1101<sub>2</sub> -> A 1 3 D<sub>16</sub> -> A13D<sub>16</sub>
* Hex to Binary: A13D<sub>16</sub> -> A 1 3 D<sub>16</sub> -> 1010 0001 0011 1101<sub>2</sub> -> 1010000100111101<sub>2</sub>
* Don't forget the leading zeros

**Convert base n to base m**

* Convert X<sub>n</sub> to decimal using the shortcut method (which works for any base)
* Convert the decimal number to base m

**Practice**

56<sub>10</sub> to Binary:  
56/2 = 28R0; 28/2=14R0; 14/2=7R0; 7/2=3R1; 3/2=1R1; 1/2=0R1  
111000<sub>2</sub>

2B5<sub>16</sub> to Decimal:  
2(16<sup>2</sup>) + 11(16<sup>1</sup>) + 5(16<sup>0</sup>) = 2(256) + 11(16) + 5(1) = 512 + 176 + 5 = 693  
693<sub>10</sub>

4A<sub>16</sub> to Octal: 
4(16<sup>1</sup>) + 10(16<sup>0</sup>) = 64 + 10 = 74
74/8=9R2; 9/8=1R1; 1/8=0R1; 0/8=0 -> 0112<sub>8</sub> -> 112<sub>8</sub>
