#from curses import ACS_GEQUAL


class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, track, score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(track)
        self.score = float(score)

    def change_name(self, new_name):
        self.new_name = new_name
        new_name = input("Enter new name: ")
        print("Student name has changed from ", self.name, " to", new_name)
        
    def change_age(self, new_age):
        self.new_age = new_age
        new_age = input("Enter new age: ")
        print("Student age has changed from ", self.age, " to", new_age)
        
    def add_track(self, new_track):
        self.new_track = new_track
        new_track = input("Enter new name: ")
        print("Student track has changed from ", self.track, " to", new_track)
        
    def get_score(self):
        self.get_score = self.score
        print("Student score remains ", self.score)
            
  
Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

