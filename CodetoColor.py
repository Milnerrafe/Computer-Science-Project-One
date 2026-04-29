import os
import tempfile
import webbrowser

filename = input("Enter the file name:")


with open(filename, "r") as file:
    text = file.read()


hex_output = text.encode("utf-8").hex()
n = 6
chunks = [hex_output[i : i + n] for i in range(0, len(hex_output), n)]


svgarray = []

numberRuning = 0
numberSet = 1 / len(chunks)

interration = 0

for i in chunks:
    interration += 1
    numberRuning += numberSet

    if interration == 1:
        svgarray.append(f'<stop stop-color="#{i}"/>')
    else:
        svgarray.append(f'<stop offset="{numberRuning}" stop-color="#{i}"/>')


svgcode = "/n".join(svgarray)

svg = f"""

<svg width="532" height="274" viewBox="0 0 532 274" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="532" height="274" fill="url(#paint0_linear_1_2)"/>
<defs>
<linearGradient id="paint0_linear_1_2" x1="532" y1="137" x2="0" y2="137" gradientUnits="userSpaceOnUse">
{svgcode}
</linearGradient>
</defs>
</svg>


"""


with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
    f.write(svg)
    file_url = "file://" + os.path.abspath(f.name)

webbrowser.open(file_url)
