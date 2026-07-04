/*
PROBLEM: Given 3 positive integers, n, b, and s, generate the next n numbers in base b starting with s in the given base. We guarantee that the base will be between 2 and 9 inclusive. We guarantee that s is a valid number in base  b. Find the base 10 value for the number of times the largest possible digit in the given base is found among all of the digits in the numbers generated.
EXAMPLE:If n=15, b=8, and s=2, the numbers generated are 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20. The largest possible digit in base 8 is 7 which occurs 2 times. 
INPUT: There will be three integers representing the number of values to be found, the base to be used between 2 and 9 inclusive, and the starting value in the base given that will be no more than 16 digits.
OUTPUT: For each set of 3 input values, output a base 10 number representing the number of times the largest digit in the inputted base occurs in the sequence of numbers generated.
*/

#include<bits/stdc++.h>
using namespace std; 

long long baseNtoTen(long long num, long long baseN) {
    string thing = to_string(num); 
    long long res = 0;
    for (char i : thing) {
        res *= baseN;
        res += i - '0'; 
    }
    return res; 
}

string baseTenToN(long long num, long long new_base) {
  string res = ""; 
  while (num > 0) {
    res.append(to_string(num%new_base)); 
    num/=new_base;
  }
  reverse(res.begin(), res.end()); 
  return res;
}

int main() {
  long long numIt, base, start;
  cin >> numIt >> base >> start; 
  long long res = 0; 
  char target = base - 1 + '0';
  for (long long i = 0; i < numIt; i++) {
      string tmp = baseTenToN(baseNtoTen(start, base) + i, base);
      res += count(tmp.begin(), tmp.end(), target); 
  }
  
  cout << res << '\n'; 
  
  return 0;
}
