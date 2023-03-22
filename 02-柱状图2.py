from pyecharts.charts import Bar
from pyecharts import options as opts

# 不习惯链式调用的开发者依旧可以单独调用方法
# 如果需要设置相应的配置项，可以根据API里的描述，去进行设置。
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题'))  # 全局配置项设置
bar.render('柱状图2.html')  # 生成文件(即render)
