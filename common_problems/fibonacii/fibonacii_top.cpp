/*
only works until the 92nd in the series due to limitations of long int
run 
g++ fibonacii_top.cpp -Wall -g -o fib

*/

#include <iostream>
#include <stdio.h>

using namespace std;

long int fib(long int num, long int visited[]){
    if(num == 0){
        return 0;
    }else if(num == 1){
        return 1;
    }else if(visited[num] != 0){
        return visited[num];
    }
    visited[num] = fib(num - 1, visited) + fib(num - 2, visited);
    return fib(num - 1, visited) + fib(num - 2, visited);
}

int main(int argc, char *argv[]){
    const char *in = argv[1];
    long int num;
    sscanf(in, "%ld", &num);
    cout << "\0";
    long int* visited = (long int*) malloc(sizeof(long int)*(num + 1));
    for(long int v = 0; v <= num; v++){
        visited[v] = 0;
    }
    cout << visited[num] << endl;
    cout << num << ":\t";
    cout << fib(num, visited) << endl;
    free(visited);
    return 0;
}
