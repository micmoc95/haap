import aiohttp                          
from homeassistant.core import ServiceCall
                                          
async def async_setup(hass, config):      
    async def call_addon(call: ServiceCall):
        async with aiohttp.ClientSession() as s:
                await s.post("http://addon:8124/dial", json={"num": call.data["num"]} )
    hass.services.async_register("mon_addon", "run", call_addon)
    return True    
