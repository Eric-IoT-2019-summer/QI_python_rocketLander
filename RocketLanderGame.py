# author    Eric
# date      07-13-2019
# email     baekek100ek@gmail.com

position = 100
velocity = 0
fuel = 100
gravity = -10
thruster = 0

print("P:\t{} V:\t{} F:\t{}".format(position, velocity, fuel))

while 1:
    if fuel != 0:
        thruster = int(input("Set your thrusters(0-20): "))

        if thruster < 0:
            print("No thrusters(0)!")
            thruster = 0
        if thruster > 20:
            print("Thrusters at max(20) !")
            thruster = 20

        if thruster > fuel:
            print("Out of fuel! thrusters at {}".format(fuel))
            thruster = fuel

    else:
        print("No fuel -- rocket is in free-fall!")
        thruster = 0

    fuel = fuel - thruster
    acceleration = gravity + thruster
    position = int(position + velocity + acceleration * 0.5)
    velocity = velocity + acceleration

    if position <= 0:
        position=0
        if velocity <= -3:
            print("P:\t{} V:\t{} F:\t{}".format(position, velocity, fuel))
            print("Rocket crashed! Velocity was {} m/s".format(velocity))
            break
        else:
            print("P:\t{} V:\t{} F:\t{}".format(position, velocity, fuel))
            print("Landing successful!")
            break
    print("P:\t{} V:\t{} F:\t{}".format(position, velocity, fuel))
