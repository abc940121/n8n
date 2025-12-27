#add airtableTool.json
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

    # Node lifecycle / messaging
    "node_notice",
    "node_notice_format",
    "node_version_status",
    "node_deprecation_status",
    "node_deprecation_message",

    # ----------------------------
    # Credential / Authentication
    # ----------------------------
    "auth_mode",
    "auth_supported_modes",
    "auth_credential_type",

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
    "param_no_data_expression",
    "param_display_options",
    "param_type_options",
    "param_ui_type",
    "param_visibility",
    "param_visibility_paths",
    "param_ui_actions",
    "param_variants",
    "param_selection_mode",
    "param_collection_mode",
    "param_collection_spec",

    # Data-path binding semantics
    "param_requires_data_path",          # requiresDataPath (none|single|multiple)
    "param_data_path_binding",           # generalized binding semantics
    "data_path_mode",                    # normalized mode indicator

    # ----------------------------
    # Dynamic loading / dependency (options & list search)
    # ----------------------------
    "param_load_options_method",         # loadOptionsMethod
    "param_search_list_method",          # searchListMethod (resourceLocator list mode)
    "param_load_options_depends_on",     # loadOptionsDependsOn
    "param_searchable",                  # searchable: true/false for list mode
    "param_options_source",              # where options come from (static|loadOptions|searchList)

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
    "option_action",
    "option_routing",
    "option_meta",

    # ----------------------------
    # Resource locator (resourceLocator)
    # ----------------------------
    "param_resource_locator",
    "locator_default",
    "locator_modes",
    "locator_mode_name",
    "locator_mode_type",
    "locator_mode_placeholder",
    "locator_mode_url_template",

    # Locator validation & extraction
    "locator_validation_rules",
    "validation_type",
    "validation_regex",
    "validation_error_message",
    "locator_extract_value_rule",
    "extract_value_type",
    "extract_value_regex",

    # ----------------------------
    # Resource mapper (resourceMapper)  [NEW from airtableTool.json]
    # ----------------------------
    "param_resource_mapper",             # whether param is resourceMapper
    "mapper_default",                    # default {mappingMode, value}
    "mapper_mapping_mode",               # mappingMode (defineBelow|autoMapInputData|...)
    "mapper_value",                      # mapper value payload (nullable/object)
    "mapper_mode",                       # resourceMapper.mode (add|update|...)
    "mapper_method",                     # resourceMapperMethod (getColumns|getColumnsWithRecordId|...)
    "mapper_field_words_singular",       # fieldWords.singular
    "mapper_field_words_plural",         # fieldWords.plural
    "mapper_add_all_fields",             # addAllFields boolean
    "mapper_multi_key_match",            # multiKeyMatch boolean

    # ----------------------------
    # Multi-select option types (multiOptions)  [NEW generalization]
    # ----------------------------
    "param_multi_select_mode",           # whether param supports multiple selection
    "param_multi_options",              # multiOptions value set (list)

    # ----------------------------
    # Query semantics (generalized)
    # ----------------------------
    "filter_type",
    "filter_match_type",
    "filter_conditions",
    "filter_condition_field",
    "filter_condition_operator",
    "filter_condition_value",
    "filter_condition_value_secondary",

    # Formula / view / field projection (Airtable tool)
    "query_filter_expression",           # e.g., filterByFormula
    "query_view",
    "fields_include",
    "fields_exclude",
    "attachments_download",
    "attachment_field_names",

    # ----------------------------
    # Sorting / pagination
    # ----------------------------
    "pagination_limit",
    "pagination_return_all",
    "sort_field",
    "sort_direction",

    # Batching / bulk processing
    "batch_size",

    # Type coercion / casting
    "typecast_enabled",

    # ----------------------------
    # Action / Operation layer
    # ----------------------------
    "action_resource",
    "action_operation",
    "action_label",
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
