#!/usr/bin/env python3
"""check_repo.py: quality gate for this repo. Run it before every commit.

  python3 tools/check_repo.py            all offline checks
  python3 tools/check_repo.py --online   also open every external link

Checks
  1. Writing: every markdown file passes slop_scan.py in strict mode (no HARD findings).
  2. Neutral: no personal names, brands or tool names in student files.
  3. Links: every relative link points to a file that exists.
  4. Frontmatter: skills and agents have a name and a description, names match files.
  5. Size: agent cards stay under 8,000 characters so they fit chat-tool instruction boxes.
  6. Questions: the 40 context questions appear word for word where they should.
"""

import argparse
import hashlib
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "skills", "anti-ai-slop-writing", "scripts"))
import slop_scan  # noqa: E402

SKIP_DIRS = {".git", "my-business", "node_modules", "__pycache__"}
TEXT_EXT = {".md", ".txt", ".py", ".json", ".yml", ".yaml"}

# Names, brands, products and outside people that must stay out of student files.
# Stored as SHA-256 hashes of the lowercase phrase (words joined by one space), so this
# file doesn't spell them out. To add one: python3 -c "import hashlib; print(hashlib.sha256(b'phrase').hexdigest())"
BLOCKED_HASHES = {
    "04020f5d5a91af496b8ec4707fd13fa11d5ac9cd35c7e1bac11bbe0d347434f3",
    "0a00c278cb9a4e7aaf5c9bb3a4378f3f0b71f0ca2da44fc7be9edafe6c3a1931",
    "16a0eeb0791b6c92451fd284dd9f599e0a7dbe7f6ebea6e2d2d06c7f74aec112",
    "16cc2fc0413e2b3d569f5465446e6dd0028d57eb85aae433618774f585abd9f0",
    "1ce102b9731fc76eaf080ff04a58f55e5de4c3afd5c8ec3a0029c8bc22f50a28",
    "1e6808a0fd427f3a1155c4fb02ac09f16b11538e73823a37f55b6b2c77876534",
    "1fd7d20f44ecc081503090764b4ddb056056bc66df6d46500b5c77832d091407",
    "248c65ea0a3bf79744f9ef2cad9477ebd460e8d49734ff6ad8ac20e2782d5003",
    "2af1ea3f8c5bfc376146b0bb9bc86b33eed5b091885df192d9157252051f998e",
    "2b1458726f4281c3e5987c4654b0695f999f83112347ca2ea3e9a12d3e23b89f",
    "2b36a6e663158ffd942c174de74dbe163bfdb1b18f6d0ffc647e00647abca9bb",
    "2c321fc12a4edf7a96b4558ea44954c1cf3e3d5d94005dcce858a37d4665ecb7",
    "2f9cb7cda5222087ae8774bc7a30bd0ac7de094e8aa354059072eece2217bbf8",
    "38c4f011587d01f6f49ac75a25359aaa0d256fa9f9f659b4dca022cb17e0b73e",
    "3987e8f923df69e1e5274036d8384db6d6c53fded54948a7e37d1bb5712df3f9",
    "3f433510b3b6c24322388c7ab736fd68f9ee80d065c75c9bc50fd13412e624d4",
    "403dd2f5a78a46e17e7d9d6d6807e8ef120c80dadb533c5d99df137bc67f4d4e",
    "435945dd1eaf3d9aca9f0daf703b7058b85b198e94cd6dc4e0f110101824b27c",
    "636ee37e8db4202e9d7f5ddbbc6c58aeb0aa9abda85ca969b41a46911095816a",
    "82c1f6391b987358909ad810ab2a9470bc7a720a3c8a3a46d7a2a3e4fbd14df8",
    "8f308606012e2ddde9c7a8e8b90c56a748b9c10835329c81c0a97fe89de70bd0",
    "947fb857fc480deb9057010f2453905b253e19f883dda37687af85bc6d73d192",
    "983f47b3080502d40b8d477e532f13f12c9e65eef2b3dabcb3d76ac804e3be13",
    "a4413ce46a6b5dfeca48bf4820780368d321451f871bf7f0626b31e039904083",
    "a8e10fe13a65fed6b88e4749706d073e5c315347a8d20a1ba4a438847e287bcf",
    "c697b854a4d3b277a2c2984dec33cbd758b7eafbc89700449b448ab1f360435e",
    "c6996ebcad8e053b7d3e866c341c14827b710d77cbd906a052ab2d92cfbf14cf",
    "ccedd614a7f6bd1d39ec701b47314fe3416824ee9395b085d21ef4cf26025fed",
    "d664f8d0dec09c35fdcca2a67bf8f0c6d2ab85f845d0c9547d4d0d360f071f0b",
    "d79059c6efd7e41920f52bcefc0f660ec31cc08f3c463f258e06c5e96c2230b2",
    "dda820158d142a0b73380cd3efa9ff7d9fa11336e9ba4b3693098964537d61a3",
    "de5de6b4ad606c9da43cc82e6bc78c90fec6c118af6386ab46c44b3e44227b18",
    "e794778fc11cfb70e3b7e8c11548423c4b70d60c5eb5a7a474b57c0f410279f8",
    "e8d00e4af5a28e10dacb085d1107171a212a8a6e267aa5d00ed04aee7d0885b4",
    "ec87d0e0735ce8d20ddf792630a066ab99a7e3370281adc2eba9c3192033ff7f",
    "f0f31656ed98d08be5a2025b2dab44a48a72e786525f98a155c1594d037aba9d",
}
# Only these two root files may carry the author credit, and only the name itself is exempt.
CREDIT_FILES = {"README.md", "LICENSE"}
CREDIT_HASH = "16cc2fc0413e2b3d569f5465446e6dd0028d57eb85aae433618774f585abd9f0"
# Plain words the writing rules avoid.
BANNED = [r"\bscrap(e|es|ed|ing|er|ers)\b", r"\bcrawl(s|ed|ing|er|ers)?\b"]
WORD_RE = re.compile(r"[a-z0-9]+")

QUESTIONS = [
    "What's your name?",
    "What's the business/brand name for this offer?",
    "What's your industry and sub-niche?",
    "Who do you want your customers to see you as?",
    "Describe your brand in 3-5 words:",
    "What's the goal of this specific project?",
    "What's the offer name?",
    "What's included in the offer?",
    "How much does the offer cost?",
    "What's the problem you solve?",
    "What are the pain points they experience due to the problem?",
    "What's the promised outcome?",
    "What are the direct and in-direct results in their life after your solution?",
    "Describe your offer in a 1 line elevator pitch:",
    "What are 3 credibility factors that make you a trusted authority?",
    "What are some strong opinions you have that reflect your brand?",
    "What's your epiphany/backstory that led you here?",
    "What are your biggest wins that help build trust?",
    "What's the process to getting the outcome?",
    "What have they tried before that didn't work and why?",
    "What's the \"new opportunity\" they haven't tried yet?",
    "How and why is your solution unique to them?",
    "Who's the perfect customer avatar?",
    "What are common values for your dream customers?",
    "What's a common enemy you both have?",
    "What's currently holding them back?",
    "What are some limiting beliefs they have around your offer?",
    "What are some limiting beliefs they have about themselves?",
    "What are some limiting beliefs they have about effort/time needed?",
    "What are some limiting beliefs they have around investing in this?",
    "What's the opportunity cost of inaction and staying the same?",
    "Who are they comparing you to and how is this different?",
    "Are you doing a special live launch deal or straight to evergreen?",
    "What makes this a no-brainer deal if they act right now?",
    "Who are your competitors?",
    "What softwares do you currently use for your websites, landing pages and funnels?",
    "How do you want your visual brand identity to look and feel?",
    "Do you currently have any images, brand assets, visual guides or logos we should use?",
    "Do you have any reviews or testimonials we can use?",
    "Anything else you think is important to know or include?",
]
QUESTION_FILES = ["setup/40-context-questions.md", "skills/context-interview/SKILL.md", "chat/SETUP-PROMPT.md"]

LINK_RE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
URL_RE = re.compile(r"https?://[^\s)<>\]\"'`]+")


def walk():
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            path = os.path.join(dp, fn)
            if os.path.splitext(fn)[1] in TEXT_EXT or fn in {"LICENSE", ".gitignore"}:
                yield path


def rel(p):
    return os.path.relpath(p, ROOT)


def blocked_phrases(text):
    """Yield (line, phrase, hash) for every 1 to 3 word phrase on the blocked list."""
    low = text.lower()
    words = [(m.group(0), m.start()) for m in WORD_RE.finditer(low)]
    for size in (1, 2, 3):
        for i in range(len(words) - size + 1):
            phrase = " ".join(w for w, _ in words[i:i + size])
            digest = hashlib.sha256(phrase.encode()).hexdigest()
            if digest in BLOCKED_HASHES:
                yield low.count("\n", 0, words[i][1]) + 1, phrase, digest


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="hide REVIEW notes")
    args = ap.parse_args()

    errors, warnings, external = [], [], set()
    scan_args = argparse.Namespace(keep=[], allow_dashes=False, scan_quotes=False, strict=True)

    for path in walk():
        r = rel(path)
        text = open(path, encoding="utf-8").read()

        # 2. neutral wording
        for pat in BANNED:
            if r == "tools/check_repo.py":
                break
            for m in re.finditer(pat, text, re.IGNORECASE):
                line = text[: m.start()].count("\n") + 1
                errors.append(f"{r}:{line} banned term '{m.group(0)}'")
        for line, phrase, digest in blocked_phrases(text):
            if digest == CREDIT_HASH and r in CREDIT_FILES:
                continue
            errors.append(f"{r}:{line} name, brand or product that belongs out of student files: '{phrase}'")

        if r.endswith(".md"):
            # 1. writing
            findings, _ = slop_scan.scan_text(text, scan_args)
            for f in findings:
                if f["severity"] == "HARD":
                    errors.append(f"{r}:{f['line']} {f['category']}: {f['match']}")
                elif f["severity"] == "REVIEW" and not args.quiet:
                    warnings.append(f"{r}:{f['line']} {f['category']}: {f['match']}")
            # 3. links
            for m in LINK_RE.finditer(text):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:")):
                    external.add(target)
                    continue
                if target.startswith("#"):
                    continue
                file_part = target.split("#", 1)[0]
                if not file_part:
                    continue
                dest = os.path.normpath(os.path.join(os.path.dirname(path), file_part))
                if not os.path.exists(dest):
                    line = text[: m.start()].count("\n") + 1
                    errors.append(f"{r}:{line} broken link -> {target}")
            for u in URL_RE.findall(text):
                external.add(u.rstrip(".,;:"))

        # 4. frontmatter
        parts = r.split(os.sep)
        if len(parts) == 3 and parts[0] == "skills" and parts[2] == "SKILL.md":
            fm = frontmatter(text)
            if not fm or not fm.get("name") or not fm.get("description"):
                errors.append(f"{r} missing name or description in frontmatter")
            elif fm["name"] != parts[1]:
                errors.append(f"{r} name '{fm['name']}' does not match folder '{parts[1]}'")
        if len(parts) == 2 and parts[0] == "agents" and re.match(r"^\d\d-", parts[1]):
            fm = frontmatter(text)
            if not fm or not fm.get("name") or not fm.get("description"):
                errors.append(f"{r} missing name or description in frontmatter")
            elif fm["name"] != parts[1][3:-3]:
                errors.append(f"{r} name '{fm['name']}' does not match file name")
            # 5. size
            if len(text) > 8000:
                errors.append(f"{r} is {len(text)} characters (limit 8,000 for chat instructions)")

    # 6. questions
    for qf in QUESTION_FILES:
        p = os.path.join(ROOT, qf)
        if not os.path.exists(p):
            errors.append(f"{qf} missing")
            continue
        t = open(p, encoding="utf-8").read()
        for q in QUESTIONS:
            if q not in t:
                errors.append(f"{qf} is missing the question: {q}")

    if args.online:
        for u in sorted(external):
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 repo-check"})
                with urllib.request.urlopen(req, timeout=20) as resp:
                    code = resp.status
            except Exception as e:  # noqa: BLE001
                code = getattr(e, "code", str(e))
            if code != 200:
                errors.append(f"external link {u} returned {code}")

    for w in warnings:
        print("REVIEW", w)
    for e in errors:
        print("ERROR ", e)
    print(f"\n{len(errors)} errors, {len(warnings)} review notes, {len(external)} external links")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
