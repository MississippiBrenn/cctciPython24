class Chapter1 :
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
    
