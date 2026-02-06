# memcourt/snapshot.py

class Snapshot:
    """
    Represents a heap snapshot at a specific moment.
    """

    def __init__(self, tag, objects):
        self.tag = tag
        self.objects = objects


def take_snapshot(tag, data_dict):
    """
    Capture variable names, object ids, and values.
    """
    objects = []

    for name, obj in data_dict.items():
        objects.append({
            "name": name,
            "id": id(obj),
            "value": repr(obj)
        })

    return Snapshot(tag, objects)
