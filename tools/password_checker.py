def check_password(password):
    score = 0 

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()-+" for char in password):
        score += 1

    #strength evaluation    
    if score <= 2:
        return f"Score: {score}/5 -> Weak"
    elif score == 3 or score == 4:
        return f"Score: {score}/5 -> Moderate"
    else:
        return f"Score: {score}/5 -> Strong"