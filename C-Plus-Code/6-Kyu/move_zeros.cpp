#include <vector>

std::vector<int> move_zeroes(const std::vector<int>& input) {
  std::vector<int> ans;
  int numOfZeroes = 0;
  
  for (int i = 0; i < input.size(); i++){
    if (input.at(i) == 0)
      numOfZeroes+=1;
    else
      ans.push_back(input.at(i));
  }
  
  for (int i = 0; i != numOfZeroes; i++){
    ans.push_back(0);
  }
  return ans;
  
}
