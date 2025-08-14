/* This is a sample C program to test lexical analyzer
   It contains various tokens, operators, and syntax elements
*/

#include <stdio.h>

int main() {
    // Variable declarations with different data types
    int number1 = 42;
    float pi = 3.14159;
    char letter = 'A';
    
    // Array declaration
    int array[10];
    
    // Arithmetic operations
    int sum = number1 + 58;
    float result = pi * 2.0;
    
    // Logical operations and control structures
    if (number1 >= 40 && number1 <= 50) {
        while (sum > 50) {
            sum -= 5;    // Compound assignment
        }
    } else {
        sum = 0;
    }
    
    // Function call with multiple parameters
    printf("Result: %d\n", sum);
    
    // For loop with different operators
    for (int i = 0; i < 10; i++) {
        array[i] = i * 2;
        if (array[i] == 10 || array[i] == 12) {
            continue;
        }
    }
    
    return 0;
}