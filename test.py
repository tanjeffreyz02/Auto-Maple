import mss, cv2, time, threading, vkeys, math, csv, winsound
import numpy as np
import keyboard as kb
# from vkeys import key_down, key_up
import os
from os import listdir
from os.path import isfile, join
# import csv

# from os import listdir
# from os.path import isfile, join

# sequence = []

# class Point:
#     def __init__(self, x, y, frequency=1, attack=True, n=1, extras=[]):
#         self.location = (x, y)
#         self.frequency = frequency
#         self.counter = 0
#         self.attack = attack
#         self.n = n
#         self.extras = extras

#     def execute(self):
#         if self.counter == 0:
#             move(self.location)
#             for e in self.extras:
#                 exec(f'commands.{e}()')
#             if self.attack:
#                 commands.shikigami('left', self.n)
#                 commands.shikigami('right', self.n)
#         self.counter = (self.counter + 1) % self.frequency

# frequency, attack, n, extras = 1, True, 1, []

# def load():
#     global sequence, frequency, attack, n, extras
#     sequence = []

#     path = './bots'
#     csv_files = [f for f in listdir(path) if isfile(join(path, f)) and '.csv' in f]
#     if not csv_files:
#         print('Unable to find .csv bot file.')
#     else:
#         with open(join(path, csv_files[0])) as f:
#             csv_reader = csv.reader(f)
#             for row in csv_reader:
#                 assert len(row) > 1, 'A Point must at least have an x and y position'
#                 frequency, attack, n, extras = 1, True, 1, []
#                 for a in row[2:]:
#                     exec('global frequency, attack, n, extras; ' + str(a))        # If you don't use global, the variables are assigned LOCALLY INSIDE exec's frame!!!
#                 print(frequency, attack, n, extras)
#                 sequence.append(Point(float(row[0]), float(row[1]), frequency, attack, n, extras))
            

# # extras=[]
# # string = "extras=['fox']"
# # exec(string)
# # print(extras)
# # print([exec(a) for a in row[2:]])
# load()

# # print(csv_files)


# import cv2
# import numpy as np

# up_template = cv2.imread('assets/up_template.png', 0)
# down_template = cv2.imread('assets/down_template.png', 0)
# left_template = cv2.imread('assets/left_template.png', 0)
# right_template = cv2.imread('assets/right_template.png', 0)



# def _multi_match(frame, template, threshold=0.70):
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
#         locations = np.where(result >= threshold)
#         return list(zip(*locations[::-1]))

# frame = cv2.imread('C:/Users/tanje/Desktop/Rune Detection/cropped/cropped1.jpg')
# locs = _multi_match(frame, up_template)

# print(locs)


# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.imshow('edges', up_template)
# cv2.waitKey(0)


# lst1 = [1]
# lst2 = lst1

# lst1 = lst1 + lst2
# print(lst1 is lst2)


# lst1 = [1]
# lst2 = lst1

# lst1 += lst2
# print(lst1 is lst2)


# import cv2
# import numpy as np
# import os

# ## Read
# # img = cv2.imread('C:/Users/tanje/Desktop/Rune Detection/cropped/cropped1.jpg')
# os.chdir('C:/Users/tanje/Desktop/Rune Detection/cropped/')
# images = [file for file in os.listdir() if os.path.isfile(file) and '.jpg' in file]

# for file_name in images:
#     ## convert to hsv
#     img = cv2.imread(file_name)
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     ## mask of green (36,25,25) ~ (86, 255,255)
#     # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
#     mask = cv2.inRange(hsv, (1, 100, 100), (75, 255, 255))

#     ## slice the green
#     imask = mask>0
#     green = np.zeros_like(img, np.uint8)
#     green[imask] = img[imask]

#     # show
#     cv2.imshow('green', green)
#     cv2.waitKey(0)

# import math
# def add(x, y):
#     return x + y

# def mul(x, y):
#     return x * y

# print((add if 4 < 3 else mul)(2, 3))

# eboss_template = cv2.imread('assets/eboss_template.jpg', 0)
# # print(eboss_template)
# # minimap_template = cv2.imread('assets/minimap_template.jpg', 0)


# def multi_match(frame, template, threshold=0.63):
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
#         locations = np.where(result >= threshold)
#         return list(zip(*locations[::-1]))


# os.chdir('C:/Users/tanje/Desktop')

# files = [file for file in os.listdir() if os.path.isfile(file) and '.jpg' in file]
# for file_name in files:
#     frame = cv2.imread(file_name)
#     height, width, channels = frame.shape
#     frame = frame[height//4:3*height//4, width//4:3*width//4]
# #     print(eboss_template)
#     # cv2.imshow('', eboss_template)
#     cv2.imshow('', frame)
# #     cv2.imshow('', minimap_template)
#     cv2.waitKey(0)
#     # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     print(multi_match(frame, eboss_template, 0.9))

print('beginning')

def test(i):
    def inner():
        while True:
            print(i)
            time.sleep(1)
    return inner

thread1 = threading.Thread(target=test(1))
thread1.daemon = True
thread1.start()
thread2 = threading.Thread(target=test('a'))
thread2.daemon = True
thread2.start()

while True:
    time.sleep(1)
    print(33)