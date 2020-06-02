import constants as const
from pyicloud import PyiCloudService
import datetime

def get_calendar_data(api):
    
    apple_events = api.calendar.events(datetime.datetime.utcnow(),datetime.datetime.utcnow() + datetime.timedelta(days=const.CONST_SYNC_DAYS))

    calendar_data = {}

    for event in apple_events:

        event_data = {}

        start_data = event['startDate'][1:6]
        end_data   = event['endDate'][1:6]

        calendar_guid  = event['pGuid']
        title          = event['title']
        start_datetime = datetime.datetime(start_data[0],start_data[1],start_data[2],start_data[3],start_data[4],0)
        end_datetime   = datetime.datetime(end_data[0],end_data[1],end_data[2],end_data[3],end_data[4],0)
        guid           = event['guid']

        event_data = {"title": title, "start_datetime": start_datetime, "end_datetime": end_datetime, "guid": guid}
        calendar_data.setdefault(calendar_guid, []).append(event_data)
    
    return calendar_data

def get_reminders_data(account):
    return None

def connect(api):

    import click

    print("Two-step authentication required. Your trusted devices are:")

    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print("  %s: %s" % (i, device.get('deviceName',
            "SMS to %s" % device.get('phoneNumber'))))

    device = click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")

    code = click.prompt('Please enter validation code')
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")

def keep_alive(api):
    api.authenticate()

def get_data(client_id, client_secret, account_type):

    api = PyiCloudService(client_id, client_secret)

    if api.requires_2sa:
        connect(api)

    apple_data = {'calendar': None, 'task': None}

    if account_type == const.CONST_CALENDAR:
        apple_data['calendar'] = get_calendar_data(api)

    elif account_type == const.CONST_TASK:
        apple_data['task'] = get_reminders_data(api)

    else:
        apple_data['calendar'] = get_calendar_data(api)
        apple_data['task'] = get_reminders_data(api)

    return apple_data
