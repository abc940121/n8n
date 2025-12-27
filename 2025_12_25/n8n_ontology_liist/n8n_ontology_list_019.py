#add airtableTrigger.json
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
    # Trigger semantics (NEW from airtableTrigger.json)
    # ----------------------------
    "trigger_type",                    # trigger|polling|webhook (generalized category)
    "trigger_mode",                    # polling schedule mode (everyDay/everyX/custom/...)
    "trigger_poll_times",              # pollTimes collection (raw/normalized)
    "trigger_poll_items",              # pollTimes.item[] normalized list

    # Poll schedule fields (normalized)
    "trigger_schedule_mode",           # everyMinute|everyHour|everyDay|everyWeek|everyMonth|everyX|custom
    "trigger_schedule_hour",
    "trigger_schedule_minute",
    "trigger_schedule_day_of_month",
    "trigger_schedule_weekday",
    "trigger_schedule_interval_value", # value for everyX
    "trigger_schedule_interval_unit",  # minutes|hours for everyX
    "trigger_schedule_cron_expression",# cronExpression for custom
    "trigger_schedule_constraints",    # min/max/range constraints for schedule params

    # Trigger event cursor / ordering fields
    "trigger_sort_field",              # e.g., Created Time / Last Modified Time
    "trigger_sort_field_description",  # explanation/requirements for this field

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
    "param_requires_data_path",
    "param_data_path_binding",
    "data_path_mode",

    # Dynamic loading / dependency (options & list search)
    "param_load_options_method",
    "param_search_list_method",
    "param_load_options_depends_on",
    "param_searchable",
    "param_options_source",

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
    # Resource mapper (resourceMapper)
    # ----------------------------
    "param_resource_mapper",
    "mapper_default",
    "mapper_mapping_mode",
    "mapper_value",
    "mapper_mode",
    "mapper_method",
    "mapper_field_words_singular",
    "mapper_field_words_plural",
    "mapper_add_all_fields",
    "mapper_multi_key_match",

    # ----------------------------
    # Multi-select option types (multiOptions)
    # ----------------------------
    "param_multi_select_mode",
    "param_multi_options",

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

    # Airtable query primitives (also used by trigger additionalFields)
    "query_filter_expression",         # e.g., formula/filterByFormula
    "query_view",                      # viewId
    "fields_include",                  # additionalFields.fields
    "fields_exclude",

    # ----------------------------
    # Attachment handling (trigger/tool common)
    # ----------------------------
    "attachments_download",
    "attachment_field_names",
    "attachment_download_mode",        # derived: by list / by mapping / by explicit names
    "attachment_field_name_separator", # e.g., comma-separated list

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
