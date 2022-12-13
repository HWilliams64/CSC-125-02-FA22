# == this tests equalities
# in this tests containment 

from collections.abc import Sequence

sentence = "The Dog jUmped oVer the cAr aNd cHased tHe caT"

user_input = input("Please type something in:")

if user_input in sentence:
    print(f'"{user_input}" is in the sentence')
    print("Something else")

elif user_input.casefold() in sentence.casefold():
    print(f'"{user_input}" is in the sentence but wrong case')

else:
    print(f'"{user_input}" is not in the sentence')


