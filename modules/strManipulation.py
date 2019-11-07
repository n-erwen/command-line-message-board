def mustInput(message):
    val = ""
    while not val.strip():
        val = input(message)
    return val

def title(string):
    border="-"*len(string)
    print(border.center(70))
    print(string.center(70))
    print(border.center(70))

def splitstr(strng):
    List = [] #container to hold the split string
    prev = 0 #index of character after the last whitespace found
    whitespace = "" #index of the last whitespace found     
    while whitespace != -1: #while there has not been a failed search:
        
        whitespace = strng.find(" ",prev) #stores the index of the first found whitespace after the 'prev' index value
        
        if whitespace == -1: #if the search has failed:
            if strng[prev:len(strng)] != "": #if the slice of strng - consisting of the 'prev' value up to the end of strng - is not blank:
                List.append(strng[prev:len(strng)]) #add this slice to 'List'
            
        else: #if the search has succeeded:
            if strng[prev:whitespace] != "": #if the slice of strng - consisting of the 'prev' value up to and not including the whitespace found in this iteration - is not blank:
                List.append(strng[prev:whitespace]) #add this slice to 'List'
        prev = whitespace+1 #set 'prev' to the index of the value after the whitespace

    return List #return the 'List' containing the split string

def isPalindrome(string):
    string = string.lower() #makes all letters in string lowercase
    for s in string:
        if s.isalnum() == False:
            string = string.replace(s,"") #removes non-alphanumeric characters
    if len(string) % 2 == 0: #if the character count is even:
        even = True
        mid = ( len(string) // 2) #returns the position (NOT index value) of the middle character in string
    else: #if the character count is odd:
        even = False
        mid = (len(string)//2)+1 #since integer division always rounds down, mid is incremented by 1
    palin = string[0:mid] #palin is a slice of string from the first to middle char (using index value)
    if even == True: #if character count is even:
        drome = string[mid:len(string)] #drome is a slice of string from the char after the middle char to the end
    elif even == False: #if the character count is odd:
        drome = string[mid-1:len(string)] #drome is a slice of string from the middle char to the end
    if palin == drome[::-1]: #if palin is equivalent to the reverse of drome:
        return True #string is a palindrome
    else: #otherwise:
        return False #string is not a palindrome

def isAnagram(s1,s2):
    s1 = s1.lower()
    s1.replace(" ","") 
    
    s2 = s2.lower()
    s2.replace(" ","") #both strings are converted into lowercase and stripped of whitespaces.
    s2 = list(s2) #all letters added to lists in both strings.
    if len(s1) == len(s2):
        
        for let in s1: #for each letter in the 1st string:
            if let in s2: #if this letter is in the 2nd string:
                i = s2.index(let)
                del s2[i] #delete this letter to [prevent errors]
            else: #if this letter is not in the second string (or the number of occurences of this letter in s1 exceeds the no. of occurences in s2):
                return False #the two strings are not anagrams of each other
        return True #if all the letters of s1 are in s2, the strings are anagrams of each other.

    else:
        return False

def jumble(word):
    import random
    word = list(word)
    sBuffer = []
    for w in word:
        if w.isspace() == True:
            i = word.index(w)
            sBuffer.append(i)
            del word[i]
    random.shuffle(word)
    for s in sBuffer:
        word.insert(s," ")
    word = "".join(word)
    return word









    
