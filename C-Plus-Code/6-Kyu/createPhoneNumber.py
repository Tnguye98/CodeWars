#include <string>
#include <iostream>
using namespace std;

string createPhoneNumber(const int arr [10]){
  string ans = "(";
  int intToString;
  
  for (int i = 0; i != 10; i++){
    intToString = arr[i];
    if (i == 3){
      ans += ") ";
    } else if (i == 6){
      ans += "-";
    }
    ans += to_string(intToString);
  }
  return ans;
}