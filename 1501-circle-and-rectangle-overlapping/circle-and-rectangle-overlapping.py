class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the x and y coordinates of the closest point on the rectangle to the circle's center.
        # We use clamping (max and min) to constrain the point within the rectangle's bounds.
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the distance from the circle's center to this closest point.
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        
        # Check if the squared distance is less than or equal to the squared radius.
        return (distance_x ** 2 + distance_y ** 2) <= (radius ** 2)