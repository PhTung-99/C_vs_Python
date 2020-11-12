#include <iostream>
#include <ctime> // time_t
#include <cstdio>
 
bool check(int n){
    if(n%4==0)
        return true;
    else
        return false;
}
void function(){
    int i=0,n=2020;
    while(i<=1000)
    {
        
        if(check(n)==true)
        {
            //printf("******************************************");
            printf("\n%d ",n);
            i++;
        }

        n++;
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

