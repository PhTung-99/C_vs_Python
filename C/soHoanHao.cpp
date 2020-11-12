#include <iostream>
#include <ctime> // time_t
#include <cstdio>
 
bool check(int n){
    int sum = 0;//khai bao biem sum
    for(int i=1;i<=n/2;i++){
        if(n%i==0) 
            sum+=i;
    }
    if(sum==n) return true; // tra ve true
    return false;
}
void function(){
        int i=0,n=0;
    while(i<=100)
    {
        
        if(check(n)==true)
        {
            printf("\n%d ",n);
            i++;
        }

        n++;
        if(n==100000)
            break;
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

