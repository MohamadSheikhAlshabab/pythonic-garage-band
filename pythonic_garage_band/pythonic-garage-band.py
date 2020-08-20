class Musician :
    try:
        members=[]
        def __init__(self,members):
            self.members+=members

        def __repr__(self):
            pass

        def __str__(self):
            pass

        def get_instrument(self):
            pass

        def play_solos(self):
            pass
    except Exception as error:
        print(f"There is an error in Musician class, which is {error}")


class Band(Musician):
    try:
        name=""
        
            
        def __init__(self,solo,name,members):
            self.solo=solo
            self.name=name
            super().__init__(members)
            


        def play_solos (self):
            return f"you should play solo {self.solo}"

        def __repr__(self):
            return f"I'm  Musician play solo on {self.solo} in band {self.name}"

        def __str__(self):
            return f"I'm Musician play solo <{self.solo}>in band <{self.name}>"

        @classmethod
        def to_list(cls):
            return Musician.members

    except Exception as error:
        print ( f"There is error in Band class, which is {error}")



class Guitarist(Band):
    try:
        def __init__(self,solo,name,members):
            self.solo=solo
            self.name=name
            Musician.members+=members
    except Exception as error:
        print ( f"There is error in Guitarist class, which is {error}")

    
class Bassist(Band):
    try:
        def __init__(self,solo,name,members):
            self.solo=solo
            self.name=name
            Musician.members+=members
    except Exception as error:
        print ( f"There is error in Bassist class, which is {error}")

class Drummer(Band):
    try:
        def __init__(self,solo,name,members):
            self.solo=solo
            self.name=name
            Musician.members+=members
    except Exception as error:
        print ( f"There is error in Drummer class, which is {error}")

if __name__=='__main__':
    michal=Band("Guitar","Michal","5")
    print(michal)
    john=Band("Bass","John","2")
    monster=Guitarist("Guitar","Monsters band","3")
    print(monster)
    bass=Bassist("Bass","Basser band","8")
    print(bass)
    nice=Drummer("Drum","Bom Bom band","9")
    print(nice)
    print(michal.to_list())