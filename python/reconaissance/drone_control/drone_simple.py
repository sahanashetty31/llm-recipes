from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(50)
#tello.rotate_counter_clockwise(90)
#tello.move_forward(100)

tello.land()