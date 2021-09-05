#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

#define nodesize 100001     //节点个数     
#define dictsize 128        //字符集大小     

//trie
typedef struct node1  
{    
    int    flag;            //值域     
    node1* next[dictsize];    
}tnode;    
tnode dict[nodesize];  
  
class Trie    
{    
    private:  
        int    size;
        tnode* root;    
    public:    
        Trie() {initial();}    
        void initial() {    
            memset(dict, 0, sizeof(dict));    
            size = 0;  	 root = newnode();    
        }
        tnode* newnode() {return &dict[size ++];}    
        int insert(char* word) {    
            tnode* now = root;    
            for (int i = 0 ; word[i] ; ++ i) {  
                if (!now->next[word[i]])    
                    now->next[word[i]] = newnode(); 
                now = now->next[word[i]];
                if (now->flag) return 1;
            }now->flag = 1;
            for (int i = 0 ; i < dictsize ; ++ i)
            	if (now->next[i])
            		return 1;
            return 0;
        }
}trie;    
//trie end

int main()
{
	int t,n;
 	char buf[12];
	while (~scanf("%d",&t))
	while (t --) {
		trie.initial();
		scanf("%d",&n);
		int flag = 0;
		for (int i = 0 ; i < n ; ++ i) {
			scanf("%s",buf);
			if (trie.insert(buf))
				flag = 1;
		}
	
		if (flag)
			printf("NO\n");
		else printf("YES\n");
	} 
    return 0;
}