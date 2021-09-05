#include <bits/stdc++.h>
using namespace std;
 
const int N=100005;
int arr[N];
int gcd(int a,int b)
{
    {int t;while(b){a=a%b;t=a;a=b;b=t;}return a;}
}
struct segment{
    int _gcd;
    int _count;
    segment(){
        _gcd=0;
        _count=0;
    }
    segment(int val)
    {
        _gcd=val;
        _count=1;
    }
    void mergee(segment left,segment right)
    {
        _count=0;
       _gcd=gcd(left._gcd,right._gcd);
       if(_gcd==left._gcd)
       {
           _count+=left._count;
       }
       if(_gcd==right._gcd)
       {
           _count+=right._count;
       }
    }
}seg[4*N];
 
void build(int low,int high,int node)
{
    if(low>high)
    return;
    if(low == high)
    {
        seg[node]=segment(arr[low]);
        return;
    }
    int mid=low+high>>1;
    build(low,mid,2*node+1);
    build(mid+1,high,2*node+2);
    seg[node].mergee(seg[2*node+1],seg[2*node+2]);
}
 
segment query(int low,int high,int lq,int hq,int node)
{
    if(low>high||low>hq||high<lq)
    return segment();
    if(lq<=low && high<=hq)     {         return seg[node];     }     int mid=low+high>>1;
    segment temp=segment();
    temp.mergee(query(low,mid,lq,hq,2*node+1),query(mid+1,high,lq,hq,2*node+2));
    return temp;
 
}
 
int main() {
    int n;
    scanf("%d",&n);
    register int i;
    for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
    build(0,n-1,0);
    int t,l,r;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&l,&r);
        printf("%d\n",(r-l+1)-query(0,n-1,l-1,r-1,0)._count);
    }
 
    return 0;
}