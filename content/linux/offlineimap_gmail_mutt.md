Title: Offlineimap, Gmail, and Mutt tutorial
Category: linux
Tags: email
Date: 2014-11-09


### History ###

A few years ago, I wrote a series of blog posts on offlineimap, mutt, and gmail
([Link Here](http://www.miggysmith.wordpress.com/gmail1)).  Since then, I spent
some time using the gmail web interface for email and then went back to mutt
and used the built in imap.  However, I've realized that neither of these are
as good as using offlineimap and mutt together, which I am back to using.  It
is totally worth the 20 minutes or so to get offlineimap and mutt set up.  This
post will show my offlineimap and mutt configurations.  I will assume you've
already installed offlineimap and mutt.

### Offlineimap ###

First, lets get offlineimap set up.  My use case will be pretty simple.  I have
a single Gmail account to which I want to connect and I only want to grab the
INBOX folder.  From this simple scenario, it should be easy to extend to
slightly more complicated scenarios.  Let's pretend that my Gmail user name is
gmail_user and the password is gmail_password. Here's a simple configuration
file (`/home/user/.offlineimaprc`), which we will explain line by line.

    [general]
    accounts = gmail_user
    ui = ttyui
    socktimeout = 30

    [Account gmail_user]
    localrepository = local-gmail_user
    remoterepository = remote-gmail_user

    [Repository local-gmail_user]
    type = Maildir
    localfolders = /home/user/mail/gmail_user

    [Repository remote-gmail_user]
    type = Gmail
    remoteuser = gmail_user@gmail.com
    remotepass = gmail_password
    sslcacertfile = /etc/ssl/certs/ca-certificates.crt
    folderfilter = lambda folder: folder in ['INBOX']

#### `[general]` ####

In this section, we have to define the accounts, which is the internal to
offlineimap name of accounts that offlineimap should be syncing.  As
described, I only have one.  If you had more, comma separate them (`accounts =
gmail_user1, gmail_user2`).  I am naming it after my Gmail user name.  The
next two lines are not necessary.  `ui` sets how fancy the output is when you
run `offlineimap` in your terminal.  `socktimeout` is the number of seconds
after which `offlineimap` should stop trying to connect if it cannot make a
connection.

#### `[Account gmail_user]` ####

Next, we need to name the mail repositories for each account.  Again, I only
have one account so I only need one `[Account ...]` section.  All we need to do
here is name the local repository (on the computer) and the remote repository
(Gmail) that hold my mail.  I've just named them `local-` and `remote-`
followed by my gmail user name.

#### `[Repository local-gmail_user]` ####

Now, I specify how my local respository is set up.  I need to tell it the type
(`Maildir`) is pretty standard and where it's located in my filesystem
(`localfolders`).  I'm pretty sure the specified folder must exist before you
run offlineimap: `mkdir -p /home/user/mail/gmail_user`.

#### `[Repository remote-gmail_user]` ####

Lastly, we specify the Gmail details.  This should be pretty obvious.
`remotepass` is your Gmail password.  `folderfilter` is what folders to sync.
As I said, I only want the INBOX.  If you also want, say your sent mail, you
might use

    folderfilter = lambda folder: folder in ['INBOX' '[Gmail]/Sent Mail']

#### Download your mail ####

At this point you should be able to download your mail.  Just run
`offlineimap` and it should start going.  If you have lots of mail, this will
take a long time.  You can refresh with `offlineimap` manually whenever you
want.  You might like to set up a cron job to do this in regular intervals.

#### Password tips ####

I have two step verification on for my google account.  If you do, too, you
might want to set up an "App password" for offlineimap.  To do this, log into
gmail, click your user in the top right corner.  Click Account.  Click
Security.  Click App passwords: Settings.  Then generate one for offlineimap.
Paste the generated code (without spaces) as your `remotepass` in offlineimap.

If you like to keep your dotfiles on github or some other publicly available
place, you might not like having your password just written out.  Some people
get fancy and integrate with keyrings and such.  I just keep my password stored
in another file (which I don't index on github) and refer to that file in my
main configuration file.  You can do that with offlineimap by utilizing its
python evaluation.  I make a file called `/home/user/.offlineimap/password.py`
and in it just a single line

    gmailpassword = "gmail_app_password"

Now, go back to your `/home/user/.offlineimaprc` and add this line to
`[general]`

    pythonfile = /home/user/.offlineimap/password.py

And change the `remotepass` line to

    remotepasseval = gmailpassword

The extra eval tells offlineimap to evaluate the value as a python expression.

### Mutt ###

Now onto configuring mutt.  I'm just going to give the basics configuration.
First, I like to keep my configuration at `/home/user/.mutt/muttrc` I also have
a `/home/user/.mutt/colors.muttrc` and some other configuration files all in
that `/home/user/.mutt/` directory.

Here's a basic muttrc configuration with comments.  Note that I will be using
mutt's built-in smtp for sending mail


    ## sending mail
    set realname = "Michael Lerch"
    set reverse_name = yes
    set from =  "gmail_user@gmail.com"
    set smtp_url = "smtp://gmail_user@smtp.gmail.com:587/"
    # file that contains the password
    source ~/.mutt/gmailpass.muttrc

    ## appearance
    # this is the best sorting algorithm
    set sort = 'threads'
    set sort_aux = 'reverse-last-date-received'

    ## receiving mail
    # needs to be consistent with offlineimap!
    set mbox_type = Maildir
    set folder = /home/user/mail/gmail_user
    # folder in which to start mutt
    set spoolfile = +/INBOX/
    # cache for even faster
    set header_cache = /home/user/mail/cache/

    ## writing mail
    # I use vim
    set editor = "vim +:silent+/^$ "

Once again, I have my password stored in a separate file that I source.  That
file contains a single line which is another App password for my google
account:

    set smtp_pass = "password"

This should get you started with offlineimap and mutt.  Have you found any
other tricks?
