
from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ssv',
        'USER': 'ssv',
        'PASSWORD': 'ssv,1',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


CELERY_BROKER_URL = "amqp://dfinity_off_chain:dfinity_off_chain,1@127.0.0.1/dfinity_off_chain",

DFINITY_NETWORK = "ic"
DFINITY_NETWORK_ORIGIN = "https://ic0.app"
DFINITY_WICP_CANISTER_ID = "o5d6i-5aaaa-aaaah-qbz2q-cai"
DFINITY_WICP_STORAGE_CANISTER_ID = "j5d6o-3iaaa-aaaah-qccra-cai"
DFINITY_ZOMBIE_CANISTER_ID = "iyzne-taaaa-aaaah-qcjga-cai"
DFINITY_ZOMBIE_STORAGE_ID = "edgk4-5iaaa-aaaai-qa7ha-cai"
DFINITY_PAGE_SIZE = 50
DFINITY_PROJECT_PATH = "/projects/dfinity_project"
DFINITY_CALL_WICP_IDENTITY = "CCCAphlaOwner"
DFINITY_CALL_WICP_STORAGE_IDENTITY = "CCCAphlaOwner"
DFINITY_CALL_ZOMBIE_IDENTITY = "CCCAphlaOwner"
DFINITY_CALL_ZOMBIE_STORAGE_IDENTITY = "CCCAphlaOwner"
