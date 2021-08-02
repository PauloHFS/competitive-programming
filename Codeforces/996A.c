#include <stdio.h>
#include <stdlib.h> 

int main(int argc, char const *argv[])
{
    int n = 0, bills = 0;
    scanf("%i", &n);
    while (n/100 != 0)
    {
        n = n - 100;
        bills++;
    }
    while (n/20 != 0)
    {
        n = n - 20;
        bills++;
    }
    while (n/10 != 0)
    {
        n = n - 10;
        bills++;
    }
    while (n/5 != 0)
    {
        n = n - 5;
        bills++;
    }
    while (n/1 != 0)
    {
        n = n - 1;
        bills++;
    }
    printf("%i", bills);
    return 0;
}
