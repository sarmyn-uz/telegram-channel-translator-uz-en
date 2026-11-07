# Telegram Channel Translator (UZ → EN)

🇺🇿 Telegram kanalingizga oʻzbekcha post joylaysiz, bot uni oʻzi tahrirlab, pastiga **inglizcha tarjimasini** qoʻshib qoʻyadi. Bitta post, ikki til.

🇬🇧 Post in Uzbek to your Telegram channel, and the bot edits the same post to append an **English translation** below it. One post, two languages.

---

## 🇺🇿 Oʻzbekcha

### Qanday ishlaydi

1. Siz kanalga oʻzbekcha post joylaysiz.
2. Telegram webhook orqali botga xabar yuboradi.
3. Bot matnni tarjima qiladi (Google, zaxira: MyMemory).
4. Bot postni tahrirlab, pastiga `🇬🇧 English:` va tarjimani qoʻshadi.

### Xususiyatlar

- Tekin: PythonAnywhere'ning bepul tarifida ishlaydi, pullik API kerak emas
- Abzaslar va boʻsh qatorlar saqlanadi (matn qatorma-qator tarjima qilinadi)
- Rasm/video ostidagi matn (caption) ham tarjima qilinadi
- Asosiy tarjimon ishlamasa, zaxira tarjimonga oʻtadi
- Webhook ishlatadi, shuning uchun botni "uygʻotib turish" shart emas

### Oʻrnatish (PythonAnywhere, bepul)

1. [@BotFather](https://t.me/BotFather) orqali bot yarating va tokenni oling.
2. Botni kanalingizga admin qiling va **Post messages** hamda **Edit messages of others** ruxsatlarini yoqing.
3. [pythonanywhere.com](https://www.pythonanywhere.com) da bepul akkaunt oching → **Web** → **Add a new web app** → **Flask** (istalgan yangi Python versiyasi, masalan 3.12).
4. `mysite/flask_app.py` ichiga shu repo'dagi `flask_app.py` kodini qoʻying va ikkita oʻzgaruvchini toʻldiring:
   - `TOKEN`: BotFather bergan token
   - `SECRET`: oʻzingiz oʻylab topgan uzun tasodifiy matn (webhook manzilining maxfiy qismi)
5. **Web** boʻlimida **Reload** bosing.
6. Brauzerda webhook'ni ulang (`TOKEN`, `USERNAME`, `SECRET` ni almashtiring):

   ```
   https://api.telegram.org/botTOKEN/setWebhook?url=https://USERNAME.pythonanywhere.com/SECRET&allowed_updates=["channel_post"]
   ```

   Javobda `"Webhook was set"` chiqishi kerak.
7. Kanalga **yangi** post joylang. Bir necha soniyadan keyin pastida inglizcha tarjima paydo boʻladi.

> Bepul web app oʻchib qolmasligi uchun PythonAnywhere → **Web** boʻlimida har ~3 oyda "Run until 3 months from today" tugmasini bosib turing.

### Tillarni oʻzgartirish

`flask_app.py` ichida `tr_google` va `tr_mymemory` funksiyalaridagi `sl` / `tl` (Google) va `langpair` (MyMemory) qiymatlarini oʻzgartiring, masalan `uz` → `ru`.

### Cheklovlar

- Tarjima Google'ning **norasmiy** manzili (`translate.googleapis.com`) orqali ishlaydi, u ogohlantirishsiz oʻzgarishi yoki ishlamay qolishi mumkin.
- Zaxira tarjimon MyMemory'ning bepul limiti kichik (kuniga ~5000 belgi, bir soʻrovda ~500 belgi).
- Tahrirdan keyin matndagi formatlash (qalin, havola) yoʻqolishi mumkin.
- Telegram limitlari: oddiy post ~4096, rasm/video ostidagi matn 1024 belgi. Uzun postlarda tahrir xato berishi mumkin.
- Bot faqat yangi postlarni tarjima qiladi, tahrirlangan postlarni emas.
- Tarjima uchun postlaringiz matni Google va MyMemory serverlariga yuboriladi.

### Xavfsizlik

- `TOKEN` va `SECRET` ni hech qachon GitHub'ga yuklamang.
- Token boshqalarga koʻrinib qolsa, [@BotFather](https://t.me/BotFather) da `/revoke` qiling va `setWebhook` ni yangi token bilan qayta bajaring.

### Muammolar

PythonAnywhere → **Web** → **Error log** ni oching. Ulanish holatini tekshirish uchun: `https://api.telegram.org/botTOKEN/getWebhookInfo`.

---

## 🇬🇧 English

A small Flask webhook bot that automatically appends an English translation under Uzbek posts in your Telegram channel.

**Setup in short:**

1. Create a bot with @BotFather and add it to your channel as an admin (with *Post messages* and *Edit messages of others*).
2. Create a free PythonAnywhere account → *Web* → *Add a new web app* → *Flask*.
3. Paste `flask_app.py`, set `TOKEN` and `SECRET`, then hit *Reload*.
4. Set the webhook:
   ```
   https://api.telegram.org/botTOKEN/setWebhook?url=https://USERNAME.pythonanywhere.com/SECRET&allowed_updates=["channel_post"]
   ```
5. Post something new in your channel.

**Notes:** uses an unofficial Google endpoint with MyMemory as a fallback; formatting may be lost after the edit; free PythonAnywhere web apps must be extended every ~3 months. Never commit your bot token.

---

## License

MIT

## Author

[@USERNAME](https://github.com/sarmyn-uz) • Telegram: [@zamin_origin](https://t.me/zamin_origin)