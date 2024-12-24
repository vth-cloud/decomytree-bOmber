import aiohttp
import asyncio
import random

url = "https://deco-my-tree-web.com/api/v1/message/id_cua_ban"
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
    "Authorization": "Token_Cua_Ban",
    "Connection": "keep-alive",
    "DNT": "1",
    "Sec-GPC": "1",
}

messages = [
    "Chúc bạn một Giáng sinh an lành và ấm áp bên gia đình và những người thân yêu.",
    "Mong rằng Giáng sinh này mang đến cho bạn thật nhiều niềm vui và hạnh phúc.",
    "Chúc bạn một mùa Giáng sinh đầy ắp tiếng cười và những kỷ niệm đáng nhớ.",
    "Chúc bạn một Giáng sinh tràn đầy ánh sáng và tình yêu thương.",
    "Mong rằng mọi ước mơ của bạn sẽ thành hiện thực trong mùa lễ này.",
    "Chúc bạn và gia đình có một mùa Giáng sinh bình an và hạnh phúc.",
    "Hy vọng rằng Giáng sinh này sẽ là thời gian để bạn tận hưởng sự yên bình và vui vẻ.",
    "Chúc bạn có một Giáng sinh rực rỡ, vui tươi và ý nghĩa.",
    "Mong rằng Giáng sinh sẽ mang đến sự ấm áp và những điều kỳ diệu cho cuộc sống của bạn.",
    "Chúc bạn có một Giáng sinh như ý và một năm mới đầy thành công.",
    "Chúc cho tất cả những mong ước của bạn sẽ trở thành hiện thực trong mùa Giáng sinh này.",
    "Giáng sinh đến, chúc bạn tràn đầy sức khỏe, niềm vui và bình an.",
    "Mong rằng tình yêu và hạnh phúc sẽ luôn tràn ngập trong ngôi nhà của bạn mùa Giáng sinh này.",
    "Chúc bạn một Giáng sinh với thật nhiều niềm vui và những khoảnh khắc đẹp.",
    "Chúc cho những ước nguyện của bạn đều được ông già Noel nghe thấy.",
    "Hy vọng mùa lễ này sẽ mang đến cho bạn niềm vui vô tận và những điều tốt đẹp nhất.",
    "Chúc bạn có một Giáng sinh thật trọn vẹn với những điều yêu thương nhất.",
    "Chúc bạn một mùa Giáng sinh tràn đầy yêu thương và hạnh phúc.",
    "Mong rằng ánh sáng của Giáng sinh sẽ luôn soi sáng con đường bạn đi.",
    "Chúc bạn có một Giáng sinh ấm áp, ý nghĩa và ngập tràn tình yêu.",
    "Chúc cho niềm vui và may mắn luôn đồng hành cùng bạn trong mùa Giáng sinh này.",
    "Chúc bạn có một Giáng sinh ngọt ngào bên gia đình và bạn bè.",
    "Mong rằng mùa Giáng sinh này sẽ mang đến những điều tuyệt vời nhất cho bạn.",
    "Giáng sinh là thời gian của sự yêu thương, hãy tận hưởng từng khoảnh khắc nhé!",
    "Chúc bạn một mùa Giáng sinh tràn đầy hạnh phúc và thành công.",
    "Mong rằng Giáng sinh sẽ là thời gian để bạn tạo ra những kỷ niệm đáng nhớ.",
    "Chúc bạn một Giáng sinh an lành và luôn tươi cười trong mọi hoàn cảnh.",
    "Chúc bạn nhận được thật nhiều quà và tình yêu trong mùa lễ này.",
    "Mong rằng ông già Noel sẽ mang đến cho bạn tất cả những điều bạn mong muốn.",
    "Chúc bạn một mùa Giáng sinh rực rỡ với đầy những bất ngờ thú vị.",
    "Chúc bạn một Giáng sinh tràn đầy niềm vui và hy vọng.",
    "Mong rằng những điều tốt đẹp sẽ đến với bạn trong mùa Giáng sinh này.",
    "Chúc bạn và gia đình một mùa Giáng sinh bình an và hạnh phúc.",
    "Mong rằng Giáng sinh này sẽ mang đến cho bạn sự bình yên và những điều may mắn.",
    "Chúc bạn luôn giữ được tinh thần vui vẻ trong mùa lễ Giáng sinh.",
    "Giáng sinh là thời điểm để sẻ chia yêu thương, chúc bạn luôn được yêu thương thật nhiều.",
    "Chúc bạn một Giáng sinh ấm áp và tràn đầy ánh sáng hy vọng.",
    "Mong rằng Giáng sinh sẽ mang đến cho bạn những phút giây hạnh phúc nhất.",
    "Chúc bạn có một Giáng sinh ý nghĩa bên những người thân yêu.",
    "Hy vọng rằng những phép màu của Giáng sinh sẽ luôn bên bạn.",
    "Chúc bạn một Giáng sinh với thật nhiều điều kỳ diệu và hạnh phúc.",
    "Mong rằng Giáng sinh sẽ mang đến cho bạn thật nhiều tiếng cười và niềm vui.",
    "Chúc bạn một mùa lễ đầy ý nghĩa và đáng nhớ.",
    "Chúc bạn một Giáng sinh an lành và hạnh phúc như bạn mong ước.",
    "Giáng sinh là thời gian của niềm vui, chúc bạn luôn cảm nhận được điều đó.",
    "Chúc bạn nhận được thật nhiều quà và những lời chúc tốt đẹp trong mùa Giáng sinh này.",
    "Mong rằng Giáng sinh sẽ là khởi đầu cho một năm mới tràn đầy thành công và may mắn.",
    "Chúc bạn một Giáng sinh thật rực rỡ, ngập tràn niềm vui và yêu thương.",
    "Chúc bạn có một mùa lễ an yên và hạnh phúc bên những người bạn yêu quý."
]

async def send_request(session):
    while True:
        try:
            random_message = random.choice(messages)
            data = {
                "name": "ong gia noel",
                "content": random_message,
                "deco_index": random.randint(1,21),
                "only_for_user": False,
            }
            async with session.post(url, headers=headers, json=data) as response:
                print(f"Thực Thi: {response.status} | Thành Công: {await response.text()}")
        except Exception as e:
            print(f"Hata: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session) for _ in range(50)]
        await asyncio.gather(*tasks)

asyncio.run(main())
