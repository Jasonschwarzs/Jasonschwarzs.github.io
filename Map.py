import pandas as pd                                                                             #强大的数据分析的第三方库，能够用于处理DataFrame类型
from pyecharts.charts import Map                                                                #导入pyecharts库，用于绘制世界地图
from pyecharts import options as opts
from pyecharts.globals import ThemeType

df=pd.read_excel("GDP.xlsx")                                                                    #读取数据
country=list(df['Country2'])                                                                    #提出country列放到列表中
gdp=list(df['GDP'])                                                                             #提出GDP列放到列表中
list= [list(z) for z in zip(country,gdp)]                                                       #将两个列表放到一起

c=(
     Map(init_opts=opts.InitOpts(width="1500px", height="600px",theme=ThemeType.DARK))         #设置地图大小
     .add("GDP",list,"world",is_map_symbol_show=False)                                          #将list传入，设置不显示小红点，地图类型为world
     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))                                 #设置不显示标签，否则会很乱
     .set_global_opts(
         title_opts=opts.TitleOpts(title="世界各国人均GDP  单位:美元"),                             #设置标题
         visualmap_opts=opts.VisualMapOpts(
            min_=100,                                                                           #设置人均GDP的最小值和最大值
            max_=140000,
            range_text = ['人均GDP（美元）颜色区间:', ''],                                          #分区间
            range_color = ['#ccfffb','#210af5'],
            is_piecewise=True,                                                                  #定义图例为分段型，默认为连续的图例
            pos_top= "middle",                                                                  #设置分段图表的位置
            pos_left="left",
            orient="vertical",                                                                  #图标纵向分布
            split_number=10                                                                     #分成10个区间
         )
    )
)
c.render('Map.html')                                                                           #做成.html文件并在浏览器中打开