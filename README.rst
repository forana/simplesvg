================
simplesvg
================
Simple python library for programatically building SVG XML. (backed by xml4h https://github.com/jmurty/xml4h)

--------
Why
--------
There are two solid libraries for doing similar things already (pySVG http://codeboje.de/pysvg/ and svgwrite https://pypi.python.org/pypi/svgwrite/), but neither does quite what I find myself needing so succinctly as this.

----------------
Installation
----------------
::

	pip install simplesvg

----------------
Functions
----------------
**A note on \*\*kwargs**
	For all of the ``kwarg``-using functions below, any arguments passed will be directly added to the XML elements. Camel case will be converted to hyphenated words automatically (e.g. ``strokeWidth`` becomes ``stroke-width``). Common usage of this would be ``fill``, ``stroke``, ``stroke-width``, and ``id``. See ``example.py`` for some usage of these.

``simplesvg.SVG(width, height, **kwargs)``
	* Creates a new SVG document with specified with and height (in pixels). Elements within can exceed these bounds (but they might not be rendered depending on what's being used to display the SVG).

``SVG.to_xml()``
	* Serializes the document to XML and returns the resulting string.

``SVG.circle(x, y, r, **kwargs)``
	* ``x``, ``y`` = coordinate for the center of the circle
	* ``r`` = radius

``SVG.rectangle(x, y, width, height, **kwargs)``
	* ``x``, ``y`` = coordinate of the upper-left corner of the rectangle
	* ``width``, ``height`` = dimensions of the rectangle

``SVG.line(x1, y1, x2, y2, **kwargs)``
	* ``x1``, ``y1`` = coordinate of the first point.
	* ``x2``, ``y2`` = coordinate of the second point.

``SVG.polygon(points, **kwargs)``
	* ``points`` = an ordered list of pairs representing points on the polygon (e.g. ``[(1,2), (3,4), (1,6]]``)

``simplesvg.rgb(r, g, b)``
	* Helper function that you can pass with ``fill`` or ``stroke`` to used RGB colors instead of named colors.

See ``example.py`` in the repo for usage of all of this.
