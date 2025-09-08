from ddgs import DDGS

class WebSearchTool:
    """
    A tool for searching the internet and retrieving content relevant to input queries.
    """
    
    def __init__(self):
        """
        Initialize the web search tool.
        """
        self.ddgs = DDGS()
    
    def get_tool_spec(self):
        """
        Returns the JSON Schema specification for the web search tool. The tool specification
        defines the input schema and describes the tool's functionality.
        For more information, see https://json-schema.org/understanding-json-schema/reference.

        :return: The tool specification for the web search tool.
        """
        return {
            "toolSpec": {
                "name": "web_search_tool",
                "description": "Searches the internet and retrieves content relevant to the input query",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query.",
                            },
                        },
                        "required": ["query"],
                    }
                },
            }
        }

    def web_search(self, input_data) -> list[dict]:
        """
        Searches the internet and retrieves content relevant to the input query

        :param input_data: The input data containing the query.
        :return: The search results.
        """
        query = input_data.get("query")

        search_results = self.ddgs.text(query, max_results=5)
        
        print("Searching the internet for: ", query)
        # search_results = [{'title': 'Capital of France Crossword Clue - NYT Crossword Answers', 'href': 'https://nytcrosswordanswers.org/capital-of-france-crossword-clue/', 'body': 'May 6, 2020 answer of Capital Of France clue in NYT Crossword Puzzle. There is One Answer total, Euros is the most recent and it has 5 letters.'},
        #                 {'title': "Capital of France's Côte d'Or Crossword Clue", 'href': 'https://nytcrosswordanswers.org/capital-of-frances-cote-dor-crossword-clue/', 'body': 'March 18, 2019 answer of Capital Of Frances Cote Dor clue in NYT Crossword Puzzle. There is One Answer total, Dijon is the most recent and it has 5 letters.'}, 
        #                 {'title': 'Relative location of Paris France - Answers', 'href': 'https://www.answers.com/movies-and-television/Relative_location_of_Paris_France', 'body': 'Aug 30, 2023 · What is the location of Paris - the capital of France? Paris is located on the Seine river, slightly north of the center of France.'}, 
        #                 {'title': 'What was the capital of France before Paris? - Answers', 'href': 'https://www.answers.com/movies-and-television/What_was_the_capital_of_France_before_Paris', 'body': 'Aug 31, 2023 · France did not exist as such in Roman times. Its territory was then divided in provinces, some extending over the borders we now have. For the Romans, Lyon (Lyons) was …'}, 
        #                 {'title': 'Paris the capital of France is located on this river? - Answers', 'href': 'https://www.answers.com/travel-destinations/Paris_the_capital_of_France_is_located_on_this_river', 'body': 'Sep 1, 2023 · Paris, France is located on the banks of the world famous River Seine. Its banks are a World Heritage site.'}]

        return search_results