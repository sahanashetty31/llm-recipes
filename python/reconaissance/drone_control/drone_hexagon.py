from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

#Move and rotate for each side of the hexagon
for _ in range(6):
    tello.move_forward(50)
    tello.rotate_clockwise(60) # Rotate 60 degrees for a hexagon

tello.land()