def setup():
    # Set the size of your sketch
    size(400, 400)
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(8):
        if i % 2 == 0:
            fill('#FF0000')
        else:
            fill('#000000')
        ellipse(200, 200, 175 - i*20, 175 - i*20)
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
