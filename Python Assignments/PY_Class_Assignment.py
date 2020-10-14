# Python:     3.8.5
# Name:       Nicholas Mireles
# Assignment: Class Assignment


class instrument():
    def __init__(self, name, section, band):
            self.name = name
            self.section = section
            self.band = band

class strings( instrument ):
    def __init__(self, name, section, band, play, strNum):
            self.play = play
            self.stringNumber = strNum
            instrument.__init__(self, name, section, band)
    def display(self):
            print("The", self.name,"is a member of the", self.section, "family used in", self.band, "bands." \
                  " It is played by", self.play, "over", self.stringNumber, "string's.")        

class brass( instrument ):
    def __init__(self, name, section, band, bore, note):
            self.bore = bore
            self.note = note
            instrument.__init__(self, name, section, band)
    def display(self):
            print("The", self.name,"is a member of the", self.section, "family used in", self.band, "bands." \
                  "It has a", self.bore, "bore, and uses", self.note, "to change pitch.")
            

b = strings("double bass","strings","symphonic","bowing","six")
b.display()
t = brass("trombone","brass","concert","cylindrical","slides")
t.display()
