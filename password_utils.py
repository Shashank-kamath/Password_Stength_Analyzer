import re

def analyze_password(password):
    length = len(password)
    lower = bool(re.search(r'[a-z]', password))
    upper = bool(re.search(r'[A-Z]', password))
    digit = bool(re.search(r'\d', password))
    special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    strength = 0
    if length >= 8:
        strength += 1
    if lower:
        strength += 1
    if upper:
        strength += 1
    if digit:
        strength += 1
    if special:
        strength += 1
    
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_description = strength_levels[strength - 1] if strength > 0 else "Very Weak"
    
    return {
        "length": length,
        "lower": lower,
        "upper": upper,
        "digit": digit,
        "special": special,
        "strength": strength_description
    }
