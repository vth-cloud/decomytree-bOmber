import aiohttp
import asyncio
import random

url = "https://deco-my-tree-web.com/api/v1/message/Your-target-id"
headers = {
    "Host": "deco-my-tree-web.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "*/*",
    "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "Referer": "https://decomytree.com/",
    "Origin": "https://decomytree.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Authorization": "ur author",
    "Connection": "keep-alive",
    "DNT": "1",
    "Sec-GPC": "1",
}

messages = [
    "Merry Christmas! Wishing you a season full of love and happiness!",
    "May your Christmas sparkle with joy and laughter!",
    "Wishing you peace, love, and joy this Christmas and throughout 2024!",
    "Merry Christmas! May your days be filled with warmth and cheer!",
    "Hope your Christmas is as sweet as a candy cane!",
    "Wishing you a holiday season that's merry and bright!",
    "May your Christmas be magical and full of surprises!",
    "Sending you warm wishes and a big hug this Christmas!",
    "Merry Christmas! Here's to love, laughter, and joy this holiday season!",
    "Have a holly, jolly Christmas filled with happiness and love!",
    "May the spirit of Christmas bring you closer to your loved ones!",
    "Wishing you a blessed and beautiful Christmas!",
    "Merry Christmas! Hope Santa brings you everything you wish for!",
    "May your holiday season be full of magic, wonder, and peace!",
    "Merry Christmas! Cheers to love and laughter in the New Year!",
    "Wishing you a holiday filled with delicious treats and joy!",
    "Hope your Christmas is filled with warmth, love, and joy!",
    "Merry Christmas! Let’s make this season bright with kindness!",
    "Wishing you a Christmas filled with beautiful moments and memories!",
    "Merry Christmas! May this season be a blessing for you and your family!",
]

async def send_request(session, counter):
    for _ in range(counter):
        try:
            random_message = random.choice(messages)
            data = {
                "name": "Hoanq Thai",
                "content": random_message,
                "deco_index": 19,
                "only_for_user": False,
            }
            async with session.post(url, headers=headers, json=data) as response:
                print(f"Thực Thi: {response.status} | Thành Công: {await response.text()}")
        except Exception as e:
            print(f"Hata: {e}")

async def main():
    counter = 20  # count message
    async with aiohttp.ClientSession() as session:
        await send_request(session, counter)

asyncio.run(main())
