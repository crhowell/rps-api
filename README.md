# My RPS API Specification
Chris's Rock, Paper, Scissors backend REST API hosted on Heroku. 

The purpose of this project was to give students both a running app to explore and a public repo to associate what the code is doing.

Feel free to play games via Postman or maybe link up your own React app to talk to it.

The backend API determines winners all you have to do is create user / login/ and play moves (rounds).

## Throttling Limits
Try not to spam the API because there is a throttler in-place. 
If you exceed the limit you will start receiving a status code of 429 "Too Many Requests". 

Anonymous API Users (unauthenticated) -- `100` requests per `hour`.

Registered API Users (authenticated) -- `1000` requests per `hour`.

These might be a bit restrictive, though its a Free tier Heroku app. Sorry not sorry! :)

> NOTE: You must attach your JWT token for all **Protected Routes** otherwise you are considered an Anonymous User and most routes will 401 since they are all protected. 

## API Endpoints
The API endpoints are described below in the following format.

Method: `<HTTP Method>`

Endpoint: `<Endpoint/URI>`

Body:  `{key:val}, [val1,val2] or NULL (NULL meaning leave it empty)` 

> (what you need to attach to body of request)

Response to expect:
```
{
  key: val
}
```

If your token expires you will get this response with a `401` status code.

```
{
    "detail": "Signature has expired."
}
```

### User Endpoints

**Register a User**  

Method: **POST** (PUBLIC ROUTE)

Endpoint: `https://chrisrh-rps-api.herokuapp.com/api/user`

Body: `{"username": "YOUR USERNAME", "password": "YOUR PASSWORD"}` 

> Probably should of made a `confirm_password` field

Response:
```
{
  "username":"YOUR USERNAME",
  "token":"JWT_TOKEN"
}
```

> NOTE: This looks very similar to the login endpoint below. Except this is for initial register.
> From now on you **use the Login endpoint** to retrieve your JWT token when it expires.

**Retrieve your JWT Token (Login)** - save it somewhere (expires in an hour)

Method: **POST** (PUBLIC ROUTE)

Endpoint: `https://chrisrh-rps-api.herokuapp.com/api/user/token`

Body: `{"username": "yourusername", "password": "passwordhere"}`

Response:

```
{
  "token":"YOUR_JWT_TOKEN",
  "user":{"username":"YOUR USERNAME "}
}
```

===

#### Protected Routes (Auth required)
Remember, you have to attach `Authorization` to Request Header with valid JWT Token or you will get a 401.

JWT Tokens expire after 1 hour, so you will have to refresh it when that happens.

**See your User Game Stats**

Method: **GET** (PROTECTED ROUTE)

Endpoint: `https://chrisrh-rps-api.herokuapp.com/api/user/profile`

Headers: `{Authorization: "JWT <JWT_TOKEN>"}`

Body: NULL

Response:
```
{
  "total_wins": 0,
  "total_losses": 0,
  "total_ties": 0,
  "username": "YOUR USERNAME"
}
```

### Game Round Endpoints

**Overall Game Stats**
Method: **GET** (PROTECTED ROUTE)

Endpoint: `https://chrisrh-rps-api.herokuapp.com/api/games`

Headers: `{Authorization: "JWT <JWT_TOKEN>"}`

Body: NULL

```
{
  "games_played": 0,
  "unique_players": 0,
  "human_wins": 0,
  "human_losses": 0,
  "bot_wins": 0,
  "bot_losses": 0,
  "ties": 0,
  "humans_played_rock": 0,
  "humans_played_paper": 0,
  "humans_played_scissors": 0
}
```

**Play New Game/Round of Rock, Paper, Scissors**

You will play against a Random Bot.

Method: **POST** (PROTECTED ROUTE)

Endpoint: `https://chrisrh-rps-api.herokuapp.com/api/games`

Headers: `{Authorization: "JWT <JWT_TOKEN>"}`

Body: `{"player_choice": "P"}`

> NOTE: `"R"` (Rock), `"P"` (Paper), `"S"` (Scissors)

Response:
```
<= {
    "player_choice": "<your choice>",
    "creator": <player ID>,
    "bot": <bot ID>,
    "bot_choice": "<bot choice here>",
    "player_has_won": <bool or null> 
}
```
> NOTE: `player_has_one` has 3 states:
> `true` (win), `false` (loss), `null` (tie)


## Future Goals
I think that is all for now. I threw this together very quickly in an evening night. Eventually can add some additional calculations/endpoints for more stats/metrics of all the games being played. And maybe introduce a slightly smarter bot to play against.
