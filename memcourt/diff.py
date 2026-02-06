# memcourt/diff.py

def diff(snapshot_a, snapshot_b):
    """
    Detect aliasing and mutations between two snapshots.
    """
    result = {
        "aliasing": [],
        "mutations": []
    }

    before = {o["name"]: o for o in snapshot_a.objects}
    after = {o["name"]: o for o in snapshot_b.objects}

    # Aliasing detection 
    id_map = {}
    for name, obj in before.items():
        id_map.setdefault(obj["id"], []).append(name)

    for names in id_map.values():
        if len(names) > 1:
            result["aliasing"].append(names)

    # Mutation detection
    for name in before:
        if before[name]["value"] != after[name]["value"]:
            result["mutations"].append({
                "variable": name,
                "before": before[name]["value"],
                "after": after[name]["value"]
            })

    return result
