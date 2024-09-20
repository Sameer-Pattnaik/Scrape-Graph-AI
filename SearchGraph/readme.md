### Documentation: Using SearchGraph for Excursions Near Trento and Saving Results as CSV and JSON

This script demonstrates how to use the `SearchGraph` class from ScrapeGraph AI to search for excursions near Trento, retrieve the top results, and save the output in both CSV and JSON formats.

#### Prerequisites
- **Python 3.x** must be installed.
- The following packages need to be installed:
  - `scrapegraphai`

#### Script Overview

1. **Import Required Libraries**:
   The script imports the necessary classes and utility functions from the `scrapegraphai` package. These include:
   - `SearchGraph` for performing the search.
   - Utility functions such as `convert_to_csv`, `convert_to_json`, and `prettify_exec_info` for saving the output and formatting execution info.
   ```python
   from scrapegraphai.graphs import SearchGraph
   from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info
   ```

2. **Graph Configuration**:
   A configuration dictionary is defined for the SearchGraph, specifying the language model and embedding model being used, along with other parameters. In this case, the configuration utilizes the `ollama/wizardlm2:7b` model with a temperature of 0. The number of maximum results is set to 5, and verbose mode is enabled for detailed output.
   ```python
   graph_config = {
       "llm": {
           "model": "ollama/wizardlm2:7b",
           "temperature": 0,
       },
       "embeddings": {
           "model": "ollama/nomic-embed-text",
           "temperature": 0,
       },
       "max_results": 5,
       "verbose": True,
   }
   ```

3. **Create and Run SearchGraph**:
   A `SearchGraph` instance is created with a specific prompt asking for the best excursions near Trento. The previously defined configuration is passed to the graph. The `run()` method is then called to execute the search and retrieve the results.
   ```python
   search_graph = SearchGraph(
       prompt="List me the best escursions near Trento",
       config=graph_config
   )

   result = search_graph.run()
   print(result)
   ```

4. **Retrieve Execution Info**:
   After running the graph, the execution details are retrieved using the `get_execution_info()` method, and the output is prettified for readability using `prettify_exec_info()`.
   ```python
   graph_exec_info = search_graph.get_execution_info()
   print(prettify_exec_info(graph_exec_info))
   ```

5. **Save the Results to CSV and JSON**:
   The `convert_to_csv()` and `convert_to_json()` utility functions are used to save the search results to `result.csv` and `result.json`, respectively.
   ```python
   convert_to_csv(result, "result")
   convert_to_json(result, "result")
   ```

#### Full Code Example
```python
"""
Example of Search Graph
"""
from scrapegraphai.graphs import SearchGraph
from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info

# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "model": "ollama/wizardlm2:7b",
        "temperature": 0,
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
    },
    "max_results": 5,
    "verbose": True,
}

# ************************************************
# Create the SearchGraph instance and run it
# ************************************************

search_graph = SearchGraph(
    prompt="List me the best escursions near Trento",
    config=graph_config
)

result = search_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = search_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Save to json and csv
convert_to_csv(result, "result")
convert_to_json(result, "result")
```

#### Output:
1. **Search Results**: The result of the search will be printed to the console. The result is a list of excursions near Trento.
2. **Execution Information**: Detailed execution information about the graph run is printed, which includes data on the configuration and process.
3. **CSV File**: The search results are saved in a file named `result.csv` in the same directory.
4. **JSON File**: The same results are saved in a JSON format in a file named `result.json`.

#### Additional Notes:
- Ensure the `ollama` models and embeddings are properly set up and running on the server specified in the configuration.
- The prompt is flexible and can be adjusted to different queries as required.