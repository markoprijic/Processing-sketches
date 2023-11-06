x =10
c =0

def setup():
    global x
    global c

    size (500,500)
    background(0)
    colorMode(RGB)
    
    
c = 0
x = 0
    
def draw():
    global x
    global c
    c = c + 1
    
    noStroke()
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 10)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)
    
    fill(c, random(255), random(255))
    circle(x, 255, 200)
     
    if x > 600:
        x = -100
    else:
        x = x +10
        
    if c > 255:
        c = 0
