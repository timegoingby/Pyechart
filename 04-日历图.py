import datetime
import random
from pyecharts.charts import Calendar
from pyecharts import options as opts


# Calendar-2017年微信步数情况
# https://blog.csdn.net/weixin_44469890/article/details/103115217
def calendar_base():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    c = (
        Calendar()
            .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c


calendar_base().render("日历图.html")  # calendar_base().render_notebook()
