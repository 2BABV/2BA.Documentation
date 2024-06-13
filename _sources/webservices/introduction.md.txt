# Introduction

_Text only available in english_

The 2BA Webservices are elementary, lightweight and fast services to allow your systems to integrate with the 2BA database. We offer services to search our database, retrieve product- or article details and services to, for example, download your selection profiles automatically. Our webservice is not intended for bulk downloads, it is intended to update a targeted number of articles quickly. For bulk downloads we recommend direct downloads or the use of 2BA selection profiles.

We offer our services via JSON (Rest services) and SOAP (XML service). The advantages of JSON in comparison to SOAP are, among others, reduced overhead and simplicity. For both JSON and SOAP services, most development environments either offer libraries or have the support built-in.

### Access

An application (the client) wishing to communicate with the services requires a ClientId and accompanying ClientSecret. Each application requires its own ClientId. The ClientId and secret of the application are used in conjunction with the username and password during authentication. With the ClientId name we can identfy the application or organisation who uses our webservices. Your software might already have a ClientId and secret in use, please contact your software partner..

**If you want to use Webservices you will need a clientid/secret and a 2BA username/password.**

Are you a software developer and not yet registered with 2BA? Click the button below. After you register, we can send you a letter of intent, which, when signed and received by us the ClientID and ClientSecret can be requested.

<button class="btn" name="button" onclick="https://my.2ba.nl/Registration/Start?reason=Invalid&type=Softwarebedrijf">Register with 2BA</button>

Registered 2BA clients can request a ClientId and ClientSecret for use with 2BA webservice via: [Request ClientId and ClientSecret.](mailto:helpdesk%402ba.nl?cc=ec%402ba.nl;th%402ba.nl&subject=Request%20ClientId%20and%20ClientSecret%20for%20use%20with%202BA%20web%20service.&body=Dear%20applicant%2C%20%0D%0A%0D%0AWe%20need%20a%20number%20of%20details%20to%20process%20the%20ClientId%20and%20ClientSecret%20application.%20%0D%0ACompany%20Name%3A%20%0D%0AApplicant%20Name%3A%20%0D%0AApplicant%20E-mail%3A%0D%0APhone%20number%3A%20%0D%0A%0D%0ARelationship%20type%3A%20Software%20supplier%20%2F%20Installer%20%2F%20Data%20supplier%20%2F%20Wholesale%2F%20Webshop%20%2F%20others%20*%20%0D%0A*%20strike%20out%20what%20does%20not%20apply.%20%0D%0A%0D%0AIf%20the%20application%20is%20for%20another%20company%2C%20then%20provide%20the%20company%20name%20and%20the%20contact%20person%20for%20whom%20you%20are%20making%20the%20request%20for.%0D%0A%0D%0AYours%20sincerely%20%0D%0A2BA%20support%20team%20%0D%0A)

### Security

To secure our Webservices, we use the [open standard OAuth2](https://www.2ba.nl/documentatie/webservices/oauth2). In a nutshell, this means that a previously acquired “accesstoken” is sent in an HTTP-header when invoking the service. The authentication can be built manually, but there are plenty of libraries available for this purpose.

View the code examples for authorizing and invoking the Webservices: [Example 1: Resource Owner Password Credentials Grant](https://www.2ba.nl/documentatie/webservices/oauth2/resource-owner-password-credentials-grant) and [Example 2: Authorization Code](https://www.2ba.nl/documentatie/webservices/oauth2/authorization-code)

### Structure

The structure of a service URL is: http(s)://api.2ba.nl/<major versionnumber>/<protocol>/<servicename>/<function>?<parameters>  
Example: [https://api.2ba.nl/1/json/Product/Search?query=kabelgoot](https://api.2ba.nl/1/json/Product/Search?query=kabelgoot)

### Versioning

The versioning is based on “[semantic versioning](http://semver.org/)“. This means that there will be no breaking changes within each major version number; the endpoint remains the same. For more information, see the [changelog](https://www.2ba.nl/documentatie/webservices/changelog).

### Current Service Endpoints and SOAP WSDL

|                |Production                                            |Bèta                                                           |
|----------------|------------------------------------------------------|---------------------------------------------------------------|
|json            |https://api.2ba.nl/**1**/json/{service}/{function}    |https://api._**beta**_.2ba.nl/**1**/json/{service}/{function}  |
|soap            |https://api.2ba.nl/**1**/soap/{service}?SingleWsdl    |https://api._**beta**_.2ba.nl/**1**/soap/{service}?SingleWsdl  |

The service endpoint is constructed with only the major version number in it. E.g.: [https://api.2ba.nl/**1**/json/Product/Search](https://api.2ba.nl/1/json/Product/Search)

### Example

To give you an impression of the API, we have provided a small C# code sample in which the function DetailsByGLNAndTradeItemId from the Product service is invoked via JSON.

```csharp
var postData = string.Format("?gln={0}&tradeItemId={1}", item.SupplierGLN, item.SuppliersTradeItemId);
var requestUri =  "/json/Product/DetailsByGLNAndTradeItemId" + postData;
var request = (HttpWebRequest)WebRequest.Create(Settings.Default.ApiUrl + requestUri);
 
request.Method = "GET";
request.Headers.Add("Authorization", "Bearer " + AuthorisationService.CurrentAuthorisation.AccessToken);
 
var responseStream = request.GetResponse().GetResponseStream();
var reader = new StreamReader(responseStream);
var data = reader.ReadToEnd();
 
var jobj = JObject.Parse(data);
item.ManufacturerName = (string)jobj["Manufacture"];
item.ManufacturerTradeItemId = (string)jobj["Productcode"];// ... 
```