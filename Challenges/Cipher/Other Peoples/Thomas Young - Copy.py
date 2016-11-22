user_input = input("-")
user_list = list(user_input)
print (user_list)
text=[]
for i in user_list:
    text.append(int(ord(i)))
print(text)


work = (0)
for i in text:
    text[0+work] = text[0+work] + 2
    work += 1


print(text)


user_list = ""
for i in text:
    user_list += chr(i)

print (user_list)    

""" 
Elegance - 4
Efficeny - 6

What you did well;

Converting the list input into a list was done well
The processing of data
Simplistic

Suggestions to imrpove;

Put comments within your code
Make some of your varible names= more clear
Some code not needed, still does the same thing
"""
