# helga-newrelic

NewRelic webhooks and commands for [helga](https://github.com/shaunduncan/helga).

## Settings

- ``NEWRELIC_API_KEY``: The api key for a particular account
- ``NEWRELIC_ACCOUNT_ID``: The numeric account id for the api key
- ``NEWRELIC_WEBHOOK_ANNOUNCE_CHANNEL``: IRC channel where received webhooks will be announced
- ``NEWRELIC_WEBHOOK_IGNORE_TYPES``: list of types (alert or deployment) to be ignored from webhooks
- ``NEWRELIC_WEBHOOK_APPS``: Optional list of whitelisted app names

## Contributing

Contributions are welcomed, as well as any bug reports!

## License

Copyright (c) 2013 Shaun Duncan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
