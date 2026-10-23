# Basin Powered Dispatch — website

Plain HTML/CSS. No build step on Netlify (publish directory = repo root).

- Edit `build.py` and run `python3 build.py` to regenerate all pages with the shared header/footer (or edit the .html files directly).
- Logo: drop `logo.svg` here and swap it in at the LOGO comment in `build.py`.
- Support bot: paste the embed snippet at the SUPPORT BOT comment in `build.py` (FAQ page).
- Demo form: submissions land in Netlify → Forms → `demo-request`. Turn on email notifications there.
- App sign-in + demo live at rigready1.netlify.app.
