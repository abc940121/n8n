#add adalo.json
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

    # Canonical, normalized representation
    "node_properties",             # normalized list/dict of parameters
    "node_raw",                    # full node json
    "node_properties_raw",         # original properties block

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
    "param_hint",                   # NEW: tooltip / hint text (e.g. Adalo collection hint)
    "param_no_data_expression",
    "param_is_node_setting",        # NEW: isNodeSetting (e.g. requestOptions)

    # UI / visibility logic
    "param_display_options",        # normalized

    # Options & constraints (standardized)
    "param_type_options",           # normalized dict: {multiple_values, min_value, max_value, rows, button_text, ...}
    "param_options",                # normalized option list (for fixed enums)
    "param_values",                 # runtime / resolved values if applicable

    # Hierarchy & grouping
    "param_parent_name",
    "param_path",
    "param_level",
    "param_group_name",
    "param_group_display_name",

    # Raw preservation
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
    "option_routing",               # NEW: routing block (request/send/output)
    "option_routing_request",       # NEW: HTTP method / url / qs
    "option_routing_send",          # NEW: send config (preSend, paginate)
    "option_routing_output",        # NEW: output transforms (postReceive)

    # ----------------------------
    # Operation / Action input
    # ----------------------------
    "action_operation",             # selected operation key
    "action_resource",              # selected resource key
    "action_input_raw",             # dict of resolved inputs
    "action_input_schema",          # optional: schema for inputs
    "action_input_keys",            # flattened input keys for indexing/search

    # ----------------------------
    # Request / Transport-level (node settings & execution behavior)
    # ----------------------------
    "request_options",              # normalized requestOptions collection
    "request_batching",             # batching config block
    "request_batch_size",           # items per batch
    "request_batch_interval",       # ms between batches
    "request_allow_unauthorized_certs",  # ignore SSL issues
    "request_proxy",                # proxy string
    "request_timeout",              # timeout in ms
]