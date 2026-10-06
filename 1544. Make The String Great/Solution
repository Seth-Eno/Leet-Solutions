class Solution:

    def makeGoodLoop(self, s: str) -> str:
        if s == (""):
            return ""
        
        great_string = ""
        #print(s)

        while len(s) > 1:
            if (s[0] == s[1].upper() and s[1].islower()) or (s[1] == s[0].upper() and s[0].islower()):
                #print(f"These charecters arent so great: {s[0] + s[1]}")
                s = s[2:]
                #print(f"Now they're gone -> {s}\n")
            else:
                #print(f"These charecters are pretty great: {s[0] + s[1]}")
                great_string += s[0]
                s = s[1:]
                #print(f"Heres my great string: {great_string}\n")

        if len(s) == 1:
            great_string += s[0]

        return(great_string)

    def makeGood(self, s: str) -> str:

        lastLastGreatString = self.makeGoodLoop(s)
        lastGreatString = self.makeGoodLoop(lastLastGreatString)

        while (lastGreatString != lastLastGreatString):
            lastLastGreatString = lastGreatString
            lastGreatString = self.makeGoodLoop(lastLastGreatString)

        return lastGreatString