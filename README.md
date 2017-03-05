# date-robot-twitter-bot
> Very simple twitter bot that tweets about the current date.


## Requirements

- python
- tweepy


## Install requirements:

```sh
pip install tweepy
```


## Config setup:

### Create a config file

```sh
touch config.py
```

### Add the twitter "consumer" and "access" codes

```sh
consumer_key = '{{your consumer key}}'
consumer_secret = '{{your consumer secret}}'
access_key = '{{your access key}}'
access_secret = '{{your access secret}}'
```


## Crontab setup:

### Open the crontab

```sh
crontab -e
```

### Add line

```sh
0 17 * * * cd {{path to bot}} && python bot.py
```
