#!/usr/bin/env python3
"""A minimal test script for verifying the Git/GitHub workflow."""


def greet(name: str = "DeepSeek Harness") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
