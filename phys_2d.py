class Obj2d:

    def __init__(self, xp, yp, xv, yv, xa, ya=-9.8, b=0.6, friction=10):
        self.xp = xp
        self.yp = yp
        self.xv = xv
        self.yv = yv
        self.xa = xa
        self.ya = ya
        self.bounce = b
        self.friction = friction



    def __repr__(self):
        return f"Pos: {self.xp, self.yp}, Spd: {self.xv, self.yv}, Acc: {self.xa, self.ya}"

    def p_update(self, time):
        self.xp += self.xv * time
        self.yp += self.yv * time

    def v_update(self, time):
        self.xv += self.xa * time
        self.yv += self.yz * time

    def collision_check(self, ground, r, l):
        if self.yp < 0:
            self.yv = -1 * max((self.bounce * self.yv) - self.friction, 0)

        if self.xp < l or self.xp > r:
            self.xv *= -1 * self.bounce


    def update(self, time, g, r, l):
        self.v_update(time)
        self.p_update(time)
        self.collision_check(g, r, l)

