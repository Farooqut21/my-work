s=input("enter a string")
def noVowel(s):
    for char in s:
        if char in 'aeiou':
            return False
    return True
