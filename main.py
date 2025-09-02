def add_numbers(a,b):
    return a+b

def subtract_numbers(a,b):
    return a-b

def multiply_numbers(a,b):
    return a*b

def divide_numbers(a,b):
    if b != 0:
        return a/b
    else:
        return None

def main():
    x = 10
    y = 5

    sum_result = add_numbers(x,y)
    print("Sum:", sum_result)

    sub_result = subtract_numbers(x,y)
    print("Subtraction:", sub_result)

    mul_result = multiply_numbers(x,y)
    print("Multiplication:", mul_result)

    div_result = divide_numbers(x,y)
    if div_result is not None:
        print("Division:", div_result)
    else:
        print("Cannot divide by zero")

    # More calculations 
    numbers = [1,2,3,4,5]
    squared_numbers = [n**2 for n in numbers]
    print("Squared numbers:", squared_numbers)

    for n in numbers:
        print("Number:", n)

if __name__ == "__main__":
    main()
