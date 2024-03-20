# Example 1 : Find common letters betweeen two strings
def commonLetter():
    str1 = input("Enter the str1 :")
    str2 = input("Enter the str2 :")

    s1 = set(str1)
    s2 = set(str2)
    print(s1 & s2)
    print(s2)

commonLetter()


# Example 2 : Count frequency of words appering in string

def frequencyWords():
    str = input("Enter the string: ")
    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
        print(d[i])
    print(d)
frequencyWords()


