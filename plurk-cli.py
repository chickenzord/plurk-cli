#!/usr/bin/env python

import click
import json
import plurkenv

plurk = plurkenv.init()

@click.group()
def cli():
  pass

@cli.command()
@click.option('--key', default = None)
def whoami(key):
  response = plurk.callAPI('/APP/Profile/getOwnProfile')
  user_info = response['user_info']
  display_name = user_info['display_name']

  data = user_info[key] if key else json.dumps(user_info, indent = 2)
  click.echo(data)

@cli.command()
@click.argument('user_id')
@click.option('--key', default = None)
def whois(user_id, key):
  response = plurk.callAPI('/APP/Profile/getPublicProfile', { 'user_id': user_id})
  user_info = response['user_info']
  display_name = user_info['display_name']

  data = user_info[key] if key else json.dumps(user_info, indent = 2)
  click.echo(data)

if __name__ == '__main__':
  cli()
