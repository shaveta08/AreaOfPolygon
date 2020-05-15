def verifyConvexPolygon(vertices):
    # Check: atleast 3 sides are required.
    if (len(vertices) < 3):
        return False
    return True


def determinant(vertex_1, vertex_2):
    # Find the determinant of two vertices using formula (x1*y2 - y1*x2).
    return (int(vertex_1[0]) * int(vertex_2[1]) - int(vertex_2[0]) * int(vertex_1[1]))


def areaOfPolygon(vertices):
    # Verification done for number of vertices.
    if (not (verifyConvexPolygon(vertices))):
        print("Please enter more than two vertices.")
        return
    else:
        sum = 0
        for i in range(len(vertices)):
            vertex1 = vertices[i]
            if ((i + 1) >= len(vertices)):
                vertex2 = vertices[i + 1 - len(vertices)]
            else:
                vertex2 = vertices[i + 1]

            sum = sum + determinant(vertex1, vertex2)

        area = abs(sum / 2)
        print(area)
        return area