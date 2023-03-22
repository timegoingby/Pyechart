from pyecharts.charts import Liquid
from pyecharts import options as opts


def liquid_base() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.66, 0.6])
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    )
    return c


liquid_base().render('水滴图.html')


def liquid_without_outline() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-无边框"))
    )
    return c


liquid_without_outline().render('水滴图-无边框.html')