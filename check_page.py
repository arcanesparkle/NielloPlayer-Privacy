#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NielloPlayer 隐私政策页面 · 结构与移动端契约判据

## 为什么会有这个脚本（2026-11-02）

线上页 `https://arcanesparkle.github.io/NielloPlayer-Privacy/` 是 Play 审核与
应用内 Custom Tabs **唯一的**展现端（`doc/defects/2026-11-02-privacy-policy-online-only.md`）。
这一轮用户报了两件事：

  1. 「目录点击咋不能跳转到对应的地方」—— 实测：16 个目录项全是 `<li>文本</li>`，
     **没有 `<a>`**；16 个 `<h2>` **没有 `id`**。点击 `scrollY 0 -> 0`、`hash` 为空。
  2. 「移动端兼容性做好了吗」—— 横向溢出确实没有（12 语言 × 320~414 共 60 组全为 0），
     但有三处真问题：`<select>` 字号 14px（iOS 聚焦会放大整页）、无 `safe-area-inset`
     （刘海/横屏遮挡）、无 `-webkit-text-size-adjust`。

修完之后，**这套契约没有任何东西在守着** —— 它是 HTML 里 192 处重复结构，改文案时
最容易「顺手简化」掉。于是把要求写成这里。

## 钉六条

| 编号 | 断言 | 为什么 |
|---|---|---|
| H1 | 12 个 `<section data-lang>`，每节 16 个章节 `<h2 id>` | 12 语言 × 16 节是产品承诺；少一节就是少一句法律说明 |
| H2 | 目录项是 `<a href="#...">`，不是纯文本 | 用户报的原始缺陷 |
| H3 | 每个 href 都能找到 id，且 **id 全局唯一** | 12 份同名 id 会让锚点命中 `display:none` 的那份 ⇒ 点了没反应 |
| H4 | 每节的 href 与 h2 的 id **同序同名** | 目录第 5 项必须指向第 5 节，不能整体错位 |
| H5 | 移动端契约：`viewport-fit=cover` / `safe-area-inset` / `scroll-margin-top` / `-webkit-text-size-adjust` / `prefers-reduced-motion` | 这几条是这一轮的修复内容，删掉任何一条都会静默退回旧观感 |
| H6 | `PRIVACY.md` 的目录每项都是链接，且数量 = 章节数 | 同一份政策的 md 副本在 GitHub 上展示，同一个缺陷形状 |

## 用法

    python check_page.py            # 0 全过 / 1 有不成立 / 2 环境错误
    python check_page.py --selftest # 阴性对照：逐条改坏，必须变红
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
HTML = REPO / "index.html"
MD = REPO / "PRIVACY.md"

LANGS = ["en", "zh", "zh-Hant", "ar", "da", "nl", "fr", "de", "ja", "ko", "no", "sv"]
SECTIONS = 16

MOBILE_CSS = [
    ("viewport-fit=cover", "iOS 刘海/圆角安全区"),
    ("safe-area-inset-left", "横屏时内容不被圆角裁掉"),
    ("-webkit-text-size-adjust", "iOS 横屏自动放大文字"),
    ("scroll-margin-top", "锚点跳转后标题不被顶边贴住"),
    ("prefers-reduced-motion", "尊重「减少动态效果」（平滑滚动必须能关）"),
    ("theme-color", "移动浏览器地址栏配色与页面一致"),
]


def run(html: str, md: str) -> list[tuple[str, bool, str]]:
    out: list[tuple[str, bool, str]] = []

    def add(name: str, ok: bool, detail: str = "") -> None:
        out.append((name, ok, detail))

    # ── H1 结构 ────────────────────────────────────────────────────────
    starts = [m.start() for m in re.finditer(r'<section data-lang="', html)]
    ends = [m.start() for m in re.finditer(r"</section>", html)]
    add("H1a 有 12 个 <section data-lang>", len(starts) == 12, f"实际 {len(starts)}")
    found = re.findall(r'<section data-lang="([^"]+)"', html)
    add("H1b 语言集合与语言选择器一致", found == LANGS, f"{found}")

    blocks = []
    for i in range(len(starts) - 1):
        blocks.append(html[starts[i]:starts[i + 1]])
    if len(starts) == 12:
        blocks.append(html[starts[-1]:ends[-1] + len("</section>")])

    short = []
    for i, blk in enumerate(blocks):
        lang = LANGS[i] if i < len(LANGS) else "?"
        n = len(re.findall(r"<h2 id=", blk))
        if n != SECTIONS:
            short.append(f"{lang}={n}")
    add(f"H1c 每节 {SECTIONS} 个带 id 的章节标题", not short, f"不符: {short}")

    # ── H2 目录项是链接 ────────────────────────────────────────────────
    bare_li = []
    for i, blk in enumerate(blocks):
        nav = re.search(r'<nav class="toc">.*?</nav>', blk, re.S)
        if not nav:
            bare_li.append(f"{LANGS[i]}: 无 nav.toc")
            continue
        lis = re.findall(r"<li>(.*?)</li>", nav.group(0), re.S)
        bad = [x[:20] for x in lis if "<a " not in x]
        if bad:
            bare_li.append(f"{LANGS[i]}: {bad[:2]}")
    add("H2 目录项都是 <a href>（不是纯文本 <li>）", not bare_li, f"{bare_li[:3]}")

    # ── H3 锚点不悬空 + id 唯一 ───────────────────────────────────────
    ids = re.findall(r'\bid="([^"]+)"', html)
    dup = [k for k, v in __import__("collections").Counter(ids).items() if v > 1]
    add("H3a id 全局唯一", not dup, f"重复: {dup[:5]}")
    hrefs = re.findall(r'href="#([^"]+)"', html)
    dangling = [x for x in hrefs if x not in set(ids)]
    add("H3b 每个页内锚点都能命中 id", not dangling, f"悬空: {dangling[:5]}")

    # ── H4 目录与章节同序同名 ─────────────────────────────────────────
    mismatch = []
    for i, blk in enumerate(blocks):
        lang = LANGS[i] if i < len(LANGS) else "?"
        pre = lang.lower() + "-"
        hs = [x for x in re.findall(r'href="#([^"]+)"', blk)]
        hi = re.findall(r'<h2 id="([^"]+)"', blk)
        if [x[len(pre):] if x.startswith(pre) else x for x in hs] != \
           [x[len(pre):] if x.startswith(pre) else x for x in hi]:
            mismatch.append(lang)
    add("H4 目录链接与章节 id 同序同名（含语言前缀）", not mismatch, f"错位: {mismatch}")

    # ── H5 移动端契约 ─────────────────────────────────────────────────
    miss = [f"{p}（{why}）" for p, why in MOBILE_CSS if p not in html]
    add("H5 移动端 CSS 契约齐全", not miss, f"缺: {miss}")

    # ── H6 md 目录 ────────────────────────────────────────────────────
    lines = md.split("\n")
    if "## 目录" not in lines:
        add("H6a PRIVACY.md 有「## 目录」", False)
        add("H6b md 目录项都是链接", True, "跳过")
    else:
        add("H6a PRIVACY.md 有「## 目录」", True)
        i = len(lines) - len(lines[lines.index("## 目录"):]) + 1
        n_items = n_links = 0
        for l in lines[i:]:
            if l.startswith("- "):
                n_items += 1
                if re.match(r"- \[.+\]\(#.+\)$", l):
                    n_links += 1
            elif l.strip() == "":
                continue
            else:
                break
        add("H6b md 目录项都是链接", n_items == SECTIONS and n_links == n_items,
            f"项 {n_items} / 链接 {n_links}")
        heads = [l[3:].strip() for l in lines
                 if l.startswith("## ") and l.strip() != "## 目录"]
        add("H6c md 章节数与目录项数一致", len(heads) == n_items,
            f"章节 {len(heads)} / 目录 {n_items}")

    return out


def main() -> int:
    if not HTML.exists() or not MD.exists():
        print(f"[ERROR] 缺文件: {HTML} / {MD}")
        return 2
    html = HTML.read_text(encoding="utf-8")
    md = MD.read_text(encoding="utf-8")
    results = run(html, md)
    bad = 0
    for name, ok, detail in results:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail and not ok else ""))
        bad += 0 if ok else 1
    print(f"\n{len(results) - bad} PASS · {bad} FAIL")
    return 0 if bad == 0 else 1


# 阴性对照：每一条注入都必须让**对应规则**变红。
# 只改坏某一处、只断言那一条 —— 别用「总数变了」当代理（本仓记过这个坑）。
MUTATIONS = [
    ("H2 目录退回纯文本", "html",
     '<li><a href="#en-who-we-are">Who we are</a></li>', '<li>Who we are</li>', "H2"),
    ("H1c 删掉一个章节 id", "html",
     '<h2 id="en-security">', '<h2>', "H1c"),
    ("H3b 造一个悬空锚点", "html",
     'href="#en-who-we-are"', 'href="#en-no-such-section"', "H3b"),
    ("H4 目录与章节错位", "html",
     '<li><a href="#en-who-we-are">Who we are</a></li>',
     '<li><a href="#en-what-this-policy-covers">Who we are</a></li>', "H4"),
    ("H5 删掉 scroll-margin-top", "html", "scroll-margin-top:14px;", "", "H5"),
    ("H6b md 目录退回纯文本", "md", "- [我们是谁](#我们是谁)", "- 我们是谁", "H6b"),
]


def selftest() -> int:
    html = HTML.read_text(encoding="utf-8")
    md = MD.read_text(encoding="utf-8")
    base = run(html, md)
    base_bad = [n for n, ok, _ in base if not ok]
    if base_bad:
        print(f"[ERROR] 基线就有红项，不能做阴性对照: {base_bad}")
        return 2
    print(f"基线 {len(base)} 条全绿\n")

    failures = []
    for name, which, old, new, rule in MUTATIONS:
        src = html if which == "html" else md
        if src.count(old) < 1:
            print(f"  [SKIP] {name}: 锚点不存在")
            failures.append(name)
            continue
        mutated = src.replace(old, new, 1)
        res = run(mutated, md) if which == "html" else run(html, mutated)
        hit = [n for n, ok, _ in res if not ok and n.startswith(rule)]
        ok = bool(hit)
        print(f"  [{'红' if ok else '绿!!'}] {name}  → {hit[:2]}")
        if not ok:
            failures.append(name)

    print()
    if failures:
        print(f"阴性对照失败: {failures}")
        return 1
    print(f"阴性对照 {len(MUTATIONS)}/{len(MUTATIONS)} 全红 ✓")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
