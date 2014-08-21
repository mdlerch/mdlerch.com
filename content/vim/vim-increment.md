Title: Increment or decrement visual selection in vim
Tags: vim
Status: Draft

vim can increment and decrement digits under the cursor with the `<C-A>`
`<C-X>` bindings, respectively.  Go try it out and then come back.

Now that you are back, let's extend this functionality to visual
selections.  First let's learn a command you can find in `:help submatch`.

    :::vim
    :s/\d+/\=submatch(0)+1/

This is a type of substitution called sub-replace-expression.  A normal
substitution looks like `:s/{pattern}/{string}/` and replaces `{pattern}`
with `{string}`.  Here we have the `\=` changes the `{string}` part to an
expression to be evaluated.  Our pattern in this case is `\d+`.  The `\d`
matches a digit and the `+` says to match one or more digit so something like
`555` is matched once and not 3 times.

So what our sub-replace-expression is going to do is find a number and then
substitute it with the evaluation of `submatch(0)+1`.  `submatch(0)` simply
returns the matched text (ie the `\d+`).  The `+1` adds one to it!

Of course, this only operates on the first occurrence of `\d+` in the current
line.  We can make this operate on every `\d+` on a line with the `g` flag for
`:s`

    :::vim
    :s/\d+/\=submatch(0)+1/g

Go ahead and give that a try.

It feels like we are close now.  This won't work quite right, but at this
point you might be tempted to add this mapping to your vimrc

    :::vim
    vnoremap <C-a> :s/\d+/\=submatch(0)+1/g

What we _want_ this to do is to increment all numbers in a visual selection.
It does do that, but it does something else as well.  Can you figure out
what's going wrong?

The problem is that the way substitute works on visual selections (ie
`:'<,'>s` is to operate on the whole line that contains the visual selection
so if you select only some of the numbers on a line, the numbers on the line
that are not selected will also be incremented.  We can fix this by adding
something to the `{pattern}`.  We want to match not just digits but digits
that are in the visual selection.  We can do that with `\%V`

    :::vim
    vnoremap <C-a> :s/\%V\d+/\=submatch(0)+1/g

Now we are getting pretty close.  There's one problem here depending on the
exact behavior that you want.  What about negative values?  Do you want -6 to
increment to -5 or to increment to -7?  Personally, I want it to increment to
-5.  If you do, too, we have to add even more to our `{pattern}` to include
negative signs along with our digit.  What we need to do is add, in front of
the `\d+` either 0 or 1 `-`'s.  To say 0 or 1, we use `\=` in our pattern.  In
the pattern, `\=` means 0 or 1.  In the replacement string, `\=` means
evaluate an expression.

So here's our final mapping:

    :::vim
    vnoremap <C-a> :s/\%V-\=\d+/\=submatch(0)+1/g

To decrement, just subtract 1 instead of adding.  How's this mapping working
for you?
