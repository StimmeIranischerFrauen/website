from flask import Flask, render_template, abort
import markdown
from pathlib import Path

app = Flask(__name__)

def render_markdown(filename):
    path = Path("content") / filename
    if not path.exists():
        abort(404)

    text = path.read_text(encoding="utf-8")
    html = markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "toc"]
    )
    return html

@app.route("/")
def home():
    content = render_markdown("home.md")
    return render_template("page.html", content=content)

@app.route("/<page>")
def page(page):
    content = render_markdown(f"{page}.md")
    return render_template("page.html", content=content)

@app.route("/events/<event_slug>")
def event_page(event_slug):
    content = render_markdown(f"events/{event_slug}.md")
    return render_template("page.html", content=content)

@app.route("/petitions/<petition_slug>")
def petition_page(petition_slug):
    content = render_markdown(f"petitions/{petition_slug}.md")
    return render_template("page.html", content=content)
