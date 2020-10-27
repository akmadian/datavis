import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.models import TickFormatter, LinearAxis, Range1d, Span
from bokeh.util.compiler import TypeScript

class PriceFormatter(TickFormatter):
  __implementation__ = TypeScript("""
    import {TickFormatter} from "models/formatters/tick_formatter"

    export class PriceFormatter extends TickFormatter {
      doFormat(ticks: string[] | string[]) {
        console.log(ticks)
        const formatted = [`$${parseFloat(ticks[0]).toFixed(2)}`]
        for (let i = 1, len = ticks.length; i < len; i++) {
          formatted.push(`$${parseFloat(ticks[i]).toFixed(2)}`)
        }
        return formatted
      }
    }
    """)

class VolumeFormatter(TickFormatter):
  __implementation__ = TypeScript("""
    import {TickFormatter} from "models/formatters/tick_formatter"

    export class VolumeFormatter extends TickFormatter {
      doFormat(ticks: string[] | string[]) {
        const formatted = [`${parseInt(ticks[0]).toLocaleString('en')}`]
        for (let i = 1, len = ticks.length; i < len; i++) {
          formatted.push(`${parseInt(ticks[i]).toLocaleString('en')}`)
        }
        return formatted
      }
    }
    """)

output_file("index.html")

df = pd.read_csv("./data/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.groupby(["Date"]).mean()

p = figure(
  plot_width=1280, 
  plot_height=720,
  title="Avocado Prices over Time"
)
p.xaxis.ticker = [
  1420329600000000000,
  1440000000000000000,
  1460000000000000000,
  1480000000000000000,
  1500000000000000000,
  1520000000000000000
]
p.xaxis.major_label_overrides = {
  1420329600000000000: "Jan 2015",
  1440000000000000000: "Aug 2015",
  1460000000000000000: "Apr 2016",
  1480000000000000000: "Nov 2016",
  1500000000000000000: "Jul 2017",
  1520000000000000000: "Mar 2018"
}
p.extra_y_ranges = {
  "Volume": Range1d(start=500000, end=1750000),
  "Price": Range1d(start=1, end=2)
}
p.yaxis.visible = False

p.vbar(
  x=df.index.values.tolist(), 
  top=df["Total Volume"].tolist(), 
  y_range_name="Volume",
  bottom=500000,
  width=0.5,
  alpha=0.2,
  legend_label="Total Volume Sold"
)

p.line(
  df.index.values.tolist(), 
  df["AveragePrice"].tolist(), 
  y_range_name="Price",
  line_width=2,
  color="green",
  legend_label="Average Price of an Avocado (USD)"
)

p.add_layout(
  LinearAxis(y_range_name="Price", formatter=PriceFormatter()), 
  "left"
)

p.add_layout(
  LinearAxis(y_range_name="Volume", formatter=VolumeFormatter()), 
  "right"
)
show(p)