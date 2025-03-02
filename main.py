from operations import matrixes, line_segment
from entities.point_2d import Point2D

def main():
  multiplication = matrixes.multiplication([[1, 2], [3, 4]], [[1, 2], [3, 4]])
  print(f'Multiplication: {multiplication}')
  
  
  line_segment_length = line_segment.calculate_length(
    point1=Point2D(3, 5),
    point2=Point2D(6, 1)
  )
  print(f'Line segment length: {line_segment_length}')
  
  line_intersection = line_segment.intersection(
    line_1_point_1=Point2D(x=0, y=0),
    line_1_point_2=Point2D(x=4, y=4),
    line_2_point_1=Point2D(x=0, y=4),
    line_2_point_2=Point2D(x=4, y=0)  
  );
  print(f'Line segment intersection: ({line_intersection.x}, {line_intersection.y})')
  
if __name__ == "__main__":
  main();