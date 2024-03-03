// Task 1: Function to add two numbers
double addTwo(double num1, double num2) {
  return num1 + num2;
}

// Task 2: Function to subtract two numbers
double subtractTwo(double num1, double num2) {
  return num1 - num2;
}

// Task 3: Function to multiply two numbers
double multiplyTwo(double num1, double num2) {
  return num1 * num2;
}

// Task 4: Function to divide two numbers
double divideTwo(double num1, double num2) {
  if (num2 == 0) {
    throw Exception('Cannot divide by zero');
  }
  return num1 / num2;
}

// Task 5: Function to get the length of a string
int stringLength(String str) {
  return str.length;
}

// Task 6: Function to get the first element of a list
dynamic getFirstElement(List list) {
  if (list.isEmpty) {
    return null;
  }
  return list[0];
}

void main() {
  // Testing the functions
  print('Task 1: ${addTwo(10, 5)}'); // Output: 15
  print('Task 2: ${subtractTwo(10, 5)}'); // Output: 5
  print('Task 3: ${multiplyTwo(10, 5)}'); // Output: 50
  print('Task 4: ${divideTwo(10, 5)}'); // Output: 2
  print('Task 5: ${stringLength("Dart")}'); // Output: 4
  print('Task 6: ${getFirstElement([1, 2, 3])}'); // Output: 1
}

