"""
Author: Gregg Oliva
"""

def capitalize_all(s: str) -> str:
    return " ".join(
        [
            word.capitalize()
            for word in s.split(" ")
        ]
    )
