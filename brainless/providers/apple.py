from configuration import CONST_APPLE
from pyicloud import PyiCloudService
from classes.events import Event
from classes.users import User
import datetime

api = PyiCloudService('joaovbmdias@icloud.com')

def connect():

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

def get_events(user, range):

    if api.requires_2sa:
        connect()

    apple_events = api.calendar.events(range['from'],range['to'])

    new_events = []

    for event in apple_events:

        start_data = event['startDate'][1:6]
        start      = datetime.datetime(start_data[0],start_data[1],start_data[2],start_data[3],start_data[4],0)
        end_data   = event['endDate'][1:6]
        end        = datetime.datetime(end_data[0],end_data[1],end_data[2],end_data[3],end_data[4],0)

        new_events.append(Event (title          = event['title'],
                                 start_datetime = start,
                                 end_datetime   = end,
                                 guid           = event['guid'],
                                 provider       = CONST_APPLE,
                                 user_id        = user.id))
    
    return sorted(new_events, key=lambda event: event.start_datetime)