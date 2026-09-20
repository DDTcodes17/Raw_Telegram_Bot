from langchain.tools import tool

@tool
def live_cricket_score(country_1:str, country_2:str):
    """This tool tells live cricket score between countre_1 and country_2"""
    return f"Current live score between {country_1} and {country_2} is 120-3"
