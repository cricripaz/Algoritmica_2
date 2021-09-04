#include <bits/stdc++.h> 
#define input freopen("in.txt", "r", stdin)
#define output freopen("out.txt", "w", stdout)
using namespace std;

int v[10000];
int parent[10000];
int rango[10000];
int sons[10000];

int n;
void init() {
    for(int i=0;  i<= n; i++) {
        parent[i] = i;
        rango[i] = 0;
        sons[i] = 1;
    }
}

int find(int x) {
    if(x == parent[x]) {
        return x;
    }
    else {
        parent[x] = find(parent[x]);
        return parent[x];
    }
}

void unionRango(int x,int y) { 
    int xRaiz = find(x);
    int yRaiz = find(y);
    if(xRaiz == yRaiz ) 
        return;

    if(rango[xRaiz] > rango[yRaiz]) {
        parent[yRaiz] = xRaiz;
        sons[xRaiz] = sons[xRaiz] + sons[yRaiz];
    } else {
        parent[xRaiz] = yRaiz;
        if(rango[xRaiz] == rango[yRaiz]) {
            rango[yRaiz]++;
        }
        sons[yRaiz] = sons[xRaiz] + sons[yRaiz];
    }
}

int main() {
    input;
    int x; 
    cin>>x; 
    int nUnion;
    
    
    
    while(x--) {
    
    cin>>n>>nUnion;
     
    map<int,string> names;
    
    map<string,int> numbers;




    for(int i=1;i<=n;i++) {
        string name;
        cin>>name;
        names[i] = name;
        numbers[name] = i;
    }

    init();

    while(nUnion--) {
        string x,y;
        cin>>x>>y; 

        unionRango(numbers[x],numbers[y]);
    }

    int personaConCovid;
    
    cout<<sons[parent[find(personaConCovid)]]-1<<endl;
    return 0;
}