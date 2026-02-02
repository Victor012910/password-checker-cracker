import string 

def score_password(password: str) -> dict:
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if len(password) >= 8:
        score += 1
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    
    return {
        "length": len(password),
        "has_lower": has_lower,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "score_0_5": score
    }

def strength_feedback(password: str) -> list:

    feedback = []
    if len(password) < 8:
        feedback.append("Password is too short (Use at minumum 8 characters)")
    if not any(c.islower() for c in password):
        feedback.append("Add lowercase letters")
    if not any(c.isupper() for c in password):
        feedback.append("Add uppercase letters")
    if not any(c.isdigit() for c in password):
        feedback.append("Add numbers")
    if not any(c in string.punctuation for c in password):
        feedback.append("Add symbols (e.g. ! @ #).")

    if not feedback:
        feedback.append("Password meets basic requirements")

    return feedback   


    


