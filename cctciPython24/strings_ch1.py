Class chapter1 {
    def reverseString(string){
        new_string = ""
        len = len(string)
        for i in len/2:
            temp = string[i]
            string[i]=string[len-i]
            string[len-i] = temp 

        print(string)
        return "reversed string"
    }
}