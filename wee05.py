# Question 1- I think overall my work for this class has been decent but i think i could do better. I am not going to lie 
# i do feel myself struggling sometimes but am afraid to ask for help. I feel like because i do not engage as much 
# during class or i get easily distracted it gets hard to focus or go back to what was talked about. I do remember some 
# coding sections that i learned in my previous classes so that has helped a bit with trying to remember and revist 
# past homeworks. I believe i have been turning in all my assignments on time and submitting it through codespace when i sync codespaces.
# I also make sure to check github just in case to see if my recent code submitted and synced to weeks. I am showing up to class on time and trying to attend
# all as much as possible unless i have a work field trip. I know work stuff is not considered an excused abscence but i feel like i 
# have been making an effort to at least show up despite having to leave work early. I do need to put more hours into this class as much as i do for 
# my other classes. As for learning from my mistakes or what do i do if a coding is not running, i usually try to look through old live codings
# then if i cant figure out i copy my code and ask ai to tell me what am i missing that it is not running correctly. Most of the time that i have been getting 
# is missing little indents, numbers or capitalizing letters etc. Little mistakes like that i need to work better on because it ruins the whole thing 
# and i have been learning with that , to make sure i am patiently working through assignments to avoid these mistakes. 
# I do enjoy this class and  i love learning about mistakes and feeling satisfied once i get it right. It is stressful and  at times i spent more than 3 hours 
#---- with an assignment because i cant figure it out. However when i finish it i feel releived and excited to move forward hoping i did it right.

# Question 1: Intersection of two strings
def intersection(foo: str, bar: str) -> str | None:
    result = ""
    for char in foo:
        if char in bar and char not in result:
            result += char
    if result == "":
        return None
    return result

# Question 2: Check if string contains letters only (A-Z or a-z)
def is_alphabetical(string: str) -> bool:
    for char in string:
        ascii_val = ord(char)
        if not ((65 <= ascii_val <= 90) or (97 <= ascii_val <= 122)):
            return False
    return True

# Question 3: Remove all non-letter characters from string
def letters_only(string: str) -> str | None:
    result = ""
    for char in string:
        ascii_val = ord(char)
        if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
            result += char
    if result == "":
        return None
    return result

# Question 4: Generate palindrome by appending reverse of input
def generate_palindrome(string: str) -> str | None:
    if string == "":
        return None
    reverse = ""
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    return string + reverse

# Question 5: Palindrome detector ignoring case and non-alphanumeric
def is_palindrome(string: str) -> bool:
    cleaned = ""
    for char in string:
        ascii_val = ord(char)
        # letters and digits only
        if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122) or (48 <= ascii_val <= 57):
            cleaned += char.lower()
    return cleaned == cleaned[::-1]


# Question 3
#--- Although my code functions properly and passes the tests, I could improve it by including more comments and docstrings that clarify the purpose and meaning of each function. 
# It could make my code clearer to understand and shows a better understanding of the concepts. 
# Also, I saw that the type of hint in my odd_words function says the return type is str 
# instead of list[str], which is wrong and has to be fixed to be more accurate. 
# These minor modifications will help me create a code that is more straightforward 
# and professional in the future. Also quick note to add is there more to this assignment i need to do
# because the return statment says contact leo for test method but i thought this is all that is in on assignments?
# with that being said i definitely need to do better on doing assignments ahead of time so if i am stuck
# i can ask for help better and have more time to make mistakes and ask questions



#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
