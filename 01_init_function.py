import asyncio, random


class Gateway:
    count = 0

    def __init__(
        self,
        hostname,
        ip_address,
    ):
        Gateway.count += 1
        self.instance_id = Gateway.count
        if not isinstance(hostname, (str)):
            raise ValueError("Hostname must be a string")
        self.hostname = hostname
        self.ip_address = ip_address
        self.firmware_version = 0

    async def upgrade_firmware(self):
        print("Starting firmware upgrade...")
        await asyncio.sleep(random.randint(1, 6))
        self.firmware_version += 1
        print(f"Firmware version upgraded to version {self.firmware_version}")


async def main():
    try:
        gw1 = Gateway("gw1", "172.16.10.1/24")
        gw2 = Gateway("gw2", "10.10.10.1/24")
        await asyncio.create_task(gw1.upgrade_firmware())
        print(f"{gw2.hostname} has an id of {gw2.instance_id}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
