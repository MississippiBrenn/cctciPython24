class Chapter1 :
    # # Determine if a string has all unique characters 
    def isUnique(self, string):
        list_string = list(string)
        sorted_lstring = sorted(list_string)
        j = 0
        for i in range(1,len(sorted_lstring)-1):
            if(sorted_lstring[j]==sorted_lstring[i]):
                return False
        
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
    
