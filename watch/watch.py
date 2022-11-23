import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if '<' not in s:
        return None
    else:
        if matches := re.search(r'(https?)(://)?(www\.)?''(youtube|youtu|youtube-nocookie)\.(com|be)/''(watch\?v=|embed/|v/|.+\?v=)?([^&=%]{11})', s):
            if 's' not in matches.group(1):
                w1 = matches.group(1) + 's' + matches.group(2)
            else:
                w1 = matches.group(1) + matches.group(2)

            w2 = matches.group(4)
            w3 = matches.group(7)
            res = w1 + f"{w2[:-2]}.be" + f'/{w3}'
            return res



if __name__ == "__main__":
    main()