import subprocess
from invoke import task


@task
def serve(ctx):
    subprocess.call('python -m http.server', shell=True)
