Title: UltiSnip snippets missing from completion menu with YouCompleteMe
Tags: vim
Date: 2015-06-19

I was having a problem in neovim where my UltiSnips snippets were working, I
could expand them, however YouCompleteMe was not displaying their availability
in the pop-up completion menu.  Actually, a couple of the snippets showed up,
but not most of them.

My problem was that UltiSnips was loading with Python 3 and YouCompleteMe is
on Python 2.  To fix the problem, I simply told UltiSnips to use Python 2:

    :::vim
    let g:UltiSnipsUsePythonVersion=2

Now, YouCompleteMe populates the completion menu with _all_ the matching
snippets.
