class Chapter1 :
    def reverseString(self, string):
        new_string = list(string)
        length = len(string)
        for i in range(len//2):
            temp = new_string[i]
            new_string[i]=string[len-i-1]
            new_string[len-i-1] = temp 

        reversed_string = "".join(new_string)
        print(reversed_string)
        return reversed_string
    
