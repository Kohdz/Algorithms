import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    def is_insect(R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)

    if not is_insect(R1, R2):
        return Rectangle(0, 0, -1, -1)  # intersection

    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        max(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        max(R1.y + R1.height, R2.y + R2.height) - max(R1.y + R2.y)
    )
