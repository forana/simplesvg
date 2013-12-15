def convert_case(text):
	s = ""
	for char in text:
		if ord(char) >= ord('A') and ord(char) <= ord('Z'):
			s += "-" + chr(ord(char) - ord('A') + ord('a'))
		else:
			s += char
	return s

class Shape:
	def __init__(self, tagname, **attrs):
		self.tagname = tagname
		self.attrs = {convert_case(k): v for k, v in attrs.items()}

	def to_xml(self, xml):
		xml.element(self.tagname).attributes(self.attrs)

class Circle(Shape):
	def __init__(self, x, y, r, *args, **kwargs):
		Shape.__init__(self, "circle", cx = x, cy = y, r = r, **kwargs)
