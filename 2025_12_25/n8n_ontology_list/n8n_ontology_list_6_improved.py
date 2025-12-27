[
    # ----------------------------
    # Node-level (n8n node definition)
    # ----------------------------
    "node_name",
    "node_display_name",
    "node_short_name",
    "node_description",
    "node_description_format",      # "plain" | "markdown" | "html"
    "node_type_identifier",
    "node_package_name",

    # Canonical, normalized representation (avoid duplicate raw-vs-parsed fields proliferation)
    "node_properties",             # normalized list/dict of parameters
    "node_raw",                    # full node json
    "node_properties_raw",         # original properties block (if separated)

    # ----------------------------
    # Parameter-level (shared schema for each property/parameter)
    # ----------------------------
    "param_name",
    "param_display_name",
    "param_type",
    "param_required",
    "param_default",
    "param_description",
    "param_description_format",     # "plain" | "markdown" | "html"
    "param_placeholder",
    "param_no_data_expression",

    # UI / visibility logic
    "param_display_options",        # normalized

    # Options & constraints (standardized: collapse many param_type_options_* into one)
    "param_type_options",           # normalized dict: {load_options_method, multiple_values, min_value, max_value, rows, ...}
    "param_options",                # normalized option list (for fixed enums)
    "param_values",                 # runtime / resolved values if applicable

    # Hierarchy & grouping (keep, but avoid redundant variants)
    "param_parent_name",
    "param_path",
    "param_level",
    "param_group_name",
    "param_group_display_name",

    # Raw preservation (only at a few stable touchpoints)
    "param_raw",
    "param_type_options_raw",
    "param_options_raw",

    # ----------------------------
    # Option-level (for entries inside param_options)
    # ----------------------------
    "option_name",
    "option_value",
    "option_action",
    "option_description",

    # ----------------------------
    # Operation / Action input (replaces many overly-fragmented an_* fields)
    # ----------------------------
    "action_operation",             # e.g., operation key / selected action
    "action_resource",              # e.g., resource key (if node uses resource/operation split)
    "action_input_raw",             # dict of resolved inputs (former an_* scattered keys)
    "action_input_schema",          # optional: JSON Schema-like structure for inputs
    "action_input_keys",            # optional: flattened keys list for indexing/search
]
