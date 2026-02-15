// COMPILE: $ gcc libcalc.c -lm

#include<math.h>
#include<stdio.h>
#include<stdlib.h>

// SINGLE VARIABLE CALCULUS

double function(double x) {
        return x; // ARBITRARY FUNCTION USED BY INTEGRAL & DERIVATIVE s
}

double f(double x) {
        return function(x); 
}


// simpson's rule with 10^-6 given the function takes one parameter and has a one char name e.g. double f(int x)
double integral(double a, double b) {
        double accuracy = 8; // the power of 10 used for step size (10^-accuracy) and number of steps (10^accuracy)
        if (a > b) return integral(b, a); 
        if (b == a) return 0; 
        double numSteps = (b - a) * pow(10, accuracy); 
        double stepSize = pow(10, -accuracy); 
        double r = ((b-a)/(3*numSteps)); 
        double t = f(a) + f(b); 
        int counter = 0; 
        double h = r*3; 
        for (double i = stepSize; i < numSteps - 1; i++) {
                double s = (2*f(a + i*h));
                if (counter%2 == 1) s *= 2; 
                t += s; 
                counter++; 
                printf("\rIteration %lf -> %lf", i, t*r); 
        }
        printf("\r\r\r"); 
        return t*r; 
}

double derivative(double a) {
        double h = pow(10, -8); 
        return (f(a+h) - f(a))/h;
}


int main() {
        printf("f(x) = x^2\n");
        printf("Integral of f(x) from 0 to 1 = %lf\n", integral(0, 1)); 
        printf("Derivative of f(x) at -2 = %lf\n", derivative(-2));
        return 0; 
}