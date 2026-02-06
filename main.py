# main.py

import argparse
import importlib.util
import os

from memcourt.snapshot import take_snapshot
from memcourt.diff import diff
from memcourt.cli import print_all


def main():
    parser = argparse.ArgumentParser(description="Heap Snapshot Engine")
    parser.add_argument("command", choices=["analyze"])
    parser.add_argument("script")
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    # LOAD SCRIPT BY FILE PATH
    script_path = os.path.abspath(args.script)

    spec = importlib.util.spec_from_file_location("user_script", script_path)
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
   

    cases = script.run()
    print("cases",cases)

    for case_name, (state, mutate) in cases.items():
        print(f"\nCASE: {case_name.upper()}")

        snap_a = take_snapshot(f"{case_name} - before", state)

        mutate()  # mutation between snapshots

        snap_b = take_snapshot(f"{case_name} - after", state)

        d = diff(snap_a, snap_b)

        print_all(snap_a, snap_b, d, args.json)


if __name__ == "__main__":
    main()



















# python main.py analyze examples.py
# python main.py analyze examples.py --json
