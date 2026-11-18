"""make.fun news-image-20261118 entry, wallet 6: infographic collage.

The bundled picture is a nine-card infographic of Wednesday
18 November 2026: the Gulf escalation (Qeshm strike, drones on Bahrain
and Kuwait), the Kerch Bridge hit, APEC in Shenzhen, the Quad in
Manila, Ebola in DR Congo, the US losing measles-free status, the
Siberia plane crash, cyclones and a quake, and the market slide.
This program publishes that picture byte for byte.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
EXPECTED_SHA_PREFIX = ""


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(8192), b""):
            h.update(block)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    payload_size = os.path.getsize(SOURCE)
    if payload_size == 0 or payload_size > 1048576:
        raise ValueError("infographic size out of bounds: %d" % payload_size)
    shutil.copyfile(SOURCE, target)
    if digest(SOURCE) != digest(target):
        raise IOError("copy mismatch for w6 infographic entry")
    print("w6 infographic collage published:", os.path.getsize(target), "bytes")


STORIES_W6 = [
    ("gulf", "US strike on Qeshm Island; Iran drones Bahrain and Kuwait"),
    ("crimea", "Kerch Bridge span falls after second Ukrainian strike"),
    ("apec", "Xi hosts APEC in Shenzhen; Putin arrives; Trump talks Thu"),
    ("quad", "Trump Modi Albanese Takaichi meet in Manila"),
    ("ebola", "DR Congo outbreak doubles to 11000 cases 5400 deaths"),
    ("measles", "United States loses measles elimination status"),
    ("crash", "Russian military plane down in Siberia, 19 dead"),
    ("storm", "Cyclone Xavier Cat5 Cook Islands; PNG quake 6.0"),
    ("markets", "Stocks slide; gold 3775 dollars; Brent 91.55 dollars"),
]


def describe_w6():
    lines = []
    for slug, headline in STORIES_W6:
        lines.append(slug.upper() + ": " + headline)
    return lines


def validate_w6(path):
    size = os.path.getsize(path)
    if size <= 0:
        raise IOError("empty infographic payload")
    return {"stories": len(STORIES_W6), "bytes": size, "date": "2026-11-18"}


if __name__ == "__main__":
    for line in describe_w6():
        print(line)
    print(validate_w6(SOURCE))
    main()
