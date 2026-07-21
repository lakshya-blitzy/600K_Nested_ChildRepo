"""Console entry point for the nested submodule sum-and-print application.

Its non-docstring executable code is identical to the parent repository's
``app.py`` (only the repository-specific docstrings differ).
It wires the reusable ``calculate_total`` helper (normally supplied by a sibling
``service.py``) to a tiny command-line demonstration: when executed directly it
would compute the sum of a fixed list of numbers, print the total, echo each
number, and print a completion message. It defines no classes, constants, or
module-level state beyond ``main`` and the standard ``__main__`` guard.

Note:
    Although this module itself is well-formed, running ``python app.py`` in
    this directory FAILS at import time with an ``ImportError``. The sibling
    ``ChildRepo/NestedChild/service.py`` is a misplaced copy of this file and
    does **not** define ``calculate_total``; its own line-1 self-import raises
    ``ImportError`` as soon as it is imported.
    `Source: ChildRepo/NestedChild/service.py:L1-L16`.
    On the verified CPython 3.12.3 interpreter the exact message is
    ``cannot import name 'calculate_total' from partially initialized module
    'service' (most likely due to a circular import)`` and the process exits
    with status code 1.
    `Source: verified by running "python app.py" under CPython 3.12.3 (exit code 1)`.
    (Secondary, informational only: the newer CPython 3.13 series reports
    ``cannot import name 'calculate_total' from 'service' (consider renaming
    '.../service.py' if it has the same name as a library you intended to
    import)`` for the same failure; the exception type and exit code are
    identical, only the wording differs.) This is documented, not fixed.

Usage:
    python app.py    # currently raises ImportError at this nested level

Source: ChildRepo/NestedChild/app.py:L1-L16
"""

from service import calculate_total

def main():
    """Run the sample computation and print results to standard output.

    Builds the fixed list ``[10, 20, 30, 40]``, computes its total via
    ``calculate_total``, prints ``Total: <total>`` using an f-string, prints
    each number on its own line in input order, and finally prints
    ``Application completed``. The input is hard-coded; the function accepts no
    arguments and reads no configuration.

    Args:
        None.

    Returns:
        None. The function's observable effect would be its standard-output
        writes. Note that ``main()`` cannot actually run in this directory
        because the module-level import of the broken sibling ``service.py``
        fails first (see the module docstring).

    Source: ChildRepo/NestedChild/app.py:L3-L16
    """
    numbers = [10, 20, 30, 40]

    total = calculate_total(numbers)

    print(f"Total: {total}")

    for number in numbers:
        print(number)

    print("Application completed")

if __name__ == "__main__":
    main()
