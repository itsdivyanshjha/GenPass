import random
import string

def generate_password(length=12):
    # Define the characters that will be used in the password
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(chars))
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password)
    
    # Join the characters into a single string
    return ''.join(password)

# Example usage
print(generate_password())

#Divyansh Jha Poll SCM Build
