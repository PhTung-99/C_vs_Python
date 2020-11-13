#include <iostream>
#include <ctime> // time_t
#include <cstdio>

int Fibonacci(int n)
{
	if (n< 0) return -1;
    if (n == 0 || n == 1)
        return n;
    return Fibonacci(n - 1) + Fibonacci(n - 2);
}

void function(){
    int i=0;
    while(i<45)
    {
        printf("\n%d",Fibonacci(i));
        i++;
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

