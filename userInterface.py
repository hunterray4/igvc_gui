import pygame, pygame_menu
import rospy
from std_msgs.msg import Int8, UInt16MultiArray, Float64, Bool
# from pacmod_msgs.msg import PacmodCmd, PositionWithSpeed, SystemRptInt
# from sensor_msgs.msg import Joy

drive_pub = rospy.Publisher('/selfdrive/status', Int8, queue_size=10)
run_pub = rospy.Publisher('/gem/operation_mode', Int8, queue_size=10)

pygame.init()
surface = pygame.display.set_mode((1000, 800))

def set_driveMode(value1, driveMode):
    drive_pub.publish(driveMode)
    print(value1)


def set_run_modes(value2, run_modes):
    run_pub.publish(run_modes)
    print(value2)


##HELLOOO

def start_the_game():
    drive_pub.publish(driveMode)
    run_pub.publish(run_modes)

menu = pygame_menu.Menu(800, 1000, 'AVRAD User Interface', theme=pygame_menu.themes.THEME_GREEN)

menu.add_selector('Drive Mode :', [('Manual Drive', 0), ('Tele-Op', 1), ('Autonomous Self-Drive', 2)], onchange=set_driveMode)
menu.add_selector('Run Mode :', [('NOT AUTONOMOUS MODE', 6), ('Regular Self-drive', 0), ('E-Stop Qualification', 1), ('Straight Lane Keeping Qualification', 2), 
        ('Left Turn Qualification', 3), ('Right Turn Qualification', 4), ('Stop Sign Detection Qualification', 5)], onchange=set_run_modes)
menu.add_button('Run', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)