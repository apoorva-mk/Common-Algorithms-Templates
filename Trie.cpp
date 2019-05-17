#include<bits/stdc++.h>
using namespace std;

const int ALPHABET_NUMBER = 26;


struct TrieNode
{
	struct TrieNode *adjacent[ALPHABET_NUMBER];
	bool isEnd;
			
};

struct TrieNode * getEmptyNode()
{	
	struct TrieNode * newNode = new TrieNode;

	for(int i=0; i<ALPHABET_NUMBER; i++)
	{
		newNode->adjacent[i] = NULL;
	} 

	newNode->isEnd = false;

	return newNode;
}

void insert(struct TrieNode *root, string element)
{
	struct TrieNode *pointer = root;

	for(int i=0; i<element.length(); i++)
	{
		if(!pointer->adjacent[element[i]-'a'])
			pointer->adjacent[element[i]-'a'] = getEmptyNode();

		pointer = pointer->adjacent[element[i]-'a'];
	}

	pointer->isEnd = true;
} 

bool search(struct TrieNode *root, string element)
{
	struct TrieNode *pointer = root;
	
	for(int i=0; i<element.length(); i++)
	{
		if(!pointer->adjacent[element[i]-'a'])
			return false;

		pointer = pointer->adjacent[element[i]-'a'];
	}

	cout<<pointer->isEnd<<" "<<pointer;

	if(pointer->isEnd==true)
		cout<<"is end true";
	return (pointer!=NULL && pointer->isEnd);
}

int main()
{
	struct TrieNode *root = getEmptyNode();
	string keys[] = {"the", "a", "there", 
                    "answer", "any", "by", 
                     "bye", "their" }; 
	
	
	for (int i=0;i<8;i++)
	{
		insert(root,keys[i]);
	}

	search(root,"a")?cout<<"yes":cout<<"no";
	search(root, "the")? cout << "Yes\n" : 
                         cout << "No\n"; 
    search(root, "these")? cout << "Yes\n" : 
                           cout << "No\n"; 

	return 0;
}