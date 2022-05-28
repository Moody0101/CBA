#!/usr/bin/python python3
# CBA : Css Bundle Algorithm.
# Author: Hossin Azmoud



import pprint


def getSize(string: str) -> None:
	print(f"size {len(string)/10**3} KB")

def reformate(s):
	return s.replace("{", " {\n").replace("}", "\n}\n\n\t").replace(";", ";\n\t")

def getContent(fn: str = "./styles.css")  -> str:
	with open(fn) as fp:
		fileContent = fp.read()
		reformaetd = reformate(fileContent)
		return reformaetd

def getlines(fn: str = "./styles.css"):
	with open(fn) as fp:
		fileContent = fp.read()
		reformaetd = reformate(fileContent)
		return reformaetd.split("\n")

def WriteCss(content: str, fn: str = "./out.css", ) -> None:
	with open(fn, "w") as fp:
		fp.write(content)
		print(f"OUTPUT -> { fn }")

def joinLines(lines: list) -> str:
	return lines.join("\n")


def minify(fileName: "./styles.css"):
	for line in lines:
		# Algo.
		print(line)



def GetCssMapping1():
	t1 = getSize(getContent())
	lines = getlines()

	ob = {}
	css = """
	.Hello {
		padding: 10px;
	}

	.Yo {
		padding: 10px;	
	}
	"""
	selector = ""



	for line in css:
		line = line.strip()

		if '@' in line:
			if db["imports"]:
				ob["imports"].append(line)
			else:
				ob["imports"] = [line]

		elif '{' in line:
			selector = line.replace("{", "")
			ob[selector] = []

		elif "}" in line:
			selector = ""
		elif len(line) == 0:
			print("Empty line, progressing..")
			continue
		else:
			if ob[selector]:
				db[selector].append(line)
			else:
				print("Indefined selector!!!")


def GetCssMapping(css):
	""" gets all the selectors and styles and maps them """
	Mapping = {}

	for line in css:
		line = line.strip()

		if '@' in line:
			if "imports" in Mapping.keys():
				Mapping["imports"].append(line)
			else:
				Mapping["imports"] = [line]

		elif '{' in line:
			selector = line.replace("{", "")
			Mapping[selector] = []

		elif "}" in line:
			selector = ""
		elif len(line) == 0:
			print("Empty line, progressing..")
			continue
		else:
			if selector in Mapping.keys():
				Mapping[selector].append(line)
			else:
				print("Indefined selector!!!")
	return Mapping

def OptimizeMapping(Mapping):
	
	newStyle = []
	newKey = ""
	optimizedCss = {}

	for class_ in Mapping.keys():
		if class_ == "imports":
			optimizedCss[class_] = Mapping[class_]
			continue
		for key in Mapping.keys():
			if key == class_:
				break
			tempSyleSheet = [Mapping[class_], Mapping[key]]
			
			for style in Mapping[key]:
				if style in Mapping[class_]:
					tempSyleSheet[0].remove(style)
					tempSyleSheet[1].remove(style)
					newKey = ", ".join([key, class_])
					newStyle.append(style)
					if not newKey in optimizedCss.keys():
						optimizedCss[newKey] = newStyle
					else:
						optimizedCss[newKey].append(style)
			optimizedCss[class_] = tempSyleSheet[0]
			optimizedCss[key] = tempSyleSheet[1]
			newStyle = []

	return optimizedCss

def creatStyleSheetFromMapping(Mapping):
	style = ""
	for key in Mapping.keys():
		style += "".join([key, "{", *Mapping[key], "}"])
	return style


cssString = """
	@import ".css";
	.Hello {
		padding: 10px;
		margin: 10px 5px;
		display: block;
	}

	.Yo {
		padding: 10px;
		margin: 10px 2em;
		display: flex;
	}
	.foo {
		backgroud: red;
		display: flex;
	}
"""
bundle = ""

css = cssString.split("\n")



mapping1 = GetCssMapping(css)

pprint.pprint(mapping1)


opt = OptimizeMapping(mapping1)

pprint.pprint(opt)

newstyling = creatStyleSheetFromMapping(opt)

print(newstyling)

savedBytes = len(cssString) - len(newstyling)

Full =  len(cssString)


print(f"{savedBytes} BYTE was saved!! approximatly {(savedBytes * 100) / Full}%")
