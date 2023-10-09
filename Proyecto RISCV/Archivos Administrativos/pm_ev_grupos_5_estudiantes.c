#include <stdio.h>

int main(){
  int *r = 0xABCD;
  int a[5] = {};
  int c = 14;
  int b = 7;

  a[0] = c+b;
  a[1] = c<<b;
  a[2] = c-a[1];
  a[3] = c & 0x0F;
  a[4] = c^b;

  //printf("Result in order %d %d %d %d %d\n", a[0], a[1], a[2], a[3], a[4]);
}
