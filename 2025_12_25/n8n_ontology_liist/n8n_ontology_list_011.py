#add affinityTrigger.json
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

    # NEW (trigger semantics / classification)
    "node_kind",                    # "trigger" | "action" | "utility" | "unknown"
    "node_is_trigger",              # bool (derived or explicit)
    "node_trigger_type",            # "webhook" | "polling" | "schedule" | "unknown"
    "node_event_source",            # e.g., "Affinity" (service/system that emits events)

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

    # NEW (multi/single selection capability; avoids overloading param_type semantics)
    "param_is_multi",               # bool (e.g., multiOptions => True)
    "param_selection_mode",         # "single" | "multi" | "none"

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

    # NEW (option identity standardization; keep name/value but also allow stable IDs if present)
    "option_id",                    # stable id if source provides it (otherwise None)

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

    # NEW (webhook-trigger transport; separate from generic request_* which is usually outbound HTTP)
    "webhook_config",               # normalized webhook block if node defines it
    "webhook_events",               # resolved/selected events list (e.g., from param_values["events"])
]