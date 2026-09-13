import asyncio, random


class Gateway:
    count = 0

    def __init__(self, **kwargs):
        Gateway.count += 1
        self.instance_id = Gateway.count
        self.hostname = kwargs.get("hostname", "default_gw")
        self.ip_address = kwargs.get("ip_address", "192.168.254.1/24")
        self.firmware_version = 0

    async def upgrade_firmware(self):
        print("Starting firmware upgrade...")
        await asyncio.sleep(random.randint(1, 6))
        self.firmware_version += 1
        print(f"Firmware version upgraded to version {self.firmware_version}")


async def main():
    try:
        arguments = {"hostname": "gw1", "ip_address": "172.16.10.1/24"}
        gw1 = Gateway(**arguments)
        gw2 = Gateway(hostname="gw2", ip_address="10.10.10.1/24")
        await asyncio.create_task(gw1.upgrade_firmware())
        print(f"{gw2.hostname} has an id of {gw2.instance_id}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
