from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types, encode

# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)

params = [
    {'type': Types.Nat, 'value': 1}
]
result = agent.query_raw("edgk4-5iaaa-aaaai-qa7ha-cai", "getHistory", encode(params))
pass

