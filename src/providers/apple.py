import constants as const
from pyicloud import PyiCloudService
from datetime import datetime, timedelta

def get_calendar_data(api):
    
    apple_events = api.calendar.events(datetime.utcnow(),datetime.utcnow() + timedelta(days=const.SYNC_DAYS))

    calendar_data = []
    temp = {}

    for event in apple_events:

        event_data = {}

        calendar_guid  = event['pGuid']
        calendar_name  = ''

        name           = event['title']
        start_data = event['startDate'][1:6]
        start_datetime = datetime(start_data[0],start_data[1],start_data[2],start_data[3],start_data[4],0)
        end_data   = event['endDate'][1:6]
        end_datetime   = datetime(end_data[0],end_data[1],end_data[2],end_data[3],end_data[4],0)
        guid           = event['guid']

        event_data = {"name": name, "start_datetime": start_datetime, "end_datetime": end_datetime, "guid": guid}
        temp.setdefault(calendar_guid, []).append(event_data)
    
    for cal, events in temp.items():
        calendar_data.append({'name': '', 'guid': cal, 'events': events})

    return calendar_data

def get_reminders_data(account):
    return None

def connect(api):

    import click

    print("Two-step authentication required. Your trusted devices are:")

    devices = api.trusted_devices
    # for i, device in enumerate(devices):
    #     print("  %s: %s" % (i, device.get('deviceName',
    #         "SMS to %s" % device.get('phoneNumber'))))

    device = 0#click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")

    code = click.prompt('Please enter validation code')
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")

def keep_alive(client_id, client_secret):
    api = PyiCloudService(client_id, client_secret)
    api.authenticate()

def get_data(client_id, client_secret, account_type):

    api = None

    try:
        api = PyiCloudService(client_id, client_secret)

        if api.requires_2sa:
            connect(api)
    except:
        print('Failed to login to user\'s apple account')

    apple_data = {const.CALENDAR: None, const.TASK: None, const.LABEL: None}

    if account_type == const.CALENDAR:
        apple_data[const.CALENDAR] = get_calendar_data(api)

    elif account_type == const.TASK:
        apple_data[const.TASK] = get_reminders_data(api)

    else:
        apple_data[const.CALENDAR] = get_calendar_data(api)
        apple_data[const.TASK] = get_reminders_data(api)

    return apple_data
