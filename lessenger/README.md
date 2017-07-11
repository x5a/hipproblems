# Hipmunk Lessenger Coding Challenge

Hello Hipmunk is built on a chatbot engine that handles conversational interactions. It manages the complexity of natural langage and controls the lifecycle of a user's interaction with the chatbot

Your challenge is to build a chatbot engine on the Hipmunk Lessenger messaging platform that implements several features described below. Keep it simple - you don't necessarily need to use any sopisticated NLP or NLU solutions to solve this problem. Feel free to take liberties with the responses - it's not a requirement to exactly match our example responses.

You can reach the Hipmunk Lessenger UI here: [Lessenger UI](https://www.hipmunk.com/jobs/hello/lessenger)

Documentation for the Hipmunk Lessenger Platform can be found here: [API Docs](api.md)

# Welcome Message

When the user joins a chat with your bot, you should respond with a personalized greeting. Example:
```
Hello, John!
```

# Weather

Your users are fascinated by the weather. Build a weather reporting capability.

## Requirements

Your chatbot engine should be able to handle the following cases:

Note: `<Location>` can be any city or reference to a city such as `SF` or `San Francisco`, or `94100`.

### Current Weather:

If the user enters one of:
* `what's the weather in <Location>`
* `weather in <Location>`
* `<Location> weather`

Respond with the current weather. Example:
```
Currently it's 48F. Rain
```

### Weather Tomorrow:
If the user enters one of:

* `What's the weather tomorrow in <Location>`
* `weather tomorrow in <Location>`
* `<Location> weather tomorrow`

Respond with a forecast for tomorrow. Example:
```
Tomorrow there will be a high of 52F and a low of 38F. Rain throughout the day.
```


### Error cases:
If the entered location is invalid such as `asdf`, you should tell the user that you didn't understand the location. Example:
```I don't know where ASDF is.```

If the user entered something that doesn't fit into the above categories, let them know that you didn't understand them. Example:
```I don't understand you.```

## Data APIs
You should use the following APIs to help you build your chatbot. You should have recieved an API key from hipmunk for each of these services.

* The DarkSky Forecast API https://darksky.net/dev/docs/forecast accepts a coordinate point and provides current weather and a forecast.
* The Google Gecoding API https://developers.google.com/maps/documentation/geocoding/start will help you convert arbitrary strings that describe to coordinate points. (hint: the query param `address` doesn't need to be a fully formed address).

# Deliverables
A zip file or GitHub link with your project. We should be A README with instructions to build and run your chatbot engine. If you choose to use a zip file, please use revision control and send the entire repository (we want to be able to see your revision history).

If you want to use outside sources for parts of your submission, please clearly cite them.

# Bonus
## Chit-chat
Your users really want to be able to talk with a bot. Handle the following cases:

### Greetings
If the user enters one of:

* `Hi`
* `Hello`
* `Aloha`

Respond with a greeting. Example:
```
Hey! I'm a weather bot.
```

### Help
If the user enters one of:

* `help`
* `halp`
* `I'm stuck`

Respond with an explaination of your features. Example:
```
Ask me "What's the weather in SF"
```

## Search
TBD. Use TF-IDF to build a search capability.
