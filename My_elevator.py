class Elevator:
    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        if self.current != self.top:
            self.current += 1
    def down(self):
        if self.current != self.bottom:
            self.current -= 1
        else:
            self.current = self.bottom
    def go_to(self, floor):
        self.floor = floor
        if self.floor < 0:
            self.current = self.bottom
        else:
            self.current = self.floor
    def __str__(self):
        return (f'Current floor: {self.current}')
   
elevator = Elevator(-1, 10, 0)

elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) 
  
elevator.go_to(5)
print(elevator)
 