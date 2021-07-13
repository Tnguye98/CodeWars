#include <math.h>
int predictAge(int age1, int age2, int age3, int age4, int age5, int age6, int age7, int age8)
{
  int listOfAges[8] = {age1, age2, age3, age4, age5, age6, age7, age8};
  int ans = 0;

  
  for (int loop = 0; loop != 8; loop ++){
    ans += (listOfAges[loop] * listOfAges[loop]);
  }
  ans = floor(sqrt(ans)/2);
  return ans;
  
}