try:
    from robot2IN013 import Robot2IN013
except:
    from src.controleur.robotReel import Robot2IN013_Mockup
from src.controleur.adaptateur import Robot2I013Adaptateur
from src.controleur.strategie import *
import threading
import time

robot = Robot2I013Adaptateur(Robot2IN013_Mockup(),300,250,20,20)
def run(strat):
    condition=True
    while condition:
        debut=time.time()
        robot.update()
        strat.step()
        print(robot.distanceParcouru,robot.angle_parcourue)
        if(strat.stop()):
            robot.setVitesse(0,0)
            condition=False
        time.sleep(time.time()-debut)
        
        
run(TracerCarre(50,robot))