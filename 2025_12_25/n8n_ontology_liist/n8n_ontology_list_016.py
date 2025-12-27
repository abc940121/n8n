#add agileCrmTool.json
[
    # ----------------------------
    # Node-level
    # ----------------------------
    "node_name",
    "node_display_name",
    "node_short_name",
    "node_description",
    "node_description_format",
    "node_type_identifier",
    "node_package_name",
    "node_properties",
    "node_raw",
    "node_classification",
    "node_tooling",

    # ----------------------------
    # Parameter-level (base)
    # ----------------------------
    "param_name",
    "param_display_name",
    "param_type",
    "param_required",
    "param_default",
    "param_description",
    "param_description_format",
    "param_hint",
    "param_hint_format",
    "param_placeholder",
    "param_links",
    "param_flags",

    # ----------------------------
    # Parameter behavior & UI
    # ----------------------------
    "param_no_data_expression",      # noDataExpression
    "param_display_options",         # displayOptions.show / hide
    "param_type_options",            # typeOptions (rows, minValue, maxValue, etc.)
    "param_ui_type",                 # notice / boolean / options / collection / fixedCollection / json
    "param_visibility",
    "param_visibility_paths",
    "param_ui_actions",              # button text, add/remove behaviors
    "param_variants",                # conditional variants
    "param_selection_mode",          # single / multiple
    "param_collection_mode",         # multipleValues, alwaysOpenEditWindow
    "param_collection_spec",         # values schema for fixedCollection / collection

    # ----------------------------
    # Parameter hierarchy
    # ----------------------------
    "param_parent_name",
    "param_path",
    "param_level",
    "param_group_name",
    "param_group_display_name",

    # ----------------------------
    # Parameter value space
    # ----------------------------
    "param_options",
    "param_constraints",
    "param_values",
    "param_raw",

    # ----------------------------
    # Option-level (options[])
    # ----------------------------
    "option_name",
    "option_value",
    "option_description",
    "option_action",                 # option.action (e.g. Create a contact)
    "option_routing",                # conditional routing / behavior
    "option_meta",

    # ----------------------------
    # Filter / Query semantics
    # ----------------------------
    "filter_type",                   # none / manual / json
    "filter_match_type",             # anyFilter / allFilters
    "filter_conditions",
    "filter_condition_field",
    "filter_condition_operator",     # EQUALS / BETWEEN / AFTER / etc.
    "filter_condition_value",
    "filter_condition_value_secondary",

    # ----------------------------
    # Sorting / pagination
    # ----------------------------
    "pagination_limit",
    "pagination_return_all",
    "sort_field",
    "sort_direction",

    # ----------------------------
    # Action / Operation layer
    # ----------------------------
    "action_resource",
    "action_operation",
    "action_label",                  # human-readable action text
    "action_input",
    "action_input_schema",
    "action_input_keys",

    # ----------------------------
    # Execution / Transport
    # ----------------------------
    "transport",
    "connection",
    "tool_config",
    "data_path_requirements",

    # ----------------------------
    # AI / Agent integration
    # ----------------------------
    "ai_config",
    "agent_config",
    "ai_io",
]