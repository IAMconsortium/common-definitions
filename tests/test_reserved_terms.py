from nomenclature import DataStructureDefinition


def test_variable_ops_as_square_brackets():
    # Check that variables use square brackets for operations
    # https://github.com/IAMconsortium/common-definitions/issues/55

    dsd = DataStructureDefinition("definitions/", dimensions=["variable"])

    error = []
    for variable, attrs in dsd.variable.items():
        if reserved_terms := [r for r in ["Index", "Share"] if "|" + r in variable]:
            error.append(f"Variable '{variable}' -> '[{''.join(reserved_terms)}]'")
    if error:
        raise ValueError(
            f"Found reserved terms in the following variables:\n{'\n - '.join(error)}"
        )
