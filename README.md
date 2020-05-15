# spider_selenium
采用selenium的爬虫，用于更快速创建爬虫

# 已支持的爬虫

# 开发中的爬虫

## 中国大学MOOC

爬取中国大学MOOC的视频文件，其视频为`m3u8`文件，比较容易操作。

爬取的原因是，其在线播放质量实在太差，经常一个`ts`文件要下载十几秒，实在难受，故有此爬虫。

以下为一些在控制台中执行的代码。

打开课件页面。

https://www.icourse163.org/learn/HUST-1003405009?tid=1207009222#/learn/content

在控制台中找到这个XHR请求，右键copy response，在控制台中执行。

https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLastLearnedMocTermDto.dwr

执行以下代码，以获取原始数据。数据会自动进行下载，复制到当前文件夹下即可。

```js
var element = document.createElement('a');
element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(JSON.stringify(s0)));
element.setAttribute('download', 'data.json');
element.style.display = 'none';
document.body.appendChild(element);
element.click();
```

执行以下代码，获取m3u8地址。

```js
result = []
for (let chapter of data){
    chapterResult = []
    for (let lesson of chapter.lessons){
        lessonId = lesson.units[0].lessonId
        url = `https://www.icourse163.org/learn/TONGJI-1002985008#/learn/content?type=detail&id=${lessonId}`
        location.href = url
        await new Promise(resolve =>setTimeout(resolve, 3000))
        chapterResult.push({
            title: lesson.units[0].name,
            video: showVideoPlayerLog().match(/https.*?m3u8/g).slice(-1)[0]
        })
    }
    result.push(chapterResult)
}

var element = document.createElement('a');
element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(JSON.stringify(result)));
element.setAttribute('download', 'm3u8.json');
element.style.display = 'none';
document.body.appendChild(element);
element.click();
```
