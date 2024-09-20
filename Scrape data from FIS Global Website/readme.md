https://scrapegraph-ai.readthedocs.io/en/latest/introduction/overview.html

Documentation: Extracting Data from FIS Global Website using SmartScraperGraph and Saving as JSON

This script demonstrates how to use the SmartScraperGraph class from ScrapeGraph AI to scrape relevant data from the FIS Global website and save the result in a JSON file.

Prerequisites

Python 3.x must be installed.

The following packages need to be installed:

scrapegraphai

Script Overview

Import Required Libraries:
The script imports json for handling JSON files and SmartScraperGraph from scrapegraphai to perform web scraping.

import json
from scrapegraphai.graphs import SmartScraperGraph

Graph Configuration:
The configuration for the language model (LLM) and embeddings is defined in a dictionary. In this case, the ollama/wizardlm2:7b model is used, with specific settings such as temperature, format, and the base URL of the server where the model is hosted.

graph_config = {
    "llm": {
        "model": "ollama/wizardlm2:7b",
        "temperature": 0,
        "format": "json",
        "base_url": "<http://localhost:11434>",  # Example base URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "<http://localhost:11434>",  # Example base URL
    },
    "verbose": True,
}

Initialize SmartScraperGraph:
The SmartScraperGraph is initialized with a scraping prompt and the URL of the FIS Global website. The configuration created earlier is passed into the constructor.

smart_scraper_graph = SmartScraperGraph(
    prompt="Extract relevant data from FIS Global website",
    source="<https://www.fisglobal.com/>",
    config=graph_config
)

Run the Scraper:
The run() method is called to execute the scraper, which returns the scraped data.

result = smart_scraper_graph.run()

Save the Result to a JSON File:
The scraped result is saved in a file named fisglobal_data.json. The json.dump() function is used to write the JSON data to the file with a readable indentation of 4 spaces.

with open('fisglobal_data.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

Print Confirmation:
Once the data is saved, a confirmation message is printed to indicate the successful extraction and storage.

print("Data extracted and saved to fisglobal_data.json.")

Full Code Example

import json
from scrapegraphai.graphs import SmartScraperGraph

# Configuration for SmartScraperGraph
graph_config = {
    "llm": {
        "model": "ollama/wizardlm2:7b",
        "temperature": 0,
        "format": "json",
        "base_url": "<http://localhost:11434>",  # Example base URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "<http://localhost:11434>",  # Example base URL
    },
    "verbose": True,
}

# Create instance of SmartScraperGraph
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract relevant data from FIS Global website",
    source="<https://www.fisglobal.com/>",
    config=graph_config
)

# Run the scraper and obtain the result
result = smart_scraper_graph.run()

# Save the result to a JSON file
with open('fisglobal_data.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

print("Data extracted and saved to fisglobal_data.json.")

Output

The scraped data will be saved to a file named fisglobal_data.json in the directory where the script is executed.

Additional Notes

Ensure that the ollama models and embeddings are properly set up and running on the local server specified in the base_url.

The FIS Global website (<https://www.fisglobal.com/)> is used as the source for scraping, and the prompt specifies that relevant data should be extracted from this site. The content of the extracted data will depend on the website structure and the capabilities of the language model used in the scraping process.

