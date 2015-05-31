Title: Setting up vim for Rcpp
Tags: vim, R, Rcpp
Date: 2015-03-28
Status: Draft


Motivation
==========

My motivation for writing this post is so to have a reference for myself about
how I set up vim for Rcpp.  If anyone else finds this useful, that's just
bonus!  Though the fine details are Rcpp related it should be applicable for
general .cpp stuff.

Plug-ins
========

The three vim plug-ins that I'll need are:

1. [neomake](http://github.com/benekastah/neomake), to check for syntax
   errors.  Note that this is a neovim plug-in.
2. [YouCompleteMe](http://github.com/Valloric/YouCompleteMe), which provides
   intelligent auto-completion, and
3. [TagHighlight](http://github.com/abudden/taghighlight-automirror), which
   provides intelligent syntax highlighting.

YouCompleteMe
=============



