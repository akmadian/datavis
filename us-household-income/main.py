"""
Data from https://www.kaggle.com/goldenoakresearch/us-household-income-stats-geo-locations?select=kaggle_income.csv
"""
from keplergl import KeplerGl

import pandas as pd

def import_data():
  df = pd.read_csv("./data/kaggle_income.csv", encoding="latin-1")
  return df

def generate_vis():
  config = {
    "version": "v1",
    "config": {
      "visState": {
        "filters": [],
        "layers": [
          {
            "id": "rfnq31gn",
            "type": "grid",
            "config": {
              "dataId": "income",
              "label": "Point",
              "color": [
                255,
                203,
                153
              ],
              "columns": {
                "lat": "Lat",
                "lng": "Lon"
              },
              "isVisible": True,
              "visConfig": {
                "opacity": 0.89,
                "worldUnitSize": 15,
                "colorRange": {
                  "name": "Global Warming",
                  "type": "sequential",
                  "category": "Uber",
                  "colors": [
                    "#5A1846",
                    "#900C3F",
                    "#C70039",
                    "#E3611C",
                    "#F1920E",
                    "#FFC300"
                  ]
                },
                "coverage": 1,
                "sizeRange": [
                  0,
                  1000
                ],
                "percentile": [
                  0,
                  100
                ],
                "elevationPercentile": [
                  0,
                  100
                ],
                "elevationScale": 5,
                "colorAggregation": "average",
                "sizeAggregation": "average",
                "enable3d": True
              },
              "hidden": False,
              "textLabel": [
                {
                  "field": None,
                  "color": [
                    255,
                    255,
                    255
                  ],
                  "size": 18,
                  "offset": [
                    0,
                    0
                  ],
                  "anchor": "start",
                  "alignment": "center"
                }
              ]
            },
            "visualChannels": {
              "colorField": {
                "name": "Median",
                "type": "integer"
              },
              "colorScale": "quantile",
              "sizeField": {
                "name": "Median",
                "type": "integer"
              },
              "sizeScale": "linear"
            }
          }
        ],
        "interactionConfig": {
          "tooltip": {
            "fieldsToShow": {
              "97ap1ofch": [
                {
                  "name": "id",
                  "format": None
                },
                {
                  "name": "State_Code",
                  "format": None
                },
                {
                  "name": "State_Name",
                  "format": None
                },
                {
                  "name": "State_ab",
                  "format": None
                },
                {
                  "name": "County",
                  "format": None
                }
              ]
            },
            "compareMode": False,
            "compareType": "absolute",
            "enabled": True
          },
          "brush": {
            "size": 0.5,
            "enabled": False
          },
          "geocoder": {
            "enabled": False
          },
          "coordinate": {
            "enabled": False
          }
        },
        "layerBlending": "normal",
        "splitMaps": [],
        "animationConfig": {
          "currentTime": None,
          "speed": 1
        }
      },
      "mapState": {
        "bearing": 24,
        "dragRotate": True,
        "latitude": 30.067203168518454,
        "longitude": -128.1037388392268,
        "pitch": 50,
        "zoom": 3.379836309981588,
        "isSplit": False
      },
      "mapStyle": {
        "styleType": "dark",
        "topLayerGroups": {},
        "visibleLayerGroups": {
          "label": True,
          "road": True,
          "border": False,
          "building": True,
          "water": True,
          "land": True,
          "3d building": False
        },
        "threeDBuildingColor": [
          9.665468314072013,
          17.18305478057247,
          31.1442867897876
        ],
        "mapStyles": {}
      }
    }
  }

  m = KeplerGl()
  m.config = config
  m.add_data(data=import_data(), name="income")
  m.save_to_html(file_name="index.html")

if __name__ == "__main__":
  generate_vis()