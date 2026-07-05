import requests
from enum import Enum

SUBSCRIPTION = ''
AUTH_TOKEN = ''

url = f'https://ntfy.sh/{SUBSCRIPTION}'

class Priority(Enum):
    Min = 1
    Low = 2
    Default = 3
    High = 4
    Max = 5


def notify(title='', message='', priority=Priority.Default, tag='', image=None):
    """
    ATTENTION: image overrides message
    """
    
    headers = { 
                'Priority' : str(priority.value), 
                'Title': title,
                'Authorization': f'Bearer {AUTH_TOKEN}'
    }
    if tag != '':
        headers['Tags'] = tag
    
    if image:
        headers['Filename'] = image
        requests.post(
            url, 
            data=open(image, 'rb'),
            headers=headers
        )
    else:
        requests.post(
            url, 
            data=message.encode(encoding='utf-8'),
            headers=headers
        )


def notify_error(title='', message='', priority=Priority.Default, image=None):
    """
    ATTENTION: image overrides message
    """
    notify(
        f'[ERROR] {title}', 
        message, 
        priority, 
        'rotating_light',
        image
    )


def notify_warning(title='', message='', priority=Priority.Default, image=None):
    """
    ATTENTION: image overrides message
    """
    notify(
        f'[WARNING] {title}',
        message,
        priority,
        'warning',
        image
    )


def notify_completion(title='', message='', priority=Priority.Default, image=None):
    """
    ATTENTION: image overrides message
    """
    notify(
        f'[Execution completed] {title}', 
        message, 
        priority, 
        'white_check_mark',
        image
    )


def notify_info(title='', message='', priority=Priority.Default, image=None):
    """
    ATTENTION: image overrides message
    """
    notify(
        f'[INFO] {title}', 
        message, 
        priority,
        'eyes',
        image
    )
