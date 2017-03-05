# date-robot-twitter-bot
> Very simple twitter bot that tweets about the current date.


## Requirements

- python
- tweepy


## Crontab setup:

### Open the crontab

```sh
crontab -e
```

### Add line

```sh
0 17 * * * cd {{path to bot}} && python bot.py
```
