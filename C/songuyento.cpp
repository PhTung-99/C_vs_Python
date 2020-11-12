#include <iostream>
#include <math.h>
#include <ctime> // time_t
#include <cstdio>
 
bool check(int n){
    if(n < 2){
        return false;
    }
    int count = 0;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0){
            count++;
        }
    }
    if(count == 0){
        return true;
    }else{
        return false;
    }
}
void function(){
        int i=0,n=0;
    while(i<=1000)
    {
        
        if(check(n)==true)
        {
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

