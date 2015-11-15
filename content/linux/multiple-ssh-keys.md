Title: Multiple accounts github ssh-keys
Tags: ssh, linux, github, git, keys, ssh-keys
Date: 2015-11-14

If you have multiple github accounts and you would like to push to repositories under each of the accounts on a single computer, then you will probably need to define multiple ssh keys.

I will assume that you already have one ssh-key working.
To get our second account going, the first step is to generate a new ssh key.

```sh
> ssh-keygen -t rsa -C "email_for_github_account2@email.com"
# request for file name (I input id_rsa_work)
```

Now, you should find multiple files in `~/.ssh/`

```sh
> ls ~/.ssh
authorized_keys  id_rsa  id_rsa.pub  id_rsa_workiva  id_rsa_workiva.pub  known_hosts
```

Now, we ought to make a configuration file so that `git` knows when to use each of the keys.
The best way, that I know how, to do this is to use the different keys based on what host you are connecting to.
Here's how I set up my config file (`~/.ssh/config`)

```
# ~/.ssh/config
Host github.com
    Hostname github.com
    User git
    IdentifyFile ~/.ssh/id_rsa

Host github-work.com
    Hostname github.com
    User git
    IdentifyFile ~/.ssh/id_rsa_work
```

So now, when I try to ssh to github.com or github-work.com, a different key will be used, but each will connect to the true github.com.  You can call the Host whatever you want, I like this setup.

Now let's make sure it works.
Log into your second account on github and add the newly generated ssh key.

Add your new ssh-key to the agent

```sh
> ssh-add ~/.ssh/id_rsa_work
```

And finally, test the connection

```sh
> ssh -T github.com
# Hi personal-account! You've successfully authenticated, but GitHub does not provide shell access.
> ssh -T github-work.com
# Hi work-account! You've successfully authenticated, but GitHub does not provide shell access.
```

Beauty.  Our new ssh key works and we can select between the two by specifying a different host name.
So, in order to put this in practice, what we have to do is specify the custom host name when we define the remote.
For example do this type of thing for a personal project:

```sh
> git clone git@github.com:personal/project.git
# or
> git remote add origin git@github.com:personal/project.git
```

And this type of thing for a work project:

```sh
> git clone git@github-work.com:work/project.git
# or
> git remote add git@github-work.com:work/project.git
```

In case you are reading to fast, the difference is that we change `git@github.com...` to `git@github-work.com...` for work projects so that the correct ssh key is automatically used.






