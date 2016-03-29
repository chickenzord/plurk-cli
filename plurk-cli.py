#!/usr/bin/env python

import click
import plurkapi

def _out(ctx, obj):
  if isinstance(obj, dict):
    for k, v in obj.iteritems():
      click.echo("%s=\"%s\"" % (k, v))
  elif isinstance(obj, Exception):
    ctx.fail(str(obj))
  else:
    click.echo(obj)

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
@click.pass_context
def whois(ctx, user_id, key, list_keys):
  try:
    user = plurkapi.whois(user_id)
    if list_keys:
      for key in user.keys():
        _out(ctx, key)
    elif key is not None:
      if key in user:
        _out(ctx, user[key])
      else:
        _out(ctx, 'Key not found: %s' % key)
    else:
      _out(ctx, user)
  except Exception as e:
    _out(ctx, e)

@cli.command('update-profile')
@click.option('--display-name', '-d', default = None)
@click.option('--full-name', '-f', default = None)
@click.pass_context
def update_profile(ctx, display_name, full_name):
  try:
    if display_name is None and full_name is None:
      _out(ctx, Exception('You must specify either --display-name or --full-name'))
    else:
      user = plurkapi.update_profile(display_name, full_name)
      _out(ctx, user)
  except Exception as e:
    _out(ctx, e)

if __name__ == '__main__':
  cli()
