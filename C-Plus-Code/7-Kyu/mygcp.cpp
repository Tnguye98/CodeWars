long long mygcd(long long a, long long b) {
   if (b == 0)
    return a;
   return mygcd(b, a % b);
}
