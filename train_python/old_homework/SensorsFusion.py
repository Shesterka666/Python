#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import copy
import time
from driver.msg import MatMask
from driver.msg import ObjectOnARoad
from driver.msg import ToMap
from driver.msg import Lights_Signs
from driver.msg import Ultrasonic
import math
from std_msgs.msg import Empty
import time
from std_msgs.msg import Empty
from enum import IntEnum
import threading
from driver.msg import Lane
import rospkg
import os 
os.environ["CUDA_VISIBLE_DEVICES"]="1"
enumerate
pubMap = rospy.Publisher('MapObjects', ToMap, queue_size='2')
pubAutomove = rospy.Publisher('FromFusion', ObjectOnARoad, queue_size='2')
pubDebug= rospy.Publisher('ForwardSonar',Int32, queue_size='2')

pubLight=rospy.Publisher('LightType',String)
rospy.init_node('SensorsFusion')
ImageLeft=None
class STATUS(IntEnum):
    NEW=1
    MODIFIED=2
    REMOVE=3
class SONARS(IntEnum):
    FORWARD=1
    BACKWARD=2 
    LEFT=3   
    RIGHT=4 

NavObjects=["Concede","Pedestrian","SlipR","OverTr","CancelAll","MRoad","Stop","Left","Right","Ordinary"]

rospack = rospkg.RosPack()
CancelAll = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/CancelAll.png')
Concede = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/Concede.png')
Mroad = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/Mroad.jpeg')
OverTR = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/OverTR.png')
Pesheh = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/pesheh_perehod.jpg')
RoudUp = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/roudUp.jpg')
SlipeR = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/slipeR.png')
Stop = cv2.resize(cv2.imread(rospack.get_path('driver')+'/stuff/visualize/stop.jpg'),(50,50))
Green = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/LightOrGreen.jpeg')
Red = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/LightOrRed.jpeg')
Section = cv2.imread(rospack.get_path('driver')+'/stuff/visualize/dopsection.jpg')
Car= cv2.imread(rospack.get_path('driver')+'/stuff/visualize/car.png')
Person= cv2.imread(rospack.get_path('driver')+'/stuff/visualize/pedestian.png')

CarOnLane= cv2.imread(rospack.get_path('driver')+'/stuff/visualize/carOnLane.png')
PersonOnLane= cv2.imread(rospack.get_path('driver')+'/stuff/visualize/pedestianOnLane.png')
Wall= cv2.imread(rospack.get_path('driver')+'/stuff/visualize/wall.jpg')
def debug(objects):
    global Stop
    img = np.zeros((200,700,3), np.uint8)
    k=0
    visualizeObjects(objects)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in objects:
        if i.confidence<0.9:
            continue
        if i.classObj=="Stop":
            h1, w1 = Stop.shape[:2]
            
            img[:h1, k:k+w1,:3] = Stop
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="RoadUp":
            h1, w1 = RoudUp.shape[:2]

            img[:h1, k:k+w1,:3] = RoudUp
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="Concede":
            h1, w1 = Concede.shape[:2]
            
            img[:h1, k:k+w1,:3] = Concede
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="Pedestrian":
            h1, w1 = Pesheh.shape[:2]
            
            img[:h1, k:k+w1,:3] = Pesheh
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="MRoad":
            h1, w1 = Mroad.shape[:2]
            
            img[:h1, k:k+w1,:3] = Mroad
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="OverTr":
            h1, w1 = OverTR.shape[:2]
            
            img[:h1, k:k+w1,:3] = OverTR
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="SlipR":
            h1, w1 = SlipeR.shape[:2]
            
            img[:h1, k:k+w1,:3] = SlipeR
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="CancelAll":
            h1, w1 = CancelAll.shape[:2]
            
            img[:h1, k:k+w1,:3] = CancelAll
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="Green":
            h1, w1 = Green.shape[:2]
            
            img[:h1, k:k+w1,:3] = Green
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="Red":
            h1, w1 = Red.shape[:2]
            
            img[:h1, k:k+w1,:3] = Red
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="Greenleft" or i.classObj=="Greenright":
            h1, w1 = Section.shape[:2]
            
            img[:h1, k:k+w1,:3] = Section
            cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
            k+=w1
        elif i.classObj=="Car":
            if  sensorFusion.IfOnRoad(i):
                h1, w1 = carOnLane.shape[:2]
                img[:h1, k:k+w1,:3] = Car
                cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                k+=w1
            else:
                h1, w1 = Car.shape[:2]
                img[:h1, k:k+w1,:3] = Car
                cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                k+=w1
        elif i.classObj=="Person":
            if  sensorFusion.IfOnRoad(i):
                h1, w1 = Person.shape[:2]
                img[:h1, k:k+w1,:3] = Person
                cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                k+=w1
            else:
                h1, w1 = Person.shape[:2]
                img[:h1, k:k+w1,:3] = Person
                cv2.putText(img,str(round(i.angle,2)),(k+3,h1+10), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,str(i.distance),(k+3,h1+30,), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                k+=w1
        # elif i.classObj in  [str(SONARS.FORWARD),str(SONARS.BACKWARD),str(SONARS.LEFT),str(SONARS.RIGHT)]:
        #     h1, w1 = Wall.shape[:2]
        #     img[:h1, k:k+w1,:3] = Wall

        #     k+=w1
        
    # Display image
  
    cv2.imshow("outImg", img)
    cv2.waitKey(1)
def CompareTwoObjects(i1,i2):
    if i1.time-i2.time>0.3:
        return i2
    elif i2.time-i1.time<0.3:
        return i1
    elif i1.confidence>i2.confidence:
        return i1
    elif i2.confidence<i1.confidence:
        return i2
    elif i1.distance>i2.distance and i2.distance!= -1 :
        return i2
    else:
        return i1
def delByClass(objects,ClassObj):
        other = [x for x in objects if x.classObj == ClassObj]
        if len(other)>0:
            for i in other:
                sensorFusion.remove(i,False)

def deleteRepeated(objects):
    for roadObject in objects:

        other = [x for x in objects if x.classObj == roadObject.classObj]
        if len(other)>1:

            newObject=roadObject
            for i in other:
                if i==roadObject:
                    continue
                newObject=CompareTwoObjects(newObject,i)
            delByClass(objects,roadObject.classObj)
            sensorFusion.add(newObject,STATUS.MODIFIED)
ObjectToColor={
    'Car':(255,255,0),
    'Person':(255,0,255),
    'Green':(0,255,0),
    'Red': (255,0,0),
    
    
}
def visualizeObjects(listOfObjects):
    image=np.zeros((256,256))
    image=cv2.rectangle(image, (123,123), (133,133), (255, 100, 100) , 2) 
    for Mapobject in listOfObjects:
<<<<<<< Updated upstream
        x=Mapobject.distance*math.cos(Mapobject.angle)
        y=Mapobject.distance*math.sin(Mapobject.angle)
        if listOfObjects.classObj in ObjectToColor:
            color=ObjectToColor[listOfObjects.classObj]
        else:
            color=(255,200,60)
        image=cv2.rectangle(image, (x-10,y-10), (x+10,y+10), color , 2) 
    cv2.imshow("2dMap",image)
    cv2.waitKey(1)
=======
        rospy.logerr("Polar Coordinates")
        x=(Mapobject.distance*100)*math.cos(Mapobject.angle)+128
        y=(Mapobject.distance*100)*math.sin(Mapobject.angle)*-1+128
        rospy.logerr(x)
        rospy.logerr(y)
        if Mapobject.classObj in ObjectToColor:
            color=ObjectToColor[Mapobject.classObj]
        else:
            color=(255,200,60)
        image=cv2.rectangle(image, (int(x-10),int(y-10)), (int(x+10),int(y+10)), color , 2) 
    cv2.imshow("2dMap",image)
    cv2.waitKey(1)

>>>>>>> Stashed changes
    
    
                
def callback():
    while not rospy.is_shutdown():
        #rospy.logerr(sensorFusion.toString())
        rospy.sleep(0.01)
        now=time.time()
        sensorFusion.removeLights()
        deleteRepeated(sensorFusion.listOfObjects)
<<<<<<< Updated upstream
        try:
            debug(sensorFusion.listOfObjects)
            vizualizeObjects(sensorFusion.listOfObjects)
            for  i in sensorFusion.listOfObjects:
                i.confidence-=0.001
                if now-i.time>1.3 and i.classObj in [ "Red", "Green"]:
                    sensorFusion.remove(i,True)
                if now-i.time>1 :
                    sensorFusion.remove(i,True)
                if i.confidence>0.8:
                    msg=ObjectOnARoad()
                    msg.X=i.x
                    msg.Y=i.y
                    msg.Height=i.height
                    msg.Width=i.width
                    msg.Distance=i.distance
                    msg.Class=i.classObj
                    pubAutomove.publish(msg)
                if i.confidence>1:
                    i.confidence=1
        except:
            pass
=======

        debug(sensorFusion.listOfObjects)
        for  i in sensorFusion.listOfObjects:
            i.confidence-=0.001
            if now-i.time>1.3 and i.classObj in [ "Red", "Green"]:
                sensorFusion.remove(i,True)
            if now-i.time>1 :
                sensorFusion.remove(i,True)
            if i.confidence>0.8:
                msg=ObjectOnARoad()
                msg.X=i.x
                msg.Y=i.y
                msg.Height=i.height
                msg.Width=i.width
                msg.Distance=i.distance
                msg.Class=i.classObj
                pubAutomove.publish(msg)
            if i.confidence>1:
                i.confidence=1

>>>>>>> Stashed changes
    
def Performlanes(data):
 
    sensorFusion.LaneLeft=[data.left[0],data.left[1]]
    sensorFusion.LaneRight=[data.right[0],data.right[1]]
class SensorFusion():
    def __init__(self):
        self.listOfObjects=[]
        self.LastSonarForward=50 
        self.LastSonarBackward=50
        self.DiffX=80
        self.DiffAngle=30
        self.DiffY=50
        self.wasStoppedForward=False
        self.wasStoppedBackward=False 
        self.LaneLeft=None
        self.LaneRight=None 
        
    def removeLights(self):
        red=[x for x in self.listOfObjects if x.classObj == "Red"]
        green=[x for x in self.listOfObjects if x.classObj == "Green"]
        if len(red)>0 and len(green)>0:
            if red[0].time>green[0].time:
                self.remove(red[0],True)
            else:
                self.remove(green[0],True)

    def add(self,Object,status):
        self.listOfObjects.append(Object)
        if Object.confidence>0.8:
            msgres=ToMap()
            msgres.Class=Object.classObj
            msgres.Distance=Object.distance
            msgres.AngleFromView=Object.angle        
            msgres.Status=status
            pubMap.publish(msgres)
            #rospy.logerr("SENSOR FUSION" + str(msgres.Class))
    def remove(self,Object,ispub):
        conf=Object.confidence
        if conf<1:
            conf+=0.1
        self.listOfObjects.remove(Object)
        if ispub:
            msgres=ToMap()
            msgres.Class=Object.classObj
            msgres.Distance=Object.distance
            if Object.x==1 and Object.y==0:
                msgres.AngleFromView=270
            elif Object.x==-1 and Object.y==0:
                msgres.AngleFromView=90
            else:
                msgres.AngleFromView=getAngleFromView(Object,1)
            msgres.Status=STATUS.REMOVE
            pubMap.publish(msgres)
        return conf
    def CheckIfPartOfObject(self,newobj,obj): #Object might be part of big object but go to his rect
        if (obj.x+obj.width) < (newobj.x+newobj.width) and (obj.x) > (newobj.x) and (obj.y) > (newobj.y) and (obj.y+obj.height) < (newobj.y+newobj.height) :
            if  obj.classObj==newobj.classObj:
                return 1
        if (newobj.x+newobj.width) < (obj.x+obj.width) and (newobj.x) > (obj.x) and (newobj.y) > (obj.y) and (newobj.y+obj.height) < (obj.y+obj.height)and obj.classObj==newobj.classObj:
            if  obj.classObj==newobj.classObj:
                return 1
        return 0
    def CompareAngle(self,obj1,obj2):
        if obj1.angle>300:
            bufobj1=(360-obj1.angle)*-1
        if obj1.angle>130:
            bufobj1=(180-obj1.angle)*-1
        else:
            bufobj1=obj1.angle
        if obj2.angle>300:
            bufobj2=(360-obj2.angle)*-1
        if obj2.angle>130:
            bufobj2=(180-obj1.angle)*-1
        else:
            bufobj2=obj2.angle
       
        return  abs(bufobj1-bufobj2)<self.DiffAngle
    def IfOnRoad(self, obj):

        if self.LaneLeft==None:
            return
        return True
        dLeft=(obj.x-self.LaneLeft[0].x)*(self.LaneLeft[1].y-self.LaneLeft[0].y)-(obj.y-self.LaneLeft[0].y)*(self.LaneLeft[1].x-self.LaneLeft[0].x)
        dRight=(obj.x-self.LaneRight[0].x)*(self.LaneRight[1].y-self.LaneRight[0].y)-(obj.y-self.LaneRight[0].y)*(self.LaneRight[1].x-self.LaneRight[0].x)
       
        #rospy.logerr(dLeft)
        #rospy.logerr(dRight)
        if dLeft>0 and dRight<0:
            return True
        else:
            return False
    def findbyCoordinates(self,newobj):
        listref=[]
        if newobj.distance==-1:
            return []
        for i in self.listOfObjects:
            if self.CompareAngle(i,newobj):
                if i.classObj==newobj.classObj:
                    if newobj.distance!=-1:
                        i.distance=newobj.distance
                    listref.append(i)
                    return listref

            if newobj.classObj in [str(SONARS.FORWARD),str(SONARS.BACKWARD),str(SONARS.LEFT),str(SONARS.RIGHT)] or i.classObj  in [str(SONARS.FORWARD),str(SONARS.BACKWARD),str(SONARS.LEFT),str(SONARS.RIGHT)]:
                continue
            if self.CheckIfPartOfObject(newobj,i):
                if newobj.distance!=-1:
                    i.distance=newobj.distance
                if i.confidence<1:
                    i.confidence+=0.05
                listref.append(i)
                return listref
            if (abs((i.x+i.width/2)-(newobj.x+newobj.width/2))<self.DiffX and abs(i.y-newobj.y)<self.DiffY and i.classObj==newobj.classObj):
                listref.append(i)
                return listref 
        return listref   
    def ProcObject(self,ObjectOnARoad):
        

        listref=self.findbyCoordinates(ObjectOnARoad)
        if len(listref)==0:
            self.add(ObjectOnARoad,STATUS.NEW)
        else:
            confMax=0
            for i in listref:
                conf=self.remove(i,False)
                if conf>confMax:
                    confMax=conf
            ObjectOnARoad.confidence=confMax+0.1
            self.add(ObjectOnARoad,STATUS.MODIFIED)
    def AddFromNS(self,newObj):
        for i in self.listOfObjects:
            #if newObj.classObj!=i.classObj or newObj.classObj not in ["Light","LightLeft","LightRight"]:
            #    continue
            if self.CompareAngle(i,newObj):
                newObj.width=i.width
                newObj.height=i.height
                newObj.x=i.x
                newObj.y=i.y
                if newObj.classObj in ["Left","Right","Ordinary"]:
                    pubLight.publish(newObj.classObj)
                    newObj.classObj=i.classObj
                conf=self.remove(i,False)
                if newObj.confidence<1: 
                    newObj.confidence=conf+0.1 
                self.add(newObj,STATUS.MODIFIED)
                #rospy.logerr("OBJECT MODIFIED OBJECT MODIFIED")
                return
        self.add(newObj,STATUS.NEW)

    def toString(self):
        bufstr=""
        for i in self.listOfObjects:
            if i.confidence>0.5:
                bufstr+=i.classObj+" Width:"+str(i.width)+" Height:"+str(i.height)+" Dist:"+str(i.distance)+" X:"+str(i.x)+" Y:"+str(i.y)+";"+"Angle:"+str(i.angle)
        return bufstr    
    def ProcSonar(self,id,value):
        if id==SONARS.FORWARD  and value>0 and value<90:
            if value<10 and self.LastSonarForward<14: 
                msg=ObjectOnARoad()
                msg.X=0
                msg.Y=0
                msg.Height=0
                msg.Width=0
                msg.Distance=value
                msg.Class="SONARS.FORWARD"
                pubAutomove.publish(msg)
                #pubAutomove.publish("FStop")
                self.wasStoppedForward=True
            if value>16 and self.wasStoppedForward:
                msg=ObjectOnARoad()
                msg.X=0
                msg.Y=0
                msg.Height=0
                msg.Width=0
                msg.Distance=value
                msg.Class="SONARS.FORWARD"
                pubAutomove.publish(msg)
                #pubAutomove.publish("FMove")
                self.wasStoppedForward=False
            self.LastSonarForward=value
            objectOnRoad=Object(1,0,value,str(id),0,0,)
            self.ProcObject(objectOnRoad) 
        elif id==SONARS.BACKWARD  and value>0 and value<45:
            if value<10 and self.LastSonarBackward<18 :
                #pubAutomove.publish("BN")
                self.wasStoppedBackward=True
            if value>15 and self.wasStoppedBackward :
                #pubAutomove.publish("BR")
                self.wasStoppedBackward=False
            self.LastSonarBackward=value
            objectOnRoad=Object(0,-1,value,str(id),0,0)
            self.ProcObject(objectOnRoad)
        elif id==SONARS.LEFT and value>0 and value<45:
            objectOnRoad=Object(-1,0,value,str(id),0,0)
            self.ProcObject(objectOnRoad)
        elif id==SONARS.RIGHT and value>0 and value<45:
            objectOnRoad=Object(1,0,value,str(id),0,0)
            self.ProcObject(objectOnRoad)    

sensorFusion=SensorFusion()
class Object():
    def __init__(self,X,Y,D,Class,Width,Height,camera_id=1):
        self.x=X
        self.y=Y
        self.distance=D
        self.classObj=Class

        self.width=Width
        self.height=Height 
        if Class in ["Red","Green","Greenleft","Greenright"]:
            self.confidence=0.4
        else:   
            self.confidence=0.6

        self.time=time.time()
        if self.x==1 and self.y==0:
            self.angle=360
        elif self.x==-1 and self.y==0:
            self.angle=180
        elif self.x==1 and self.y==1:
            self.angle=270
        elif self.x==-1 and self.y==-1:
            self.angle=180    
        else:
            self.angle=getAngleFromView(self,camera_id)   
    
def getAngleFromView(obj,camera_id):
    if camera_id==0:
        center=360
        angleview=45
    else:
        center=180
        angleview=65
    x1=obj.x+obj.width/2
    if x1>352:
        x1=obj.x+obj.width/2-352
        Angle=(math.degrees(math.atan((2*x1 * math.tan(math.radians(45)))/704)))
    else:
        Angle=center-(angleview-math.degrees(math.atan((2*x1 * math.tan(math.radians(45)))/704)))
    return Angle
def NewObject(msg):
    global sensorFusion
    objectOnRoad=Object(msg.X,msg.Y,msg.Distance,msg.Class,msg.Width,msg.Height,msg.camera)
    sensorFusion.ProcObject(objectOnRoad)
        

 
def PerformmessageSonic(msg):
    global LastSonarForward,LastSecondSonar,wasStoppedForward,wasStoppedBackward  
    #rospy.logerr(msg)  
    firstSonar  = int(msg.top)
    SecondSonar = int(msg.bottom)
    ThirdSonar  = int(msg.left)
    sensorFusion.ProcSonar(SONARS.FORWARD,firstSonar) 
    sensorFusion.ProcSonar(SONARS.BACKWARD, SecondSonar)    
    sensorFusion.ProcSonar(SONARS.LEFT, ThirdSonar)
        
def PerformmessageNS(msg):
    if msg.isforCar:
        objectFromNS=Object(0,0,msg.D,NavObjects[msg.Type],0,0)
        objectFromNS.angle=msg.R
        sensorFusion.AddFromNS(objectFromNS)
        #rospy.logerr(msg)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            rospy.Subscriber('Objects',ObjectOnARoad,NewObject)
            rospy.Subscriber('Ultrasonic',Ultrasonic,PerformmessageSonic)

            rospy.Subscriber('NSToSensorFusion',Lights_Signs,PerformmessageNS)
            rospy.Subscriber('LanesContour',Lane,Performlanes)
            thread = threading.Thread(target=callback)
            thread.start()
            rospy.spin()
           
    finally:
        cv2.destroyAllWindows()
