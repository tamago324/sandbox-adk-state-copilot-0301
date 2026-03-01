from ag_ui_adk import ADKAgent
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext


def user_name_setter(user_name: str, tool_context: ToolContext):
    """ユーザー名をセットします。"""
    tool_context.state["user_name"] = user_name


hello_agent = LlmAgent(
    name="hello_agent",
    description="ユーザー名を state に保存するエージェント",
    model="gemini-2.5-flash-lite",
    instruction="""
ユーザーからの入力はでは、ユーザー名が入力されます。
ユーザー名を受け取ったら、 'user_name_setter' ツールを使ってユーザー名を保存してください。
""",
    tools=[user_name_setter],
)


adk_hello_agent = ADKAgent(
    adk_agent=hello_agent,
    user_id="demo_user",
    session_timeout_seconds=3600,
    use_in_memory_services=True,
)
