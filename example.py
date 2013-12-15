import simplesvg

svg = simplesvg.SVG(200, 200)
svg.circle(100, 100, 10, fill = "blue", id="c1")

print(svg)
