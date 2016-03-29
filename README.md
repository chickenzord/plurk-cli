# plurk-cli
Command line tools for Plurk

Not available on Pip yet.

# Configuration

You can set these in environment variables, or by creating `.env` in the project
root.

```
PLURK_APP_KEY=
PLURK_APP_SECRET=
PLURK_TOKEN=
PLURK_TOKEN_SECRET=
```

Get yourself a key on http://www.plurk.com/PlurkApp/

# How to use

Run `plurk-cli --help` or `plurk-cli <COMMAND> --help` for more information.

Some sample commands:

```
plurk-cli whoami
plurk-cli whois akhy
plurk-cli update-profile --display-name "Chick~en~Ciel"
plurk-cli post "Hello World!"
```

# Feature plans

- Complete Plurk API support
- Redis caching
- DSL for composing several commands together
