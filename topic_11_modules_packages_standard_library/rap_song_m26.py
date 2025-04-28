class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f'New Song made:\n{self.title} - {self.author}\n')
 
    def sing(self, max_lines=-1):
        print(f'{self.title} - {self.author}')
        lines_to_sing = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in lines_to_sing:
            print(line)
        return self
 
    def yell(self, max_lines=-1):
        print(f'{self.title} - {self.author}')
        lines_to_yell = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in lines_to_yell:
            print(line.upper())
        return self
 
# 1.B
# Tie kas jūtas komfortabli, uztaisiet Rap klasi kas manto no Song
# Papildu metode break_it ar diviem noklusētiem parametriem max_lines un drop vienādu ar "yeah", kura līdzīga sing, bet pievienot drop aiz katra vārda...
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH
 
class Rap(Song):
    # Rap inherits from Song so we can use the same __init__ method without redefining it
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        # print(f'New Rap Song made:\n{self.title} - {self.author}\n')

    def break_it(self, max_lines=1, drop="yeah"):
        print(f'BREAK IT FOR {self.title} - {self.author}')
        lines_to_break = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in lines_to_break:
            words = line.split()
            new_line = f' {drop} '.join(words) + f' {drop}'
            print(new_line)
        return self
 
# AI izveidoja pus kodu, līdzīgi kā apmācības komentāri kodā. Pašam puse nav skaidra un puse arī nestrādā, laikam mana puse :D.
 
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
 
# ziemelmeita.sing(1)
# ziemelmeita.sing(1).yell()
zrap.break_it(1, "YAH")