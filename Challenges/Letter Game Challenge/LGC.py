"""
 * Created by josep on 19/10/2017.
 
* Rules -
* Can't use lists/dic
* Can't use single varibles i.e. E = 1
* Need to use strings
"""

score = 0
points = "EARIOTNSLCUDPMHGBFYWKVXZJQ"


word = input("Enter a word\n- ").upper()

for letter in word:
    try:
        score += points.index(letter) + 1
    except ValueError:
        pass 

print("The score for that word is", score)
