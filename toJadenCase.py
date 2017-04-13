def toJadenCase(string):
        
        ans = []
        x = ''
        w_a = []
        for word in string:
                if word == ' ':
                        w_a.append(x)
                        x = ''
                if word != ' ':
                    x += word
        w_a.append(x)
        
        i = 0
        for word in w_a:
            c = len(w_a)
            if i == (c-1):
                ans.append(word.capitalize())
            else:
                ans.append(word.capitalize()+ ' ')
            i += 1
        
        final = ''
        for word in ans:
            final += word
        return final

quote = "How can mirrors be real if our eyes aren't real"

toJadenCase(quote)

