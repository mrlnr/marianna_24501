from typing import List

class Vector:
  def __init__(self, vector: List[float]):
    self.vector = vector
  def __repr__(self):
      return f"Vector({self.vector})"
  def __add__(self, other):
    if len(self.vector) != len(other.vector):
      raise ValueError("vector length mismatch")
    else:
      v3 = []
      for i in range(0, len(self.vector)):
        current_sum = self.vector[i] + other.vector[i]
        v3.append(current_sum)
      return Vector(v3)
  def __sub__(self, other):
    if len(self.vector) != len(other.vector):
      raise ValueError("vector length mismatch")
    else:
      v3 = []
      for i in range(0, len(self.vector)):
        current_min = self.vector[i] - other.vector[i]
        v3.append(current_min)
      return Vector(v3)
  def __mul__(self, other):
    if len(self.vector) != len(other.vector):
      raise ValueError("vector length mismatch")
    else:
      v3 = []
      for i in range(0, len(self.vector)):
        pr = self.vector[i] * other.vector[i]
        v3.append(pr)
      return Vector(v3)
  def __truediv__(self, other):
    if len(self.vector) != len(other.vector):
      raise ValueError("vector length mismatch")
    else:
      v3 = []
      for i in range(0, len(self.vector)):
        delen = self.vector[i] / other.vector[i]
        v3.append(delen)
      return Vector(v3)
  def __matmul__(self, other):
    if len(self.vector) != len(other.vector):
      raise ValueError("vector length mismatch")
    else:
      scalar = 0
      for i in range(0, len(self.vector)):
        pr = self.vector[i] * other.vector[i]
        scalar += pr
      return scalar
  def __getitem__(self, item):
    return self.vector[item]



