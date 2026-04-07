class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height) - 4
        self.pos = 0
        self.moved = False  # to handle edge case

    def step(self, num):
        if self.perimeter == 0:
            return

        self.pos = (self.pos + num) % self.perimeter
        self.moved = True

    def getPos(self):
        p = self.pos

        # Bottom edge (left → right)
        if p < self.w:
            return [p, 0]

        p -= self.w

        # Right edge (bottom → top)
        if p < self.h - 1:
            return [self.w - 1, p + 1]

        p -= (self.h - 1)

        # Top edge (right → left)
        if p < self.w - 1:
            return [self.w - 2 - p, self.h - 1]

        p -= (self.w - 1)

        # Left edge (top → bottom)
        return [0, self.h - 2 - p]

    def getDir(self):
        if not self.moved:
            return "East"

        p = self.pos

        if p == 0:
            return "South"
        if p < self.w:
            return "East"

        p -= self.w
        if p < self.h - 1:
            return "North"

        p -= (self.h - 1)
        if p < self.w - 1:
            return "West"

        return "South"