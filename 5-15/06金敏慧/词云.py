import pyecharts.options as opts
from pyecharts.charts import WordCloud

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://gallery.echartsjs.com/editor.html?c=xS1jMxuOVm

目前无法实现的功能:

1、暂无
"""

data = [
    ("我们", "999"),
    ("这个", "888"),
    ("比如说", "777"),
    ("觉得", "688"),
    ("问题", "588"),
    ("一个", "516"),
    ("所以", "515"),
    ("这样", "483"),
    ("现在", "462"),
    ("咨询", "449"),
    ("什么", "429"),
    ("比较", "407"),
    ("实际上", "406"),
    ("然后", "406"),
    ("一样", "386"),
    ("时候", "385"),
    ("企业", "375"),
    ("可能", "355"),
    ("项目", "355"),
    ("就是", "335"),
    ("里面", "324"),
    ("员工", "304"),
    ("还是", "304"),
    ("公司", "284"),
    ("但是", "284"),
    ("没有", "284"),
    ("事情", "254"),
    ("因为", "254"),
    ("角度", "253"),
    ("一点", "253"),
    ("能力", "223"),
    ("那么", "223"),
    ("怎么样", "223"),
    ("东西", "223"),
    ("能够", "223"),
    ("来说", "223"),
    ("相当于", "223"),
    ("肯定", "223"),
    ("取费", "223"),
    ("30", "152"),
    ("解决", "152"),
    ("你们", "152"),
    ("自己", "152"),
    ("他们", "152"),
    ("不是", "152"),
    ("有些", "152"),
    ("大家", "152"),
    ("不能", "112"),
    ("来讲", "112"),
    ("业主", "112"),
    ("客户", "112"),
    ("真的", "112"),
    ("什么样", "112"),
    ("这种", "112"),
    ("整个", "92"),
    ("行业", "92"),
    ("服务", "92"),
    ("原来", "92"),
    ("不好", "92"),
    ("10", "92"),
    ("人均产值", "72"),
    ("个人", "72"),
    ("多少", "72"),
    ("人家", "72"),
    ("EPC", "71"),
    ("很多", "71"),
    ("通过", "71"),
    ("这么", "71"),
    ("刚才", "71"),
    ("也好", "71"),
    ("全过程", "71"),
    ("考虑", "71"),
    ("一些", "71"),
    ("未来", "71"),
    ("建筑", "71"),
    ("20", "71"),
    ("有个", "71"),
    ("就是说", "71"),
    ("或者", "41"),
    ("投资", "41"),
    ("当然", "41"),
    ("这里", "41"),
    ("价值", "41"),
    ("大部分", "41"),
    ("是不是", "41"),
    ("或者说", "41"),
    ("广场", "41"),
    ("一下", "41"),
    ("我要", "21"),
    ("怎么", "21"),
    ("前面", "21"),
    ("家里", "21"),
    ("业务", "21"),
    ("社区", "21"),
    ("创造", "21"),
    ("第二个", "11"),
    ("需求", "11"),
    ("包括", "11"),
    ("说实话", "11"),
    ("工作", "11"),
    
]


(
    WordCloud()
    .add(series_name="热点分析", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("basic_wordcloud1.html")
)