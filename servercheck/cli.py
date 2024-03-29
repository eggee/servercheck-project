import click
import json
import sys

@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)

def cli(filename, server):
    if not filename and not server:
        raise click.UsageError("must provide a JSON file or servers")

    #Create a set to prevent duplicate server /port combinations

    servers = set()

    #If --filename or -f option isused then attempt to read
    # the file and add all values to the 'servers' set.
    if filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("Error: Unable to open or read JSON file")
            sys.exit(1)

    # if --server -r -s option are used then add those values
    # to the set.
    if server:
        for s in server:
            servers.add(s)

    print(servers)

if __name__ == "__main__":
    cli()

