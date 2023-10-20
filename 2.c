#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

int main(){
	printf("All prime Values Are: "); 
	bool *arr = malloc(sizeof(bool)*101);
	for(int i = 2 ; i<101; i++){
		if(!arr[i]){
			printf("%d\t",i);	
			for(int j = 1 ; j*i<101;j++)
				arr[j*i] = true;
		}
	}
	free(arr);
}
