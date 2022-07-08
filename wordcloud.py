import pandas as pd                                                                             #强大的数据分析的第三方库，能够用于处理DataFrame类型
from pyecharts import options as opts
from pyecharts.charts import WordCloud

df=pd.read_excel("GDP.xlsx")                                                                    #读取数据
country=list(df['Country2'])                                                                    #提出country列放到列表中
gdp=list(df['GDP'])                                                                             #提出GDP列放到列表中
list= [list(z) for z in zip(country,gdp)]  

c = (
    WordCloud()
    .add(shape='diamond',series_name="GDP of different countries in the world", data_pair=list,\
         word_size_range=[5, 50],is_draw_out_of_bound= False,width=2000,height=1000)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="GDP of different countries in the world", \
                title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("wordcloud.html")
)