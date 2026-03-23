import json
import csv
import sys

def main():
    input_file = 'n8n_training_data_v2_humanized.jsonl'
    csv_output = 'workflow_difficulty_list.csv'

    data_list = []
    
    # Read data
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                item = json.loads(line)
                query = item.get('input', '')
                output_str = item.get('output', '{}')
                
                try:
                    output_data = json.loads(output_str)
                    nodes = len(output_data.get('nodes', []))
                except Exception:
                    nodes = 0
                
                data_list.append({
                    'index': i + 1,
                    'query': query,
                    'nodes': nodes
                })
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        sys.exit(1)

    # Sort to find quantiles
    sorted_nodes = sorted([d['nodes'] for d in data_list])
    n = len(sorted_nodes)
    if n == 0:
        print("No valid data found.")
        sys.exit(1)
        
    threshold_low = sorted_nodes[n // 3]      # ~33rd percentile
    threshold_mid = sorted_nodes[2 * n // 3]  # ~66th percentile

    print(f"Total workflows: {n}")
    print(f"Thresholds -> Low: <= {threshold_low} nodes, Medium: {threshold_low + 1} to {threshold_mid} nodes, High: > {threshold_mid} nodes")

    # Categorize and write CSV
    counts = {'Low': 0, 'Medium': 0, 'High': 0}
    with open(csv_output, 'w', encoding='utf-8', newline='') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=['Index', 'Difficulty', 'Node_Count', 'User_Query'])
        writer.writeheader()
        
        for d in data_list:
            nodes = d['nodes']
            if nodes <= threshold_low:
                diff = 'Low'
            elif nodes <= threshold_mid:
                diff = 'Medium'
            else:
                diff = 'High'
                
            counts[diff] += 1
            d['difficulty'] = diff
            
            writer.writerow({
                'Index': d['index'],
                'Difficulty': diff,
                'Node_Count': nodes,
                'User_Query': d['query']
            })

    print(f"Categories count: Low: {counts['Low']}, Medium: {counts['Medium']}, High: {counts['High']}")
    print(f"List successfully saved to {csv_output}")

    # Generate an artifact markdown file with a sample
    artifact_md = r"C:\Users\User\.gemini\antigravity\brain\87883a2e-fe38-4df7-8c0d-34fc2c7645c8\workflow_difficulty_summary.md"
    try:
        with open(artifact_md, 'w', encoding='utf-8') as f_md:
            f_md.write("# Workflow Difficulty List Summary\n\n")
            f_md.write(f"Total workflows categorized: {n}\n\n")
            f_md.write("### Criteria:\n")
            f_md.write(f"- **Low**: <= {threshold_low} nodes\n")
            f_md.write(f"- **Medium**: {threshold_low + 1} to {threshold_mid} nodes\n")
            f_md.write(f"- **High**: > {threshold_mid} nodes\n\n")
            f_md.write("### Distribution:\n")
            f_md.write(f"- **Low**: {counts['Low']} workflows\n")
            f_md.write(f"- **Medium**: {counts['Medium']} workflows\n")
            f_md.write(f"- **High**: {counts['High']} workflows\n\n")
            f_md.write("A detailed CSV file containing all 1963 classified workflows has been saved to `workflow_difficulty_list.csv`.\n\n")
            f_md.write("### Sample Workflows (Top 5 of each category):\n\n")
            
            f_md.write("#### Low Difficulty\n")
            for d in [x for x in data_list if x['difficulty'] == 'Low'][:5]:
                f_md.write(f"- [{d['nodes']} nodes] {d['query']}\n")
                
            f_md.write("\n#### Medium Difficulty\n")
            for d in [x for x in data_list if x['difficulty'] == 'Medium'][:5]:
                f_md.write(f"- [{d['nodes']} nodes] {d['query']}\n")
                
            f_md.write("\n#### High Difficulty\n")
            for d in [x for x in data_list if x['difficulty'] == 'High'][:5]:
                f_md.write(f"- [{d['nodes']} nodes] {d['query']}\n")
    except Exception as e:
        print(f"Failed to generate artifact md: {e}")

if __name__ == '__main__':
    main()
