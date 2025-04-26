import re
"""CRITERIA FOR PASSWORD [5]
Entered password should contain
1)length > 8, 2) at least 1 uppercase letter ,3) lowercase letters, 4) special character,and 5)digits """

def pass_strn_check(password):

    stren_criteria ={"Length": int(len(password)>=8) , "digit":int(bool(re.search(r"\d",password))),"upper":int(bool(re.search(r"[a-z]",password))) , "lower" : int(bool(re.search(r"[a-z]",password))) , "spl_char":int(bool(re.search(r"[^A-za-z0-9]",password))) }
    stren_score = sum(stren_criteria.values())
    
    
    if stren_score == 5:
        strength = "very strong"
    elif stren_score == 4:
        strength = "strong"
    elif stren_score ==3:
        strength="Moderate"
    elif stren_score==2:
        strength="weak"
    else:
        strength="very weak"

    feedback=""
    if not stren_criteria["Length"]:
        feedback+="password should be at least 8 characters \n"
    if not stren_criteria["digit"]:
        feedback+="password should contain atleast 1 digit \n"
    if not stren_criteria["upper"]:
        feedback+="password should contain atleast one uppercase \n "
    if not stren_criteria["lower"]:
        feedback+="password should also contain loer case letters \\n "
    if not stren_criteria["spl_char"]:
        feedback+="password should contain atleast one special character \n"
    return f"password feedback : \n\t password strength = {stren_score} \n\t Feedback : \n"+feedback    

if __name__ == "__main__":
    password = input("Enter your password : ")
    print(pass_strn_check(password))

