#!/usr/bin/env python

import rosbag
import tf

import matplotlib.pyplot as plt
from HTMLParser import HTMLParser
from sys import argv
import xml.etree.ElementTree as ET
import matplotlib as mpl
import matplotlib.patches as patches



class husky_data(object): 
    def __init__(self):
        self.x = []
        self.y = []
        self.quaternion = []
        self.color = 'black'
        self.scans = []


if __name__ == "__main__":

    NUMBER_HUSKIES = int(argv[1])

    pose_offset = []
    if NUMBER_HUSKIES == 4:
        pose_offset += [[-5,-7,'yellow']]
        pose_offset += [[-5,-9,'green']]
        pose_offset += [[-7,-7,'red']]
        pose_offset += [[-7,-9,'lime']]
        bagfile = '/home/ntbeyers/Desktop/Bagfiles/SimulationData/4Robots/2016-04-26-18-33-04.bag'
        worldfile = '/home/ntbeyers/sim_tools_husky/src/my_husky_sim/worlds/ssrr_mid.world'
        axes = [-8,10, -10, 8]

    if NUMBER_HUSKIES == 8:
        pose_offset += [[-5,-7,'yellow']]
        pose_offset += [[-7,-7,'green']]
        pose_offset += [[-5,-11,'red']]
        pose_offset += [[-7,-9,'lime']]
        pose_offset += [[-7,-5,'limegreen']]
        pose_offset += [[-5,-9,'crimson']]
        pose_offset += [[-5,-5,'gold']]
        pose_offset += [[-7,-11,'darkgreen']]
        bagfile = '/home/ntbeyers/Desktop/Bagfiles/SimulationData/8Robots/2016-04-26-20-27-58.bag'
        worldfile = '/home/ntbeyers/sim_tools_husky/src/my_husky_sim/worlds/8_robot.world'
        axes = [-10,10, -12, 10]

    if NUMBER_HUSKIES == 20:
        pose_offset += [[0,0,'yellow']]
        pose_offset += [[0,-2,'green']]
        pose_offset += [[0,-4,'gold']]
        pose_offset += [[0,-6,'red']]
        pose_offset += [[0,-8,'darkgreen']]
        pose_offset += [[-2,-0,'firebrick']]
        pose_offset += [[-2,-2,'chartreuse']]
        pose_offset += [[-2,-4,'springgreen']]
        pose_offset += [[-2,-6,'greenyellow']]
        pose_offset += [[-2,-8,'mediumspringgreen']]
        pose_offset += [[-4,-0,'goldenrod']]
        pose_offset += [[-4,-2,'forestgreen']]
        pose_offset += [[-4,-4,'orange']]
        pose_offset += [[-4,-6,'crimson']]
        pose_offset += [[-4,-8,'seagreen']]
        pose_offset += [[-6,-0,'darkred']]
        pose_offset += [[-6,-2,'lime']]
        pose_offset += [[-6,-4,'lightgreen']]
        pose_offset += [[-6,-6,'limegreen']]
        pose_offset += [[-6,-8,'mediumseagreen']]
        bagfile = '/home/ntbeyers/Desktop/Bagfiles/SimulationData/20Robots/vid6.bag'
        worldfile = '/home/ntbeyers/sim_tools_husky/src/my_husky_sim/worlds/20_robot.world'
        axes = [-20,20, -20, 20]



    bag = rosbag.Bag(bagfile)

    data_list = []
    for husky_num in range(NUMBER_HUSKIES):
        topic_list = []
        namespace ='husky' + str(husky_num+1)
        topic_list += ['/' + namespace + '/odometry/gps']
        #topic_list += ['/husky' + str(husky_num+1) + '/imu/data']
        #topic_list += ['/husky' + str(husky_num+1) + '/scan']
        print topic_list
        data = husky_data()
        for topic, msg, t in bag.read_messages(topics=topic_list):
            if topic == topic_list[0]:
                data.x += [msg.pose.pose.position.x + pose_offset[husky_num][0]]
                data.y += [msg.pose.pose.position.y + pose_offset[husky_num][1]]
                data.color = pose_offset[husky_num][2]
            # if topic == topic_list[1]:
            #     quaternion = [msg.orientation.x, msg.orientation.y,msg.orientation.z, msg.orientation.w]
            #     data.quaternion += [quaternion]
            # if topic == topic_list[2]:
            #     data.scans += [msg.ranges]

        data_list += [data]
    bag.close()


    fig1 = plt.figure()
    ax = fig1.add_subplot(111, aspect='equal')

    for husky in data_list:
        plt.plot(husky.x[::5], husky.y[::5], '-o' , c=husky.color, markeredgecolor='none')


    world = open(worldfile,'r').read()

    root = ET.fromstring(world)

    targets = []
    walls = []
    obstacles = []
    for child in root.find('world').find('state'):
        model = child.attrib.get('name')
        if str(model)[:8] == 'unit_box':
            pose = child.find('pose').text.split()[:2]
            targets += [pose]
        if str(model)[:8] == 'jersey_b':
            pose = child.find('pose').text.split()[:6]
            pose = [pose[0], pose[1], pose[5]]
            walls += [pose]
        if str(model)[:8] == 'Construc':
            pose = child.find('pose').text.split()[:2]
            obstacles += [pose]
    
    height = .5
    for target in targets:
        x = float(target[0]) - height/2
        y = float(target[1]) - height/2

        r1 = patches.Rectangle((x,y), .7, .7, color="blue", alpha=0.50)
        ax.add_patch(r1)

    for obstacle in obstacles:
        x = float(obstacle[0])
        y = float(obstacle[1])

        r1 = patches.Circle((x,y), 0.2, color="black", alpha=0.50)
        ax.add_patch(r1)

    plt.xlim(axes[0], axes[1])
    plt.xlim(axes[2], axes[3])
        

    plt.show()





    