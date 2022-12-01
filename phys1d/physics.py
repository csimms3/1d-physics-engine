import random



class Obj:

    def __init__(self, p, v, a=-98, b=0.6):
        self.position = p
        self.velocity = v
        self.acceleration = a
        self.bounce = b


    def __repr__(self):
        return f"Pos: {self.position}, Spd: {self.velocity}, Acc: {self.acceleration}"

    def p_update(self, time):
        self.position += self.velocity * time

    def v_update(self, time):
        if self.position >= 0:
            self.velocity += self.acceleration * time
        else:
            self.velocity *= -1 * self.bounce
            self.position = 0

    def ground_check(self):
        if self.position < 1 and 0 > self.velocity > -2:
            self.position = 0
            self.velocity = 0

    def update(self, time):
        self.v_update(time)
        self.p_update(time)
        self.ground_check()

