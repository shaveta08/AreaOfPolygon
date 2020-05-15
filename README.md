# AreaOfPolygon
AreaOfPolygon
Project:

Language: Python version 3.7 and above.

Script Name: scratch.py

Script Description: 
The script scratch.py has three major functions created for calculating the Area of Convex Polygon.
1.	 verifyConvexPolygon: This function contains the major checks to verify the convex polygon vertices entered by the end user. It returns true or false based on the checks.
2.	determinant: This function receives two vertices as arguments and calculates the determinant of two polygon vertices and returns the same.
3.	areaOfPolygon: This function receives the vertices of convex polygon in form of list of lists as argument and returns the area of the polygon created by those vertices. 

Assumptions:
1.	Vertices must be sent in form of List of lists. For Example: vertices are: (2,5),(5,1),(-4,3) then input should be either [ [2,5],  [5,1] , [-4,3] ] or [ [‘2’,’5’], [‘5’,’1’] ,[‘-4’,’3’] ].
2.	 The coordinates must be taken in counterclockwise or clockwise order around the polygon, beginning and ending at the same point.


Compilation and Execution Instructions:

1.	Download or clone the file scratch.py.
2.	Open the command prompt.
3.	On command prompt use the following commands:

3.1.	  > python scratch.py

input : Vertices in form of List of lists.

3.2.	  >python –c “import scratch; scratch.areaOfPolygon(input)”
