def build_actions(profile: dict, user_inputs: dict) -> list:
    """
    Build a list of executable actions for the crawler by combining a site profile
    with high-level user inputs (e.g., supplier_id, country, etc.).

    - Replaces logical field names in the profile with actual selectors
    - Injects values only if present in user_inputs
    - Dynamically adds dropdown li:has-text(...) clicks for autocompletes
    - Keeps static selectors and wait steps intact
    """
    actions = []
    fields = profile.get("fields", {})

    for step in profile.get("actions", []):
        # Handle "type" actions
        if "type" in step:
            type_step = {}
            for logical_key, expected_value in step["type"].items():
                if logical_key in user_inputs and expected_value == "VALUE":
                    selector = fields.get(logical_key)
                    if selector:
                        type_step[selector] = user_inputs[logical_key]
            if type_step:
                actions.append({"type": type_step})

        # Handle "click" actions
        elif "click" in step:
            selector_key = step["click"]

            # If it's a field key AND the user provided input
            if selector_key in fields and selector_key in user_inputs:
                resolved_selector = fields[selector_key]
                actions.append({"click": resolved_selector})

                # Add dynamic dropdown click based on value
                value = user_inputs[selector_key]
                dropdown_selector = f"ul.ui-autocomplete li:has-text('{value}')"
                actions.append({"wait": dropdown_selector})
                actions.append({"click": dropdown_selector})

            # If it's not a logical field key, treat as raw (like button:has-text(...))
            elif selector_key not in fields:
                actions.append(step)

            # Else skip (e.g., product_category click when no input was given)

        # Handle wait (int or selector)
        elif "wait" in step:
            actions.append(step)

        # Allow passthrough of unknown action types
        else:
            actions.append(step)

    return actions
