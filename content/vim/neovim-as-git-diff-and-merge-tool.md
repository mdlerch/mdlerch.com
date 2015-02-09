Title: neovim as git diff and merge tool
Tags: vim neovim
Date: 2015-02-08

You've made the switch.  You are now using neovim for all your text editing,
and you've hardly even noticed that you aren't using regular old vim.  Except
one thing.  Your git difftool and mergetool aren't quite right.  One of two
things is happening.  Either you are using old vim (which is fine, but you
want to switch _completely_ to neovim) or things are breaking because you have
gone so far as to not just install neovim but to also remove vim!

So why is this happening?  Your git mergetool is still set to vim even
though you set your core.editor to nvim.  So, we just tell git to use `nvim`
for your mergetool.

First, you probably have or want something like this:

    git config --global merge.tool vimdiff

That `vimdiff` in there is _not_ the `vimdiff` executable.  It refers to a
built-in script.  There's also `vimdiff2` and `vimdiff3`.  (3 is the best by
the way.)  Those built-in scripts call the `merge_tool_path` executable.  Which
will be set to `vim` by default.  You can change that with

    git config --global mergetool.path nvim

All done.  The difftool uses the mergetool by default so that's all you need
to set!
