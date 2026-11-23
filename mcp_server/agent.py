from pathlib import Path
from google.adk.agents import Agent
from google.adk.models import FallbackModel, Gemini, LiteLlm
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.genai import types
from mcp import StdioServerParameters

folder = Path(__file__).parent.joinpath("files").resolve()
folder.mkdir(exist_ok=True)
cds_format = folder.joinpath("cds_view_format.md").read_text(encoding="utf-8")

root_agent = Agent(
    name="filesystem_agent",
    model=FallbackModel(
        models=[
            LiteLlm(
                model="ollama_chat/llama3.2",
                api_base="http://localhost:11434",
            ),
            Gemini(
                model="gemini-3.8-flash",
                retry_options=types.HttpRetryOptions(
                    attempts=3,
                    initial_delay=1,
                    max_delay=4,
                ),
            ),
        ]
    ),
    instruction=(
        f"Help users manage files in {folder}. Use absolute paths. "
        "For requests to create an ABAP CDS view, read and follow the "
        "CDS format reference below. Reuse its annotation order and "
        "$session.client as clnt projection element, but never copy "
        "table-specific names, fields, keys, or descriptions. Read relevant "
        "table-specific files in the managed folder for schema context. "
        "If reliable fields and keys are unavailable, ask the user for them "
        "instead of inventing them.\n\n"
        f"{cds_format}"
    ),
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@modelcontextprotocol/server-filesystem", str(folder)],
                )
            )
        )
    ]
)