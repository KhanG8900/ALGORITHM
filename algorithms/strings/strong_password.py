"""
The signup page required her to input a name and a password. However, the password
must be strong. The website considers a password to be strong if it satisfies the following criteria:

1) Its length is at least 6.
2) It contains at least one digit.
3) It contains at least one lowercase English character.
4) It contains at least one uppercase English character.
5) It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong.
Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

Input Format
The first line contains an integer  denoting the length of the string.
The second line contains a string consisting of  characters, the password
typed by Louise. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Sample Input 1: strong_password(3,"Ab1")
Output: 3 (Because She can make the password strong by adding  characters,for example, $hk, turning the password into Ab1$hk which is strong.
2 characters aren't enough since the length must be at least 6.)

Sample Output 2: strong_password(11,"#Algorithms")
Output: 1 (Because the password isn't strong, but she can make it strong by adding a single digit.)

"""
branch_coverage = {
    "strong_password_1": False,  # if branch for any(i.isdigit() for i in password) == False
    "strong_password_2": False,  # if branch for any(i.islower() for i in password) == False
    "strong_password_3": False,  # if branch for any(i.isupper() for i in password) == False
    "strong_password_4": False,  # if branch for any(i in '!@#$%^&*()-+' for i in password) == False
    "strong_password_5": False  # invisible else branch

}
counter = 0

def strong_password(n, password):
    count_error = 0
    # Return the minimum number of characters to make the password strong
    if any(i.isdigit() for i in password) == False:
        branch_coverage["strong_password_1"] = True
        count_error = count_error + 1
    if any(i.islower() for i in password) == False:
        branch_coverage["strong_password_2"] = True
        count_error = count_error + 1
    if any(i.isupper() for i in password) == False:
        branch_coverage["strong_password_3"] = True
        count_error = count_error + 1
    if any(i in '!@#$%^&*()-+' for i in password) == False:
        branch_coverage["strong_password_4"] = True
        count_error = count_error + 1

    branch_coverage["strong_password_5"] = True
    return max(count_error, 6 - n)


def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    total = len(branch_coverage)
    hit = sum(branch_coverage.values())
    result = hit / total * 100
    print("The total branch coverage is:", result, "%" )


strong_password(3, "Ab1")
print_coverage()
print("\n")
strong_password(11, "#Algorithms")
print_coverage()
print("\n")
strong_password(5, "12345")
print_coverage()
print("\n")
strong_password(5, "abcde")
print_coverage()

print()
