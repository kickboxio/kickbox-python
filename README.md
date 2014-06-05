<p align="center">
  <img src="https://static.kickbox.io/kickbox_github.png" alt="Kickbox Email Verification Service">
  <br>
</p>

# Email Verification Library for Python

Kickbox determines if an email address is not only valid, but associated with a actual user. Uses include:

* Preventing users from creating accounts on your applications using fake, misspelled, or throw-away email addresses.
* Reducing bounces by removing old, invalid, and low quality email addresses from your mailing lists.
* Saving money and projecting your reputation by only sending to real email users.

## Getting Started

To begin, hop over to [kickbox.io](http://kickbox.io) and create a free account. Once you've signed up and logged in, click on **API Settings** and then click **Add API Key**. Take note of the generated API Key - you'll need it to setup the client as explained below.

## Installation

Make sure you have [pip](https://pypi.python.org/pypi/pip) installed

```bash
$ pip install kickbox
```

#### Versions

Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Usage

```python
import kickbox

# Then we instantiate a client (as shown below)
```

### Build a client

__Using this api without authentication gives an error__

##### Authorization header token

```python
client = kickbox.Client('1a2b3', client_options)
```

### Client Options

The following options are available while instantiating a client:

 * __base__: Base url for the api
 * __api_version__: Default version of the api (to be used in url)
 * __user_agent__: Default user-agent for all requests
 * __headers__: Default headers for all requests
 * __request_type__: Default format of the request body

### Response information

__All the callbacks provided to an api call will recieve the response as shown below__

```python
response = client.klass('args').method('args', method_options)

response.code
# >>> 200

response.headers
# >>> {'x-server': 'apache'}
```

##### JSON response

When the response sent by server is __json__, it is decoded into a dict

```python
response.body
# >>> {'user': 'pksunkara'}
```

### Method Options

The following options are available while calling a method of an api:

 * __api_version__: Version of the api (to be used in url)
 * __headers__: Headers for the request
 * __query__: Query parameters for the url
 * __body__: Body of the request
 * __request_type__: Format of the request body

### Request body information

Set __request_type__ in options to modify the body accordingly

##### RAW request

When the value is set to __raw__, don't modify the body at all.

```python
body = 'username=pksunkara'
# >>> 'username=pksunkara'
```

###  api



```python
kickbox = client.kickbox()
```

#####  (GET /verify?email=:email)

Email Verification

The following arguments are required:

 * __email__: Email address to verify

```python
response = kickbox.verify("test@example.com", options)
```

## Contributors
Here is a list of [Contributors](https://github.com/kickbox/kickbox-python/contributors)

### TODO

## License
MIT

## Bug Reports
Report [here](https://github.com/kickbox/kickbox-python/issues).

## Contact
Chaitanya Surapaneni (chaitanya.surapaneni@kickbox.io)
