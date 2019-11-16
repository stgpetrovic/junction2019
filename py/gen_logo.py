from typing import Dict

SVG = """
<svg width="500" height="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  {basket}
  {eyes}
  {mouth}
</svg>
"""

DOMAIN = "https://green-basket.xyz/"

class IncludeImage():
    def __init__(self: 'IncludeImage', href: str, x: float, y: float, height: float, width: float) -> None:
        self.href = href
        self.x = x
        self.y = y
        self.height = height
        self.width = width


    def format(self: 'IncludeImage') -> str:
        return '<image xlink:href="{href}" x="{x}" y="{y}" height="{height}" width="{width}"/>'.format(
            href=DOMAIN + self.href,
            x=self.x,
            y=self.y,
            height=self.height,
            width=self.width,
        )

    def to_dict(self: 'IncludeImage') -> Dict[str, str]:
        return {
            "href": self.href,
            "x": "{:.0f}".format(self.x),
            "y": "{:.0f}".format(self.y),
            "height": "{:.0f}".format(self.height),
            "width": "{:.0f}".format(self.width),
        }


def logo(health: float, sustinable: float) -> Dict[str, Dict[str, str]]:
    return {
        "basket": basket(health, sustinable).to_dict(),
        "eyes": eyes(health, sustinable).to_dict(),
        "mouth": mouth(health, sustinable).to_dict(),
    }

def logo_svg(health: float, sustainable: float) -> str:
    return SVG.format(
        basket=basket(health, sustainable).format(),
        eyes=eyes(health, sustainable).format(),
        mouth=mouth(health, sustainable).format(),
    )


def basket(health:float, sustinable: float) -> IncludeImage:
    return IncludeImage("images/basket.png", 0, 0, 300, 300)

def eyes(health:float, sustinable: float) -> IncludeImage:
    if health < 33:
        return IncludeImage("images/angry-eyes.png", 90, 150, 75, 125)
    if health < 66:
        return IncludeImage("images/concerened-eyes.png", 90, 155, 75, 125)
    return IncludeImage("images/happy-eyes.png", 90, 150, 75, 125)

def mouth(health:float, sustinable: float) -> IncludeImage:
    if sustinable < 33:
        return IncludeImage("images/shocked-mouth.png", 28, 225, 60, 250)
    if sustinable < 66:
        return IncludeImage("images/happy-mouth.png", 65, 225, 50, 175)
    return IncludeImage("images/tasty-mouth.png", 25, 225, 60, 250)
