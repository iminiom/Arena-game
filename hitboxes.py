class Hitbox:
    def __init__(self,x,y,w,h):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.width

    def go_to(self,x,y):
        
        self.xpos = x
        self.ypos = y
        self.bottom = y + self.height
        self.top = y
        self.left = x
        self.right = x + self.width
    
    
def is_colliding(hitbox1 : Hitbox,hitbox2 : Hitbox):
    """checks if it is colliding"""
    colliding = False
    
    if ((hitbox1.bottom>=hitbox2.top and hitbox1.bottom<=hitbox2.bottom) or (hitbox1.top>=hitbox2.top and hitbox1.top<=hitbox2.bottom)) and ((hitbox1.left>=hitbox2.left and hitbox1.left<=hitbox2.right ) or (hitbox1.right>=hitbox2.left and hitbox1.right<=hitbox2.right)):
        colliding = True
    return colliding

def is_touching(h1 : Hitbox, h2: Hitbox):
    "Unlike is_colliding , here it's only if it's strictly the same values (== instead of <= / >=)"
    
    from_where = ''
    if h1.bottom == h2.top:
        from_where = 'down'
    elif h1.top == h2.bottom:
        from_where = 'up'
    elif h1.right == h2.left:
        from_where = 'right'
    elif h1.left == h2.right:
        from_where = 'left'
        
    return from_where 

h1 = Hitbox(0,0,10,10)
h2 = Hitbox(5,5,10,10)
h1.go_to(5,5)
