#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<conio.h>

int main()
{
  int a, b, c;
  clrscr();
  printf("Enter three sides of the triangle : ");
  scanf("%d %d %d", &a, &b, &c);

  if((a > 10) || (b > 10) || (c > 10)){
    printf("Out of range");
    getch();
    exit(0);
  }
  if((a<b+c)&&(b a+c)&&(c<a+b)){
    if((a==b)&&(b==c)){
      printf("Equilateral triangle");
    }
    else if((a!=b)&&(a!=c)&&(b!=c)){
      printf("Scalene triangle");
    }
  else
    printf("Isosceles triangle");
  }
  else {
    printf("triangle cannot be formed");
  }
  getch();
  return 0;
}