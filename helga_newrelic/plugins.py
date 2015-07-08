from lxml import etree

from twisted.internet import reactor

import requests

from helga import settings
from helga.plugins import Command, ResponseNotReady


class NewRelicStats(Command):

    command = 'newrelic'
    aliases = ['perf']
    help = ('Get quick insight into a NewRelic app performance. Usage: '
            'helga (newrelic|perf|nrstats) <app_name>')

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        self.api_key = settings.NEWRELIC_API_KEY
        self.account_id = settings.NEWRELIC_ACCOUNT_ID
        self.endpoint = 'https://api.newrelic.com/api/v1/accounts/{id}/applications'.format(id=self.account_id)
        self.api_headers = {'x-api-key': self.api_key}

        # Simpler mapping of name -> id. Loaded on demand
        self.apps = {}

    def get_app_id(self, app_name):
        # Load apps if they haven't been already
        if not self.apps:
            url = '{e}.xml'.format(e=self.endpoint)
            resp = requests.get(url, headers=self.api_headers)
            resp.raise_for_status()
            root = etree.fromstring(resp.content)

            for app in root.findall('application'):
                id = app.find('id').text
                name = app.find('name').text

                if name:
                    self.apps[name] = id
        return self.apps[app_name]

    def get_stats(self, app_name, client, channel):
        try:
            app_id = self.get_app_id(app_name)
        except:
            client.msg(channel, "Unknown app: {a}".format(a=app_name))
            return

        # Get the stats
        url = '{e}/{i}/threshold_values.xml'.format(e=self.endpoint, i=app_id)
        resp = requests.get(url, headers=self.api_headers)
        resp.raise_for_status()
        root = etree.fromstring(resp.content)

        begin, end = None, None

        thresholds = root.findall('threshold_value')
        if not thresholds:
            client.msg(channel, 'No stats found')
            return

        for thresh in thresholds:
            name = thresh.attrib['name']
            value = thresh.attrib['formatted_metric_value']

            if begin is None and end is None:
                begin = thresh.attrib['begin_time']
                end = thresh.attrib['end_time']
                client.msg(channel, 'Summary Stats For {a}: {b} to {e}'.format(a=app_name, b=begin, e=end))

            client.msg(channel, '{n}: {v}'.format(n=name, v=value))

    def run(self, client, channel, nick, message, cmd, args):
        try:
            app_name = args[0]
        except IndexError:
            return

        client.msg(channel, "Looking up stats for {a}".format(a=app_name))
        reactor.callLater(1, self.get_stats, app_name, client, channel)
        raise ResponseNotReady
