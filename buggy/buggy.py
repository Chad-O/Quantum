def add_numbers(a, b):
  return a + b

def main():
  # This line will raise a TypeError because `a` and `b` are not numbers.
  result = add_numbers("1", "2")

if __name__ == "__main__":
  main()