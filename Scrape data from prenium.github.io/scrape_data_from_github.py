import pandas as pd
from scrapegraphai.graphs import SmartScraperGraph

# Step 1: Define the configuration for SmartScraperGraph
graph_config = {
    "llm": {
        "model": "ollama/llama2",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11434",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
}

# Step 2: Initialize SmartScraperGraph with the scraping prompt and source
smart_scraper_graph = SmartScraperGraph(
    prompt="scrape data from website",
    source="https://perinim.github.io/projects",
    config=graph_config
)

# Step 3: Run the scraper to obtain the data
result = smart_scraper_graph.run()

# Step 4: Convert the result to a pandas DataFrame
df = pd.DataFrame(result)

# Step 5: Save the DataFrame to a JSON file
json_file_path = "scraped_data.json"
df.to_json(json_file_path, orient="records", indent=4)

# Step 6: Print confirmation message
print(f"Data has been saved to {json_file_path}")
