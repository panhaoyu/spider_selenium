import os
import json
import m3u8
import asyncio
import aiofiles
import aiohttp


async def download(url, path):
    m = m3u8.load(url)
    for file in m.files:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{m.base_uri}{file}') as response:
                data = await response.content.read()
                async with aiofiles.open(path, mode='ab') as f:
                    print(path, file)
                    await f.write(data)


async def main():
    with open('data.json', mode='r', encoding='utf-8') as f:
        meta_data = json.load(f)
    with open('m3u8.json', mode='r', encoding='utf-8') as f:
        video_data = json.load(f)
    for chapter_index, chapter_temp in enumerate(zip(meta_data, video_data)):
        chapter_meta, chapter_video = chapter_temp
        lesson_data = chapter_meta['lessons']
        lesson_data = [lesson_datum for lesson_datum in lesson_data
                       if len([unit for unit in lesson_datum['units'] if unit['contentType'] == 1])]
        length = len(lesson_data)
        for lesson_index, lesson in enumerate(chapter_video[:length]):
            title = lesson['title']
            video = lesson['video']
            file_name = os.path.join('mooc_dst', f'{chapter_index + 1}.{lesson_index + 1}. {title}.mp4')
            await download(video, file_name)


asyncio.run(main())
