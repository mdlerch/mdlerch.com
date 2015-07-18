Title: turn off cli alias
Tags: linux, alias, cli
Date: 2015-07-18

tl;dr: `\cmd`

There may be a situation where you have masked a command with a shell alias.
For example, you may always run a command with certain flags so you might do
something like

    ::sh
    $ alias ls='ls --color'

If, for whatever reason, you'd like to run the default `ls` (or any command
masked by an alias), just prepend with `\`: `\ls`
