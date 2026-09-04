"""Offline access-control audit helpers."""

def unexpected_principals(expected, observed):
    return sorted(set(observed) - set(expected))

def missing_principals(expected, observed):
    return sorted(set(expected) - set(observed))

def compare(expected, observed):
    return {
        "unexpected": unexpected_principals(expected, observed),
        "missing": missing_principals(expected, observed),
        "ok": set(expected) == set(observed),
    }
