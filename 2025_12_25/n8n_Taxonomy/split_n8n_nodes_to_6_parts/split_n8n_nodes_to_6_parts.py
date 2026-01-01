import json
import os

# 定義分類關鍵字規則 (由上而下匹配，優先權遞減)
CATEGORIES = {
    "01_Core_Logic": {
        "keywords": [
            "n8n-nodes-base.if", "n8n-nodes-base.switch", "n8n-nodes-base.merge", 
            "n8n-nodes-base.set", "n8n-nodes-base.function", "n8n-nodes-base.webhook", 
            "n8n-nodes-base.schedule", "n8n-nodes-base.cron", "n8n-nodes-base.splitInBatches", 
            "n8n-nodes-base.wait", "n8n-nodes-base.executeWorkflow", "n8n-nodes-base.start",
            "n8n-nodes-base.itemLists", "n8n-nodes-base.httpRequest", "n8n-nodes-base.code",
            "n8n-nodes-base.noOp", "n8n-nodes-base.dateTime", "n8n-nodes-base.crypto",
            "Variable", "Flow", "Trigger"
        ],
        "file_name": "nodes_01_core_logic.json"
    },
    "02_AI_Data": {
        "keywords": [
            "OpenAI", "Anthropic", "LangChain", "Pinecone", "Qdrant", "Supabase", "Weaviate",
            "HuggingFace", "Mistral", "Llama", "Vertex AI", "Bedrock", "Stability AI",
            "Vector", "Embeddings", "Chat", "Classifier", "Sentiment"
        ],
        "file_name": "nodes_02_ai_data.json"
    },
    "03_Dev_Cloud": {
        "keywords": [
            "AWS", "Amazon", "Google Cloud", "Azure", "DigitalOcean", "Heroku",
            "Docker", "Kubernetes", "Git", "GitHub", "GitLab", "Bitbucket",
            "Postgres", "MySQL", "Mongo", "Redis", "MariaDB", "SQLite", "Snowflake",
            "Elasticsearch", "Kafka", "RabbitMQ", "MQTT", "FTP", "SFTP", "SSH",
            "GraphQL", "S3", "Lambda"
        ],
        "file_name": "nodes_03_dev_cloud.json"
    },
    "04_Sales_Marketing": {
        "keywords": [
            "Salesforce", "HubSpot", "Pipedrive", "Zoho", "Mailchimp", "ActiveCampaign",
            "Shopify", "WooCommerce", "Stripe", "PayPal", "Typeform", "JotForm",
            "Google Analytics", "Facebook", "Instagram", "LinkedIn", "Twitter", "X",
            "TikTok", "YouTube", "WordPress", "SendGrid", "Twilio"
        ],
        "file_name": "nodes_04_sales_marketing.json"
    },
    "05_Productivity_Ops": {
        "keywords": [
            "Google", "Microsoft", "Office", "Slack", "Discord", "Telegram", "Mattermost",
            "Notion", "Trello", "Asana", "Jira", "ClickUp", "Monday", "Airtable",
            "Dropbox", "Box", "OneDrive", "Zoom", "Webex", "Calendar", "Sheet", "Excel",
            "Gmail", "Outlook", "Drive"
        ],
        "file_name": "nodes_05_productivity_ops.json"
    }
}

# 預設分類
UNCATEGORIZED_FILE = "nodes_06_uncategorized.json"

def classify_node(node):
    name = node.get("name", "").lower()
    display_name = node.get("displayName", "").lower()
    full_text = f"{name} {display_name}"
    
    # 依序檢查分類
    for cat_key, rules in CATEGORIES.items():
        for keyword in rules["keywords"]:
            if keyword.lower() in full_text:
                return cat_key, rules["file_name"]
    
    return "06_Uncategorized", UNCATEGORIZED_FILE

def main():
    input_file = "n8n_nodes_summary.json"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        nodes = json.load(f)

    # 初始化容器
    buckets = {key: [] for key in CATEGORIES.keys()}
    buckets["06_Uncategorized"] = []
    
    file_map = {key: val["file_name"] for key, val in CATEGORIES.items()}
    file_map["06_Uncategorized"] = UNCATEGORIZED_FILE

    # 開始分類
    for node in nodes:
        cat_key, _ = classify_node(node)
        buckets[cat_key].append(node)

    # 寫入檔案與報告
    report_lines = []
    total_count = 0
    
    print("--- Classification Summary ---")
    for cat_key, nodes_list in sorted(buckets.items()):
        file_name = file_map[cat_key]
        count = len(nodes_list)
        total_count += count
        
        # 寫入 JSON 檔案
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(nodes_list, f, indent=2, ensure_ascii=False)
            
        print(f"{cat_key}: {count} nodes -> Saved to {file_name}")
        
        # 產生報告內容
        report_lines.append(f"\n=== {cat_key} ({count} nodes) ===")
        # 只列出 DisplayName 方便快速檢視
        node_names = sorted([n.get('displayName') for n in nodes_list])
        report_lines.append(", ".join(node_names))

    # 輸出驗證報告
    with open("category_validation_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"\nTotal Processed: {total_count}")
    print("Verification report saved to: category_validation_report.txt")
    print("You can now open 'category_validation_report.txt' to verify the lists.")

if __name__ == "__main__":
    main()