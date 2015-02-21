Title: Emailing (mutt) and vim advanced config
Tags: vim, mutt, email, linux, unix
Date: 2014-12-29

Here are some tips you might like for advanced emailing with vim.  I use mutt
as my email client, but these tips should be mostly applicable to any other
email client you might use.

First, let's talk about format flowed text.  Perhaps you believe so strongly in
72 character width emails that you tend to enforce this philosophy on everyone
you email.  If you are a more reasonable person, you prefer 72 characters for
writing and in some circumstances reading, but certainly not while reading on a
phone, for example.  The solution to this is format flow text.

Essentially, any line that ends in white space is continued on the next line
and any line that ends not on white space terminates a paragraph.  Hence,
email clients that respect format flow treat any newlines preceded by a space
a soft return and any preceded by a non-space a hard return.

To use this in mutt and vim, we first have to turn on format flow in mutt so
that it puts a flag in the email header.

    # muttrc
    set text_flowed

Now, we need to make sure that vim is on board.  I now add the following to
`.vim/ftplugin/mail.vim`

    :::vim
    " ftplugin/mail.vim
    setl tw=72
    setl fo=aw

The first line sets the textwidth for the current buffer to be 72 characters.
The second line turns on formatting options 'a' and 'w'.  The 'a' option is
not necessary, but it is nice.  'w' denotes that paragraphs are terminated by
lines that end in non-white space.  'a' automatically reformats a paragraph so
if you edit the interior of paragraph, vim will automatically apply the 72
character width across the whole paragraph.  For slightly more, see
`:help fo-table`.

Great, we now have format flow text working.  We can write emails and the
reader no longer has to read jagged edge emails on their phone!  In fact, now
that the emails are no longer so ugly, we might have email conversations with
people!  But now we have a new annoyance.  In mutt (at least this is the case
without setting `edit_headers`) what I observe is that on a reply, I am given
a file to edit where the first line says "On Mon Dec, 29, Someone wrote:".
That's pretty annoying.  I'd like there to be a blank line between my new email
and that line.  Sure I can press "O" in vim and open a new line and then make
sure I hit return twice, but if I'm going to do that every time, it should be
automatic.

So I set up an `autocmd` to insert two blank lines at the top of the email if
the email already contains content.  First, let's write a function that does
this and then call it in an autocmd.  Here's the function:

    :::vim
    " add two blank lines if already content
    function IsReply()
        if line('$') > 1
            :1
            :put! =\"\n\n\"
            :1
        endif
    endfunction

What this does is checks the line number of the last line, if it is greater
than 1 (ie there already is content) it goes to the first line and pastes two
returns and then returns to the first line.

Now, we call that function in an autocmd and our ftplugin/mail.vim file now
looks like this:

    :::vim
    " ftplugin/mail.vim
    function IsReply()
        if line('$') > 1
            :1
            :put! =\"\n\n\"
            :1
        endif
    endfunction

    augroup mail_filetype
        autocmd!
        autocmd! VimEnter /tmp/mutt* :call IsReply()
    augroup END

    setl tw=72
    setl fo=aw

This is pretty nice, but how should we handle the formatting of the quoted text
from the reply?  Surely, we'd like to apply format flow to that as well.
Indeed, we can using the external program `par` which is a text formatter and
adding some spaces at the ends of lines.  If you have `par` installed, you can
add to the `IsReply()` function:

    :::vim
    function IsReply()
        if line('$') > 1
            :%!par w72q
            :%s/^.\+\ze\n\(>*$\)\@!/\0 /e
            :%s/^>*\zs\s\+$//e
            :1
            :put! =\"\n\n\"
            :1
        endif
    endfunction

These three new lines do the following.  First, they let `par` reformat the
file (make sure you have `par` installed!).  The argument w72q sets the width
to 72 and supports quotes, meaning it will not make a mess of the '>'
characters indicating quote level.

The next line `:%s/^.\+\ze\n\(>*$\)\@!/\0 /e` is a search and replace across
the whole buffer.  It searches for any lines that contains one or more
characters followed by a line that is not 0 characters or only '>' characters.
The actual matched bit is the original line.  The substitution is that same
line with a space at the end.

The next line `:%s/^>*\zs\s\+$//e` is another search and replace across the
whole buffer.  I suspect it is possible to combine these two search and
replaces, but I haven't bothered to figure it out yet.  What this one does it
looks for any lines that are the '>' followed by whitespace.  Such lines are
replaced by just the string of '>'.

Thus, blank lines are not swallowed up by flowed text!

Ah, now writing email is so much nicer.  It's not totally perfect, but it's
pretty good. Another thing we can do is start in insert mode.  Very rarely do I
not want to immediately insert text when writing an email.  Let's add that to
the augroup.  Also, before anything else, get rid of old signatures.

    :::vim
    " ftplugin/mail.vim
    function IsReply()
        if line('$') > 1
            :g/^>\s\=--\s\=$/,$ delete
            :%!par w72q
            :%s/^.\+\ze\n\(>*$\)\@!/\0 /e
            :%s/^>*\zs\s\+$//e
            :1
            :put! =\"\n\n\"
            :1
        endif
    endfunction

    augroup mail_filetype
        autocmd!
        autocmd VimEnter /tmp/mutt* :call IsReply()
        autocmd VimEnter /tmp/mutt* :exe 'startinsert'
    augroup END

    setl tw=72
    setl fo=aw


