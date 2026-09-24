from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

HEADER_START = "<!-- TERVYNIX_ANIMATED_HEADER_START -->"
HEADER_END = "<!-- TERVYNIX_ANIMATED_HEADER_END -->"
FOOTER_START = "<!-- TERVYNIX_ANIMATED_FOOTER_START -->"
FOOTER_END = "<!-- TERVYNIX_ANIMATED_FOOTER_END -->"

FILES = {
    "VISION.md": {
        "title": "Tervynix Vision",
        "subtitle": "From developer workspace to complete developer platform",
        "lines": [
            "One+Workspace.+One+Developer+Platform.",
            "Code+%E2%86%92+Run+%E2%86%92+Debug+%E2%86%92+Manage+%E2%86%92+Deploy",
            "Developer+Control+%E2%80%A2+Performance+%E2%80%A2+Reliability",
            "Building+the+long-term+vision+of+Tervynix"
        ],
        "badges": [
            ("Vision", "Long--Term", "8B5CF6"),
            ("Status", "Evolving", "238636"),
        ],
    },
    "ROADMAP.md": {
        "title": "Tervynix Roadmap",
        "subtitle": "Completed → In Progress → Planned",
        "lines": [
            "Workspace+Foundation+%E2%86%92+Backend+Modernization",
            "PostgreSQL+%E2%86%92+Redis+%E2%86%92+BullMQ+%E2%86%92+Rust",
            "AI+%E2%86%92+Cloud+%E2%86%92+Deployment+%E2%86%92+Collaboration",
            "Engineering+Tervynix+one+validated+milestone+at+a+time"
        ],
        "badges": [
            ("Roadmap", "Active", "238636"),
            ("Project", "Building%20in%20Public", "8B5CF6"),
        ],
    },
    "CHANGELOG.md": {
        "title": "Tervynix Changelog",
        "subtitle": "Engineering milestones, migrations, and reliability work",
        "lines": [
            "Track+meaningful+engineering+milestones",
            "Runtime+%E2%80%A2+Persistence+%E2%80%A2+Architecture+%E2%80%A2+Reliability",
            "PostgreSQL+Migration+%E2%80%A2+Runtime+History+%E2%80%A2+Testing",
            "Every+milestone+makes+Tervynix+more+reliable"
        ],
        "badges": [
            ("Changelog", "Engineering", "3178C6"),
            ("Status", "Active", "238636"),
        ],
    },
    "CONTRIBUTING.md": {
        "title": "Contributing to Tervynix",
        "subtitle": "Build, discuss, test, document, and improve",
        "lines": [
            "Ideas+%E2%80%A2+Bug+Reports+%E2%80%A2+Documentation+%E2%80%A2+Feedback",
            "Professional+Discussion.+Strong+Engineering.",
            "Help+improve+developer+workflows",
            "Build+with+Tervynix"
        ],
        "badges": [
            ("Contributions", "Welcome", "238636"),
            ("Community", "Professional", "3178C6"),
        ],
    },
    "CODE_OF_CONDUCT.md": {
        "title": "Tervynix Code of Conduct",
        "subtitle": "Professional communication. Constructive collaboration.",
        "lines": [
            "Respect+Developers",
            "Focus+on+Engineering",
            "Build+Constructively",
            "Keep+the+Tervynix+community+professional"
        ],
        "badges": [
            ("Community", "Respectful", "238636"),
            ("Standard", "Professional", "3178C6"),
        ],
    },
    "SECURITY.md": {
        "title": "Tervynix Security",
        "subtitle": "Responsible disclosure and secure engineering",
        "lines": [
            "Protect+Users.+Protect+Infrastructure.",
            "Report+Security+Issues+Responsibly",
            "Never+Publish+Secrets+or+Active+Exploits",
            "Security+is+a+core+Tervynix+engineering+boundary"
        ],
        "badges": [
            ("Security", "Responsible%20Disclosure", "D73A49"),
            ("Project", "Tervynix", "3178C6"),
        ],
    },
    "SUPPORT.md": {
        "title": "Tervynix Support",
        "subtitle": "Get help, report issues, and find the right project channel",
        "lines": [
            "Questions+%E2%86%92+Discussions",
            "Bugs+%E2%86%92+GitHub+Issues",
            "Security+%E2%86%92+Responsible+Disclosure",
            "Find+the+right+path+for+Tervynix+support"
        ],
        "badges": [
            ("Support", "Community", "238636"),
            ("Discussions", "Enabled", "8B5CF6"),
        ],
    },
    "docs/ARCHITECTURE.md": {
        "title": "Tervynix Architecture",
        "subtitle": "Workspace → Services → Persistence → Runtime Infrastructure",
        "lines": [
            "Next.js+%E2%86%92+NestJS+%2F+Fastify+%E2%86%92+Domain+Services",
            "PostgreSQL+%2B+Drizzle+%E2%80%A2+WebSockets",
            "Redis+%E2%80%A2+BullMQ+%E2%80%A2+Rust+Runtime+Agent",
            "Migrate.+Validate.+Keep+the+platform+operational."
        ],
        "badges": [
            ("Architecture", "Modular", "3178C6"),
            ("Migration", "Incremental", "238636"),
        ],
    },
    "docs/DEVELOPMENT_STATUS.md": {
        "title": "Tervynix Development Status",
        "subtitle": "Implemented, in progress, hardening, and planned",
        "lines": [
            "Implemented+%E2%9C%85+%E2%80%A2+In+Progress+%F0%9F%9F%A1+%E2%80%A2+Planned+%E2%9A%AA",
            "Runtime+History+PostgreSQL+Scope+%E2%80%94+Complete",
            "22+Focused+Tests+%E2%80%A2+8+Real+PostgreSQL+Tests",
            "Engineering+status+without+marketing+overclaim"
        ],
        "badges": [
            ("Development", "Active", "238636"),
            ("Runtime%20History", "Scoped%20Complete", "3178C6"),
        ],
    },
    "docs/FEATURES.md": {
        "title": "Tervynix Features",
        "subtitle": "Current capabilities and future platform direction",
        "lines": [
            "Editor+%E2%80%A2+Terminal+%E2%80%A2+Processes+%E2%80%A2+Ports",
            "Runtime+History+%E2%80%A2+Realtime+%E2%80%A2+Authentication",
            "AI+%E2%80%A2+Cloud+%E2%80%A2+Deployment+%E2%80%A2+Collaboration",
            "One+connected+developer+workspace"
        ],
        "badges": [
            ("Features", "Developer%20Platform", "3178C6"),
            ("Status", "Evolving", "238636"),
        ],
    },
    "docs/FAQ.md": {
        "title": "Tervynix FAQ",
        "subtitle": "Quick answers about the project, architecture, and roadmap",
        "lines": [
            "What+is+Tervynix%3F",
            "What+is+implemented+today%3F",
            "Where+is+the+architecture+going%3F",
            "How+can+developers+contribute%3F"
        ],
        "badges": [
            ("FAQ", "Project%20Guide", "3178C6"),
            ("Tervynix", "Active%20Development", "238636"),
        ],
    },
}


def remove_existing_block(text: str, start: str, end: str) -> str:
    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end) + r"\s*",
        re.DOTALL,
    )
    return pattern.sub("", text)


def strip_first_h1(text: str) -> str:
    return re.sub(r"^\s*#\s+.+?\r?\n+", "", text, count=1)


def make_badges(items):
    return "\n".join(
        f'<img src="https://img.shields.io/badge/{label}-{value}-{color}?style=for-the-badge" />'
        for label, value, color in items
    )


def make_header(config, is_doc=False):
    lines = ";".join(config["lines"])
    back = "../README.md" if is_doc else "./README.md"
    architecture = "./ARCHITECTURE.md" if is_doc else "./docs/ARCHITECTURE.md"
    roadmap = "../ROADMAP.md" if is_doc else "./ROADMAP.md"

    return f'''{HEADER_START}
<div align="center">

# {config["title"]}

### {config["subtitle"]}

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2400&pause=900&color=36BCF7&center=true&vCenter=true&width=950&lines={lines}"
  alt="{config["title"]} animated header"
/>

<br />

{make_badges(config["badges"])}

<br /><br />

<a href="{back}">← Project Home</a> •
<a href="{architecture}">Architecture</a> •
<a href="{roadmap}">Roadmap</a>

</div>

---

{HEADER_END}

'''


def make_footer(is_doc=False):
    home = "../README.md" if is_doc else "./README.md"
    return f'''

---

{FOOTER_START}
<div align="center">

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2200&pause=1200&color=36BCF7&center=true&vCenter=true&width=760&lines=Build+with+Tervynix.;One+workspace.+One+runtime.+One+developer+platform.;Code+%E2%86%92+Run+%E2%86%92+Debug+%E2%86%92+Manage"
  alt="Build with Tervynix"
/>

<br />

<a href="{home}">← Back to Tervynix</a>

</div>
{FOOTER_END}
'''


def animate_file(relative_path: str, config: dict):
    path = ROOT / relative_path

    if not path.exists():
        print(f"SKIP (missing): {relative_path}")
        return

    text = path.read_text(encoding="utf-8")

    text = remove_existing_block(text, HEADER_START, HEADER_END)
    text = remove_existing_block(text, FOOTER_START, FOOTER_END)
    text = strip_first_h1(text).strip()

    is_doc = relative_path.startswith("docs/")
    output = make_header(config, is_doc) + text + make_footer(is_doc)

    path.write_text(output.rstrip() + "\n", encoding="utf-8")
    print(f"UPDATED: {relative_path}")


def main():
    print()
    print("Animating Tervynix documentation...")
    print()

    for relative_path, config in FILES.items():
        animate_file(relative_path, config)

    print()
    print("Done.")
    print()
    print("Files intentionally NOT changed:")
    print("  LICENSE")
    print("  README.md")
    print("  .github/ISSUE_TEMPLATE/*")
    print("  .github/PULL_REQUEST_TEMPLATE.md")
    print()
    print("Review with:")
    print("  git diff")
    print("  git status")
    print()


if __name__ == "__main__":
    main()
