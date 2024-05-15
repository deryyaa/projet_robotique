from src.controleur.adaptateur import Robot2I013Adaptateur
try:
    from robot2IN013 import Robot2IN013 as Robot
    robot=Robot2I013Adaptateur(Robot(),300,250,20,20)
except ImportError:
    from src.controleur.robotReel import Robot2IN013_Mockup
    robot = Robot2I013Adaptateur(Robot2IN013_Mockup(),300,250,20,20)
from src.controleur.strategie import *
import threading
import time

def update(fps):
    robot.update()
    time.sleep(fps)

def run(strat):
    condition=True
    #threading.Thread(target=update).start()
    while condition:
        debut=time.time()
        threading.Thread(target=update(time.time()-debut,)).start()
        strat.step()
        time.sleep(time.time()-debut)
        print(robot.distanceParcouru,robot.angle_parcourue)
        if(strat.stop()):
            robot.setVitesse(0,0)
            condition=False
        
        
run(TracerCarre(300,robot))
