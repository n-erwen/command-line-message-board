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









    
