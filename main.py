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

def update():
    while True:
        robot.update()
        time.sleep(1/60.0)
        

def run(strat):
    condition=True
    threading.Thread(target=update).start()
    strat.start()
    while condition:
        debut=time.time()
        strat.step()
        #print("robot : ",robot.distanceParcouru,robot.angle_parcourue)
        strat.step()
        if(strat.stop()):
            robot.setVitesse(0,0)
            robot.stopRec()
            condition=False
        time.sleep(time.time()-debut)
        
        
#run(TracerCarre(300,robot))
#run(AvancerToutDroit(300,robot))
run(Avancer(robot))