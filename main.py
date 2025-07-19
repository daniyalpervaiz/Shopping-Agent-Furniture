from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool
from dotenv import load_dotenv
import os
import requests
import rich

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please check your .env file")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)
config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True,
)

@function_tool
def get_products():
    """Retrieve all available products from the online source.
    """
    url = "https://hackathon-apis.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return products
    except requests.RequestException as e:
        return {"error": str(e)}

agent = Agent(
    name = "Shopping Agent",
    instructions = 
    """You are a helpful assistant. Use the product list provided by the Agent to suggest a product based on the user's query. Be friendly and supportive in your responses.""",
    tools = [get_products]
)
result = Runner.run_sync(
    agent,
    #input = input("\033[1;36m which thing you want to buy?\033[0m "),
    input = "Can you show me all the available products along with their names, prices & description? ",
    run_config = config
)
test_query = [
    "show me all the products available, including teir names, prices & discounted prices in PKR",
    "What recommendations do you have for enhancing or upgrading my room?",
    "What's a good buy these days, you think?",
    "Which furniture piece do you need - sofa, table, or chair?",
    "What's trending as a smart purchase currently?"

]
for query in test_query:
    rich.print(f"\n[b cyan] user Prompt:[/b cyan] {query}")

    result = Runner.run_sync(
        agent, 
        input = query,
        run_config = config
    )

rich.print(result.final_output)