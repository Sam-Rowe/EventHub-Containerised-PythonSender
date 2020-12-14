import os
import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from faker import Faker

async def run():

    faker = Faker() 
    
    eventhub_connection_STR = os.getenv('EVENT_HUB_CONN_STR')

    eventhub_name = os.getenv('EVENT_HUB_NAME')
    
    print(eventhub_connection_STR)
    print(eventhub_name)
    
    producer = EventHubProducerClient.from_connection_string(conn_str= eventhub_connection_STR, eventhub_name= eventhub_name)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(faker.name()))
        event_data_batch.add(EventData(faker.name()))
        #event_data_batch.add(EventData(faker.simple_profile()))

        # Send the batch of events to the event hub.
        while (True):
            await producer.send_batch(event_data_batch)
        
            

loop = asyncio.get_event_loop()
loop.run_until_complete(run())