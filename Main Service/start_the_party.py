import asyncio
import utils.email_service as email_service
from gpt3 import great_ape

async def procedure():

    response_objects = await email_service.process_new_messages(great_ape.call_gpt3)
    for response_object in response_objects:
        email_service.send_message(response_object)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(procedure())
