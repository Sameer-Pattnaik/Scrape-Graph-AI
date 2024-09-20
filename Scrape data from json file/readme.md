Documentation for JSON Scraper using ScrapeGraphAI

This documentation covers the steps involved in setting up a scraping graph using ScrapeGraphAI and processing a JSON file to extract specific data such as titles and narratives of cases.

Prerequisites

Libraries and Dependencies

Ensure you have the following installed:

ScrapeGraphAI library (for scraping and running graphs)

dotenv library (for managing environment variables)

Python 3.7+

Ollama models (for running LLM and embedding)

Install dependencies:

pip install scrapegraphai python-dotenv

Environment Variables

To load environment variables (like API keys, base URLs, etc.), you should have a .env file. Ensure it's correctly configured and contains relevant settings for your project.

Required Files

A valid JSON file to be processed (e.g., Fraud_Report_2022.json).

Script Overview

1. Loading Environment Variables

Using the dotenv library, environment variables are loaded to avoid hard-coding sensitive data in your script.

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

2. Reading the JSON File

To ensure that the file path is valid, the script checks if the JSON file exists at the specified location. The content of the file is read and stored in a variable text.

import os

# Path to the JSON file
FILE_PATH = "C:\\Users\\hp\\Downloads\\ScrapgraphAI(2)\\Fraud_Report_2022.json"

# Verify if file exists, otherwise print an error message
if not os.path.exists(FILE_PATH):
    print(f"File not found: {FILE_PATH}")
else:
    with open(FILE_PATH, 'r', encoding="utf-8") as file:
        text = file.read()  # Reading file content

3. Configuring the JSON Scraper Graph

The graph configuration is defined, specifying the models to be used for Large Language Model (LLM) and embeddings, along with a local URL for interacting with the LLM.

graph_config = {
    "llm": {
        "model": "ollama/wizardlm2:7b",  # LLM model used
        "temperature": 0,
        "format": "json",  # Specified format
        "base_url": "<http://localhost:11434>",  # Localhost base URL for Ollama API
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Embedding model used
        "temperature": 0,
        "base_url": "<http://localhost:11434>",  # Localhost base URL for Ollama API
    },
    "verbose": True,  # Enable verbose logging for debugging
}

4. Running the Scraper Graph

An instance of JSONScraperGraph is created, passing in the prompt to extract specific data (titles and narratives) from the JSON file content. The graph is then executed using the run method, and the result is printed.

from scrapegraphai.graphs import JSONScraperGraph

json_scraper_graph = JSONScraperGraph(
    prompt="List me all the titles and narratives of cases",  # Prompt to extract specific data
    source=text,  # Pass the content of the file as the source
    config=graph_config
)

# Run the graph and store the result
result = json_scraper_graph.run()
print(result)  # Display the result

5. Getting Execution Info

Once the graph has run, you can retrieve the graph's execution information to review details of the process. The execution info is prettified for easy readability.

from scrapegraphai.utils import prettify_exec_info

# Get execution info
graph_exec_info = json_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))  # Print the execution info in a readable format

6. Saving Results as CSV and JSON

Finally, the extracted results are saved to both CSV and JSON formats using utility functions.

from scrapegraphai.utils import convert_to_csv, convert_to_json

# Save the result in CSV format
convert_to_csv(result, "result")

# Save the result in JSON format
convert_to_json(result, "result")

Example Usage

Run the script to extract data from a JSON file and save the output to CSV and JSON formats. The process flow:

Load environment variables.

Read the JSON file content.

Define and configure the scraping graph.

Execute the graph and retrieve results.

Output the execution details and save the results.

Expected Output

Graph Result: Printed titles and narratives of cases extracted from the JSON file.

Execution Info: Detailed log of the graph execution process.

CSV File: result.csv containing the extracted data.

JSON File: result.json containing the extracted data.

Troubleshooting

Ensure the correct file path is specified for your JSON file.

Verify that the ollama server is running locally at localhost:11434.

Adjust the prompt and graph configuration as needed to suit the structure of your JSON data.

