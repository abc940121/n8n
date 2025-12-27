[
    # ----------------------------
    # Node-level (identity & metadata)
    # ----------------------------
    "node_name",
    "node_display_name",
    "node_short_name",
    "node_description",
    "node_description_format",      # "plain" | "markdown" | "html"
    "node_type_identifier",
    "node_package_name",

    # Canonical / normalized
    "node_properties",              # normalized list/dict of parameters

    # Raw preservation (single source of truth)
    "node_raw",                     # full node json


    # ----------------------------
    # Parameter-level (canonical schema)
    # ----------------------------
    "param_name",
    "param_display_name",
    "param_type",
    "param_required",
    "param_default",

    # Text (UI copy)
    "param_description",
    "param_description_format",     # "plain" | "markdown" | "html"
    "param_hint",
    "param_hint_format",            # "plain" | "markdown" | "html"
    "param_placeholder",

    # Behavior / execution flags
    "param_no_data_expression",
    "param_is_node_setting",

    # Visibility logic (canonical)
    "param_display_options",        # normalized

    # Options & constraints (canonical)
    "param_type_options",           # normalized dict
    "param_options",                # normalized option list (fixed enums)

    # Runtime / resolved values
    "param_values",                 # resolved values if applicable

    # Hierarchy & grouping
    "param_parent_name",
    "param_path",
    "param_level",
    "param_group_name",
    "param_group_display_name",

    # Raw preservation (single source of truth)
    "param_raw",


    # ----------------------------
    # Option-level (entries inside param_options)
    # ----------------------------
    "option_name",
    "option_value",
    "option_action",
    "option_description",

    # Routing (single object; no split fields)
    "option_routing",               # normalized routing block


    # ----------------------------
    # Action / Operation (selected + resolved inputs)
    # ----------------------------
    "action_operation",             # selected operation key
    "action_resource",              # selected resource key
    "action_input",                 # resolved inputs dict (was action_input_raw)
    "action_input_schema",          # optional: schema for inputs
    "action_input_keys",            # flattened input keys for indexing/search


    # ----------------------------
    # Request / Transport (execution behavior)
    # ----------------------------
    "request_options",              # normalized requestOptions collection
    "request_batching",             # batching config block (was +size/+interval)
    "request_allow_unauthorized_certs",
    "request_proxy",
    "request_timeout",
]