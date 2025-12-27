#add agent.json
[
    # ============================================================
    # Node-level (identity, description, raw)
    # ============================================================
    "node_name",
    "node_display_name",
    "node_short_name",
    "node_description",
    "node_description_format",          # "plain" | "markdown" | "html"
    "node_type_identifier",
    "node_package_name",

    "node_properties",                  # canonical normalized parameters (list/dict)
    "node_raw",                         # single source of truth


    # ============================================================
    # Node-level classification (MECE bucket for trigger/AI/etc.)
    # ============================================================
    "node_classification",              # dict: {kind,is_trigger,trigger_type,event_source,is_ai,ai_role,ai_provider,...}


    # ============================================================
    # Parameter-level (canonical)
    # ============================================================
    "param_name",
    "param_display_name",
    "param_type",
    "param_required",
    "param_default",

    # Text/UX copy (keep formats minimal but explicit)
    "param_description",
    "param_description_format",         # "plain" | "markdown" | "html"
    "param_hint",
    "param_hint_format",                # "plain" | "markdown" | "html"
    "param_placeholder",

    # Behavior flags (execution/runtime)
    "param_flags",                      # dict: {no_data_expression,is_node_setting,...}

    # Selection & options (MECE)
    "param_selection_mode",             # "single" | "multi" | "none"
    "param_options",                    # list of option entries (fixed enums)
    "param_constraints",                # dict: typeOptions + other constraints (normalized)

    # Visibility & availability (all conditions merged)
    "param_visibility",                 # dict: {display,disabled,version,is_hidden,ui_kind,...}

    # Hierarchy & grouping
    "param_parent_name",
    "param_path",
    "param_level",
    "param_group_name",
    "param_group_display_name",

    # Runtime / resolved
    "param_values",

    # Raw
    "param_raw",


    # ============================================================
    # Option-level (inside param_options)
    # ============================================================
    "option_name",
    "option_value",
    "option_description",
    "option_routing",                   # normalized routing block (or None)
    "option_meta",                      # dict: {id,icon,label,type,action,...} (sparse)


    # ============================================================
    # Action / Operation (selected operation + resolved inputs)
    # ============================================================
    "action_resource",
    "action_operation",
    "action_input",                     # resolved inputs dict
    "action_input_schema",              # optional schema for inputs
    "action_input_keys",                # flattened keys for indexing/search


    # ============================================================
    # Transport (inbound trigger + outbound request unified)
    # ============================================================
    "transport",                        # dict: {inbound:{...}, outbound:{...}}


    # ============================================================
    # AI / Agent configuration (normalized, avoids field explosion)
    # ============================================================
    "ai_config",                        # dict: provider/role/model/system/user/tools/output_parser/etc (normalized)
    "agent_config",                     # dict: agent_type, iterations, intermediate_steps, prompt blocks... (normalized)
    "ai_io",                            # dict: {requires_output_format, supports_output_parser, has_tools,...} (derived)


    # ============================================================
    # External connection (credentials / datasource / db)
    # ============================================================
    "connection",                       # dict: {credentials_ref, data_source, db:{dialect,include,ignore,limits,...}}
]