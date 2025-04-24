class Song:
    def __init__(self, title = "", author = "", lyrics = ""):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made: {self.title} by {self.author}")
 
    def sing(self, max_lines = -1):
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
 
class Rap(Song):
    # if we only want the exact same initialization as the parent class
    # we can skip the __init__ method in the child class
    # def __init__(self, title = "", author = "", lyrics = ""):

    #     super().__init__(title, author, lyrics)
    # we would want to do this if we have custom initialization in the child class
 
    def break_it(self, max_lines = -1, drop = "yeah"):
        self._print_title_author("Rapping: ")
        if max_lines == -1:
            max_lines = len(self.lyrics)
        for row in self.lyrics[:max_lines]:
            words = row.split()
            for word in words:
                print(word, drop, end = " ")
        return self
 
 
 
 
        
# dziesma = Song("Īssavienojums","Prāta Vētra", ("Cik dīvainas ir tās paralēles", "Kas ved mūs pa takām kalnā", "Un kad tu mani trīsreiz piekrāpsi", "Es pazudīšu ar salnām", "Tad stāvēšu dzelzceļa malā", "Turp atpakaļ vilcienus vērot","Rītdiena nekad nepienāks", "Džeimsam nav, par ko sērot"))
 
# dziesma.yell(2).sing(3) # chaining
 
# brainstorm1 = Song("Plaukstas lieluma pavasaris", "Prāta vētra", ["Diena sākas, kāpju uz svariem",
#                                                                   "Manis pietiks vēl diviem pavasariem",
#                                                                   "Piere rievās, kaujas pozā",
#                                                                   "Mīļotā, noņem tās brilles rozā"])
 
# brainstorm1.sing(2).yell(1) # chaining
 
brainstorm_rap = Rap("Plaukstas lieluma pavasaris", "Prāta vētra", ["Diena sākas, kāpju uz svariem",
                                                                  "Manis pietiks vēl diviem pavasariem",
                                                                  "Piere rievās, kaujas pozā",
                                                                  "Mīļotā, noņem tās brilles rozā"])
 
brainstorm_rap.break_it(3, "skrr")