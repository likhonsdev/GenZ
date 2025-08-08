import os
import pandas as pd

def update_benchmark_docs(metrics_path, docs_path):
    """Update the benchmark documentation with the latest metrics."""
    with open(metrics_path, 'r') as f:
        metrics = json.load(f)

    # Create a DataFrame from the metrics
    df = pd.DataFrame([metrics])

    # Format the DataFrame as a Markdown table
    markdown_table = df.to_markdown(index=False)

    # Read the existing documentation
    with open(docs_path, 'r') as f:
        docs_content = f.read()

    # Replace the old benchmark table with the new one
    # This is a simple replacement, a more robust solution would use a placeholder
    updated_docs = docs_content.replace("<!-- BENCHMARK_TABLE -->", markdown_table)

    # Write the updated documentation
    with open(docs_path, 'w') as f:
        f.write(updated_docs)

if __name__ == "__main__":
    # This is a placeholder for the actual documentation update logic
    # In a real-world scenario, this script would be more complex
    print("Benchmark documentation update script executed successfully.")
