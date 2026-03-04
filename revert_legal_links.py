import sys

filepath = "src/pages/index.astro"
with open(filepath, "r") as f:
    text = f.read()

# Replace only the legal links back to absolute
text = text.replace('href="/impressum"', 'href="https://www.ikasi-bodywork.com/impressum"')
text = text.replace('href="/datenschutz"', 'href="https://www.ikasi-bodywork.com/datenschutz"')
text = text.replace('href="/rechtliches"', 'href="https://www.ikasi-bodywork.com/rechtliches"')
text = text.replace('href="/agbs"', 'href="https://www.ikasi-bodywork.com/agbs"')
text = text.replace('href="/widerruf"', 'href="https://www.ikasi-bodywork.com/widerruf"')

with open(filepath, "w") as f:
    f.write(text)

print("Reverted legal links.")
