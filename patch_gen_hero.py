import sys

with open("D:/Cybersecurity/uziii2208/scripts/gen_hero.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace colors
content = content.replace('DARK_PURPLE = "#A78BFA"', 'DARK_PURPLE = "#FFFFFF"')
content = content.replace('LIGHT_PURPLE = "#7C3AED"', 'LIGHT_PURPLE = "#FFFFFF"')

# Replace ticker messages
old_ticker_msgs = """TICKER_MESSAGES = [
    "devsecops",
    "devops intern — 7 sep 2026 to 5 mar 2027",
    "uitm shah alam · final year computer science (hons)",
    "self-hosts everything, no open inbound ports",
    "open to freelance work",
]"""
new_ticker_msgs = """TICKER_MESSAGES = [
    "security researcher",
    "vulnerability hunter",
    "chasing CVEs one bug at a time",
    "white hat · open source",
    "Hyperdope AI",
]"""
content = content.replace(old_ticker_msgs, new_ticker_msgs)

# Replace ticker colors
content = content.replace('TICKER_INK = "#EDE6FF"', 'TICKER_INK = "#FFFFFF"')
content = content.replace('TICKER_GROUND = "#050409"', 'TICKER_GROUND = "#000000"')
content = content.replace('TICKER_EDGE = "#2A2440"', 'TICKER_EDGE = "#333333"')
content = content.replace('TICKER_MID = "#D6C4FF"', 'TICKER_MID = "#AAAAAA"')
content = content.replace('TICKER_BLOOM = "#7C3AED"', 'TICKER_BLOOM = "#FFFFFF"')

# Replace main references
old_main = """def main():
    model = build_model(read_art("ascii-art.txt"))
    wordmark = read_art("syamxm.txt")

    write("hero-dark.svg", build_spinner(model, DARK_PURPLE, "syamxm logo, rotating"))
    write("hero-light.svg", build_spinner(model, LIGHT_PURPLE, "syamxm logo, rotating"))
    write("wordmark-dark.svg", build_wordmark(wordmark, DARK_PURPLE, "SYAMXM"))
    write("wordmark-light.svg", build_wordmark(wordmark, LIGHT_PURPLE, "SYAMXM"))
    write("ticker.svg", build_ticker(TICKER_MESSAGES, "status ticker"))"""

new_main = """def main():
    model = build_model(read_art("ascii-art.txt"))
    wordmark = read_art("uziii2208.txt")

    write("hero-dark.svg", build_spinner(model, DARK_PURPLE, "uziii2208 logo, rotating"))
    write("hero-light.svg", build_spinner(model, LIGHT_PURPLE, "uziii2208 logo, rotating"))
    write("wordmark-dark.svg", build_wordmark(wordmark, DARK_PURPLE, "UZIII2208"))
    write("wordmark-light.svg", build_wordmark(wordmark, LIGHT_PURPLE, "UZIII2208"))
    write("ticker.svg", build_ticker(TICKER_MESSAGES, "status ticker"))"""

content = content.replace(old_main, new_main)

with open("D:/Cybersecurity/uziii2208/scripts/gen_hero.py", "w", encoding="utf-8") as f:
    f.write(content)
