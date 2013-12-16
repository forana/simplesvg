"""
python example.py
"""

import simplesvg

svg = simplesvg.SVG(200, 200)
svg.circle(100, 100, 100, fill = "blue", stroke = "green", strokeWidth = "3", id="c1")
svg.rectangle(50, 50, 100, 50, fill = "green")
svg.line(100, 0, 100, 180, stroke = "red", strokeWidth = "5")
svg.polygon([(50, 100), (100, 100), (150, 150)], fill = simplesvg.rgb(255,200,0))

print(svg)
