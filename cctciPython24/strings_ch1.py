class Chapter1 :
   # #  given n x n matrix, rotate image by 90 degress
   def rotate90(self, matrix)
        return [list(reversed(col)) for col in zip(*matrix)]
    # #  compress string to letter and letter count 
    def stringCompression(self, string):
        prev = string[0]
        count = 1
        new_string = ""
        for i in range(1, len(string)): 
            letter = string[i]
            if letter == prev: 
                count +=1
            else: 
                new_string +=prev+str(count)
                
                count = 1
            prev = letter 

        new_string += prev + str(count)

        return new_string

    # # words are one edit away from each other 
    def oneAway(self, string1, string2): 
        if abs(len(string1)-len(string2)) > 1: 
            return False 
        letter1set = list()
        extraletters = list()
        for letter in string1:
            letter1set.append(letter)
        for letter2 in string2:
            if letter2 in letter1set: 
                letter1set.remove(letter2)
            elif letter2 not in letter1set: 
                extraletters.append(letter2)
        return len(extraletters) + len(letter1set) <=1
       

    # # is the word the same back and forth 
    def palindromePermuation(self, string): 
        odds = set()
        string = string.replace(" ", "").lower()
        for letter in string: 
            if letter in odds: 
                odds.remove(letter)
            else: 
                odds.add(letter)
        return len(odds) <= 1

    # # replace all spaces in string with %20
    def URLify(self, string):
        return string.replace(' ', '%20')

    # # Given two strings write a method to decide if one is a permutation of another 
    def checkPermutations(self, string1, string2):
        same_letter_count = 0; 
        if len(string1) != len(string2):
            return False
        return sorted(string1) == sorted(string2)
        

    # # Determine if a string has all unique characters 
    def isUnique(self, string):
        seen_chars = set() 

        for letter in string: 
            if letter in seen_chars: 
                return False
            seen_chars.add(letter)

        return True

    def reverseString(self, string):
        new_string = list(string)
        length = len(string)
        for i in range(length // 2):
            temp = new_string[i]
            new_string[i]=string[length - i - 1]
            new_string[length - i - 1] = temp 

        reversed_string = "".join(new_string)
       
        return reversed_string
    
