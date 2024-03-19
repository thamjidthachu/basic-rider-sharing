import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class RideTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'ride_tracking'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def update_ride_location(self, event):
        ride_id = event['ride_id']
        location = event['location']
        await self.send(text_data=json.dumps({
            'ride_id': ride_id,
            'location': location
        }))