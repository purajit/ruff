# Errors.
foo == "a" or foo == "b"

foo != "a" and foo != "b"

foo == "a" or foo == "b" or foo == "c"

foo != "a" and foo != "b" and foo != "c"

foo == a or foo == "b" or foo == 3  # Mixed types.

"a" == foo or "b" == foo or "c" == foo

"a" != foo and "b" != foo and "c" != foo

"a" == foo or foo == "b" or "c" == foo

foo == bar or baz == foo or qux == foo

foo == "a" or "b" == foo or foo == "c"

foo != "a" and "b" != foo and foo != "c"

foo == "a" or foo == "b" or "c" == bar or "d" == bar  # Multiple targets

foo.bar == "a" or foo.bar == "b"  # Attributes.

# OK
foo == "a" and foo == "b" and foo == "c"  # `and` mixed with `==`.

foo != "a" or foo != "b" or foo != "c"  # `or` mixed with `!=`.

foo == a or foo == b() or foo == c  # Call expression.

foo != a or foo() != b or foo != c  # Call expression.

foo in {"a", "b", "c"}  # Uses membership test already.

foo not in {"a", "b", "c"}  # Uses membership test already.

foo == "a"  # Single comparison.

foo != "a"  # Single comparison.

foo == "a" == "b" or foo == "c"  # Multiple comparisons.

foo == bar == "b" or foo == "c"  # Multiple comparisons.

foo == foo or foo == bar  # Self-comparison.

foo[0] == "a" or foo[0] == "b"  # Subscripts.

foo() == "a" or foo() == "b"  # Calls.

import sys

sys.platform == "win32" or sys.platform == "emscripten"  # sys attributes

foo == "a" or "c" == bar or foo == "b" or "d" == bar  # Multiple targets

foo == "a" or ("c" == bar or "d" == bar) or foo == "b"  # Multiple targets

foo == "a" or foo == "b" or "c" != bar and "d" != bar  # Multiple targets

foo == "a" or ("c" != bar and "d" != bar) or foo == "b"  # Multiple targets

foo == "a" and "c" != bar or foo == "b" and "d" != bar  # Multiple targets

foo == 1 or foo == True # Different types, same hashed value

foo == 1 or foo == 1.0 # Different types, same hashed value

foo == False or foo == 0 # Different types, same hashed value

foo == 0.0 or foo == 0j # Different types, same hashed value
