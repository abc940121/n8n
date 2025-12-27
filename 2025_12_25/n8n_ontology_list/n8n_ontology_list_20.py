#add airtop.json
ontology_list = [
    # ----------------------------
    # Node-level (n8n node definition)
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
    # Parameter-level (shared schema for each property/parameter)
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
    "param_selection_mode",
    "param_options",
    "param_constraints",
    "param_collection_mode",
    "param_collection_spec",
    "param_visibility",
    "param_visibility_paths",
    "param_ui_actions",
    "param_variants",
    "param_parent_name",
    "param_path",
    "param_level",
    "param_group_name",
    "param_group_display_name",
    "param_values",
    "param_raw",

    # ----------------------------
    # Option-level (for param_options items)
    # ----------------------------
    "option_name",
    "option_value",
    "option_description",
    "option_routing",
    "option_meta",

    # NEW (from airtop.json: option objects can include an explicit action label)
    "option_action",

    # ----------------------------
    # Action / routing / tooling layers
    # ----------------------------
    "action_resource",
    "action_operation",
    "action_input",
    "action_input_schema",
    "action_input_keys",
    "transport",
    "ai_config",
    "agent_config",
    "ai_io",
    "tool_config",
    "connection",
    "data_path_requirements",

    # ----------------------------
    # NEW: validation & extraction (common in resourceLocator/modes and general params)
    # ----------------------------
    "param_validation",
    "param_validation_type",
    "param_validation_properties",
    "param_validation_regex",
    "param_validation_error_message",

    "param_extract_value",
    "param_extract_value_type",
    "param_extract_value_regex",

    # ----------------------------
    # NEW: url / expression-like defaults (seen in Airtable/Airtop style fields)
    # ----------------------------
    "param_url_template",
    "param_default_is_expression",

    # ----------------------------
    # NEW: typeOptions decomposed (to avoid losing important behavior in param_type_options blob)
    # ----------------------------
    "param_load_options_depends_on",
    "param_type_options_rows",

    "param_type_options_load_options_method",
    "param_type_options_search_list_method",
    "param_type_options_searchable",

    "param_type_options_resource_mapper_method",
    "param_type_options_resource_mapper_mode",
    "param_type_options_field_words_singular",
    "param_type_options_field_words_plural",
    "param_type_options_add_all_fields",
    "param_type_options_multi_key_match",

    # ----------------------------
    # NEW: data-path requirements at parameter level (e.g., requiresDataPath: single/multiple)
    # ----------------------------
    "param_requires_data_path",

    # ----------------------------
    # NEW: notice-style parameters (e.g., type: notice with HTML content)
    # ----------------------------
    "param_notice",
    "param_notice_format",
]
