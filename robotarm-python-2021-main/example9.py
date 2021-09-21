from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for pillars in range(1,5):
    for x in range(0, pillars):
        robotArm.grab()
        for z in range(0, 5):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(0, 5):
            robotArm.moveLeft()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()