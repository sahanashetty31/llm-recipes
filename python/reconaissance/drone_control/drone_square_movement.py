from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

for _ in range(4):
    tello.move_forward(50)
    tello.rotate_counter_clockwise(90)
tello.land()