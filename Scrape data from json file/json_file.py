import os
from dotenv import load_dotenv
from scrapegraphai.graphs import JSONScraperGraph
from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info

# Load environment variables
load_dotenv()

# ************************************************
# Read the JSON file
# ************************************************

# Update the path to the correct location of your JSON file
FILE_PATH = "C:\\Users\\hp\\Downloads\\ScrapgraphAI(2)\\Benchmarking\\Input\\Fraud_Report_2022.json"

# Debugging: Print the file path
print(f"File path: {FILE_PATH}")

# Verify the file exists
if not os.path.exists(FILE_PATH):
    print(f"File not found: {FILE_PATH}")
else:
    with open(FILE_PATH, 'r', encoding="utf-8") as file:
        text = file.read()

    # ************************************************
    # Define the configuration for the graph
    # ************************************************

    graph_config = {
        "llm": {
            "model": "ollama/wizardlm2:7b",
            "temperature": 0,
            "format": "json",  # Specify the format explicitly
            "base_url": "http://localhost:11434",
        },
        "embeddings": {
            "model": "ollama/nomic-embed-text",
            "temperature": 0,
            "base_url": "http://localhost:11434",
        },
        "verbose": True,
    }

    # ************************************************
    # Create the JSONScraperGraph instance and run it
    # ************************************************

    json_scraper_graph = JSONScraperGraph(
        prompt="List me all the titles and narratives of cases",
        source=text,  # Pass the content of the file, not the file object
        config=graph_config
    )

    result = json_scraper_graph.run()
    print(result)

    # ************************************************
    # Get graph execution info
    # ************************************************

    graph_exec_info = json_scraper_graph.get_execution_info()
    print(prettify_exec_info(graph_exec_info))

    # Save to json or csv
    convert_to_csv(result, "result")
    convert_to_json(result, "result")
