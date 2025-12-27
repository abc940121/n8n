#add agentTool.json
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
    # Node-level classification (trigger/AI/tool/etc.)
    # ============================================================
    "node_classification",              # dict: {kind,is_trigger,trigger_type,event_source,is_ai,ai_role,ai_provider,...}

    # NEW (tool semantics; covers nodes like "AI Agent Tool")
    "node_tooling",                     # dict: {is_tool,tool_kind,tool_label,tool_purpose,...}


    # ============================================================
    # Parameter-level (canonical)
    # ============================================================
    "param_name",
    "param_display_name",
    "param_type",
    "param_required",
    "param_default",

    # Text/UX copy
    "param_description",
    "param_description_format",         # "plain" | "markdown" | "html"
    "param_hint",
    "param_hint_format",                # "plain" | "markdown" | "html"
    "param_placeholder",

    # Behavior flags (execution/runtime)
    "param_flags",                      # dict: {no_data_expression,is_node_setting,...}

    # Selection & options
    "param_selection_mode",             # "single" | "multi" | "none"
    "param_options",                    # list of option entries (fixed enums)
    "param_constraints",                # dict: typeOptions + other constraints (normalized)

    # Visibility & availability (all conditions merged)
    "param_visibility",                 # dict: {display,disabled,version,is_hidden,ui_kind,...}

    # NEW (UI embedded actions inside displayName/description HTML)
    # Example: <a data-action='openSelectiveNodeCreator' data-action-parameter-connectiontype='ai_outputParser'>...</a>
    "param_ui_actions",                 # list[dict]: extracted actions from HTML (action, parameters, connectiontype, etc.)

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
    # AI / Agent configuration (normalized)
    # ============================================================
    "ai_config",                        # dict: provider/role/model/system/user/tools/output_parser/fallback/etc
    "agent_config",                     # dict: agent_type, iterations, batching, passthroughBinaryImages, etc
    "ai_io",                            # dict: {requires_output_format, has_output_parser, needs_fallback, ...} (derived)

    # NEW (explicit tool-layer config; avoids smearing "toolDescription/text" into generic ai_config)
    "tool_config",                      # dict: {tool_description,user_prompt,requires_output_parser,needs_fallback,...}


    # ============================================================
    # External connection (credentials / datasource / db)
    # ============================================================
    "connection",                       # dict: {credentials_ref, data_source, db:{dialect,include,ignore,limits,...}}
]
