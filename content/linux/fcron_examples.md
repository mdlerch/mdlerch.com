Title: Fcron examples for every 30 minutes and once a week
Tags: fcron, cron
Date: 2014-11-10

This is mostly a note for myself, but maybe other people will also find it
useful.

There are two types of jobs I'm going to talk about here.  They are jobs to be
run at regular **intervals** and jobs to be run **periodically**.  Regular
intervals means every x unit of time.  Maybe every 4 days.  Maybe every half
hour.  Periodic means once a week or once a day.

### Intervals ###

Let's say you download your email with the command `do_email` and you want to
do this every 30 minutes.  Fire up `fcrontab -e` and put in this entry:

    :::bash
    @ 30 do_email

The @ sign says this is an interval based command and 30 is the time interval
in minutes.  You can specify more precisely by using multipliers of m, w, d,
h, and s for months, weeks, days, hours, and seconds, respectively.  For
example

    :::bash
    @ 2h05 do_email

will download your email every 2 hours and 5 minutes.

### Periodic ###

Let's say that you want a command to be run in some regular interval.  Maybe
you want to download podcasts once a week.  If you use the command
`get_podcasts` to download your podcasts you could use this entry:

    :::bash
    %weekly  * 9-17 get_podcasts

This will run the command get_podcasts once a week at any minute and sometime
between 9am and 5pm.  A "week" starts on Monday and goes to Sunday so fcron
will try to do this Monday between 9 and 5.  If your computer is on, it will
try again on Tuesday.

Lot's more good stuff at [http://fcron.free.fr/doc/en/fcrontab.5.html]
