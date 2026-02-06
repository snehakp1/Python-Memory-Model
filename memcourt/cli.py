# memcourt/cli.py

import json

def print_all(snapshot_a, snapshot_b, diff_result, as_json=False):
    if as_json:
        print(json.dumps({
            "snapshot_before": snapshot_a.__dict__,
            "snapshot_after": snapshot_b.__dict__,
            "diff": diff_result
        }, indent=2))
        return

    print(f"\nSNAPSHOT A: {snapshot_a.tag}")
    for obj in snapshot_a.objects:
        print(obj)

    print(f"\nSNAPSHOT B: {snapshot_b.tag}")
    for obj in snapshot_b.objects:
        print(obj)

    print("\nDIFF RESULT")
    print("-" * 30)

    if diff_result["aliasing"]:
        print("Aliasing detected:")
        for group in diff_result["aliasing"]:
            print("  ->", group)
    else:
        print("No aliasing detected.")

    if diff_result["mutations"]:
        print("\nMutations detected:")
        for m in diff_result["mutations"]:
            print(f"  {m['variable']}: {m['before']} -> {m['after']}")
    else:
        print("\nNo mutations detected.")
