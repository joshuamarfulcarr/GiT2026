import string
def check_password(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    if any(c.islower() for c in password):
        score += 1
    else:        feedback.append("Password should include at least one lowercase letter.")
    if any(c.isdigit() for c in password):            
        score += 1
    else:
        feedback.append("Password should include at least one digit.")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")
    if score == 4:
        label = "Strong"
    elif score == 3:
        label = "Moderate"
    else:
        label = "Weak"
    return label, feedback    
    
    
password= input("Enter your password:")
label, feedback = check_password(password)
print(f"Password strength: {label}")
print(f"Password strength: {feedback}")
