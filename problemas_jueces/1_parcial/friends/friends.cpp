#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define MAXN 30000

     int id [MAXN];  
     int sz [MAXN];   
     int conCom;  

    void init(int N) {
        conCom = N;
        for (int i = 0; i < N; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

   
    int find(int p) {
        while (p != id[p])
            p = id[p];
        return p;
    }


    bool connected(int p, int q) {
        return find(p) == find(q);
    }


  
    void makeUnion(int p, int q) {
        int i = find(p);
        int j = find(q);
        if (i == j) return;

    
        if   (sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i]; }
        else                 { id[j] = i; sz[i] += sz[j]; }
        conCom--;
    }

int main()
{
        int n,m,a,b,i,test;
        scanf("%d",&test);
        while(test--){
        scanf("%d %d",&n,&m);
        init(n);
        
        for(i=0;i<m;i++)
        {
            scanf("%d %d",&a,&b);
            a--;b--;
            makeUnion(a, b);

        }
        printf("%d\n",*max_element(sz,sz+n));
        }
    return 0;
}