This is my first deliverable for the Grand Circus course.
My first bit of code in the project looked sloppy (see below, my if loop only is there below).
I revised it and made if look and function smoother in the graded versions.
if holes == int(3):
    h1 = int(input("How many putts for hole 1? "))
    par = 9
    strokes = 0 + h1
    h2 = int(input("How many putts for hole 2? "))
    strokes += h2
    h3 = int(input("How many putts for hole 3? "))
    strokes += h3
    score = strokes - par

elif holes == int(6):
    h1 = int(input("How many putts for hole 1? "))
    par = 18
    strokes = h1
    h2 = int(input("How many putts for hole 2? "))
    strokes += h2
    h3 = int(input("How many putts for hole 3? "))
    strokes += h3
    h4 = int(input("How many putts for hole 4? "))
    strokes += h4
    h5 = int(input("How many putts for hole 5? "))
    strokes += h5
    h6 = int(input("How many putts for hole 6? "))
    strokes += h6
    score = strokes - par

    
