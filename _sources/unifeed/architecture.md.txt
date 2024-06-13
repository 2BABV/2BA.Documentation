# 2BA DaaS Reference Architecture

Text only available in engish

### Data as a Service

The 2BA DaaS reference architecture offers a **consistent**, **fast** and **safe** way to communicate with the 2BA database and is, where possible, based on **(open) standards**. For most components in this architecture 2BA has defined its own implementation, but because of the (open) standards, it is possible for some components to be defined by third parties.

This architecture also offers the ability for the customer to transparently connect multiple service providers.

Below is a short description of the individual components.

### Webservices

Webservices are the basis for the Data as a Service architecture. The [2BA Webservices](https://www.2ba.nl/documentatie/webservices) offer elementary, fast and lightweight services to access the product- and article data from the 2BA. The services support both JSON and SOAP. You can easily integrate your system with these webservices so as to always have the latest data available.

### Catalogue

A catalogue offers the same data as the webservices, but provides them in a User Interface. 2BA’s catalogue implementation is [Unifeed](https://unifeed.2ba.nl/). You can find the complete Unifeed documentation [here](https://www.2ba.nl/documentatie/unifeed). Using Unifeed, the end-user can directly search and query the 2BA database. It is also possible to compose selection lists. Unifeed offers several interfaces (OCI, JSON) to easily pull singular data or selection lists to the customer’s business software.

### OpenID

OpenID is an open standard for the authentication of users. 2BA customers can log into all 2BA applications with the same 2BA credentials (username/password). The possibilities of OpenID, however, extend much further. Third parties could also use 2BA OpenID to authenticate their application. The advantage for the user is that he/she does not have to remember his/her credentials for each application/website. It would also be possible for 2BA to support other trusted OpenID providers. This could, in theory, enable you to log into 2BA using, for example, your Google account.

### OAuth 2.0

OAuth is a widely accepted internet standard for authorization. In short, this means that you authorize an application once to use your credentials to retrieve data from 2BA. You enter your credentials (username/password) at 2BA one time and authorize the application. In response, the application receives a “Token”. The application will then use this token in all future requests to 2BA. The “Token” is used by 2BA to identify the application and user that requested the data.  
Using this method, a form of **Single-Sign-On** can be achieved. The user can at all times revoke the authorization, invalidating the “Token” in the process.

### ERP or Calculation application

Eventually, the 2BA data needs to be used somewhere. Chances are that this happens in an ERP or Calculation application. These applications can choose whether to use the 2BA REST Services or Unifeed to retrieve the data. 2BA itself does not produce ERP or Calculation applications. We do have a demo application available to demonstrate the functionality with both interface methods. You can download the [2BA DemoCalc](https://www.2ba.nl/documentatie/unifeed/democalc) application.

### Supplier Conditions

The majority of the prices in 2BA’s systems tend to be gross prices. It is also possible for customers to have obtained supplier conditions (surcharges). These conditions vary per customer and have to be stored and retrieved separately. To this end, we developed the 2BA Condition Service. The 2BA Condition Services can run either locally at the customer’s location, or centralized at 2BA. Unifeed seamlessly integrates with the 2BA Condition Service, enabling Unifeed to display and adopt the net prices.
