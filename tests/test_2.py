from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types, encode

# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)

params = [
    {'type': Types.Principal, 'value': 'ici4c-dgxam-uzc5b-rqbkm-pcfwc-hpyek-6vsom-u5rhm-cjsh7-6n64i-bae'},
    {'type': Types.Nat, 'value': 10000000000}
]
result = agent.update_raw("gvbup-jyaaa-aaaah-qcdwa-cai", "transfer", encode(params))
pass

