import asyncio
from time import sleep

async def main():
    await asyncio.sleep(5)
    print("ola")

async def oi():
    print("olá, executando")


el = asyncio.get_event_loop()

t = asyncio.gather(el.create_task(main()), el.create_task(oi()))
el.run_until_complete(t)
# el.close()
# asyncio.run(main())
# asyncio.run(oi())
