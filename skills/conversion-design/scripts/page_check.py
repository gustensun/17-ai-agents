#!/usr/bin/env python3
"""page_check.py: the checks of the hierarchy test that can be read from code.

  python3 skills/conversion-design/scripts/page_check.py page.html
  python3 skills/conversion-design/scripts/page_check.py https://example.com/page
  python3 skills/conversion-design/scripts/page_check.py --funnel page.html      one page, one action
  python3 skills/conversion-design/scripts/page_check.py --ship page.html        brackets block the launch
  python3 skills/conversion-design/scripts/page_check.py page.html extra.css     add CSS files by hand
  python3 skills/conversion-design/scripts/page_check.py contrast "#ffffff" "#111111"

It reads the HTML, its <style> blocks and the stylesheets it links to. It can't see the
rendered page, so the squint test and the look at 390px and 1440px still need a screenshot.
Exit code 1 while any FAIL remains. Python 3 standard library only.
"""

import argparse
import os
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SKIP_TEXT = {"script", "style", "noscript", "template", "svg", "head"}
WEAK_CTA = {"submit", "learn more", "click here", "read more", "more", "click", "go", "here"}
EYEBROW_CLASS = re.compile(r"(eyebrow|kicker|overline|pre-?title|super-?title|pretitle|label-top)", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U0001F1E6-\U0001F1FF]")
SYMBOL = re.compile("[\U00002600-\U000027BF]")
BRACKET = re.compile(r"\[[A-Z][A-Z0-9 :,./'&%$+()-]{1,80}\]")
GENERIC_FONTS = {
    "serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "ui-sans-serif", "ui-serif",
    "ui-monospace", "ui-rounded", "-apple-system", "blinkmacsystemfont", "segoe ui", "helvetica neue",
    "helvetica", "arial", "georgia", "times new roman", "inherit", "initial", "unset", "emoji",
    "apple color emoji", "segoe ui emoji", "noto color emoji", "courier new", "menlo", "consolas",
}
DEFAULT_LOOK = {"inter", "roboto", "open sans", "arial", "helvetica"}


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []  # Node or str

    def text(self):
        out = []
        for c in self.children:
            if isinstance(c, str):
                out.append(c)
            elif c.tag not in SKIP_TEXT:
                out.append(c.text())
        return re.sub(r"\s+", " ", " ".join(out)).strip()

    def classes(self):
        return self.attrs.get("class", "") or ""


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def walk(node):
    for c in node.children:
        if isinstance(c, Node):
            yield c
            yield from walk(c)


def visible_text(node):
    parts = []
    for c in node.children:
        if isinstance(c, str):
            parts.append(c)
        elif c.tag not in SKIP_TEXT:
            parts.append(visible_text(c))
    return " ".join(parts)


def read_source(src):
    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0 page-check"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "ignore")
    with open(src, encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb):
    def ch(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(hex_to_rgb(a)), luminance(hex_to_rgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def font_primaries(css, html):
    fams = set()
    stacks = re.findall(r"font-family\s*:\s*([^;}{]+)", css, re.I)
    stacks += [v for v in re.findall(r"--[\w-]+\s*:\s*([^;}{]+)", css)
               if re.search(r"\b(serif|sans-serif|monospace|system-ui)\b", v)]
    for st in stacks:
        first = st.split(",")[0].strip().strip("'\"").lower()
        if first and not first.startswith("var(") and first not in GENERIC_FONTS:
            fams.add(first)
    for fam in re.findall(r"fonts\.googleapis\.com/css2?\?([^\"'>]+)", html):
        for name in re.findall(r"family=([^&:;\"']+)", fam):
            fams.add(urllib.parse.unquote_plus(name).strip().lower())
    return fams


def check(src, extra_css, funnel, ship):
    html = read_source(src)
    b = Builder()
    b.feed(html)
    root = b.root
    nodes = list(walk(root))
    css_parts = [n.text() for n in nodes if n.tag == "style"]
    for n in nodes:
        if n.tag == "link" and "stylesheet" in (n.attrs.get("rel") or "") and n.attrs.get("href"):
            href = n.attrs["href"]
            if src.startswith(("http://", "https://")):
                target = urllib.parse.urljoin(src, href)
            elif href.startswith(("http://", "https://", "//")):
                continue
            else:
                target = os.path.join(os.path.dirname(os.path.abspath(src)), href.split("?")[0])
            try:
                css_parts.append(read_source(target))
            except Exception:  # noqa: BLE001
                pass
    for f in extra_css:
        css_parts.append(read_source(f))
    css = "\n".join(css_parts)

    out = []  # (severity, check, message)

    def add(sev, name, msg):
        out.append((sev, name, msg))

    # Document basics
    if not any(n.tag == "meta" and (n.attrs.get("name") or "").lower() == "viewport" for n in nodes):
        add("FAIL", "viewport", "No viewport meta tag, so phones show a zoomed-out desktop page. Add "
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> to the head.")
    html_tag = next((n for n in nodes if n.tag == "html"), None)
    if html_tag is not None and not html_tag.attrs.get("lang"):
        add("WARN", "lang", "The <html> tag has no lang attribute. Add one, for example lang=\"en\".")
    if not any(n.tag == "title" and n.text() for n in nodes):
        add("WARN", "title", "No page title. Add a <title> that names the offer.")
    if not any(n.tag == "meta" and (n.attrs.get("name") or "").lower() == "description" for n in nodes):
        add("WARN", "description", "No meta description. Add one sentence that says what the page offers.")

    # Headings
    heads = [n for n in nodes if re.fullmatch(r"h[1-6]", n.tag)]
    h1s = [h for h in heads if h.tag == "h1"]
    if len(h1s) != 1:
        add("FAIL", "h1-count", f"Found {len(h1s)} <h1> elements. Keep exactly one H1: the main promise "
            "of the page. Turn any others into H2.")
    last = 0
    for h in heads:
        lvl = int(h.tag[1])
        if last and lvl > last + 1:
            add("FAIL", "heading-order", f"<{h.tag}> \"{h.text()[:60]}\" skips a level after <h{last}>. "
                f"Use <h{last + 1}> or restyle with CSS.")
        last = lvl
        t = h.text()
        if "!" in t:
            add("WARN", "heading-exclamation", f"Heading \"{t[:60]}\" has an exclamation mark. Let the words "
                "carry it.")

    # Eyebrow labels above headings
    upper_classes = set()
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        if re.search(r"text-transform\s*:\s*uppercase", body, re.I):
            upper_classes.update(re.findall(r"\.([\w-]+)", sel))
    for h in heads:
        if h.tag not in ("h1", "h2") or h.parent is None:
            continue
        sibs = [c for c in h.parent.children if isinstance(c, Node) or (isinstance(c, str) and c.strip())]
        i = sibs.index(h)
        if i == 0:
            continue
        prev = sibs[i - 1]
        if not isinstance(prev, Node) or prev.tag in ("img", "picture", "svg", "figure", "video", "a", "button"):
            continue
        pt = prev.text()
        cls = prev.classes()
        words = len(pt.split())
        caps = pt.isupper() and len(pt) >= 3
        styled_caps = any(c in upper_classes for c in cls.split())
        if pt and words <= 6 and (EYEBROW_CLASS.search(cls) or caps or styled_caps):
            add("FAIL", "eyebrow", f"A small label \"{pt[:40]}\" sits above the heading \"{h.text()[:50]}\". "
                "Delete the label and let the heading carry the section. On the hero, a pre-headline that "
                "calls out the reader in a full phrase can stay.")

    # Visible text checks
    body = next((n for n in nodes if n.tag == "body"), root)
    vt = visible_text(body)
    if "\u2014" in vt or re.search(r"(?<!\d)\u2013|\u2013(?!\d)", vt):
        sample = re.search(r".{0,30}[\u2014\u2013].{0,30}", vt)
        add("FAIL", "dash", f"Em or en dash in the copy (\"{sample.group(0).strip() if sample else ''}\"). "
            "Rewrite with a full stop, comma, colon or brackets. Ranges use a hyphen: 3-5.")
    if EMOJI.search(vt):
        add("FAIL", "emoji", "Emoji in the page text. Use one icon set with one stroke weight, or no icons.")
    sym = sorted(set(SYMBOL.findall(vt)))
    if sym:
        add("WARN", "symbols", f"Text symbols used as graphics ({' '.join(sym[:6])}). Icons come from one drawn "
            "set. Star ratings appear only with a real, named source.")
    if "{{" in html:
        add("FAIL", "leftover", "A {{variable}} was never filled. Fill it or turn it into a [BRACKET] the "
            "owner can see.")
    nums = sorted({t for t in re.findall(r"(?<![\w/])0[1-9](?![\w%])", vt)})
    if len(nums) >= 3:
        add("WARN", "section-numbers", f"Numbers like {', '.join(nums[:4])} look like decorative section "
            "numbers. Keep them only if the order matters to the reader.")
    brackets = sorted(set(BRACKET.findall(vt)))
    if brackets:
        sev = "FAIL" if ship else "INFO"
        add(sev, "brackets", f"{len(brackets)} placeholder(s) still need real facts: {', '.join(brackets[:12])}"
            + (" ..." if len(brackets) > 12 else "") + ". Fill each one from the Brain or the owner before launch.")

    # Buttons and calls to action
    ctas = []
    for n in nodes:
        cls = n.classes().lower()
        is_btn = n.tag == "button" or (n.tag == "a" and re.search(r"\b(btn|button|cta)", cls))
        if n.tag == "input" and (n.attrs.get("type") or "").lower() == "submit":
            label = (n.attrs.get("value") or "submit").strip()
            if label.lower() in WEAK_CTA:
                add("FAIL", "weak-cta", f"A button says \"{label}\". Use a verb plus what they get, "
                    "for example \"Get the checklist\" or \"Book my call\".")
            continue
        if not is_btn:
            continue
        label = n.text() or n.attrs.get("aria-label", "")
        if label.strip().lower().rstrip(".") in WEAK_CTA:
            add("FAIL", "weak-cta", f"A button says \"{label.strip()}\". Use a verb plus what they get, "
                "for example \"Get the checklist\" or \"Book my call\".")
        if n.tag == "a":
            href = (n.attrs.get("href") or "").strip()
            inside_nav = False
            p = n.parent
            while p is not None:
                if p.tag in ("nav", "header", "footer"):
                    inside_nav = True
                    break
                p = p.parent
            if href and not inside_nav and not href.startswith("#"):
                ctas.append(href)
    dests = sorted(set(ctas))
    if len(dests) > 1:
        sev = "FAIL" if funnel else "WARN"
        add(sev, "one-action", f"Buttons go to {len(dests)} different places: {', '.join(dests[:6])}. "
            "A funnel page has one job: point every main button at the same next step and turn the rest "
            "into text links or remove them.")
    if funnel:
        for n in nodes:
            if n.tag == "nav" and sum(1 for c in walk(n) if c.tag == "a") >= 3:
                add("WARN", "nav", "This funnel page has a navigation menu. Hide nav links on funnel pages so "
                    "the only way forward is the main button.")
                break

    # Images
    for n in nodes:
        if n.tag != "img":
            continue
        srcname = (n.attrs.get("src") or "")[-40:]
        if "alt" not in n.attrs:
            add("FAIL", "alt", f"Image {srcname} has no alt attribute. Describe it, or use alt=\"\" if it's "
                "pure decoration.")
        style = n.attrs.get("style") or ""
        if not (n.attrs.get("width") and n.attrs.get("height")) and "aspect-ratio" not in style:
            add("WARN", "image-size", f"Image {srcname} has no width and height, which makes the page jump "
                "while it loads. Set both, or an aspect-ratio.")

    # Form labels
    label_for = {n.attrs.get("for") for n in nodes if n.tag == "label"}
    for n in nodes:
        if n.tag not in ("input", "select", "textarea"):
            continue
        typ = (n.attrs.get("type") or "text").lower()
        if typ in ("hidden", "submit", "button", "image", "reset"):
            continue
        has = n.attrs.get("id") in label_for or n.attrs.get("aria-label") or n.attrs.get("aria-labelledby")
        p = n.parent
        while not has and p is not None:
            if p.tag == "label":
                has = True
            p = p.parent
        if not has:
            name = n.attrs.get("name") or n.attrs.get("id") or typ
            add("FAIL", "label", f"The field \"{name}\" has no visible label. Add a <label for> above it. "
                "Placeholder text is never the label.")

    # CSS: decoration and fonts
    if re.search(r"background-clip\s*:\s*text", css, re.I):
        add("FAIL", "gradient-text", "Gradient text found (background-clip: text). Use weight or size for "
            "emphasis.")
    if re.search(r"backdrop-filter\s*:\s*blur", css, re.I):
        add("WARN", "glass", "backdrop-filter blur found. Keep it only where it does a job (a sticky bar over "
            "photos), never as decoration on cards.")
    fams = font_primaries(css, html)
    if len(fams) > 2:
        add("WARN", "fonts", f"{len(fams)} font families: {', '.join(sorted(fams))}. Use 2 at most: one "
            "display, one text. A monospace for data is fine if the Style Block names it.")
    plain = sorted(fams & DEFAULT_LOOK)
    if plain:
        add("WARN", "default-font", f"{', '.join(plain)} is a default look. Check the headline uses the "
            "display font from the Style Block.")

    # Token contrast (only tokens set on :root, html or body, so component tokens don't mislead)
    root_css = " ".join(body for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css)
                        if re.search(r"(^|[\s,]):root\b|(^|[\s,])html\b|(^|[\s,])body\b", sel.strip()))
    tokens = {k.lower(): v for k, v in re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", root_css)}
    pairs = [(bg, fg) for bg in ("--bg", "--paper", "--background", "--surface")
             for fg in ("--ink", "--text", "--fg", "--foreground") if bg in tokens and fg in tokens]
    pairs += [("--accent", fg) for fg in ("--accent-ink", "--accent-text", "--on-accent", "--accent-fg")
              if "--accent" in tokens and fg in tokens]
    for bg, fg in pairs:
        try:
            r = contrast(tokens[bg], tokens[fg])
        except ValueError:
            continue
        if r < 4.5 and bg == "--accent":
            add("WARN", "contrast", f"{fg} on {bg} is {r:.2f}:1. If {fg} is the text colour on the main "
                "button (as in the Style Block), it needs 4.5:1. If it's a darker shade for hover, ignore this.")
        elif r < 4.5:
            add("FAIL", "contrast", f"{fg} on {bg} is {r:.2f}:1. Body text needs 4.5:1. Darken or lighten "
                "the token and recheck.")
        else:
            add("INFO", "contrast", f"{fg} on {bg} is {r:.2f}:1 (passes AA).")

    # Skim test outline
    outline = [f"{h.tag.upper()} {h.text()[:90]}" for h in heads if h.tag in ("h1", "h2")]
    return out, outline


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "contrast":
        if len(sys.argv) != 4:
            print("Usage: page_check.py contrast \"#ffffff\" \"#111111\"")
            return 2
        try:
            r = contrast(sys.argv[2], sys.argv[3])
        except ValueError:
            print("Use hex colours like #1a4be0 or #fff.")
            return 2
        verdict = "passes AA for body text" if r >= 4.5 else (
            "passes AA for large text only (24px, or 19px bold)" if r >= 3 else "fails AA")
        print(f"{r:.2f}:1, {verdict}.")
        return 0 if r >= 4.5 else 1

    ap = argparse.ArgumentParser(description="Code-level checks from the hierarchy test.")
    ap.add_argument("page", help="HTML file or URL")
    ap.add_argument("css", nargs="*", help="extra CSS files")
    ap.add_argument("--funnel", action="store_true", help="one page, one action: competing buttons FAIL")
    ap.add_argument("--ship", action="store_true", help="leftover [BRACKETS] FAIL")
    args = ap.parse_args()
    try:
        out, outline = check(args.page, args.css, args.funnel, args.ship)
    except FileNotFoundError:
        print(f"Can't find {args.page}. Pass the path to the built HTML file, for example dist/index.html, "
              "or a live URL.")
        return 2
    except Exception as e:  # noqa: BLE001
        print(f"Couldn't read {args.page} ({e}). If it's a URL, open it in a browser to check it loads, "
              "or save the page as HTML and pass the file.")
        return 2
    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    print(args.page)
    groups = {}
    for sev, name, msg in sorted(out, key=lambda x: order[x[0]]):
        groups.setdefault((sev, name), []).append(msg)
    for (sev, name), msgs in groups.items():
        for msg in msgs[:3]:
            print(f"  {sev:<4}  {name}: {msg}")
        if len(msgs) > 3:
            print(f"  {sev:<4}  {name}: {len(msgs) - 3} more like this.")
    if outline:
        print("  Skim test (read these in order; they should tell the whole argument):")
        for line in outline:
            print(f"        {line}")
    fails = sum(1 for o in out if o[0] == "FAIL")
    warns = sum(1 for o in out if o[0] == "WARN")
    tail = ("Fix every FAIL, then do the screenshot checks in the hierarchy test."
            if fails else "No code-level fails. Now do the screenshot checks in the hierarchy test.")
    print(f"  Summary: {fails} FAIL, {warns} WARN. {tail}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
