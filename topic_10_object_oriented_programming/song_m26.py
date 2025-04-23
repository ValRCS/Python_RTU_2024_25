class Song:
    def __init__(self, title='', author='', lyrics=(), secret = "hunter2"):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        self.__secret = secret # so by using __ we can hide the secret from the outside world
        # self.__secret will still be accessible from the outside world, but it will be harder to access
        # inside our class we can access it as self.__secret
        print(f"New Song made: {self.title} by {self.author}")
 
    def sing(self, max_lines=-1):
        # if self.author and self.title:
        #     print(f"Autors: {self.author} - Dziesma: {self.title}")
        self._print_author_title()
        # for i, line in enumerate(self.lyrics):
        #     if max_lines != -1 and i >= max_lines:
        #         break
        #     print(line)
        # alternative is to check maxlines first then use slicing
        if max_lines == -1:
            max_lines = len(self.lyrics)
        # all other cases are fine for slicing
        for line in self.lyrics[:max_lines]:
            print(line)
        return self
 
    def yell(self, max_lines=-1):
        # if self.author and self.title:
        #     print(f"Autors: {self.author} - Dziesma: {self.title}")
        self._print_author_title()
        for i, line in enumerate(self.lyrics):
            if max_lines != -1 and i >= max_lines:
                break
            print(line.upper())
        return self
    
    # let's create a helper method to print author and title
    # we will use _ to indicate this is for internal use only - semi private
    def _print_author_title(self):
        if self.author and self.title:
            print(f"Autors: {self.author} - Dziesma: {self.title}")
        elif self.title:
            print(f"Dziesma: {self.title}")
        elif self.author:
            print(f"Autors: {self.author}")
        else:
            print("Nav informācijas par autoru vai dziesmu")
        return self
    
    # let's add get secret method to get the secret
    def get_secret(self):
        # add authorization check here if needed
        # for example, check if the user is authorized to access the secret
        return self.__secret
    
#Tagad izveidojam dažas dziesmas ar dziesmu tekstiem
dziesma1 = Song("Div' pļaviņas", "Tautasdziesma", ("Div' pļaviņas", "Es nopļāvu", "Sarkanā'i", "Āboliņ"))

dziesma1.sing(2).yell(3).sing()

# now we can get secret using get_secret method
print(dziesma1.get_secret()) # hunter2
# now direct access is not easily done
try:
    print(dziesma1.__secret) # this will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")