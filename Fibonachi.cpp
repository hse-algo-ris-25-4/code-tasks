#include <iostream>
#include <vector>
using namespace std;

int Fibonacci_rec(int n) {
  if (n == 0) {
    return 1;
  }
  if (n == 1) {
    return 1;
  }
  return Fibonacci_rec(n - 1) + Fibonacci_rec(n - 2);
}

int Fibonacci_iter(int n) {
  vector<int> nums(n + 1, 0);
  nums[0] = 1;
  nums[1] = 1;
  for (int i = 2; i <= n; ++i) {
    nums[i] = nums[i - 1] + nums[i - 2];
  }
  return nums[n];
}

int Fibonacci(int n) {
  if (n == 1 || n == 0) {
    return 1;
  }
  int a = 1;
  int b = 1;
  int res = 0;
  for (int i = 2; i <= n; ++i) {
    res = a + b;
    a = b;
    b = res;
  }
  return res;
}

int main() {
  setlocale(LC_ALL, "Russian");
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  cout << "Рекурсивно: " << Fibonacci_rec(n) << "\n";
  cout << "Итеративно: " << Fibonacci_iter(n) << "\n";
  cout << "Итеративно без массива: " << Fibonacci(n) << "\n";

}
