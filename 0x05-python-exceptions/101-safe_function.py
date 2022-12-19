#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exc:
        print("Exception:", exc, file=sys.stderr)
        return None
