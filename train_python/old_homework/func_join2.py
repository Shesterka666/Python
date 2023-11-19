#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np
import copy
import func_join2
import math

def find_near_lines(left_lines,right_lines):
    for z in range(0,len(right_lines)):
        for x in range(0,5):
            right_lines[z][x] = int(right_lines[z][x])


    right=[]
    list_all_right=[0,0,0,0,0,]
    if (len(right_lines) != 1):
        for i in range(0,len(right_lines)):
            l, s = ((list_all_right,right_lines[i] ), (list_all_right, right_lines[i]))[list_all_right < right_lines[i]]
            list_all_right = [l[x] + s[x] if x < len(s) else l[x] + 0 for x in range(len(l))]
        for i in range(0,5):
            list_all_right[i]=list_all_right[i]/len(right_lines)
        list_all_right=[list_all_right]
        right = list_all_right
        #print("Del_llines_right_1", list_all_right)
    else:
        #print("Del_llines_right_2", right_lines)
        right = right_lines

    left =[]
    list_all_left=[0,0,0,0,0,]

    try:
        #print(len(left_lines[0]))
        if (len(left_lines) != 1):
            for i in range(0, len(left_lines)):
                l, s = ((list_all_left, left_lines[i]), (list_all_left, left_lines[i]))[list_all_left < left_lines[i]]

                list_all_left = [l[x] + s[x] if x < len(s) else l[x] + 0 for x in range(len(l))]
            for i in range(0, 5):
                list_all_left[i] = list_all_left[i] / len(left_lines)
            left = [list_all_left]
        else:
            left = left_lines
        qq = abs(right[0][1] - left[0][1])
        if (qq < 20):
            return left[0][0]
        return None

    except TypeError:
        left = [left_lines]
        qq = abs(right[0][1] - left[0][1])
        if (qq < 20):
            return left[0][0]
        return None

def find_points(image,cnts,Pedestrian):
    list=[]
    ss = DetectShape()
    for c in cnts:
        q = ss.detect(c,Pedestrian)


        if (q is None or q > 280 or q < 25):
            continue

        cX = None
        cY = None
        M = cv2.moments(c)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except:
            cX = None
            cY = None

        if(cX <= 90 and cY <= 90):
            #print("BOX", q,cX,cY)
            continue
        # if(cY != None and cY > 180 and q < 35):
        #     continue

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], 0, (0, 255, 0), 4)


        r1 = ((box[0][0] - box[1][0]) ** 2 + (box[0][1] - box[1][1]) ** 2) ** 0.5
        r2 = ((box[1][0] - box[2][0]) ** 2 + (box[1][1] - box[2][1]) ** 2) ** 0.5
        qwe = image
        param2 = float(r2 / r1)
        param = float(r1 / r2)

        # print("BOX___", box)
        # print("PARAM_1_2", param,param2)
        #print("SUPER_MEGA_PARAMETR__",param2,param,q)
        if(param > 3):
            continue

        # if (param > param2):
        #     k = param / param2
        #     if (k > 35):
        #         print("YDA4a__SUPER_MEGA_PARAMETR__", param2, param, k, q)
        #     else:
        #         continue
        # if (param < param2):
        #     k = param2 / param
        #     if (k > 35):
        #         print("YDA4a__SUPER_MEGA_PARAMETR__", param2, param, k, q)
        #     else:
        #         continue

        x = ( box[0][0] + box[1][0] )/2
        y = ( box[0][1] + box[1][1] )/2

        xx = (box[2][0] + box[3][0]) / 2
        yy = (box[2][1] + box[3][1]) / 2

        lenght_cent_line_box = ((xx - x)**2 + (yy - y)**2) ** 0.5

        ugol = math.atan2((yy - y), (xx - x))
        ugol = math.degrees(ugol)
        rotate1 = int(ugol)
        if( abs(rotate1) >=0 and abs(rotate1) <=10):
            continue

        #print("BOX", q, cX, cY, rotate1)


        #print("SIZE___", q,x,xx,y,yy,param,param2)


        if( lenght_cent_line_box > 35 and math.fabs(y - yy) < 25 ):
            continue

        #print("BIFBIG__",q)
        # if(q < 75 and (y >100 or yy > 100)):
        #     print("DRAW3___", q)
        #     continue
        # if(230 < q < 320):
        #     if((20 < y < 130) or (20 < yy < 130)):
        #         print("DRAW4___", q,y,yy,box)
        #         continue
        if(y == yy):
            #print("DRAW1___", q)
            continue
        if (x == xx):
            #print("DRAW2___", q)
            continue
        cv2.line(image, (x, y), (xx, yy), (255, 255, 255), 4)
        cv2.drawContours(image, [box], 0, (0, 0, 255), 4)

        cv2.drawContours(qwe, [box], 0, (0, 0, 255), 4)
        cv2.imshow("FindContours",qwe)
        list.append([x,y,xx,yy])

    return list

# write list conversely
def pre_list(list):
    ll=[]
    for i in range(0,len(list)):
        ll.append(list[len(list)-1-i])
    return ll

def equence(list):
    final=[]
    final.append(list[0])
    z = 0
    for i in range(1,len(list)):
        q_1 = list[z][3]-list[z][1]
        q_2 = list[z][2]-list[z][0]
        x = (q_2*( abs(list[i][1] - list[z][1]) ))/q_2 + list[z][0]
        if( abs( list[i][0] - x ) <60):
            distance = round(((list[i][2] - list[z][0]) ** 2 + (list[i][1] - list[z][3]) ** 2) ** 0.5)
            if(distance > 200):
                continue
            final.append(list[i])
            z = i
            continue
        else:
            continue
    return  final

def draw_line(image , final):
    i=0
    for i in range(len(final)-1):
            cv2.line(image,(final[i][1],final[i][2]),(final[len(final)-1][3],final[len(final)-1][4]),(255, 0, 0),2,2)
    if(len(final)):
        cv2.line(image, (final[0][1], final[0][2]), (final[0][3], final[0][4]), (255, 0, 0),
                 3, 2)

def find_line(list):
    i = 0
    final = []
    for i in range(len(list)):
        ugol = math.atan2((list[i][3] - list[i][1]),
                          (list[i][2] - list[i][0]))
        ugol = round(math.degrees(ugol))
        if(i !=0):
            if((abs(ugol - final[0][0]) < 25)):
                final.append([ugol, list[i][0], list[i][1], list[i][2], list[i][3]])
                continue
            else:
                continue
        final.append([ugol,list[i][0],list[i][1],list[i][2],list[i][3]])
    if(len(final)==0):
        return None
    return final


def transform_video(canny):
    _, cnts, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return cnts


class DetectShape:
    def __init__(self):
        pass
    def detect(self , c,Pedestrian):
        peri = cv2.arcLength(c, True)
        return peri

         # if(Pedestrian == True):
         #     if (peri < 280 and peri > 90):
         #            return None
         #    if (peri < 280 and peri > 20):
         #        return peri
         #    return None


# def algo(frame):
#     isReal = True
#     global ugol_last, right, left, prev_left_lines, prev_right_lines, direction
#     frame = adjust_gamma(frame,0.9)
#     frame = cv2.resize(frame, (480, 320))
#     frame = frame[100:320]
#
#     cannyim = function.segment(frame)
#     cv2.imshow("q", cannyim)
#     cv2.moveWindow("q",1100,10)
#     left_lines=None
#     left_lines = function.SUPER_PUPER_DUPER(cannyim,frame,Pedestrian)
#     lines=[]
#     lines=cv2.HoughLinesP(cannyim, rho=1, theta=np.pi / 180, threshold=9, minLineLength=15, maxLineGap=4)
#     if not lines  is None and lines[0][0][0]:
#         for i in lines:
#             rotate = math.atan2((i[0][3] - i[0][1]), (i[0][2] - i[0][0]))
#             rotate = abs(int(math.degrees(rotate)))
#             if(rotate >= 45 or rotate<=145):
#                 ddd=1
#             else:
#                 lines.remove(i)
#
#
#     if lines is None:
#         return
#     linesimg = function.draw_lines_from_haf(lines, frame)
#     if left_lines is None or left_lines == False:
#
#         left_lines, right_lines, isReal = function.findLinesFromCenter(lines, linesimg, Pedestrian)
#     else:
#         right_lines = function.findRightLineFromCenter(lines, linesimg, Pedestrian)
#     cv2.imshow('HAPH', linesimg)
#     cv2.moveWindow("HAPH", 1100, 400)
#     k = cv2.waitKey(1) & 0xFF
#
#     if left_lines == 0:
#         return ugol_last
#     if len(right_lines) == 0:  ### tyt cvoe napisatb
#         return ugol_last
#
#
#     for i in range(len(right_lines)):
#         right_lines[i] = [int(item) for item in right_lines[i]]
#     try:
#         for i in range(len(left_lines)):
#             left_lines[i] = [int(item) for item in left_lines[i]]
#     except TypeError:
#         left_lines = [int(item) for item in left_lines]
#
#     firsty = function.draw_lines(left_lines, frame)
#     firsty = function.draw_lines(right_lines, frame)
#
#     if (left_lines != False or right_lines != False):
#         left = left_lines
#         right = right_lines
#     else:
#         left_lines = left
#         right_lines = right
#
#     for i in range(len(right_lines)):
#         right_lines[i] = [int(item) for item in right_lines[i]]
#     try:
#         #print(len(left_lines[0]))
#         for i in range(len(left_lines)):
#             left_lines[i] = [int(item) for item in left_lines[i]]
#
#     except TypeError:
#         left_lines = [int(item) for item in left_lines]
#
#     new_left=[[0,0,0,0,0]]
#     new_right=[[0,0,0,0,0]]
#     centr_x, centr_y, cx1, cx2, cy1, cy2, kbase = function.new_direct_line(firsty, left_lines, right_lines,new_left,new_right)
#     print(new_left , new_right )
#
#     function.for_direct_move(frame,lines,new_left,new_right)
#
#
#     ugol1 = func_join2.find_near_lines(left_lines, right_lines)
#     if (ugol1 != None):
#         return ugol1
#     ##################
#
#     if centr_x is None:
#         return ugol_last
#     left_lines=new_left
#     right_lines=new_right
#     centr_x = int(centr_x)
#     centr_y = int(centr_y)
#     ugol = function.ugol(firsty, centr_x, centr_y, cx1, cx2, cy1, cy2, left_lines, right_lines)
#     print("ZZZZZ___",centr_x, centr_y)
#
#
#     if (abs(k) < 1.5 and isReal == False):
#         ugol = -90
#     if (abs(k)<1.5 and isReal==False):
#         ugol=-90
#     cv2.line(firsty, (centr_x, centr_y), (230, 275), (0, 0, 255), 1, 1)
#     if (fm < 10):
#         ugol = ugol_last
#         cv2.putText(frame, "BLUURRREEDDD FUCK", (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5, cv2.LINE_AA)
#
#
#     raznost = centr_x - 230
#     if(abs(raznost) < 20):
#         #cv2.putText(frame, str(raznost)+"  malo", (170, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#         cv2.putText(frame, str(0), (60, 60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (250, 190, 100), 4)
#         cv2.imshow('lines', firsty)
#         cv2.moveWindow('lines', 620, 10)
#         return 0
#
#     if( 20 <= abs(raznost) <= 40):
#         #cv2.putText(frame, str(raznost)+"  sredne", (170, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#         cv2.putText(frame, str(int(ugol*0.8)), (60, 60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (250, 190, 100), 4)
#         cv2.imshow('lines', firsty)
#         cv2.moveWindow('lines', 620, 10)
#         return int(ugol*0.8)
#
#     cv2.putText(frame, str(ugol), (60, 60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (250, 190, 100), 4)
#     cv2.putText(frame, str(raznost), (170, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#     cv2.imshow('lines', firsty)
#     cv2.moveWindow('lines', 620, 10)
#     return ugol