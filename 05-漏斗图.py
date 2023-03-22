from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts import options as opts


def funnel_base():
    c = (Funnel()
         .add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
         .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
         )
    return c


funnel_base().render('漏斗图.html')
