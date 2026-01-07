from invoke import task


@task
def run(context):
    """Inicia o servidor FastAPI"""
    context.run("uv run uvicorn src.app.main:app --reload")
