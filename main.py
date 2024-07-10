def check_length(pass1):
    points = 1
    pass_length = len(pass1)
    if pass_length <= 12:
        points += 1
    elif 13 <= pass_length <= 19:
        points += 2
    else:
        points += 3
    return points


def check_cap_num_char(pass2):
    points = 0
    caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_char = [",", ".", "/", "<", ">", "?", "!", "@", "#", "$", "%", "^",
                    "&", "*", "(", ")", "-", "_", "~", "`"]
    for i in pass2:
        if i in caps:
            points += 2
        elif i in num:
            points += 1
        elif i in special_char:
            points += 3
    return points


if "__main__" == __name__:
    again = "yes"
    repeat = ["yes", "ye", "y"]
    dismiss = ["no", "n"]
    while again in repeat:
        password = input("Enter a password: ")
        length = check_length(password)
        cap_num_char = check_cap_num_char(password)
        strength = length + cap_num_char
        if strength <= 10:
            print("Your password is weak")
            if length <= 2:
                print("You can improve your password by adding more characters")
            if cap_num_char <= 5:
                print("You can significantly improve your password by"
                      " adding more capitalized letters and special characters")
            if 6 <= cap_num_char <= 9:
                print("You can improve you password by adding more special characters")
        elif 11 <= strength <= 19:
            print("Your password is okay")
            if length <= 2:
                print("You can improve your password by adding more characters")
            if 6 <= cap_num_char <= 9:
                print("You can improve you password by adding more special characters")
        elif strength >= 20:
            print("Your password is strong, good job!")
        again = input("Would you like to check the strength of another password? ")
        again = again.lower()
        while again not in repeat and again not in dismiss:
            print("Invalid input, try again")
            again = input("Would you like to check the strength of another password? ")
            again = again.lower()


