#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        def new_function(*args):
            a, b = args
            return fct(a, b)
        return new_function(*args)
    except Exception as e:
        print(f"Exception: {e}", file = sys.stderr)
        return None