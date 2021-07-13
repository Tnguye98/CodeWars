namespace Triangle
{
  bool isTriangle(int a, int b, int c){
  int listOfNum[] = {a, b, c};
  for (int i = 0; i != 3;i++){
    if (listOfNum[i] <= 0){
      return false;
    }
    switch (i){
      case 0:
        if (a >= long(long(b) + long(c))){
          return false;
        }
      case 1:
        if (b >= (long(a) + long(c))){
          return false;
        }
      case 2:
        if (c >= (long(a) + long(b))){
          return false;
        }
    }
  }
  return true;
}
  }