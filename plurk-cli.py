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

@cli.command()
@click.option('--display-name', '-d', default = None)
@click.option('--full-name', '-f', default = None)
@click.pass_context
def update(ctx, display_name = None, full_name = None):
  data = dict()
  if display_name:
    data['display_name'] = display_name
  if full_name:
    data['full_name'] = full_name

  try:
    response = plurk.callAPI('/APP/Users/update', data)
    result = {
      'display_name': response['user']['display_name'],
      'full_name': response['user']['full_name']
    }
    output = response['error_text'] if 'error_text' in response else json.dumps(result, indent = 2)
  except Exception as e:
    output = str(e)

  click.echo(output)

if __name__ == '__main__':
  cli()
