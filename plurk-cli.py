#!/usr/bin/env python

import click
import json
import plurkenv

plurk = plurkenv.init()

@click.group()
def cli():
  pass

@cli.command()
@click.option('--key', '-k', default = None)
@click.option('--list-keys', '-l', is_flag = True)
@click.pass_context
def whoami(ctx, key, list_keys):
  ctx.forward(whois, user_id = None)

@cli.command()
@click.argument('user_id', default = None)
@click.option('--key', '-k', default = None)
@click.option('--list-keys', '-l', is_flag = True)
def whois(user_id, key, list_keys):
  if user_id:
    response = plurk.callAPI('/APP/Profile/getPublicProfile', { 'user_id': user_id})
  else:
    response = plurk.callAPI('/APP/Profile/getOwnProfile')
  user_info = response['user_info']

  if list_keys:
    for key in user_info.keys():
      click.echo(key)
  else:
    data = user_info[key] if key else json.dumps(user_info, indent = 2)
    click.echo(data)

if __name__ == '__main__':
  cli()
