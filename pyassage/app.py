import click
import logging
import sys

from .client import CloudPassageAPI


@click.group()
@click.option('--client-key',
              envvar='CPAPI_CLIENT_KEY',
              help='The client key for the API')
@click.option('--client-secret',
              envvar='CPAPI_CLIENT_SECRET',
              help='The client secret for the API')
@click.option('-v', '--verbose',
              count=True,
              help='Raise logging level to DEBUG')
@click.version_option()
@click.pass_context
def cli(ctx, client_key, client_secret, verbose):

    if verbose > 0:
        log = logging.getLogger("pyassage")
        log.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        log.addHandler(ch)
        log.debug("Verbose mode ON.")

        if verbose > 1:
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
            requests_log.addHandler(ch)
            requests_log.debug("Requests logging turned ON.")

    ctx.obj = CloudPassageAPI(client_key, client_secret)


@cli.command()
@click.pass_obj
def announcements(api):
    announcements = api.get_system_announcements()
    for a in announcements:
        click.echo(a.announcement)
