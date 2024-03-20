#include <iostream>
#include <stdio.h>

using namespace std;

long int fib(long int num){
    if(num == 0){
        return 0;
    }else if(num == 1){
        return 1;
    }
    return fib(num - 1) + fib(num - 2);
}

int main(int argc, char *argv[]){
    const char *in = argv[1];
    long int num;
    sscanf(in, "%d", &num);
    cout << num << ":\t";
    cout << fib(num) << endl;
    return 0;
}
