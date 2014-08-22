Title: vim different format in different regions
Tags: vim
Status: Draft

vim allows you to have different syntax highlighting in different regions (see
[http://vim.wikia.com/wiki/Different_syntax_highlighting_within_regions_of_a_file]
for example.

What I would like to do is to have different format options, in particular,
different wrap line settings in different regions.  My specific file type is R
Markdown (Rmd) files.  For prose, I like to have automatic linewrap (fo+=t)
and in code, I don't (though I do like to see the 80th column).  In an Rmd
file, there are code regions and prose regions.  Using the above link, we can
highlight R in the code chunk and Markdown in the prose chunk but it would be
awesome if we could change format options in the different regions.

I don't have a perfect way of doing it, but I do have a way of doing it pretty
well.  My strategy will be to check, every time I enter insert mode, whether I
am in a code region or a prose region.  Depending on which region I am in, I
will set linewrap or turn it off.  Here's how I do it in vimscript.

First, I need to define a function to check whether I am in a code or prose
region.  For Rmd, a code region begins with 

    ```{r ...

(possibly with preceding whitespace) and ends with

    ```

(also possibly with preceding whitespace).  I will check for the most recent
previous code region beginning and the most recent previous code region ending.
If the most recent beginning occurred more closely to the current line than the
most recent ending (or if there is no ending) that means I am in a code chunk
and I should turn off my line wrap.  Otherwise, I should turn it off.  Here's a
function to do that:

    :::vim
    function InCodeRegion()
        let codestart = search("^[ \t]*```[ ]*r", "bncW")
        let codeend = search("^[ \t]*```$", "bncW")
        if codestart > codeend
            set fo-=t
        else
            set fo+=t
        endif
    endfunction

Now, I just need to call this function whenever I enter insert mode.

    :::vim
    autocmd InsertEnter * call InCodeRegion

I put these in my file `.vim/after/ftplugin/rmd.vim`.

This works pretty well, but it does not turn on automatically as I write the
code region opener.  That is, as I go from prose to code by typing

    :::vim
    ```{r}

I do not automatically change my format options.  Can you improve this?

