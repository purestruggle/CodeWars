#Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth
#(2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on 
#Twitter, he is known for almost always capitalizing every word.

#Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual 
#quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

#Example:

#Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
#Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def toJadenCase(string):
        
        ans = []
        x = ''
        w_a = []
        
        #puts string of letters into seperate words.
        for word in string:
                if word == ' ':
                        w_a.append(x)
                        x = ''
                if word != ' ':
                    x += word
        w_a.append(x)
        
        #capitalize first letter of each word in list w_a.
        i = 0
        for word in w_a:
            c = len(w_a)
            if i == (c-1):
                ans.append(word.capitalize())
            else:
                ans.append(word.capitalize()+ ' ')
            i += 1
        
        #cat list elements into full string.
        final = ''
        for word in ans:
            final += word
        return final
