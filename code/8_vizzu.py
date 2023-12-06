import pandas as pd
from ipyvizzu import Config, Data, Style
from ipyvizzustory import Story, Slide, Step

df = pd.read_excel("data/dataset.xlsx")
data = Data()
data.add_df(df)

story = Story(data)
story.set_size(640, 320)
story.set_feature("tooltip", True)

story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": None, "max": None}},
                    "color": "group",
                    "lightness": None,
                    "size": "x",
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": None,
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                        },
                    }
                }
            ),
        )
    )
)

story.play()