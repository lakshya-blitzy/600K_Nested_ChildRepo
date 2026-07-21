"""Misplaced copy of ``app.py`` that is broken at runtime (documented, not fixed).

This nested ``service.py`` is a **byte-identical copy of
``ChildRepo/NestedChild/app.py``** committed under the wrong filename. Instead
of the arithmetic helpers exposed by the parent and ``ChildRepo`` ``service.py``
modules (``calculate_total`` / ``calculate_average``), it contains a ``main()``
entry point and, on line 1, the statement ``from service import
calculate_total``.

Because this module is itself named ``service``, that line is a **self-import**:
the ``service`` module attempts to import a name from itself while it is still
being initialized. ``calculate_total`` is never defined in this file, so the
import fails and the module cannot be imported or executed. Running the sibling
``app.py`` fails for the same reason, since it also imports from ``service``.

This defect is **DOCUMENTED, NOT REPAIRED**, per the documentation-only scope of
this task. Resolution guidance (restore the real ``calculate_total`` /
``calculate_average`` helpers, as in the parent/``ChildRepo`` ``service.py``)
lives in the Known Limitations / Troubleshooting section of
``ChildRepo/NestedChild/README.md``.

Raises:
    ImportError: cannot import name 'calculate_total' from partially
        initialized module 'service' (most likely due to a circular import).
        Raised by the line-1 self-import as soon as this module is imported or
        run.

Source: ChildRepo/NestedChild/service.py:L1-L16
"""

from service import calculate_total

def main():
    """Run the fixed-list sum-and-print workflow (unreachable at runtime).

    Mirrors the parent ``main()``: it would build the fixed list
    ``[10, 20, 30, 40]``, delegate summation to ``calculate_total``, print
    ``Total: <total>`` via an f-string, print each number on its own line, and
    finally print ``Application completed``. In practice this body never
    executes, because the module-level self-import on line 1 raises
    ``ImportError`` before ``main()`` can be called.

    Args:
        None.

    Returns:
        None. The intended side effect is standard-output writes, but the
        function is unreachable because module import fails first.

    Source: ChildRepo/NestedChild/service.py:L3-L16
    """
    numbers = [10, 20, 30, 40]

    total = calculate_total(numbers)

    print(f"Total: {total}")

    for number in numbers:
        print(number)

    print("Application completed")

if __name__ == "__main__":
    main()
