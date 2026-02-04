# memcourt/heap.py

import gc
import sys
from typing import Dict, Any


class HeapSnapshot:
    """
    Represents a snapshot of Python heap memory.
    Objects are modeled as nodes.
    References are modeled as edges.
    """

    def __init__(self, tag: str):
        self.tag = tag
        self.objects: Dict[int, Dict[str, Any]] = {}

    def capture(self):
        """
        Capture all currently tracked objects by Python GC.
        """
        gc.collect()  # clean up unreachable objects

        for obj in gc.get_objects():
            try:
                obj_id = id(obj)
                self.objects[obj_id] = {
                    "id": obj_id,
                    "type": type(obj).__name__,
                    "repr": repr(obj)[:80],  # truncate long repr
                    "size": sys.getsizeof(obj),
                }
            except Exception:
                # Some objects cannot be inspected safely
                pass

    def summary(self):
        """
        Return a simple summary.
        """
        return {
            "tag": self.tag,
            "total_objects": len(self.objects),
        }


def snapshot(tag: str) -> HeapSnapshot:
    """
    Public API to take a heap snapshot.
    """
    snap = HeapSnapshot(tag)
    snap.capture()
    return snap


def diff(snapshot_a: HeapSnapshot, snapshot_b: HeapSnapshot):
    """
    Compare two snapshots.
    """
    ids_a = set(snapshot_a.objects.keys())
    ids_b = set(snapshot_b.objects.keys())

    created = ids_b - ids_a
    destroyed = ids_a - ids_b

    return {
        "created_objects": len(created),
        "destroyed_objects": len(destroyed),
    }
