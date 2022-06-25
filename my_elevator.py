# make class Elevator which can up and down on 1 floor, select floor and go to it
class Elevator:
    # init bottom - lower floor, top higher floor, current - where we are now
    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
    # function to make up on the floor
    def up(self):
        if self.current != self.top:
            self.current += 1
    # function to make down on the floor
    def down(self):
        if self.current != self.bottom:
            self.current -= 1
        else:
            self.current = self.bottom
    # function to select the floor where we are going to
    def go_to(self, floor):
        self.floor = floor
        if self.floor < 0:
            self.current = self.bottom
        else:
            self.current = self.floor
    def __str__(self):
        return (f'\nCurrent floor: {self.current}')
    
# object elevator   
elevator = Elevator(-1, 10, 0)

# 1st testing elevator
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) 

# 2nd testing elevator
elevator.go_to(5)
print(elevator)
 