import solve_cube
from solve_cube import cube
from get_position import *

def main():
  ## Write a code here to get following values from video feed or camera images
  top = [['Y','Y','Y'],['Y','Y','Y'],['O','O','O']]
  bottom = [['W','W','R'],['W','W','R'],['W','W','R']]
  left = [['B','B','R'],['B','B','R'],['B','B','Y']]
  right = [['O','G','G'],['O','G','G'],['W','G','G']]
  front = [['G','G','G'],['R','R','Y'],['R','R','Y']]
  back = [['O','O','W'],['O','O','W'],['B','B','B']]

  #back = [['G','R','B'],['B','O','G'],['W','O','W']]
  #front = [['B','O','Y'],['O','R','Y'],['B','Y','O']]
  #left = [['Y','W','G'],['B','B','R'],['Y','G','Y']]
  #right = [['O','G','G'],['O','G','G'],['W','G','G']]
  #top = [['R','W','B'],['W','Y','B'],['R','B','G']]
  #bottom = [['O','O','O'],['R','W','Y'],['O','G','R']]
  c = cube(top, bottom, left, right, front, back)
  print(c)
  moves = input("Enter moves to scramble the cube: ")
  x = input("Do you want to see the cube state after every move? (y/n) ")
  c.render_moves(moves, x)
  print("After scramble:")
  print(c)
  #print(c.goal_test_fl())
  c.solve_first_layer()
  print("\nSuccessfully solved the first layer!!\n\n\n")
  c.solve_second_layer()
  print("\nSuccessfully solved second layer!\n\n\n")
  #print(c)
  c.solve_third_layer()
  print("\nSuccessfully solved last layer!\n\n\n")
  print(c)

main()