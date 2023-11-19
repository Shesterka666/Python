#!/usr/bin/env python
import numpy as np
import cv2
import socket
import rospy
import glob
import time
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from driver.msg import MatMask
def undisort(image):
    #dist = np.array([-8.87526040e+00, 1.29373398e+02, -7.94401950e-02,1.27190163e-01, 0])
    #newcameramtx =np.array([[ 2.06364111e+03 , 0.00000000e+00 , 2.75231745e+02],
    #[ 0.00000000e+00 , 8.32927185e+02 , 1.55751891e+02],
    #[ 0.00000000e+00 , 0.00000000e+00 , 1.00000000e+00]])

    #mtx = np.array([[ 2.53495726e+03 , 0.00000000e+00 , 2.55682611e+02],
    #[ 0.00000000e+00 , 9.96872166e+02 , 1.64156218e+02],
    #[ 0.00000000e+00 , 0.00000000e+00 , 1.00000000e+00]])
    #roi=(33,7,431,304)


    dist = np.array([-0.47707499, 0.17952963, -0.01711304, 0.00985758, 0])

    mtx = np.array([[322.01254797, 0., 231.13229282],
    [0., 312.00676229, 166.91633028],
    [0., 0., 1.]])

    newcameramtx = np.array([[215.70178223, 0., 243.22750551],
    [0., 207.62965393, 153.06267954],
    [0., 0., 1.]])
    roi = (18, 27, 447, 250)

    img = image
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (480, 320), 5)
    dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

    x, y, w, h = roi
    dst = dst[y:y + h, x:x + w]

    #cv2.imshow("dsd", dst)
    #cv2.waitKey(1)
    return dst



def VideoStreamingTest():
    cap = cv2.VideoCapture("/home/max/output.h264")
    originals = glob.glob("/home/max/segmentation/orig*")
    originals.sort()
    segm = glob.glob("/home/max/segmentation/segm*")
    segm.sort()
    while (cap.isOpened()): 
        #frameoriginals=cv2.imread(originals[i])
        _,framesegm=cap.read()
        frameoriginals=framesegm
        msg=MatMask()

        imageRosMask = CvBridge().cv2_to_imgmsg(framesegm, "rgb8")
        msg.Mask=imageRosMask
        imageRosOriginal = CvBridge().cv2_to_imgmsg(frameoriginals, "rgb8")
        msg.Original=imageRosOriginal
        pub.publish(imageRosOriginal)
        cv2.imshow("video",frameoriginals)
	cv2.imshow("videoSegm",framesegm)
        key = cv2.waitKey(100) % 0x100
        if key == 27:
            break
    



if __name__ == '__main__':
    rospy.loginfo("111")
    pub = rospy.Publisher('FromRaspberry', Image, queue_size='1')
    rospy.init_node('Segmentation')
    VideoStreamingTest()

