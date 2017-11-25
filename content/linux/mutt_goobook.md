Title: Fixing mutt and goobook
Category: linux
Tags: mutt
Date: 2015-01-27

There are a lot of blog posts out there that show how to combine mutt and
goobook.  However, all of them that I have seen are wrong.  This isn't a long,
post, I'm not going to tell you _about_ goobook and mutt, I'm just going to
tell you the problem and the _correct_ usage.  I imagine this also goes for
other query commands besides goobook.

First the problem.  If you query a single word, things work fine.  If you
query two words, say a first and last name, goobook breaks.  For example, if
you type "joe smith" and then hit tab (or however you query) the display gets
messed up and goobook says "unrecognized argument: smith".  So, you change
your query to just "joe" and then you have to manually wade through all of
the "joe"'s in you contact list.

This is because you probably have this line in your mutt config:

    set query_command="goobook query '%s'"

Don't feel bad, that line is in lots of blog posts.

This is what you should have:

    set query_command="goobook query %s"

That is, no quotes around the `%s`.  Mutt adds them automatically (see `man
muttrc`).

Finally, you can type a first _and_ last name to query!

