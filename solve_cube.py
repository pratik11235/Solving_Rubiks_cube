#from IPython.core.display import display_javascript
from distutils.command.sdist import sdist
from logging.config import DEFAULT_LOGGING_CONFIG_PORT
from signal import SIGFPE
from turtle import fd
import matplotlib.pyplot as plt
import itertools

from numpy import diagflat
from get_position import *

# Cube object class
class cube:
  # Initialization method
  def __init__(self, top, bottom, left, right, front, back):
    [[self.t1,self.t2,self.t3],[self.t4,self.t5,self.t6],[self.t7,self.t8,self.t9]] = top
    [[self.b1,self.b2,self.b3],[self.b4,self.b5,self.b6],[self.b7,self.b8,self.b9]] = bottom
    [[self.l1,self.l2,self.l3],[self.l4,self.l5,self.l6],[self.l7,self.l8,self.l9]] = left
    [[self.r1,self.r2,self.r3],[self.r4,self.r5,self.r6],[self.r7,self.r8,self.r9]] = right
    [[self.f1,self.f2,self.f3],[self.f4,self.f5,self.f6],[self.f7,self.f8,self.f9]] = front
    [[self.ba1,self.ba2,self.ba3],[self.ba4,self.ba5,self.ba6],[self.ba7,self.ba8,self.ba9]] = back
    self.solved = False
    if self.check_side_solved(top) and self.check_side_solved(bottom) and self.check_side_solved(left) and self.check_side_solved(right) and self.check_side_solved(front) and self.check_side_solved(back):
      self.solved = True
    else:
      self.solved = False
  
  def check_cube_solved(self):
    top = [[self.t1,self.t2,self.t3],[self.t4,self.t5,self.t6],[self.t7,self.t8,self.t9]]
    bottom = [[self.b1,self.b2,self.b3],[self.b4,self.b5,self.b6],[self.b7,self.b8,self.b9]]
    left = [[self.l1,self.l2,self.l3],[self.l4,self.l5,self.l6],[self.l7,self.l8,self.l9]]
    right = [[self.r1,self.r2,self.r3],[self.r4,self.r5,self.r6],[self.r7,self.r8,self.r9]]
    front = [[self.f1,self.f2,self.f3],[self.f4,self.f5,self.f6],[self.f7,self.f8,self.f9]]
    back = [[self.ba1,self.ba2,self.ba3],[self.ba4,self.ba5,self.ba6],[self.ba7,self.ba8,self.ba9]]
    if self.check_side_solved(top) and self.check_side_solved(bottom) and self.check_side_solved(left) and self.check_side_solved(right) and self.check_side_solved(front) and self.check_side_solved(back):
      self.solved = True
    else:
      self.solved = False

  # Function to check if a side is solved or not
  def check_side_solved(self, side):
    if len(side) == 3 and len(side[0]) == 3:
      first_val = side[0][0]
      for row in side:
        for val in row:
          if val != first_val:
            return False
      else:
        return True
    else:
      return False
  
  # Sub function to draw the rubik's cube at the given axis and color with correct annotation
  def draw_rect(self, axis, color, annotation):
    rectangle = plt.Rectangle((axis[1], axis[0]), 1, 1, fc=color, ec="black")
    plt.gca().add_patch(rectangle)
    plt.text(axis[1]+0.1275, axis[0]+0.1275, annotation, fontsize = 8)
  
  # Sub function to return the color name from color code to be used in matplotlib plotting function
  def ret_color(self, color_code):
    if color_code.lower() == "o":
      return "orange"
    elif color_code.lower() == 'r':
      return "red"
    elif color_code.lower() == 'g':
      return "green"
    elif color_code.lower() == 'b':
      return "blue"
    elif color_code.lower() == 'w':
      return "white"
    elif color_code.lower() == 'y':
      return "yellow"
    return "error"
    
  # Function to plot the cube when cube object is printed
  def __str__(self):
    plt.axes()
    # back face
    self.draw_rect((11,3), self.ret_color(self.ba1), "ba1")
    self.draw_rect((11,4), self.ret_color(self.ba2), "ba2")
    self.draw_rect((11,5), self.ret_color(self.ba3), "ba3")
    self.draw_rect((10,3), self.ret_color(self.ba4), "ba4")
    self.draw_rect((10,4), self.ret_color(self.ba5), "ba5")
    self.draw_rect((10,5), self.ret_color(self.ba6), "ba6")
    self.draw_rect((9,3), self.ret_color(self.ba7), "ba7")
    self.draw_rect((9,4), self.ret_color(self.ba8), "ba8")
    self.draw_rect((9,5), self.ret_color(self.ba9), "ba9")

    # left face
    self.draw_rect((8,0), self.ret_color(self.l1), "l1")
    self.draw_rect((8,1), self.ret_color(self.l2), "l2")
    self.draw_rect((8,2), self.ret_color(self.l3), "l3")
    self.draw_rect((7,0), self.ret_color(self.l4), "l4")
    self.draw_rect((7,1), self.ret_color(self.l5), "l5")
    self.draw_rect((7,2), self.ret_color(self.l6), "l6")
    self.draw_rect((6,0), self.ret_color(self.l7), "l7")
    self.draw_rect((6,1), self.ret_color(self.l8), "l8")
    self.draw_rect((6,2), self.ret_color(self.l9), "l9")
    
    # top face
    self.draw_rect((8,3), self.ret_color(self.t1), "t1")
    self.draw_rect((8,4), self.ret_color(self.t2), "t2")
    self.draw_rect((8,5), self.ret_color(self.t3), "t3")
    self.draw_rect((7,3), self.ret_color(self.t4), "t4")
    self.draw_rect((7,4), self.ret_color(self.t5), "t5")
    self.draw_rect((7,5), self.ret_color(self.t6), "t6")
    self.draw_rect((6,3), self.ret_color(self.t7), "t7")
    self.draw_rect((6,4), self.ret_color(self.t8), "t8")
    self.draw_rect((6,5), self.ret_color(self.t9), "t9")
    
    # right face
    self.draw_rect((8,6), self.ret_color(self.r1), "r1")
    self.draw_rect((8,7), self.ret_color(self.r2), "r2")
    self.draw_rect((8,8), self.ret_color(self.r3), "r3")
    self.draw_rect((7,6), self.ret_color(self.r4), "r4")
    self.draw_rect((7,7), self.ret_color(self.r5), "r5")
    self.draw_rect((7,8), self.ret_color(self.r6), "r6")
    self.draw_rect((6,6), self.ret_color(self.r7), "r7")
    self.draw_rect((6,7), self.ret_color(self.r8), "r8")
    self.draw_rect((6,8), self.ret_color(self.r9), "r9")
    
    # front face
    self.draw_rect((5,3), self.ret_color(self.f1), "f1")
    self.draw_rect((5,4), self.ret_color(self.f2), "f2")
    self.draw_rect((5,5), self.ret_color(self.f3), "f3")
    self.draw_rect((4,3), self.ret_color(self.f4), "f4")
    self.draw_rect((4,4), self.ret_color(self.f5), "f5")
    self.draw_rect((4,5), self.ret_color(self.f6), "f6")
    self.draw_rect((3,3), self.ret_color(self.f7), "f7")
    self.draw_rect((3,4), self.ret_color(self.f8), "f8")
    self.draw_rect((3,5), self.ret_color(self.f9), "f9")
    
    # below face
    self.draw_rect((2,3), self.ret_color(self.b1), "b1")
    self.draw_rect((2,4), self.ret_color(self.b2), "b2")
    self.draw_rect((2,5), self.ret_color(self.b3), "b3")
    self.draw_rect((1,3), self.ret_color(self.b4), "b4")
    self.draw_rect((1,4), self.ret_color(self.b5), "b5")
    self.draw_rect((1,5), self.ret_color(self.b6), "b6")
    self.draw_rect((0,3), self.ret_color(self.b7), "b7")
    self.draw_rect((0,4), self.ret_color(self.b8), "b8")
    self.draw_rect((0,5), self.ret_color(self.b9), "b9")

    print("Displaying the cube....")
    plt.axis('scaled')
    #ax = plt.gca()
    plt.gca().axes.xaxis.set_ticklabels([])
    plt.gca().axes.yaxis.set_ticklabels([])
    plt.show()

    return ""

  # Function to rotate the right face clockwise
  def right(self):
    self.ba3, self.ba6, self.ba9, self.t3, self.t6, self.t9, self.f3, self.f6, self.f9, self.b3, self.b6, self.b9 = self.t3, self.t6, self.t9, self.f3, self.f6, self.f9, self.b3, self.b6, self.b9, self.ba3, self.ba6, self.ba9
    self.r1, self.r2, self.r3, self.r6, self.r9, self.r8, self.r7, self.r4 = self.r7, self.r4, self.r1, self.r2, self.r3, self.r6, self.r9, self.r8
    
  # Function to rotate right face anti clockwise
  def rightbar(self):
    self.t3, self.t6, self.t9, self.f3, self.f6, self.f9, self.b3, self.b6, self.b9, self.ba3, self.ba6, self.ba9 = self.ba3, self.ba6, self.ba9, self.t3, self.t6, self.t9, self.f3, self.f6, self.f9, self.b3, self.b6, self.b9
    self.r7, self.r4, self.r1, self.r2, self.r3, self.r6, self.r9, self.r8 = self.r1, self.r2, self.r3, self.r6, self.r9, self.r8, self.r7, self.r4

  # Function to rotate left face clockwise
  def left(self):
    self.ba1, self.ba4, self.ba7, self.t1, self.t4, self.t7, self.f1, self.f4, self.f7, self.b1, self.b4, self.b7 = self.b1, self.b4, self.b7, self.ba1, self.ba4, self.ba7, self.t1, self.t4, self.t7, self.f1, self.f4, self.f7
    self.l1, self.l2, self.l3, self.l6, self.l9, self.l8, self.l7, self.l4 = self.l7, self.l4, self.l1, self.l2, self.l3, self.l6, self.l9, self.l8
  
  # Function to rotate left face anticlockwise
  def leftbar(self):
    self.b1, self.b4, self.b7, self.ba1, self.ba4, self.ba7, self.t1, self.t4, self.t7, self.f1, self.f4, self.f7 = self.ba1, self.ba4, self.ba7, self.t1, self.t4, self.t7, self.f1, self.f4, self.f7, self.b1, self.b4, self.b7
    self.l7, self.l4, self.l1, self.l2, self.l3, self.l6, self.l9, self.l8 = self.l1, self.l2, self.l3, self.l6, self.l9, self.l8, self.l7, self.l4
  
  # Function to rotate upper face clockwise
  def up(self):
    self.l3, self.l6, self.l9, self.f1, self.f2, self.f3, self.r7, self.r4, self.r1, self.ba9, self.ba8, self.ba7 = self.f1, self.f2, self.f3, self.r7, self.r4, self.r1, self.ba9, self.ba8, self.ba7, self.l3, self.l6, self.l9
    self.t1, self.t2, self.t3, self.t6, self.t9, self.t8, self.t7, self.t4 = self.t7, self.t4, self.t1, self.t2, self.t3, self.t6, self.t9, self.t8

  # Function to rotate upper face anti clockwise
  def upbar(self):
    self.f1, self.f2, self.f3, self.r7, self.r4, self.r1, self.ba9, self.ba8, self.ba7, self.l3, self.l6, self.l9 = self.l3, self.l6, self.l9, self.f1, self.f2, self.f3, self.r7, self.r4, self.r1, self.ba9, self.ba8, self.ba7
    self.t7, self.t4, self.t1, self.t2, self.t3, self.t6, self.t9, self.t8 = self.t1, self.t2, self.t3, self.t6, self.t9, self.t8, self.t7, self.t4

  # Function to rotate down face clockwise
  def down(self):
    self.f7, self.f8, self.f9, self.r9, self.r6, self.r3, self.ba3, self.ba2, self.ba1, self.l1, self.l4, self.l7 = self.l1, self.l4, self.l7, self.f7, self.f8, self.f9, self.r9, self.r6, self.r3, self.ba3, self.ba2, self.ba1
    self.b1, self.b2, self.b3, self.b6, self.b9, self.b8, self.b7, self.b4 = self.b7, self.b4, self.b1, self.b2, self.b3, self.b6, self.b9, self.b8

  # Function to rotate down face anti clockwise
  def downbar(self):
    self.l1, self.l4, self.l7, self.f7, self.f8, self.f9, self.r9, self.r6, self.r3, self.ba3, self.ba2, self.ba1 = self.f7, self.f8, self.f9, self.r9, self.r6, self.r3, self.ba3, self.ba2, self.ba1, self.l1, self.l4, self.l7
    self.b7, self.b4, self.b1, self.b2, self.b3, self.b6, self.b9, self.b8 = self.b1, self.b2, self.b3, self.b6, self.b9, self.b8, self.b7, self.b4

  # Front face clockwise
  def front(self):
    self.l7, self.l8, self.l9, self.t7, self.t8, self.t9, self.r7, self.r8, self.r9, self.b3, self.b2, self.b1 = self.b3, self.b2, self.b1, self.l7, self.l8, self.l9, self.t7, self.t8, self.t9, self.r7, self.r8, self.r9
    self.f1, self.f2, self.f3, self.f6, self.f9, self.f8, self.f7, self.f4 = self.f7, self.f4, self.f1, self.f2, self.f3, self.f6, self.f9, self.f8

  # Front face anti clockwise
  def frontbar(self):
    self.b3, self.b2, self.b1, self.l7, self.l8, self.l9, self.t7, self.t8, self.t9, self.r7, self.r8, self.r9 = self.l7, self.l8, self.l9, self.t7, self.t8, self.t9, self.r7, self.r8, self.r9, self.b3, self.b2, self.b1
    self.f7, self.f4, self.f1, self.f2, self.f3, self.f6, self.f9, self.f8 = self.f1, self.f2, self.f3, self.f6, self.f9, self.f8, self.f7, self.f4

  # Back face clockwise
  def back(self):
    self.l1, self.l2, self.l3, self.t1, self.t2, self.t3, self.r1, self.r2, self.r3, self.b9, self.b8, self.b7 = self.t1, self.t2, self.t3, self.r1, self.r2, self.r3, self.b9, self.b8, self.b7, self.l1, self.l2, self.l3
    self.ba1, self.ba2, self.ba3, self.ba6, self.ba9, self.ba8, self.ba7, self.ba4 = self.ba7, self.ba4, self.ba1, self.ba2, self.ba3, self.ba6, self.ba9, self.ba8

  # Back face anti clockwise
  def backbar(self):
    self.t1, self.t2, self.t3, self.r1, self.r2, self.r3, self.b9, self.b8, self.b7, self.l1, self.l2, self.l3 = self.l1, self.l2, self.l3, self.t1, self.t2, self.t3, self.r1, self.r2, self.r3, self.b9, self.b8, self.b7
    self.ba7, self.ba4, self.ba1, self.ba2, self.ba3, self.ba6, self.ba9, self.ba8 = self.ba1, self.ba2, self.ba3, self.ba6, self.ba9, self.ba8, self.ba7, self.ba4

  def copy(self):
    top = [[self.t1,self.t2,self.t3],[self.t4,self.t5,self.t6],[self.t7,self.t8,self.t9]]
    bottom = [[self.b1,self.b2,self.b3],[self.b4,self.b5,self.b6],[self.b7,self.b8,self.b9]]
    left = [[self.l1,self.l2,self.l3],[self.l4,self.l5,self.l6],[self.l7,self.l8,self.l9]]
    right = [[self.r1,self.r2,self.r3],[self.r4,self.r5,self.r6],[self.r7,self.r8,self.r9]]
    front = [[self.f1,self.f2,self.f3],[self.f4,self.f5,self.f6],[self.f7,self.f8,self.f9]]
    back = [[self.ba1,self.ba2,self.ba3],[self.ba4,self.ba5,self.ba6],[self.ba7,self.ba8,self.ba9]]

    return cube(top, bottom, left, right, front, back)

  def render_moves(self, moves, x = "n"):
    moves_arr = moves.split(" ")
    try:
      for i in moves_arr:
        if i.upper() == "R":
          self.right()
        elif i.upper() == "R'":
          self.rightbar()
        elif i.upper() == "L":
          self.left()
        elif i.upper() == "L'":
          self.leftbar()
        elif i.upper() == "U":
          self.up()
        elif i.upper() == "U'":
          self.upbar()
        elif i.upper() == "D":
          self.down()
        elif i.upper() == "D'":
          self.downbar()
        elif i.upper() == "F":
          self.front()
        elif i.upper() == "F'":
          self.frontbar()
        elif i.upper() == "B":
          self.back()
        elif i.upper() == "B'":
          self.backbar()
        elif i.upper() == " ":
          continue
        elif i.upper() == "":
          continue
        else:
          print("Error: There is some invalid move input in the entered moves string.")
          return
        if x.lower() == "y":
          print(self)
      self.check_cube_solved()
    except Exception as err:
      print(err)
      return
  
  def goal_test_fl_cross1(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8:
      return True
    else:
      return False

  def goal_test_fl_cross2(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6:
      return True
    else:
      return False

  def goal_test_fl_cross3(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6 and self.t5 == self.t8 and self.f2 == self.f5:
      return True
    else:
      return False

  def goal_test_fl_cross4(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6 and self.t5 == self.t8 and self.f2 == self.f5 and self.t5 == self.t6 and self.r4 == self. r5:
      return True
    else:
      return False

  def goal_test_fl_corner1(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6 and self.t5 == self.t8 and self.f2 == self.f5 and self.t5 == self.t6 and self.r4 == self. r5 and self.ba5 == self.ba7 and self.l3 == self.l5 and self.t1 == self.t5:
      return True
    else:
      return False

  def goal_test_fl_corner2(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6 and self.t5 == self.t8 and self.f2 == self.f5 and self.t5 == self.t6 and self.r4 == self. r5 and self.ba5 == self.ba7 and self.l3 == self.l5 and self.t1 == self.t5 and self.t7 == self.t5 and self.l5 == self.l9 and self.f5 == self.f1:
      return True
    else:
      return False

  def goal_test_fl_corner3(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6 and self.t5 == self.t8 and self.f2 == self.f5 and self.t5 == self.t6 and self.r4 == self. r5 and self.ba5 == self.ba7 and self.l3 == self.l5 and self.t1 == self.t5 and self.t7 == self.t5 and self.l5 == self.l9 and self.f5 == self.f1 and self.t5 == self.t9 and self.f5 == self.f3 and self.r5 == self.r7:
      return True
    else:
      return False

  def goal_test_fl_corner4(self):
    if self.t2 == self.t5 and self.ba5 == self.ba8 and self.t4 == self.t5 and self.l5 == self.l6 and self.t5 == self.t8 and self.f2 == self.f5 and self.t5 == self.t6 and self.r4 == self. r5 and self.ba5 == self.ba7 and self.l3 == self.l5 and self.t1 == self.t5 and self.t7 == self.t5 and self.l5 == self.l9 and self.f5 == self.f1 and self.t5 == self.t9 and self.f5 == self.f3 and self.r5 == self.r7 and self.t5 == self.t3 and self.ba5 == self.ba9 and self.r5 == self.r1:
      return True
    else:
      return False
  
  def find_moves(self, self_copy, goal_func1, goal_func2, moves_depth_limit):
    legal_moves = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]
    comb_count_limit = moves_depth_limit
    comb_count = 0
    new = []
    i = ""
    while goal_func1() == False:
      new.append(legal_moves)
      perf_moves = list(itertools.product(*new))
      for i in perf_moves:
        self_copy = self.copy()
        self_copy.render_moves(" ".join(list(i)), "n")
        if goal_func2() == True:
          break
      if goal_func2() == True:
        break
      comb_count += 1
      if comb_count == comb_count_limit:
        break
    return i
    
  def rotate_cube_anticlock(self):
    self_copy = self.copy()
    # move front to right
    self.r7 = self_copy.f1; self.r4 = self_copy.f2; self.r1 = self_copy.f3; 
    self.r8 = self_copy.f4; self.r5 = self_copy.f5; self.r2 = self_copy.f6; 
    self.r9 = self_copy.f7; self.r6 = self_copy.f8; self.r3 = self_copy.f9; 
    # move right to back
    self.ba7 = self_copy.r1; self.ba4 = self_copy.r2; self.ba1 = self_copy.r3; 
    self.ba8 = self_copy.r4; self.ba5 = self_copy.r5; self.ba2 = self_copy.r6; 
    self.ba9 = self_copy.r7; self.ba6 = self_copy.r8; self.ba3 = self_copy.r9; 
    # move back to left
    self.l7 = self_copy.ba1; self.l4 = self_copy.ba2; self.l1 = self_copy.ba3; 
    self.l8 = self_copy.ba4; self.l5 = self_copy.ba5; self.l2 = self_copy.ba6; 
    self.l9 = self_copy.ba7; self.l6 = self_copy.ba8; self.l3 = self_copy.ba9; 
    # move left to front
    self.f7 = self_copy.l1; self.f4 = self_copy.l2; self.f1 = self_copy.l3; 
    self.f8 = self_copy.l4; self.f5 = self_copy.l5; self.f2 = self_copy.l6; 
    self.f9 = self_copy.l7; self.f6 = self_copy.l8; self.f3 = self_copy.l9; 
    # rotate top face anticlock
    self.t7 = self_copy.t1; self.t9 = self_copy.t7; self.t3 = self_copy.t9; self.t1 = self_copy.t3; # corners
    self.t8 = self_copy.t4; self.t6 = self_copy.t8; self.t2 = self_copy.t6; self.t4 = self_copy.t2; # edges

    # rotate down face clockwise
    self.b1 = self_copy.b7; self.b7 = self_copy.b9; self.b9 = self_copy.b3; self.b3 = self_copy.b1; # corners
    self.b4 = self_copy.b8; self.b8 = self_copy.b6; self.b6 = self_copy.b2; self.b2 = self_copy.b4; # edges

  def solve_fl_corner(self):
    for i in range(4):
      pos = get_position_corner(self, self.t5, self.f5, self.r5)
      if pos == 1:
        self.render_moves("B D D B' R' D' R", "n")
        print("Moves: B D D B' R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 2:
        self.render_moves("B' D' B R' D' R", "n")
        print("Moves: B' D' B R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 3:
        self.render_moves("F' D F D R' D' R", "n")
        print("Moves: F' D F D R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 4:
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 5:
        self.render_moves("D D R' D' R", "n")
        print("Moves: D D R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 6:
        self.render_moves("D' R' D' R", "n")
        print("Moves: D' R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 7:
        self.render_moves("D R' D' R", "n")
        print("Moves: D R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      elif pos == 8:
        self.render_moves("R' D' R", "n")
        print("Moves: R' D' R")
        while self.t9 != self.t5:
          self.render_moves("R' D' R D R' D' R", "n")
          print("Moves: R' D' R D R' D' R")
      else:
        print("Error occured while rotating the cube.")
        return
      print(self)
      print("Rotate cube in right direction (such that the top face rotates anti-clockwise).")
      self.rotate_cube_anticlock()

  def solve_first_layer(self):
    legal_moves = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]
    final_moves = []
    comb_count_limit = 7
    comb_count = 0
    new = []
    i = ""
    while self.goal_test_fl_cross1() == False:
      new.append(legal_moves)
      perf_moves = list(itertools.product(*new))
      for i in perf_moves:
        self_copy = self.copy()
        self_copy.render_moves(" ".join(list(i)), "n")
        if self_copy.goal_test_fl_cross1() == True:
          break
      if self_copy.goal_test_fl_cross1() == True:
        break
      comb_count += 1
      if comb_count == comb_count_limit:
        break
    final_moves = final_moves + list(i)
    print("1. Solved first edge piece...")
    print(" ".join(list(i)))
    self.render_moves(" ".join(list(i)), "n")
    print(self)

    comb_count = 0
    new = []
    i = ""
    while self.goal_test_fl_cross2() == False:
      new.append(legal_moves)
      perf_moves = list(itertools.product(*new))
      for i in perf_moves:
        self_copy = self.copy()
        self_copy.render_moves(" ".join(list(i)), "n")
        if self_copy.goal_test_fl_cross2() == True:
          break
      if self_copy.goal_test_fl_cross2() == True:
        break
      comb_count += 1
      if comb_count == comb_count_limit:
        break
    final_moves = final_moves + list(i)
    print("2. Solved second edge piece...")
    print(" ".join(list(i)))
    self.render_moves(" ".join(list(i)), "n")
    print(self)

    comb_count = 0
    new = []
    i = ""
    while self.goal_test_fl_cross3() == False:
      new.append(legal_moves)
      perf_moves = list(itertools.product(*new))
      for i in perf_moves:
        self_copy = self.copy()
        self_copy.render_moves(" ".join(list(i)), "n")
        if self_copy.goal_test_fl_cross3() == True:
          break
      if self_copy.goal_test_fl_cross3() == True:
        break
      comb_count += 1
      if comb_count == comb_count_limit:
        break
    final_moves = final_moves + list(i)
    print("3. Solved third edge piece...")
    print(" ".join(list(i)))
    self.render_moves(" ".join(list(i)), "n")
    print(self)

    comb_count = 0
    new = []
    i = ""
    while self.goal_test_fl_cross4() == False:
      new.append(legal_moves)
      perf_moves = list(itertools.product(*new))
      for i in perf_moves:
        self_copy = self.copy()
        self_copy.render_moves(" ".join(list(i)), "n")
        if self_copy.goal_test_fl_cross4() == True:
          break
      if self_copy.goal_test_fl_cross4() == True:
        break
      comb_count += 1
      if comb_count == comb_count_limit:
        break
    final_moves = final_moves + list(i)
    print("4. Solved fourth and last edge piece...")
    print(" ".join(list(i)))
    self.render_moves(" ".join(list(i)), "n")
    print(self)
  
    print("\nMoves required to get first layer cross are as follows:")
    print(" ".join(final_moves))

    print("\nPosition of corner yellow orange and blue is " + str(get_position_corner(self, 'y', 'o', 'b')))
    #self.rotate_cube_anticlock()

    self.solve_fl_corner()
    print(self)
  
  def solve_second_layer(self):
    for i in range(4):
      pos = get_position_edge(self, self.f5, self.r5)
      if pos == 1:
        self.render_moves("B D B' D' L' D' L", "n")
        print("B D B' D' L' D' L")
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D F D F' D' R' D' R")
      elif pos == 2:
        self.render_moves("B' D' B D R D R' D D", "n")
        print("B' D' B D R D R' D D")
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D' D' R' D' R D F D F'")
      elif pos == 3:
        self.render_moves("L D' L' D' F' D F D'", "n")
        print("L D' L' D' F' D F D'")
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D' D' R' D' R D F D F'")
      elif pos == 4:
        if self.r8 != self.r5:
          self.render_moves("R' D' R D F D F' D'", "n")
          print("R' D' R D F D F' D'")
          if self.r6 == self.r5:
            self.render_moves("D F D F' D' R' D' R", "n")
            print("Moves: D F D F' D' R' D' R")
          else:
            self.render_moves("D' D' R' D' R D F D F'", "n")
            print("Moves: D' D' R' D' R D F D F'")
      elif pos == 5:
        self.render_moves("D'", "n")
        print("D'")
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D' D' R' D' R D F D F'")
      elif pos == 6:
        self.render_moves("D D", "n")
        print("D D")
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D' D' R' D' R D F D F'")
      elif pos == 7:
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D' D' R' D' R D F D F'")
      elif pos == 8:
        self.render_moves("D", "n")
        print("D")
        if self.r6 == self.r5:
          self.render_moves("D F D F' D' R' D' R", "n")
          print("Moves: D F D F' D' R' D' R")
        else:
          self.render_moves("D' D' R' D' R D F D F'", "n")
          print("Moves: D' D' R' D' R D F D F'")
      else:
        print(pos)
        print("Error occured while rotating the cube.")
        return
      print(self)
      print("Rotate cube in right direction (such that the top face rotates anti-clockwise).")
      self.rotate_cube_anticlock()
  
  def cube_upside_down(self):
    self_copy = self.copy()
    self.f1 = self_copy.ba1; self.f2 = self_copy.ba2; self.f3 = self_copy.ba3; 
    self.f4 = self_copy.ba4; self.f5 = self_copy.ba5; self.f6 = self_copy.ba6; 
    self.f7 = self_copy.ba7; self.f8 = self_copy.ba8; self.f9 = self_copy.ba9; 
    
    self.ba1 = self_copy.f1; self.ba2 = self_copy.f2; self.ba3 = self_copy.f3; 
    self.ba4 = self_copy.f4; self.ba5 = self_copy.f5; self.ba6 = self_copy.f6; 
    self.ba7 = self_copy.f7; self.ba8 = self_copy.f8; self.ba9 = self_copy.f9; 
    
    self.t1 = self_copy.b1; self.t2 = self_copy.b2; self.t3 = self_copy.b3; 
    self.t4 = self_copy.b4; self.t5 = self_copy.b5; self.t6 = self_copy.b6; 
    self.t7 = self_copy.b7; self.t8 = self_copy.b8; self.t9 = self_copy.b9; 
    
    self.b1 = self_copy.t1; self.b2 = self_copy.t2; self.b3 = self_copy.t3; 
    self.b4 = self_copy.t4; self.b5 = self_copy.t5; self.b6 = self_copy.t6; 
    self.b7 = self_copy.t7; self.b8 = self_copy.t8; self.b9 = self_copy.t9; 

    self.l1 = self_copy.l9; self.l3 = self_copy.l7; self.l9 = self_copy.l1; self.l7 = self_copy.l3; 
    self.l2 = self_copy.l8; self.l8 = self_copy.l2; self.l4 = self_copy.l6; self.l6 = self_copy.l4; 

    self.r1 = self_copy.r9; self.r3 = self_copy.r7; self.r9 = self_copy.r1; self.r7 = self_copy.r3; 
    self.r2 = self_copy.r8; self.r8 = self_copy.r2; self.r4 = self_copy.r6; self.r6 = self_copy.r4; 
    

  def solve_third_layer(self):
    #print("Under construction....")
    #print(self)
    print("Turn the cube upside down....")
    self.cube_upside_down()

    # Solving the cross on last layer
    #print(self.t2, self.t4, self.t6, self.t8)
    while self.t2 != self.t5 or self.t4 != self.t5 or self.t6 != self.t5 or self.t8 != self.t5:
      print("Entered while loop")
      if self.t2 != self.t5 and self.t4 == self.t5 and self.t6 == self.t5 and self.t8 != self.t5:
        self.render_moves("U", "n")
        print("Moves: U")
      elif self.t2 == self.t5 and self.t4 == self.t5 and self.t6 != self.t5 and self.t8 != self.t5:
        self.render_moves("U", "n")
        print("Moves: U")
      elif self.t2 != self.t5 and self.t4 == self.t5 and self.t6 != self.t5 and self.t8 == self.t5:
        self.render_moves("U U", "n")
        print("Moves: U U")
      elif self.t2 != self.t5 and self.t4 != self.t5 and self.t6 == self.t5 and self.t8 == self.t5:
        self.render_moves("U'", "n")
        print("Moves: U'")
      self.render_moves("L U F U' F' L'", "n")
      print("L U F U' F' L'")
      print(self)
    
    # Orientation of cross on last layer
    while self.f5 != self.f2:
      self.render_moves("U", "n")
      print("Moves: U")

    switch_edge = "R' U' R U' R' U' U' R U'"
    if self.l5 == self.l6 and self.r5 == self.r4 and self.ba5 == self.ba8:
      print("Last layer cross solved....")
    elif self.l5 != self.l6 and self.r5 != self.r4 and self.ba5 == self.ba8:
      self.render_moves(switch_edge + " U' " + switch_edge + " U " + switch_edge, "n")
      print("Moves: " + switch_edge + " U' " + switch_edge + " U " + switch_edge)
    elif self.l5 != self.l6 and self.r5 == self.r4 and self.ba5 != self.ba8:
      self.render_moves(switch_edge, "n")
      print("Moves: " + switch_edge)
    elif self.l5 == self.l6 and self.r5 != self.r4 and self.ba5 != self.ba8:
      self.render_moves("U' " + switch_edge + " U", "n")
      print("Moves: " + "U' " + switch_edge + " U")
    elif self.l5 != self.l6 and self.r5 != self.r4 and self.ba5 != self.ba8:
      if self.ba8 == self.l5:
        self.render_moves(switch_edge + " U' " + switch_edge + " U", "n")
        print("Moves: " + switch_edge + " U' " + switch_edge + " U")
      elif self.ba8 == self.r5:
        self.render_moves("U' " + switch_edge + " U " + switch_edge, "n")
        print("Moves: " + "U' " + switch_edge + " U " + switch_edge)
      
    rot_corners_anticlock = "R U' L' U R' U' L U"
    rot_corners_clock = "L' U R U' L U R' U'"

    loc = get_position_corner(self, self.f5, self.r5, self.t5)
    if loc == 1:
      self.render_moves(rot_corners_anticlock,"n")
      print("Moves: " + rot_corners_anticlock)
    elif loc == 2:
      self.render_moves("U' " + rot_corners_clock + " U", "n")
      print("Moves: " + "U' " + rot_corners_clock + " U")
    elif loc == 3:
      self.render_moves("U' " + rot_corners_anticlock + " U", "n")
      print("Moves: " + "U' " + rot_corners_anticlock + " U")
    elif loc == 4:
      print("Moves: ")
    else:
      print(loc)
      print("\n\n\nERROR: There is some error with the cube.")
    
    while get_position_corner(self, self.l5, self.f5, self.t5) != 3:
      self.render_moves(rot_corners_clock, "n")
      print("Moves: " + rot_corners_clock)

    rot_corn_clock = "R' D R D' R' D R"
    rot_corn_anticlock = "R' D' R D R' D' R"

    #flag = 0
    #counter = 0
    while self.t1 != self.t5 or self.t3 != self.t5 or self.t7 != self.t5 or self.t9 != self.t5:
      flag = 0
      counter = 0
      if self.f3 == self.t5:
        flag = 1
        self.render_moves(rot_corn_clock)
        print("Moves: " + rot_corn_clock)
        #for i in range(3):
        while flag == 1 and counter <= 3:
          self.render_moves("U")
          print("Moves: U")
          if self.t9 != self.t5:
            self.render_moves(rot_corn_anticlock)
            print("Moves: " + rot_corn_anticlock)
            flag = 0
          counter += 1
      
      if self.r7 == self.t5:
        flag = 1
        self.render_moves(rot_corn_anticlock)
        print("Moves: " + rot_corn_anticlock)
        flag == 1
        #for i in range(3):
        while flag == 1 and counter <= 3:
          self.render_moves("U")
          print("Moves: U")
          if self.t9 != self.t5:
            self.render_moves(rot_corn_clock)
            print("Moves: " + rot_corn_clock)
            flag = 0
          counter += 1
      
      self.render_moves("U")
      print("Moves: U")
    print(self)

    while self.f3 != self.f5:
      self.render_moves("U")
      print("Moves: U")

