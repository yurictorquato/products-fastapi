from invoke import task


@task
def run(context):
    """Inicia o servidor FastAPI"""
    context.run("PYTHONPATH=src uvicorn app.main:app --reload")
