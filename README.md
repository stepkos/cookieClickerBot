# cookieClickerBot
It's a bot to play in cookie clicker (https://orteil.dashnet.org/cookieclicker/)

## How to run?
### You can use finished build!
```
build/
```

### Or take a look on my code!
* Install Python
* Install Selenium
* Download driver (recomended "chromedriver")

* Fill the data in config
```
config.json
```

```json
{
    "DRIVER_PATH": "<path to driver>",
    "SAVE_PATH": "<path to save file>",
    "clickBeforeSave": 1000,
    "seriesBeforeBuy": 30
}
```

* Run
```
cookieClickerBot.py
```

## Functionalities
* Clicking at cookie 50 times per second!
* Automaticly Buy Upgrades!
* Automaticly Buy Buildings!
* Automaticly Export Save!
* Automaticly Import Save when you run bot!
* Print messeges what is happend!
* JSON config to adjust parameters!

## License
All rights reserved
