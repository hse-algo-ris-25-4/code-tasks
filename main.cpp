#include <iostream>
#include <iomanip>
#include <vector>
#include <random>
using namespace std;

long long Calculate_determinant(const vector<vector<long long>>& nums) {
  if (nums[0].size() == 1) {
    return nums[0][0];
  }
  if (nums[0].size() == 2) {
    return nums[0][0] * nums[1][1] - nums[0][1] * nums[1][0];
  }
  if (nums[0].size() == 3) {
    return nums[0][0] * nums[1][1] * nums[2][2] +
      nums[1][0] * nums[2][1] * nums[0][2] +
      nums[0][1] * nums[1][2] * nums[2][0] -

      nums[0][2] * nums[1][1] * nums[2][0] -
      nums[0][1] * nums[1][0] * nums[2][2] -
      nums[0][0] * nums[2][1] * nums[1][2];
  }

  long long sum = 0;
  
  for (size_t q = 0; q < nums.size(); ++q) {
    vector<vector<long long>> arr(nums.size() - 1, vector<long long>(nums.size() - 1, 0));
    size_t k_str = 0;
    size_t h_stolb = 0;
    for (size_t i = 1; i < nums.size(); ++i) {
      for (size_t j = 0; j < nums.size(); ++j) {
        if (j != q) {
          arr[k_str][h_stolb] = nums[i][j];
          if (h_stolb == arr.size() - 1) {
            h_stolb = 0;
            ++k_str;
          } else {
            ++h_stolb;
          }
        }
      }
    }
    int znak;
    (q % 2 == 0 ? znak = 1 : znak = -1);
    if (nums[0][q] != 0) {
      sum += nums[0][q] * znak * Calculate_determinant(arr);
    }
  }
  return sum;
}

vector<vector<long long>> Generate_matrix_and_det(long long n, long long det) {

  long long x = -20;
  long long y = 20;
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<long long> dist(x, y);

  vector<vector<long long>> matrix(n, vector<long long>(n, 0));
  matrix[0][0] = det;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (i == 0 && j == 0) {
        continue;
      }
      if (i == j) {
        matrix[i][j] = 1;
      } else if (j > i) {
        matrix[i][j] = dist(gen);
      } else {
        matrix[i][j] = 0;
      }
    }
  }

  for (int i = 1; i < n; ++i) {
    long long num = dist(gen);
    for (int j = 0; j < n; ++j) {
      matrix[i][j] += matrix[0][j] * num;
    }
  }
  return matrix;
}

int main() {
  setlocale(LC_ALL, "Russian");
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cout << "Введите число n - размер матрицы ";
  cin >> n;
  /*if (n > 0) {
    vector<vector<long long>> nums(n, vector<long long>(n, 0));
    for (size_t i = 0; i < n; ++i) {
      for (size_t j = 0; j < n; ++j) {
        cin >> nums[i][j];
      }
    }
    cout << "Определитель равен = " << Calculate_determinant(nums) << "\n";
  } else {
    cout << "Вы ввели n <= 0\n";
  }
  cout << "\n---------------\n";*/

  cout << "Введите определитель ";
  long long det;
  cin >> det;
  vector<vector<long long>> matrix = Generate_matrix_and_det(n, det);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cout << setw(4) << matrix[i][j];
    }
    cout << "\n";
  }
}
