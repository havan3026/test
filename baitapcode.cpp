#include <stdio.h>
int main(){
    int n,a,b; //tổng số đề làm mỗi tuần, số đề Facker sẽ làm và số đề Jack sẽ làm.
    scanf("%d %d %d",&n,&a,&b);
    int arr[n];
    for(int i=0;i<n-1;i++)
        scanf("%d",&arr[i]);
        {
            for (int j= 0 ; j<n-1; j++)
            {
            if(a[j]>a[j+1])
                {
            int tmp
            tmp=a[j]
            a[j]=a[j+1];
            a[j+1]=tmp
                }
            }
        }
    return 0;
}