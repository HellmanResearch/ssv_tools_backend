
from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ssv',
        'USER': 'root',
        'PASSWORD': 'Ipfs@111',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


# CELERY_BROKER_URL = "amqp://dfinity_off_chain:dfinity_off_chain,1@127.0.0.1/dfinity_off_chain",

# DFINITY_PROJECT_PATH = "/root/local/WICP"
# DFINITY_NETWORK = "ic"
# DFINITY_WICP_CANISTER_ID = "7xlb5-raaaa-aaaai-qa2ja-cai"
# DFINITY_CALL_WICP_IDENTITY = "default"

