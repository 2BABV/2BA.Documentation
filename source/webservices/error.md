# Error codes

### HTTP Status Codes

The Webservices use HTTP status codes to inform the client application about the response.

|Code            |Text                  |Description                                                                                            |
|----------------|----------------------|-------------------------------------------------------------------------------------------------------|
|200             |OK                    |Successful response.                                                                                   |
|400             |BadRequest            |The request was invalid. The accompanying message can explain why.                                     |
|401             |Unauthorized          |The user is not authorized for this service. The accompanying message can explain why or what service. |
|500             |InternalServerError   |	An unexpected error has occurred. Contact us with the error number from the message.                |   

### Error message

In addition to the http status code, a message containing extra information is sent to the application. This message consists of the fields IsError (boolean), ErrorMessage (string) and Status (string). The Error Message contains information that may help troubleshoot the issue. The Status field contains a textual representation of the http status code.

Example:

```csharp
{
    "IsError": true
    "ErrorMessage": "Incorrect format for featureFilter: {\"EF001360\":\"EV000278\" fzljk dfjf l;j a }",
    "Status": "BadRequest"`
}
```


### JSON

It is not possible to filter the response based on HTTP status codes if jsonp was used to invoke the services. In this case, you can make use of the returned data object.

Example:

```js
callback(
	{
		"IsError":true,
		"ErrorMessage":"Incorrect format for featureFilter:{\"EF003356\":\"EV005821",
		"Status":"BadRequest"
	},
	400
);
```

```js
function callback(data) {
	if (data.IsError) {
		alert(data.Status + ': ' + data.ErrorMessage);
	} else {
		// Do something with data
	}
}
```