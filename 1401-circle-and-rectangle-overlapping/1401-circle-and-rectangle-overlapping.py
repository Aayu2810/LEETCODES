class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:

        def distance(ux, uy, vx, vy):
            return (ux - vx) ** 2 + (uy - vy) ** 2

        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True
       
        if x1 <= xCenter <= x2 and y2 <= yCenter <= y2 + radius:
            return True
        
        if x1 <= xCenter <= x2 and y1 - radius <= yCenter <= y1:
            return True
       
        if x1 - radius <= xCenter <= x1 and y1 <= yCenter <= y2:
            return True

        if x2 <= xCenter <= x2 + radius and y1 <= yCenter <= y2:
            return True
       
        if distance(xCenter, yCenter, x1, y2) <= radius**2:
            return True

        if distance(xCenter, yCenter, x1, y1) <= radius**2:
            return True
       
        if distance(xCenter, yCenter, x2, y2) <= radius**2:
            return True
        
        if distance(xCenter, yCenter, x2, y1) <= radius**2:
            return True       
        return False