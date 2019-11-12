#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def carousel():
    carousel={
  "type": "flex",
  "altText": "Flex Message",
  "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://tblg.k-img.com/restaurant/images/Rvw/62698/150x150_square_62698123.jpg",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": "https://linecorp.com/"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "KINKA sushi bar izakaya 渋谷",
            "size": "lg",
            "weight": "bold",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "size": "sm"
              },
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "size": "sm"
              },
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "size": "sm"
              },
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "size": "sm"
              },
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "size": "sm"
              },
              {
                "type": "text",
                "text": "評価:3.51",
                "flex": 0,
                "margin": "md",
                "size": "sm",
                "color": "#999999"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "場所:",
                    "flex": 1,
                    "size": "xs",
                    "color": "#AAAAAA"
                  },
                  {
                    "type": "text",
                    "text": "渋谷駅 530m\n居酒屋、寿司、日本酒バー",
                    "flex": 5,
                    "size": "xs",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "予算:",
                    "flex": 1,
                    "size": "xs",
                    "color": "#AAAAAA"
                  },
                  {
                    "type": "text",
                    "text": "夜:￥4,000～￥4,999\n昼:～￥999",
                    "flex": 5,
                    "size": "xs",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "定休日:",
                    "flex": 1,
                    "size": "xs",
                    "color": "#AAAAAA"
                  },
                  {
                    "type": "text",
                    "text": "1月1日",
                    "flex": 5,
                    "size": "xs",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "詳細",
              "uri": "https://tabelog.com/tokyo/A1303/A130301/13199924/"
            },
            "height": "sm",
            "style": "link"
          },
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  ]
}
}
    return carousel