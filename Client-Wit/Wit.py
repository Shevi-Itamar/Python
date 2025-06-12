import os

from Modul import Create_a_new_folder
from Repository import repository
import click
import asyncio

repository = repository()
import requests

try:
    response = requests.get("http://localhost:8000/")
    print(response.status_code)
    print(response.text)
except Exception as e:
    print("Error:", e)
@click.group()

def cli():
    pass

@click.command()
def init():
    if not os.path.exists(os.path.join(os.getcwd(),'.wit')):
        Create_a_new_folder(os.getcwd(),'.wit')

@click.command()
@click.argument('path')
def add(path):
    repository.add(path)

@click.command()
@click.argument('message')
def commit(message):
    repository.commit(message)

@click.command()
def log():
    repository.log()

@click.command()
def status():
    repository.status()

@click.command()
def push():
    repository.push()


@click.command()
@click.argument('commit_id')
def checkout(commit_id):
    repository.checkout(commit_id)


cli.add_command(init)
cli.add_command(add)
cli.add_command(checkout)
cli.add_command(status)
cli.add_command(log)
cli.add_command(commit)
cli.add_command(push)

if __name__=='__main__':
    cli()






