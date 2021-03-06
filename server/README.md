# Connecting to Digital Ocean and starting the server
```
ssh root@{{IPAddress}}
cd server
nodejs server.js
```

# API documentation
All calls are prefixed with `/api/v1/`.

## RPI calls
```
GET /checkuser/:stationid

Output:
200 With "" if no user is logged in or {userID} if one is logged in
404 No stationID found
500 Internal server error
```


Push a video for a user that is logged in to a station:
```
POST /video

Input:
userID;
stationID;
timestamp;
random;
signature;

Output:
200 Added a video
404 User with userID not found
500 Internal server error
```


## Frontend calls
NOTE: Input must NOT be provided as JSON, but as x-www-form-urlencoded. 

```
POST /user/register

Input:
username
password
email
firstname
lastname

Output:
200 If a user was created
403 If a user was NOT created (see node server console output)
```



```
POST /user/login

Input:
username
password

Output:
200 If logged in
403 If not logged in (see node server console output)
```

```
GET /user/sessions [requires login]

Output:
200 With array of session of videos
403 If not logged in
500 Internal server error
```


```
POST /user/startSession/:stationID [requires login]

Output: 
200 OK
404 No stationID found
500 Internal server error
```

```
POST /user/endSession/:stationID [requires login]

Output: 
200 OK
404 No stationID found
500 Internal server error
```

```
DELETE /user/session/:sessionID [requires login]

Output: 
200 OK
404 No sessionID found
500 Internal server error
```


```
POST /user/videos/:videoID [requires login]

Output: 
200 OK
404 No videoID found
500 Internal server error
```