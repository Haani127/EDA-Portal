# You are using Python
import numpy as np


cityA = np.array(list(map(float, input().split())))


cityB = np.array(list(map(float, input().split())))


temp_array = np.array([cityA, cityB])

print("\n2D Temperature Array (Cities x Days):")
print(temp_array)

hottest_days = np.argmax(temp_array, axis=1)
print("\nHottest day (0-indexed) for each city:")
print(hottest_days)


transposed = temp_array.T
print("\nTransposed Array (Days x Cities):")
print(transposed)


flattened = transposed.flatten()
print("\nFlattened 1D Array:")
print(flattened)