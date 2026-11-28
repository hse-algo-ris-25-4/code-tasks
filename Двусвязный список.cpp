#include <algorithm>
#include <cstddef>
#include <iostream>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::size_t;

template<typename T>
class deque {
  struct Node {
    Node* prev;
    Node* next;
    T value;
  };

  Node* head = nullptr;
  Node* tail = nullptr;
  size_t size = 0;
  
public:
  deque() = default;

  deque(const deque& other) : deque() {
    for (const Node* node = other.head; node != nullptr; node = node->next) {
      push_back(node->value);
    }
  }

  deque& operator=(const deque&) = delete;

  class Iterator {
    Node* current = nullptr;
  public:

    Iterator& operator++() {
      current = current->next;
      return *this;
    }

    bool operator!=(const Iterator& other) const {
      return this->current != other.current;
    }

    T& operator*() {
      return current->value;
    }
    explicit Iterator(Node* node) : current(node) {} // explicit означает, что C++ не будет автоматически превращать Node* в Iterator
  };

  Iterator begin() {
    return Iterator(head);
  }

  Iterator end() {
    return Iterator(nullptr);
  }

  void push_back(const T& value) {
    Node* new_node = new Node{ nullptr, nullptr, value };
    if (tail != nullptr) {
      tail->next = new_node;

      new_node->prev = tail;
      tail = new_node;
    } else {
      head = new_node;
      tail = new_node;
    }
    ++size;
  }

  void pop_back() {
    if (size > 0) {
      Node* old_tail = tail;
      tail = old_tail->prev;
      if (size >= 2) {
        tail->next = nullptr;
      } else {
        head = nullptr;
      }
      delete old_tail;
      --size;
    }
  }

  void pop_front() {
    if (size > 0) {
      Node* old_head = head;
      head = old_head->next;
      if (size >= 2) {
        head->prev = nullptr;
      } else {
        tail = nullptr;
      }
      delete old_head;
      --size;
    }
  }

  void push_front(const T& value) {
    Node* new_node = new Node{ nullptr, nullptr, value };
    if (head != nullptr) {
      head->prev = new_node;

      new_node->next = head;
      head = new_node;
    } else {
      head = new_node;
      tail = new_node;
    }
    ++size;
  }

  ~deque() {
    while (size > 0) {
      pop_back();
    }
  }
};


int main() {
  std::ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  deque<int> nums;
  int n;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    int value;
    cin >> value;
    nums.push_back(value);
  }

  deque<int> copy = nums;
  copy.pop_back();

  for (auto it = nums.begin(); it != nums.end(); ++it) {
    cout << *it << ' ';
  }
  cout << '\n';

  for (auto it = copy.begin(); it != copy.end(); ++it) {
    cout << *it << ' ';
  }
  cout << '\n';
}
