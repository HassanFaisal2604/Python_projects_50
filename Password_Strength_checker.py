def check_password_strength(password):
    criteria = {
        "Has digits": any(char.isdigit() for char in password),
        "Has uppercase": any(char.isupper() for char in password),
        "Sufficient length": len(password) >= 8
    }
    
    print("Password criteria:")
    for criterion, is_met in criteria.items():
        print(f"- {criterion}: {'Yes' if is_met else 'No'}")
    
    is_strong = all(criteria.values())
    print(f"\nPassword strength: {'Strong' if is_strong else 'Weak'}")
    
    return is_strong

# Main program
password = input("Enter your password: ")
check_password_strength(password)