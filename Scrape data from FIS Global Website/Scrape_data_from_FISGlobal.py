import json
from scrapegraphai.graphs import SmartScraperGraph

# Configuration for SmartScraperGraph
graph_config = {
    "llm": {
        "model": "ollama/wizardlm2:7b",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11434",  # Example base URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # Example base URL
    },
    "verbose": True,
}

# Create instance of SmartScraperGraph
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract relevant data from FIS Global website",
    source="https://www.fisglobal.com/",
    config=graph_config
)

# Run the scraper and obtain the result
result = smart_scraper_graph.run()

# Save the result to a JSON file
with open('fisglobal_data.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

print("Data extracted and saved to fisglobal_data.json.")