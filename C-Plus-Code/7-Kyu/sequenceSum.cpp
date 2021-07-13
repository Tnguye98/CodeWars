int sequenceSum(int start, int end, int step)
{
  int ans = 0;
  for (int i = start; i < end + 1; i += step){
    ans += i;
  }
  return ans;
}