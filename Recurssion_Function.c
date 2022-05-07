#include <stdio.h>
int main()
{
    int sum_of_digits(int n);
    int n, sum;
    printf("Enter any number to find sum of digits: ");
    scanf("%d", &n);
    sum = sum_of_digits(n);
    printf("Sum of digits of %d: %d", n, sum);
    return 0;
}

int sum_of_digits(int n)
{
    if(n==0)
        return 0;  
    return ((n%10) + sum_of_digits(n/10));
}
