import sys
from flask import Flask, request
import requests

TOKEN = "TOKEN"  #o'z telegram botingizning tokenini yozing
SECRET = "KALIT" #ixtiyoriy sirli kalit so'z
API = f"https://api.telegram.org/bot{TOKEN}"
SEP = "\n\n🇬🇧 English:\n"

app = Flask(__name__)

def tr_google(chunk):
    r = requests.get(
        "https://translate.googleapis.com/translate_a/single",
        params={"client": "gtx", "sl": "uz", "tl": "en", "dt": "t", "q": chunk},
        timeout=10,
    )
    r.raise_for_status()
    return "".join(p[0] for p in r.json()[0] if p[0])

def tr_mymemory(chunk):
    r = requests.get(
        "https://api.mymemory.translated.net/get",
        params={"q": chunk, "langpair": "uz|en"},
        timeout=10,
    )
    r.raise_for_status()
    d = r.json()
    if d.get("responseStatus") != 200:
        raise Exception(d.get("responseDetails"))
    return d["responseData"]["translatedText"]

def translate(text):
    out = []
    for line in text.split("\n"):
        if not line.strip():
            out.append(line)
            continue
        for fn in (tr_google, tr_mymemory):
            try:
                out.append(fn(line))
                break
            except Exception as e:
                print(fn.__name__, "ERROR:", e, file=sys.stderr)
        else:
            raise RuntimeError("hamma tarjimonlar xato berdi")
    return "\n".join(out)

@app.route(f"/{SECRET}", methods=["POST"])
def hook():
    data = request.get_json(force=True, silent=True) or {}
    post = data.get("channel_post")
    if not post:
        return "ok"
    text = post.get("text") or post.get("caption")
    if not text or SEP in text:
        return "ok"
    try:
        en = translate(text)
    except Exception as e:
        print("TRANSLATE ERROR:", e, file=sys.stderr)
        return "ok"
    key = "text" if "text" in post else "caption"
    method = "editMessageText" if key == "text" else "editMessageCaption"
    r = requests.post(f"{API}/{method}", timeout=10, json={
        "chat_id": post["chat"]["id"],
        "message_id": post["message_id"],
        key: text + SEP + en,
    })
    print("EDIT RESULT:", r.text, file=sys.stderr)
    return "ok"