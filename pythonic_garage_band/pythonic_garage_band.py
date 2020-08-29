from abc import abstractmethod, ABC
class Musician(ABC) :
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        """
        This represent method of class Musician,
        return name of musicain.
        """
        return self.name

    def __str__(self):
        """
        This string method of class Musician,
        return name of musicain.
        """
        return self.name

    @staticmethod
    def get_instrument(self):
        """
        This get_instrument method.
        """
        pass

    @staticmethod
    def play_solo(self):
        """
        This play_solo method of class Musician.
        """
        pass


class Band(ABC):
    bands=[]
    def __init__(self,name,members):
        self.members=members
        self.name=name
        Band.bands.append(self)
        


    def play_solos (self):
        """
        This is play_solos method of class Band,
        return each musician to play solo.
        """
        solo=[]
        [solo.append(i.play_solo) for alone in self.members ]
        return solo

    def __repr__(self):
        return f"We're Musician members {self.members} in band {self.name}"

    def __str__(self):
        return f"We're Musician members <{self.members}> in band <{self.name}>"

    @classmethod
    def to_list(cls):
        """
        This to_list method of Band,
        return all created bands. 
        """
        return cls.bands

class Guitarist(Musician):

    def __init__(self,name,instrument):
        self.instrument=instrument
        self.name=name

    def play_solo(self):
        return "Trmmmm Teeerrm"
    
    def get_instrument(self):
        return self.instrument

    
class Bassist(Musician):
    def __init__(self,name,instrument):
        self.instrument=instrument
        self.name=name

    def play_solo(self):
        return "TrnTraaan"
    
    def get_instrument(self):
        return self.instrument

class Drummer(Musician):
    def __init__(self,name,instrument):
        self.instrument=instrument
        self.name=name

    def play_solo(self):
        return "Dug Dooog"
    
    def get_instrument(self):
        return self.instrument


if __name__=='__main__':
    michal=Band("Guitar","michal")
    jamil=Band("Drum","jamil")
    gasan=Band("Bass","gasan")
    print(michal)
    print(gasan.__repr__())
    print(jamil)
    print(michal.members)
    john=Band("Bass","John")
    monster=Guitarist("Guitar","Monsters band")
    print(monster)
    print(monster.__repr__())
    print(monster.__str__())
    bass=Bassist("Bass","Basser band")
    print(bass)
    nice=Drummer("Drum","Bom Bom band")
    print(nice)
    print(michal.to_list())