Title: Tutorial to get cmus rockin'
Category: linux
Tags: tutorial, cmus, linux
Date: 2014-12-07

`cmus` is a console based music player.  It's rather feature filled which can
mean that getting it set up "just right" might require some work.  This post is
to help you get `cmus` set up to rock!  There are a few introductory tutorials
out there, but they only scratch the surface.  My goal is to skip over the very
introductory stuff--you've probably already figured that stuff out--and tell
you _my_ opinions on how to interact with `cmus`.  I am assuming you've found
the `:add` command, you already know how to play music, and are familiar with
the different views (1-7).

Lastly, if you aren't familiar with it, you can set default keybindings and
commands to be run in a file like `~/.config/cmus/rc`:  take a look at the
FILES part of `man cmus`.


### Controlling the player ###

The three main operations you need for a music player are play/pause toggle,
next track, previous track.  The keybindings for these are `c`, `b`, and `z`,
respectively.  I can only guess that these are a pneumonic in some language
that is not English.  Especially `b` meaning _next_ is bizarre for me.
However, you _should not_ use these commands anyway.  For these operations, you
_should not_ have to browse back to your music player.  You should just hit a
keybinding wherever you are and your window manager should take care of the
rest.

To do this with `cmus`, we use the `cmus-remote` which comes with `cmus`.  For
play/pause toggle: `cmus-remote -u`.  For next track: `cmus-remote -n`.  For
previous track: `cmus-remote -r`.  Note that the previous track command
performs _correctly_ without any hacking.  If you near the beginning of the
track, go back to the previous; if you are past the beginning of the track, go
back to the start of this track.

Set up your window manager to recognize a keybinding for each of the
`cmus-remote` commands and forget about `c`, `b`, and `z`.

### The playback Modes ###

Now that we have the basics down, we need to understand the way `cmus` thinks
about your music.  There are two sources, or playback Modes: the _library_ and
the _playlist_.  This might sound backwards, but this is how you should think
of these sources: the _library_ is a dynamic subset of all of your tracks; the
_playlist_ is a fixed list of tracks (or files) to be played.  You might like
to think about _library_ or _playlist_ as the Major Mode.  The default
keybinding in `cmus` to switch between these Modes is `M`.  I'll keep using the
capital M in Mode in reference to the default keybinding.

You can read about playlists in `man cmus`.  Here's a couple quick tips:
if you already have playlists saved to files, you can add the contents of the
playlist file with the `win-add-p`.  The default key for this is `y`.  I
prefer `p` for playlist so I have

    unbind -f p common
    unbind -f p library win-add-p
    unbind -f p browser win-add-p

in my `rc` file.  If you have a single folder where all the playlists live,
you might want to add this to your `rc` file:

    cd /path/to/playlists/

This way you have access to the playlists right away in the browser (5) view.

Now, let's talk about _library_ Mode.  Library Mode has 3 minor modes.  I'm
using a lower case _m_ here since the default keybinding to switch between the
minor modes is `m`.  The minor modes are _all_, _artist_, and _album_.  Pretty
self explanatory.  If you like to listen to one artist or album at a time, then
that's all you need to know.  Just play what you want in view 1 or 2, make sure
you are in _library_ Mode, and then set the minor mode to _artist_ or _album_
as you wish.

If you like to listen to a variety of tracks, most likely with shuffle, you
will want the minor mode to be _all_.  You still might not want to listen to
literally all of your files.  Maybe you have podcasts and music in your library
and you only want to listen to music.  This is what filters are for.  You don't
want to do this with playlists because _library_ Mode can be more dynamic and
you can take advantage of the library views (1 and 2) while in _library_ Mode.
There are a few filters defined by default in the filters view (6).  You might
add some filters to filter by music or podcast.  Maybe: `:fset
music=filename="/path/to/music/*"` and `:fset
podcast=filename"/path/to/podcasts/*`.  You are probably now tempted to hit
_enter_ on the designated filter on filters view.  It doesn't do what you
want.  How you really do it is you hit _space>_.  `[*]` indicates the filter
will be applied, `[!]` indicates the filtered tracks will be _removed_ from
the library, and `[ ]` indicates the filter will not be active.  Hit _space_
until you have the right setting and then hit _enter_.  Or, for filters you
may use often, set some bindings in your `rc` file:

    bind -f common A factivate music
    bind -f common P factivate podcast

This is how I think about `cmus`.  The queue is pretty neat, too, but I find I
rarely use it.
