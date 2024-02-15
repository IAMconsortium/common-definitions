from nomenclature import DataStructureDefinition


def test_legacy_variables():
    # Check that (new) variables are not referenced as deprecated legacy variables
    dsd = DataStructureDefinition("definitions/", dimensions=["variable"])
    existing_variables = list(dsd.variable)

    legacy_variables = {}
    for code, attrs in dsd.variable.items():
        for project in ["navigate", "engage"]:
            if project in attrs.extra_attributes:
                legacy_var = attrs.__getattr__(project)
                if legacy_var in existing_variables:
                    legacy_variables[legacy_var] = code

    if legacy_variables:
        error = [
            f"'{legacy_var}' -> '{code}'" + "\n"
            for legacy_var, code in legacy_variables.items()
        ]

        raise ValueError(
            "Deprecated variables from legacy projects:\n" f"{''.join(error)}"
        )
