// lucky number  
// sum of first half digits=sum of second half digits
// no of digits should be even
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int n;
    cin>>n;
    int temp=n;
    int len=0;
    while (temp>0)
    {
        len++;
        temp/=10;

    }
    int halflength=len/2;
    int first=0;
    int second=0;
    while (halflength>0)
    {
        int r=n%10;
        second+=r;
        halflength--;
        n/=10;


    }
    int halflength2=len/2;
    while (halflength>0)
    {
        int r=n%10;
        first+=r;
        halflength--;
        n/=10;


    }
    if (first==second)
    {
        cout<<"yes lucky";

    }
    else{
        cout<<"Not lucky";
        
    }
    
    return 0;
}


