#include <iostream>
#include <ctime> // time_t
#include <cstdio>

int Fibonacci(int n)
{
    if (n == 1 || n == 2)
        return 1;
    return Fibonacci(n - 1) + Fibonacci(n - 2);
}

void function(){
    int i=1;
    while(i<45)
    {
        i++;
        printf("\n%d",Fibonacci(i));
    }

}
int main()
{
	clock_t tic = clock();
	function();
	clock_t toc = clock();
	printf("\n%f", (double)(toc - tic) / CLOCKS_PER_SEC);
 
 
return 0;
}

