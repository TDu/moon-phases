# Moon-phases
>  A script that scrapes from the web the next full/new moon dates.

## How it works
This is a python script that scrapes from timeanddate.com the next full/new moon dates and print them out.
I use this script with cron and redirect the ouput to a file so I can display the result with conky.

## How to set it up
Clone the repository.

Add a new line to the crontab file, the one below check every hour, which is maybe a little bit much.

    0 * * * * python {full path to script}/moonphase.py > {full path to log}/moon.log

Add this line to .conkyrc file to display the information.

    ${font Mono:size=10}${execi 3600 cat {full path to log file}/moon.log} ${font}
