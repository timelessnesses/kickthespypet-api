import asyncio
from pprint import pprint as print

import kickthespypet_api

lol = kickthespypet_api.KickTheSpyPetAPI()

print(lol.get_bot_by_server_id(1049706293700591677))
print(lol.get_bot_by_server_id("1049706293700591677"))
print(lol.get_bot_by_server_invite("pQPt8HBUPu"))  # cobalt community server
print(lol.get_bot_user_ids_int(False, True))
lol.close()


async def main():
    lol = kickthespypet_api.AsyncKickTheSpyPetAPI()

    print(await lol.get_bot_by_server_id(1049706293700591677))
    print(await lol.get_bot_by_server_id("1049706293700591677"))
    print(await lol.get_bot_by_server_invite("pQPt8HBUPu"))  # cobalt community server
    print(await lol.get_bot_user_ids_int(False, True))
    await lol.close()
    async with kickthespypet_api.AsyncKickTheSpyPetAPI() as client:
        print(await client.get_bot_user_ids_int(False, True))


asyncio.run(main())

with kickthespypet_api.KickTheSpyPetAPI() as client:
    print(client.get_bot_user_ids_int(False, True))
