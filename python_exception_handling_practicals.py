# 1: Age Verification System

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    print("Valid age:", age)

except ValueError as e:
    print("Error:", e)

# 2: Product Price Checker

try:
    price = int(input("Enter product price: "))

    if price < 0:
        raise ValueError("Price cannot be negative.")

    print("Product price:", price)

except ValueError as e:
    print("Error:", e)

# 3: Tuple Element Access

try:
    cities = ("Prayagraj", "Lucknow", "Kanpur", "Varanasi",
              "Delhi", "Jaipur", "Mumbai")

    print("Cities:", cities)
    position = int(input("Enter city position (0-6): "))

    print("City:", cities[position])

except IndexError:
    print("Error: Invalid position.")

except ValueError:
    print("Error: Please enter an integer.")

# 4: Contact Information Lookup

try:
    contacts = {
        "Aman": "9876543210",
        "Riya": "9876543211",
        "Rahul": "9876543212"
    }

    name = input("Enter contact name: ")
    print("Phone number:", contacts[name])

except KeyError:
    print("Error: Contact not found.")

# 5: File Writing Operation

try:
    filename = input("Enter filename: ")
    text = input("Enter text to write: ")

    with open(filename, "w") as file:
        file.write(text)

    print("Text written successfully.")

except PermissionError:
    print("Error: Permission denied.")

# 6: Valid Roll Number Input

while True:
    try:
        roll_number = int(input("Enter roll number: "))

        if roll_number > 0:
            print("Valid roll number:", roll_number)
            break
        else:
            print("Roll number must be greater than zero.")

    except ValueError:
        print("Error: Enter a valid integer.")

# 7: Custom Exception for Voting Eligibility

class NotEligibleToVoteError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise NotEligibleToVoteError(
            "You are not eligible to vote."
        )

    print("You are eligible to vote.")

except NotEligibleToVoteError as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid age.")

# 8: Bank Account Deposit Validation

try:
    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    print("Deposit successful.")
    print("Deposited amount:", amount)

except ValueError as e:
    print("Error:", e)

# 9: Shopping Cart Quantity Check

try:
    quantity = int(input("Enter item quantity: "))

    if quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    print("Quantity:", quantity)

except ValueError as e:
    print("Error:", e)

# 10: Password Strength Validator

try:
    password = input("Enter your password: ")

    if len(password) < 8:
        raise ValueError(
            "Password must be at least 8 characters long."
        )

    print("Password is valid.")

except ValueError as e:
    print("Error:", e)