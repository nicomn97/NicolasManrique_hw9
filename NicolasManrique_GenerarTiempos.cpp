#include <iostream>
#include <math.h>
#include <ctime>

using namespace std;


int fibonacci (int N);

float get_time(int N);

int main () {
    for(int i = 0; i<35;i+=1){
       cout << i;
       cout << ",";
       cout << get_time(i); 
       cout << "\n";
   }
   return 0;
}



int fibonacci(int N) {

   if(N==0){
      return 0;
    }  
   else if(N==1){
      return 1;
    }
   else{
      return fibonacci(N-1)+fibonacci(N-2);

   }
}


float get_time(int N){

    clock_t t;
    t=clock();
    fibonacci(N);
    t=clock()-t;
    float time = ((float)t)/CLOCKS_PER_SEC;
    return time;

}


