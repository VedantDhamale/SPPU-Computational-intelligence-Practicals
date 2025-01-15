import rpyc

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 18861)
    num = int(input("Enter an integer to calculate its factorial: "))
    result = conn.root.calculate_factorial(num)
    print(f"The factorial of {num} is {result}")