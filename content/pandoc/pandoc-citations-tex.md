Title: Tutorial for pandoc citations: markdown to latex
Tags: pandoc, bibtex, natbib, tutorial, example
Date: 2014-08-31

I am trying to move _all_ of my writing over to markdown, and then using
pandoc to produce the true target format.  Often that is latex, and often
there are citations involved.  This post will be an example (or two) of
dealing with citations in markdown so that pandoc can handle things
appropriately.

I use mendeley to organize my academic papers and it happily produces .bib
files for different collections.  So, my assumption is that you already have
your references specified in a .bib file.  You should also have pandoc and a
latex installation.  You should also install `pandoc-citeproc` which is
separate from pandoc.  If you have pandoc through RStudio, it probably also
came with pandoc-citeproc.  Otherwise, you should be able to install it the
same way that you installed pandoc (perhaps `cabal install --global
pandoc-citeproc`).  As you'll see in this post, pandoc-citeproc is not
strictly necessary.

I'll talk about two scenarios for generating latex output.  The first is you
go straight from markdown to a pdf with no intermediate steps.  The pandoc
latex default template (or your own latex pandoc template) is good enough.
The second scenario will be that we want to generate a .tex file from our
markdown and then possibly tweak the .tex file and finally compile it to pdf.

For the first scenario, we want to take `input.md` convert it to `output.pdf`
while linking in `ref.bib`.  Here's the pandoc call to do that

    :::shell
    pandoc input.md -t latex --filter pandoc-citeproc --bibliography=ref.bib -o output.pdf

The `--bibliography` flag is not necessary, we could specify this in the YAML
at the top of the markdown file:

    :::markdown
    ---
    title: My Title
    author: ME!
    bibliography: ref.bib
    ---

You might also add in some flags like `-S` to make sure quotes and such are
handled intelligently.  To cite a reference in `ref.bib` that has a reference
key of RefKey, just type `[@RefKey]` in your markdown source.  If you don't
want parentheses around the citation, drop the square brackets `@RefKey`, if
you don't want to say something like "Heinz and Huntz say blah (Heinz and
Huntz, 1992)" and would rather get "Heinz and Huntz say blah (1992)" do this:
`[-@RefKey]`.

If you have cls file, you can give pandoc the flag `--csl=FILE`.  I don't know
much about this, I'm used to .bst files for natbib.

You might be thinking that if you wanted to go .tex instead .pdf, you would
just change the output to `-o output.tex`.  However, this is probably not what
you want.  The `pandoc-citeproc` is going through and evaluating all of your
citations, so you won't see, in your .tex file, things like
"\citep{HeinzHuntz1992}".  Instead, the citation will be expanded to it's
actual text.  To get the "raw" latex source, you should not use
`pandoc-citeproc`.  Instead, we'll let latex use natbib/bibtex to actually
expand the citations.  To generate the .tex, run a line like this:

    :::shell
    pandoc input.md -t latex -s -S --natbib --bibliography=ref.bib -o output.tex

I have found that I must specify the `--bibliography` flag even if it is
stated in the YAML of the markdown source.  Now, you can go into the .tex
file, tweak things, set the bibliography style to your .bst, etc.  Citation is
done the same way as above (using the `@` sign) which is translated to the
latex `\cite` family as appropriate.

Do you have any additional tricks for dealing with pandoc, markdown, latex and
citations


