import json

from helga import log, settings
from helga.plugins.webhooks import route


logger = log.getLogger(__name__)

# Allows to choose which channel to announce on - default #newrelic
channel = getattr(settings, 'NEWRELIC_WEBHOOK_ANNOUNCE_CHANNEL', '#newrelic')

# What alert types should we ignore? (alert, deployment)
ignore_types = getattr(settings, 'NEWRELIC_WEBHOOK_IGNORE_TYPES', [])

# Specific message formats
message_formats = {
    'alert': '[{severity}][{app}] {message} at {timestamp} ({alert_url})',
    'deployment': '[{type}][{app}] {revision} - {description} by {deployed_by} at {timestamp}',
}


@route('/newrelic', methods=['POST'])
def newrelic(request, irc_client):
    logger.info('Received NewRelic webhook')
    if 'alert' in request.args:
        key = 'alert'
        data = json.loads(request.args[key][0])
    elif 'deployment' in request.args:
        key = 'deployment'
        data = json.loads(request.args[key][0])
    else:
        logger.warning('Received NewRelic webhook with no valid POST param')
        return 'No valid POST param found'

    app_name = data['application_name']

    # Check and make sure we want this
    if key in ignore_types:
        return 'ok - ignored type {}'.format(key)

    if hasattr(settings, 'NEWRELIC_WEBHOOK_APPS') and app_name not in settings.NEWRELIC_WEBHOOK_APPS:
        return 'ok - app {} is being ignored'.format(app_name)

    # Server alerts are a bit different
    if 'servers' in data:
        data['message'] = '{} on {}'.format(data['message'], ','.join(data['servers']))

    fmt_data = {
        'type': key,
        'app': app_name,
        'timestamp': data['created_at'],
    }

    fmt_data.update(data)
    irc_client.msg(channel, message_formats[key].format(**fmt_data))
    return 'ok - message sent'
