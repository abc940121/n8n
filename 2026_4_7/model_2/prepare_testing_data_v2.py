import os
import json

TESTING_DATA_DIR = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\n8n_workflow_generator\n8n_templates\testing_data"
OUTPUT_FILE = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\test_100_prompts.jsonl"

def format_prompt(workflow_data):
    """
    Construct the prompt in the same way as the training data.
    Based on create_train_messages.jsonl, it seems to be:
    "I need a workflow that " + [workflow description]
    """
    description = workflow_data.get("workflow", {}).get("description", "")
    if not description:
        description = workflow_data.get("metadata", {}).get("description", "")
    
    # Clean up some common artifacts if they exist (though usually it's best to keep it exact)
    prompt = f"I need a workflow that {description}"
    return prompt

def main():
    # Read the first 100 JSON files
    files = [f for f in os.listdir(TESTING_DATA_DIR) if f.endswith(".json") and f != "templates_index.json"]
    # Sort files by their integer ID to ensure consistency
    files.sort(key=lambda x: int(x.split("_")[1]) if len(x.split("_")) > 1 and x.split("_")[1].isdigit() else 0)
    
    top_100_files = files[:100]
    print(f"Selecting {len(top_100_files)} files for testing.")
    
    processed_count = 0
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_f:
        for filename in top_100_files:
            filepath = os.path.join(TESTING_DATA_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as in_f:
                try:
                    data = json.load(in_f)
                    prompt = format_prompt(data)
                    
                    # Store both the prompt and the original ID for evaluation later
                    out_f.write(json.dumps({
                        "id": data.get("workflow", {}).get("id", filename),
                        "prompt": prompt,
                        "ground_truth": data.get("workflow", {}).get("workflow", {}) # The actual nodes/connections
                    }, ensure_ascii=False) + "\n")
                    processed_count += 1
                except Exception as e:
                    print(f"Error parsing {filename}: {e}")
                    
    print(f"Successfully wrote {processed_count} testing items to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
