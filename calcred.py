import click
import netaddress

@click.group()
def cli():
    pass

@cli.command()
@click.argument('net')
def net(net): #Declaración de comando
    "NET value 0.0.0.0/0"
    netaddress.calculared(net)

cli()