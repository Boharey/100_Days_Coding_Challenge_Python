#Area calculator
import math

test_h = int(input("Height of wall : "))
test_w = int(input("Width of wall : "))
coverage = 5

def paint_cal(height,width,cover):
  total_cans = (height*width)/cover
  print(f"you'll need {math.ceil(total_cans)} cans of paint.")
paint_cal(height = test_h,width = test_w,cover = coverage)

