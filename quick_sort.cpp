#include<bits/stdc++.h>

using namespace std;

int partition(int a[], int low,int high)
{
	int pivot=a[high];
	int i=low-1;

	for(int j=low;j<=high-1;j++)
	{
		if(a[j]<=pivot)
		{
			i++;
			int temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}
	
	i++;
	a[high]=a[i];
	a[i]=pivot;

	return i;

}

void quicksort(int arr[],int low,int high)
{
	if(low<high)
	{
		int p=partition(arr,low,high);
		quicksort(arr, low, p - 1); 
        	quicksort(arr, p + 1, high);
	} 
}

int main()
{
	int n,temp;
	cout<<"\nEnter number of elements: ";
	cin>>n;
	int a[n];
	cout<<"\nEnter elements: ";
	for(int i=0;i<n;i++)
		cin>>a[i];

	quicksort(a,0,n-1);
	cout<<"\n";
	for(int i=0;i<n;i++)
		cout<<a[i]<<" ";

}
		
