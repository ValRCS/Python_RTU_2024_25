class Song:
    def __init__(self, title="",author="",lyrics=(), secret="hunter2"):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        self.__secret = secret # private variable, not accessible from outside the class
        print(f"New Song made: {self.title} by {self.author}")
 
    def sing(self, max_lines=-1): #ar a vēlējos uztaisīt parametru, kas izdrukātu tikai tik rindiņas, cik prasīts
        self._print_title_author("Singing: ")
        if max_lines == -1:
            max_lines = len(self.lyrics)

        for row in self.lyrics[:max_lines]:
            print(row)
        # enable chaining
        return self
 
    def yell(self, max_lines = -1):
        self._print_title_author("Shouting: ")
        if max_lines == -1:
            max_lines = len(self.lyrics)
        for row in self.lyrics[:max_lines]:
            print(row.upper())
        # enable chaining
        return self
    
    # if you prepend a single underscore to a method name,
    # it is considered a "protected" method, meaning it is intended for internal use only
    # and should not be accessed from outside the class.
    # however this is just a convention and does not enforce any restrictions.


    def _print_title_author(self, prefix=""):
        print(f"{prefix}{self.title} by {self.author}")
        # enable chaining
        return self
    
    # we can actually hide methods and variables
    # by prepending a double underscore to the name __
    # we have __secret variable in the class
    # so lets define public method to print it
    def print_secret(self):
        # we could add extra logic with this method, like checking if the user is allowed to see the secret
        print(f"Secret: {self.__secret}")
        # enable chaining
        return self
 
dziesma = Song("Īssavienojums","Prāta Vētra", ("Cik dīvainas ir tās paralēles", "Kas ved mūs pa takām kalnā", "Un kad tu mani trīsreiz piekrāpsi", "Es pazudīšu ar salnām", "Tad stāvēšu dzelzceļa malā", "Turp atpakaļ vilcienus vērot","Rītdiena nekad nepienāks", "Džeimsam nav, par ko sērot"))
 
dziesma.sing()
dziesma.yell()

dziesma.yell(2).sing(3) # chaining

brainstorm1 = Song("Plaukstas lieluma pavasaris", "Prāta vētra", ["Diena sākas, kāpju uz svariem",
                                                                  "Manis pietiks vēl diviem pavasariem",
                                                                  "Piere rievās, kaujas pozā",
                                                                  "Mīļotā, noņem tās brilles rozā"])

brainstorm1.sing(2).yell(1) # chaining

try:
    print(brainstorm1.__secret) # this will raise an error, because __secret is private
except AttributeError as e:
    print(f"Error: {e}")

# instead we have to use our own method
brainstorm1.print_secret() # this will work, because print_secret is public method
