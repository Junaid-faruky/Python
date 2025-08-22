def safe_division():
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Division operation completed")

safe_division()
