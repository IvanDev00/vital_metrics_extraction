def is_vertically_aligned(box1, box2):
    """Check if two bounding boxes are vertically aligned."""
    x1, y1 = box1[0]
    x2, y2 = box2[0]

    # Check if the horizontal midpoints of the boxes are close
    midpoint1 = x1 + (box1[1][0] - x1) / 2
    midpoint2 = x2 + (box2[1][0] - x2) / 2
    return abs(midpoint1 - midpoint2) < (box1[1][0] - x1) / 2