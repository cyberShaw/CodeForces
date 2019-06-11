def replaceVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    ans = ''
    for c in word:
        if c not in vowels:
            ans = ans + '.' + c            
    return ans   

x = input().lower()
print(replaceVowels(x))
