def replaceVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    ans = ''
    for c in word:
        if c in vowels:
            ans = word.replace(c,'')
    #for c in word:
    #   ans[c:c] = '.'
    ans = ans.casefold()
    return ans


x = input()
print(replaceVowels(x))
