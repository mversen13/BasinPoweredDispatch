"""Assembles the static pages with a shared header/footer. Output = plain .html files (no build step needed on Netlify)."""
from pathlib import Path

APP = "https://basinpowereddispatch.com"
NAV = [("index.html", "Home"), ("carriers.html", "Carriers"), ("operators.html", "Operators"),
       ("about.html", "About")]


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B1F38">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://basinpowereddispatch.com/og-image.jpg">
</head>
<body>"""


def header(active):
    links = "".join(
        f'<li><a href="{h}"{" class=active" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f"""
<header>
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Basin Powered Dispatch home">
      <img src="logo-light.png" alt="Basin Powered Dispatch" width="168" height="40">
    </a>
    <button class="menu-btn" aria-label="Menu" onclick="document.getElementById('menu').classList.toggle('open')">&#9776;</button>
    <ul id="menu">
      {links}
      <li><a href="{APP}/">Sign in</a></li>
      <li><a href="demo.html">Try the demo</a></li>
      <li><a href="contact.html"{" class=active" if active == "contact.html" else ""}>Contact</a></li>
      <li><a class="btn btn-primary" href="join.html">Try it free</a></li>
    </ul>
  </div>
</header>
<main>"""


FOOTER = f"""
</main>
<footer>
  <div class="wrap">
    <div>&copy; <span id="yr">2026</span> Basin Powered Dispatch</div>
    <nav>
      <a href="join.html">Try it free</a>
      <a href="demo.html">Try the demo</a>
      <a href="contact.html">Contact</a>
      <a href="{APP}/">Sign in</a>
      <a href="{APP}/privacy/">Privacy</a>
      <a href="{APP}/terms/">Terms</a>
    </nav>
  </div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear()</script>
</body>
</html>
"""


def ic(path):
    return f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
I = {
 "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "building": '<path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/>',
 "broadcast": '<circle cx="12" cy="12" r="2"/><path d="M16.2 7.8a6 6 0 0 1 0 8.4M7.8 16.2a6 6 0 0 1 0-8.4M19.1 4.9a10 10 0 0 1 0 14.2M4.9 19.1a10 10 0 0 1 0-14.2"/>',
 "activity": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-6 7-6s7 2.5 7 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M22 20c0-3-2-5.2-5-5.8"/>',
 "rotate": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
 "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
}

CTA = """
<section class="cta">
  <div class="wrap">
    <h2>Why wait? Try it free.</h2>
    <p class="lead">Join the network free or click through the demo first. It takes two minutes.</p>
    <div class="btns"><a class="btn btn-primary" href="join.html">Try it free</a><a class="btn btn-ghost" href="demo.html">Try the demo</a></div>
  </div>
</section>"""

BOARD = """
<div class="board" aria-hidden="true">
  <div class="board-top"><b>Dispatch board</b><span class="pill green">9 drivers on</span></div>
  <div class="cols">
    <div class="col"><h4>Needs driver</h4>
      <div class="job"><b>Red Mesa 14H</b><span>Fresh water &middot; 2 trucks</span><span class="pill amber">Offering&hellip;</span></div>
      <div class="job"><b>Coyote Draw 3</b><span>Vac &middot; 1 truck</span><span class="pill amber">Offering&hellip;</span></div>
    </div>
    <div class="col"><h4>On the way</h4>
      <div class="job"><b>Big Spring SWD</b><span>Luis &middot; ETA 22 min</span><span class="pill blue">En route</span></div>
      <div class="job"><b>Mustang Pad</b><span>Ray &middot; ETA 9 min</span><span class="pill blue">En route</span></div>
    </div>
    <div class="col"><h4>Done</h4>
      <div class="job"><b>Caprock 7</b><span>Ana &middot; 3 loads</span><span class="pill green">Complete</span></div>
      <div class="job"><b>Sand Hills 2</b><span>Mike &middot; 2 loads</span><span class="pill green">Complete</span></div>
    </div>
  </div>
  <div class="drivers">
    <div class="drv"><span class="dot"></span>Luis</div><div class="drv"><span class="dot"></span>Ana</div>
    <div class="drv"><span class="dot busy"></span>Ray</div><div class="drv"><span class="dot"></span>Mike</div>
    <div class="drv"><span class="dot off"></span>Jesse</div>
  </div>
</div>"""

PHONE = """
<div class="phone" aria-hidden="true"><div class="screen">
  <div class="hdr">New job for you</div>
  <div class="offer">
    <div class="tag">Offer &middot; 6:00 AM</div>
    <h5>Red Mesa 14H</h5>
    <dl><dt>Load</dt><dd>Fresh water</dd><dt>Trucks</dt><dd>2</dd><dt>County</dt><dd>Midland</dd></dl>
    <div class="yn"><div class="yes">Accept</div><div class="no">Decline</div></div>
  </div>
  <div class="mini"><span>Pin sent to your maps</span><b>&#10003;</b></div>
</div></div>"""

REPORTS = """
<div class="reports" aria-hidden="true">
  <div class="r-top"><b>Reports</b><span class="pill blue">This week</span></div>
  <div class="r-kpis">
    <div><small>Jobs</small><b>37</b><em>28 done</em></div>
    <div><small>Time to first driver</small><b>5 min</b><em>typical, ASAP jobs</em></div>
    <div><small>Offers taken</small><b>83%</b><em>66 yes &middot; 5 no</em></div>
    <div><small>Answer time</small><b>77 sec</b><em>typical</em></div>
  </div>
  <div class="r-grid">
    <div class="r-card"><h4>Barrels by day</h4><div class="rbars"><div class="rbar"><i style="height:98%"></i><span>10/19</span></div><div class="rbar"><i style="height:58%"></i><span>10/20</span></div><div class="rbar"><i style="height:65%"></i><span>10/21</span></div><div class="rbar"><i style="height:46%"></i><span>10/22</span></div><div class="rbar"><i style="height:58%"></i><span>10/23</span></div><div class="rbar"><i style="height:6%"></i><span>10/24</span></div></div></div>
    <div class="r-card"><h4>Top operators</h4><div class="rop"><span>Red Mesa Energy</span><b>15 jobs</b><i style="width:100%"></i></div><div class="rop"><span>Permian Basin Resources</span><b>5 jobs</b><i style="width:33%"></i></div><div class="rop"><span>Sandhill Resources</span><b>4 jobs</b><i style="width:27%"></i></div><div class="rop"><span>Desert Fox Oil</span><b>2 jobs</b><i style="width:13%"></i></div></div>
  </div>
  <div class="r-card"><h4>Drivers</h4>
    <table class="rtable"><thead><tr><th>Driver</th><th>Accepted</th><th>Rate</th><th>Answers in</th></tr></thead><tbody><tr><td><b>Wade Pruitt</b> <small>Vac 103</small></td><td>6/6</td><td><span class="rpct">100%</span></td><td>84 sec</td></tr><tr><td><b>Eli Navarro</b> <small>303</small></td><td>6/7</td><td><span class="rpct">86%</span></td><td>2 min</td></tr><tr><td><b>Ray Castillo</b> <small>Vac 102</small></td><td>6/9</td><td><span class="rpct lo">67%</span></td><td>60 sec</td></tr><tr><td><b>Brandon Kemp</b> <small>304</small></td><td>4/8</td><td><span class="rpct lo">50%</span></td><td>60 sec</td></tr></tbody></table>
  </div>
</div>"""


OP_AVAIL = """
<div class="avail" aria-hidden="true">
  <div class="avail-top"><b>Trucks available</b><span class="pill blue">Closest first</span></div>
  <div class="avail-loc">Red Mesa 31-4H Pad &middot; Midland County</div>
  <div class="avail-row"><span><b>Caprock Fluid Services</b><small>About 5 min from their yard</small></span><span class="pill green">3 trucks free</span></div>
  <div class="avail-row"><span><b>Mesa Vac &amp; Water</b><small>About 15 min from their yard</small></span><span class="pill green">2 trucks free</span></div>
  <div class="avail-row"><span><b>Lone Star Vac Service</b><small>Not on the platform yet</small></span><span class="pill blue">Gets it by email</span></div>
  <div class="avail-btns"><div class="avail-cta">Send to Caprock</div><div class="avail-cta ghost">Send to all</div></div>
</div>"""

ORDER = """
<div class="order" aria-hidden="true">
  <div class="avail-top"><b>New order</b><span class="pill green">Ready to send</span></div>
  <div class="o-row"><i>1</i><div><small>Location</small><b>Red Mesa 31-4H Pad</b><em>Midland County &middot; saved</em></div></div>
  <div class="o-row"><i>2</i><div><small>Job order</small><b>Fresh water haul &middot; 2 trucks</b></div></div>
  <div class="o-row"><i>3</i><div><small>Driver certifications</small><span class="chip">H2S</span><span class="chip">SafeLand</span><span class="chip">PEC</span></div></div>
  <div class="o-row"><i>4</i><div><small>When</small><b>As soon as possible</b></div></div>
  <div class="o-row"><i>5</i><div><small>Required forms</small><b>JSA &middot; Site safety checklist</b></div></div>
  <div class="o-row"><i>6</i><div><small>Send to</small><b>Caprock Fluid Services</b><em>3 trucks free</em></div></div>
  <div class="avail-cta">Send order &rarr;</div>
</div>"""

STATUS = """
<div class="order" aria-hidden="true">
  <div class="avail-top"><b>Your orders</b><span class="pill blue">Live</span></div>
  <div class="st-row"><span><b>Vacuum truck &middot; 1 truck</b><small>Red Mesa 31-4H Pad</small></span><span class="pill blue">Trucks rolling</span></div>
  <div class="st-row"><span><b>Produced water &middot; 3 trucks</b><small>Ridgeline 7 Tank Battery</small></span><span class="pill blue">Trucks working</span></div>
  <div class="st-row"><span><b>Fresh water &middot; 1 truck</b><small>Bluestem 22 Battery &middot; Sun 1:00 PM</small></span><span class="pill green">Accepted</span></div>
  <div class="st-row"><span><b>Fresh water &middot; 2 trucks</b><small>Mesa 12 Pad &middot; Sun 6:30 AM</small></span><span class="pill amber">Waiting on company</span></div>
  <div class="st-row"><span><b>Produced water &middot; 2 trucks</b><small>Ridgeline 7 Tank Battery</small></span><span class="pill gray">Done</span></div>
</div>"""

PAGES = {}

PAGES["index.html"] = ("Basin Powered Dispatch · No missed calls. No missed loads.",
"Dispatch for oilfield vac and water haulers. Orders in, drivers offered, operators updated — without calling down the list.", f"""
<section class="hero">
  <div class="wrap grid">
    <div>
      <div class="eyebrow">Powering basins across the U.S.</div>
      <h1>No missed calls.<br>No missed loads.</h1>
      <p class="lead" style="margin-top:18px">Orders come in. The right driver gets the offer. The operator sees the truck coming. Nobody's calling down a list.</p>
      <p class="lead" style="margin-top:12px;color:#fff;font-weight:600">Bridging the gap between operators and the crews that keep the basin running.</p>
      <div class="btns"><a class="btn btn-primary" href="join.html">Try it free</a><a class="btn btn-ghost" href="demo.html">Try the demo</a></div>
    </div>
    <div class="mock-stack">{BOARD}{PHONE}</div>
  </div>
</section>

<div class="pain"><div class="wrap row">
  <div><h3>Phone rings at 4 AM.</h3><p>Miss it and the job goes to someone else.</p></div>
  <div><h3>Calling driver after driver.</h3><p>Who's on? Who's close? Who's up next?</p></div>
  <div><h3>&ldquo;What's the status?&rdquo;</h3><p>Operators calling back for updates on their job order.</p></div>
</div></div>

<section id="how">
  <div class="wrap center">
    <div class="eyebrow">How it works</div>
    <h2>Four steps. No whiteboard.</h2>
    <div class="cards four" style="text-align:left">
      <div class="card"><div class="step-num">1</div><h3>Job order received</h3><p>Call, text, email or form. Every order lands in one place.</p></div>
      <div class="card"><div class="step-num">2</div><h3>Dispatch team gets alerted</h3><p>Use automation or manually select drivers.</p></div>
      <div class="card"><div class="step-num">3</div><h3>Trucks hit the road</h3><p>Driver taps Accept, gets the location and job details, and rolls. One tap updates each stage of the job.</p></div>
      <div class="card"><div class="step-num">4</div><h3>Visibility of the fleet</h3><p>Carriers and operators see real-time progress of the job.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="cards two" style="margin-top:0">
      <div class="aud"><div class="eyebrow">For carriers</div><h2>Fill every load.</h2><p>Know who's on, offer jobs in order, and track every truck from one screen.</p><a class="more" href="carriers.html">For carriers &rarr;</a></div>
      <div class="aud"><div class="eyebrow">For operators</div><h2>Find trucks fast. No phone calls.</h2><p>See which haulers have availability. Pick one or send to them all. Request dispatch in a couple of clicks.</p><a class="more" href="operators.html">For operators &rarr;</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap center">
    <div class="eyebrow">Join the network. Power the basin.</div>
    <h2>Operators and carriers. One platform.</h2>
    <p class="lead">The basin runs on carriers getting the right trucks, equipment and material to operators. Operators send jobs. Carriers fill them. The more haulers and operators on Basin, the faster trucks move.</p>
    <div class="btns" style="justify-content:center"><a class="btn btn-primary" href="join.html?type=carrier">Join as a carrier</a><a class="btn btn-dark" href="join.html?type=operator">Join as an operator</a></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="free">
      <div><div class="eyebrow" style="color:#fff;opacity:.8">Free to start</div><h2>Use it free. Pay as you grow.</h2><p>No contracts to get going. Plans scale with your fleet.</p><div class="btns" style="margin-top:20px"><a class="btn" style="background:#fff;color:var(--navy)" href="join.html">Try it free</a></div></div>
      <div class="tiers">
        <div class="tier"><b>Carriers</b>Free for your first 30 dispatch hauls</div>
        <div class="tier"><b>Operators</b>Free for your first 10 job orders</div>
      </div>
    </div>
  </div>
</section>
{CTA}""")

PAGES["carriers.html"] = ("For Carriers · Basin Powered Dispatch",
"Dispatch for vac and water-hauling fleets. Offer jobs in order, track every truck, stop working the phone.", f"""
<section class="hero small">
  <div class="wrap grid">
    <div>
      <div class="eyebrow">For carriers</div>
      <h1>Fill every load without working the phone.</h1>
      <p class="lead" style="margin-top:18px">Built for the 24/7 pace of oilfield hauling.</p>
      <div class="btns"><a class="btn btn-primary" href="join.html?type=carrier">Try it free</a><a class="btn btn-ghost" href="demo.html">Try the demo</a></div>
    </div>
    <div>{PHONE}</div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="cards compact">
      <div class="card"><div class="icon">{ic(I["users"])}</div><h3>Who's on, at a glance</h3><p>See every driver on duty, off duty, on a job or returning from one.</p></div>
      <div class="card"><div class="icon">{ic(I["rotate"])}</div><h3>Auto-pick or hand-pick</h3><p>Let it send the job to whoever's up next or pick the driver yourself. No answer? It rolls to the next one.</p></div>
      <div class="card"><div class="icon"><img src="icon-b.png" alt="" style="width:30px;height:auto"></div><h3>Right on the driver's phone</h3><p>Job, load, and map pin. He taps Accept and goes.</p></div>
      <div class="card"><div class="icon">{ic(I["truck"])}</div><h3>Track every truck</h3><p>On my way, on site, done. You see it live.</p></div>
      <div class="card"><div class="icon">{ic(I["phone"])}</div><h3>Never miss an order</h3><p>Calls, texts and emails all land on one board.</p></div>
      <div class="card"><div class="icon">{ic(I["check"])}</div><h3>Operators stay updated</h3><p>They see status themselves. Fewer callbacks.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div>{BOARD}</div>
    <div>
      <div class="eyebrow">Free to start</div>
      <h2>Your first 30 dispatch hauls are free.</h2>
      <p class="lead">Run real jobs before you pay a dime. Plans scale with your fleet when you're ready.</p>
      <ul class="checks"><li>No contract to start</li><li>We set it up with you</li><li>Your drivers, your rotation</li></ul>
      <div class="btns"><a class="btn btn-primary" href="join.html?type=carrier">Try it free</a><a class="btn btn-dark" href="demo.html">Try the demo</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split rev">
    <div>
      <div class="avail" aria-hidden="true">
        <div class="avail-top"><b>Operator view &middot; Trucks available</b><span class="pill blue">Midland</span></div>
        <div class="avail-row you"><span><b>Your company</b><small>Vac &middot; Water</small></span><span class="pill green">4 trucks open</span></div>
        <div class="avail-row"><span><b>Caprock Fluid Services</b><small>Water</small></span><span class="pill green">2 trucks open</span></div>
        <div class="avail-row"><span><b>Lone Star Vac</b><small>Vac</small></span><span class="pill amber">1 truck open</span></div>
        <div class="avail-cta">Request dispatch &rarr;</div>
      </div>
    </div>
    <div>
      <div class="eyebrow">Grow with the network</div>
      <h2>Get in front of new operators.</h2>
      <p class="lead">As the network grows, so do your opportunities. Operators looking for trucks see who's available, so new job orders can find you.</p>
      <ul class="checks"><li>Show up when operators need trucks</li><li>Work with operators you don't know yet</li><li>More operators on the network, more jobs for you</li></ul>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div>{REPORTS}</div>
    <div>
      <div class="eyebrow">Reports</div>
      <h2>Know your numbers.</h2>
      <p class="lead">See how your drivers and your operators are performing, without building a spreadsheet.</p>
      <ul class="checks">
        <li>Offers taken, passed or missed by driver</li>
        <li>How fast drivers answer and trucks get assigned</li>
        <li>Loads and barrels by day, by service</li>
        <li>Which operators you work with most</li>
      </ul>
    </div>
  </div>
</section>
{CTA}""")

PAGES["operators.html"] = ("For Operators · Basin Powered Dispatch",
"See which oilfield haulers have trucks available, pick one or send the job to all of them. Get trucks on the road in a few clicks.", f"""
<section class="hero small">
  <div class="wrap grid">
    <div>
      <div class="eyebrow">For operators</div>
      <h1>Get trucks moving without picking up the phone.</h1>
      <p class="lead" style="margin-top:18px">See which haulers have availability right now. Pick one or send to them all. Request dispatch in a couple of clicks.</p>
      <div class="btns"><a class="btn btn-primary" href="join.html?type=operator">Try it free</a><a class="btn btn-ghost" href="demo.html">Try the demo</a></div>
    </div>
    <div>{OP_AVAIL}</div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="cards compact">
      <div class="card"><div class="icon">{ic(I["eye"])}</div><h3>See who's available</h3><p>Live truck availability across carriers, closest first.</p></div>
      <div class="card"><div class="icon">{ic(I["building"])}</div><h3>Pick a company</h3><p>Send to a hauler you already use or try a new one.</p></div>
      <div class="card"><div class="icon">{ic(I["broadcast"])}</div><h3>Or send to all</h3><p>Busy day? Send it out. The first carrier to accept gets the job.</p></div>
      <div class="card"><div class="icon">{ic(I["activity"])}</div><h3>Track the status</h3><p>Every order, from accepted to trucks rolling to done.</p></div>
      <div class="card"><div class="icon">{ic(I["pin"])}</div><h3>Saved locations</h3><p>Pick a pad or battery you've ordered to before. No retyping or sending pins.</p></div>
      <div class="card"><div class="icon">{ic(I["shield"])}</div><h3>Compliance on the order</h3><p>Require certs like H2S, SafeLand, PEC or TWIC. Add a JSA or your own required forms.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split rev">
    <div>{STATUS}</div>
    <div>
      <div class="eyebrow">Free to start</div>
      <h2>Your first 10 job orders are free.</h2>
      <p class="lead">Bring the haulers you already use. Try it on real work before you commit.</p>
      <ul class="checks"><li>Works with your current carriers</li><li>No payments run through Basin Powered Dispatch</li><li>Flat pricing, not per job</li></ul>
      <div class="btns"><a class="btn btn-primary" href="join.html?type=operator">Try it free</a><a class="btn btn-dark" href="demo.html">Try the demo</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>{ORDER}</div>
    <div>
      <div class="eyebrow">Order in a few clicks</div>
      <h2>Get trucks on the road in just a few clicks.</h2>
      <p class="lead">One short order. No calls, no texts, no chasing.</p>
      <ul class="checks">
        <li>Pick a saved location. Drivers get the pin and directions</li>
        <li>Choose the service and how many trucks or enter barrels</li>
        <li>Add required certs, a JSA or your own forms</li>
        <li>As soon as possible or schedule ahead</li>
        <li>Send to one company or to all of them</li>
      </ul>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap center">
    <div class="eyebrow">Grow the network</div>
    <h2>More haulers. More options.</h2>
    <p class="lead">Your go-to hauler is booked? See who else has trucks open nearby. Every carrier that joins gives you more options when you need trucks.</p>
    <div class="cards compact" style="margin-top:36px;text-align:left">
      <div class="card"><div class="icon">{ic(I["check"])}</div><h3>Keep your regulars</h3><p>Send to the carriers you already trust.</p></div>
      <div class="card"><div class="icon">{ic(I["truck"])}</div><h3>Try someone new</h3><p>When your regulars are busy, others nearby can take it.</p></div>
      <div class="card"><div class="icon">{ic(I["users"])}</div><h3>Bring your haulers</h3><p>Invite your carriers. Free for them to join. Not on yet? They still get your order by email.</p></div>
    </div>
  </div>
</section>
{CTA}""")

PAGES["about.html"] = ("About · Basin Powered Dispatch",
"Most oilfield dispatching is still manual. Basin Powered Dispatch bridges the gap between operators and carriers.", f"""
<section class="hero small">
  <div class="wrap">
    <div class="eyebrow">About</div>
    <h1>Most dispatching is still done by hand.</h1>
    <p class="lead" style="margin-top:18px;max-width:680px">The oilfield has modernized almost everything. Getting trucks from a job order to a location still runs on phone calls and whiteboards. We built Basin Powered Dispatch with partners in the Permian Basin to change that.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="mv">
      <div class="mv-card">
        <div class="eyebrow">Our mission</div>
        <p>Bring operators and carriers onto one network so trucks get on the road fast, any hour of any day the basin needs them.</p>
      </div>
      <div class="mv-card">
        <div class="eyebrow">Our vision</div>
        <p>A growing network where operators and carriers work as true partners, spending less time on the phone and more time growing their business. Built with and for the industry, powering dispatch across North America.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap ab-split">
    <div>
      <div class="eyebrow">What's missing</div>
      <h2>Plenty of software moves freight. Little of it dispatches.</h2>
      <p class="lead">Good transportation systems are out there. Few are built for the dispatch itself: taking a job order, getting trucks on the road, seeing the job through to done and getting those trucks back out.</p>
      <p class="lead" style="margin-top:14px">For carriers, a missed 2 AM call is a lost job. For operators, it's hours on the phone finding trucks.</p>
    </div>
    <ol class="flow">
      <li><i>1</i><b>Job order in</b><span>Call, text, email or form</span></li>
      <li><i>2</i><b>Trucks on the road</b><span>The right drivers, fast</span></li>
      <li><i>3</i><b>Job done</b><span>Every stage tracked</span></li>
      <li><i>4</i><b>Back on the road</b><span>Ready for the next one</span></li>
    </ol>
  </div>
</section>
{CTA}""")

FAQS = [
    ("What is Basin Powered Dispatch?", "A dispatch board for oilfield haulers. Orders come in, drivers get offers on their phone, and operators see truck status live."),
    ("Who is it for?", "Trucking companies running about 10 to 75 trucks (vac, water and fluid haulers) and the operators who hire them."),
    ("What does it cost?", "Free to start. Carriers get their first 30 dispatch hauls free. Operators get their first 10 job orders free. Paid plans scale with fleet size. Ask us on a demo."),
    ("Does it handle billing or payments?", "No. We stick to dispatch. No money runs through the platform, and your billing stays how it is today."),
    ("Can operators and carriers both use it?", "Yes. Carriers dispatch their own drivers. Operators can see who's available, pick a carrier or send a job to all of them."),
    ("Where do you work?", "We're starting in the Permian Basin and expanding from there."),
    ("How do I join?", "Tap Try it free, tell us if you're a carrier or an operator, and we'll get you set up. No contract."),
    ("Can I try it first?", "Yes. The demo is a sample hauling company you can click through as the dispatcher, a driver or an operator. Nothing is real and nothing gets sent."),
]

PAGES["faq.html"] = ("FAQ · Basin Powered Dispatch",
"Common questions about Basin Powered Dispatch.", f"""
<section class="hero small">
  <div class="wrap">
    <div class="eyebrow">FAQ</div>
    <h1>Quick answers.</h1>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="faq">
      {"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS)}
    </div>
    <div class="bot-slot">
      <h3>Still have a question?</h3>
      <p>Ask our assistant below.</p>
      <!-- SUPPORT BOT: paste the bot's embed snippet here -->
    </div>
  </div>
</section>
{CTA}""")

PAGES["demo.html"] = ("Try the Demo · Basin Powered Dispatch",
"Click through Basin Powered Dispatch as a dispatcher, driver or operator.", """
<section class="hero">
  <div class="wrap grid">
    <div>
      <div class="eyebrow">Try the demo</div>
      <h1>Click through it yourself.</h1>
      <p class="lead" style="margin-top:18px">A sample hauling company with 14 drivers and three weeks of work. Be the dispatcher, a driver or the operator.</p>
      <ul class="checks" style="color:#fff">
        <li>Nothing is real. No texts or emails go out.</li>
        <li>Switch roles any time.</li>
        <li>Takes about two minutes.</li>
      </ul>
    </div>
    <form class="form-card" name="demo-request" method="POST" action="demo-ready.html" data-netlify="true" netlify-honeypot="company-url">
      <input type="hidden" name="form-name" value="demo-request">
      <p class="hidden"><label>Leave blank <input name="company-url"></label></p>
      <h3>Open the demo</h3>
      <p class="sub">Tell us who you are and we'll take you right in.</p>
      <div class="row2">
        <div class="field"><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
        <div class="field"><label for="company">Company</label><input id="company" name="company" required autocomplete="organization"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="type">I'm a&hellip;</label>
          <select id="type" name="type" required><option value="">Choose one</option><option>Carrier / trucking company</option><option>Operator</option><option>Other</option></select></div>
        <div class="field"><label for="trucks">Trucks (optional)</label><input id="trucks" name="trucks" inputmode="numeric"></div>
      </div>
      <button class="btn btn-primary" type="submit">Open the demo &rarr;</button>
      <p class="fine">We'll only use this to follow up about Basin Powered Dispatch.</p>
    </form>
  </div>
</section>""")

PAGES["join.html"] = ("Try It Free · Basin Powered Dispatch",
"Join Basin Powered Dispatch free as a carrier or an operator.", """
<section class="hero">
  <div class="wrap grid">
    <div>
      <div class="eyebrow">Join the network</div>
      <h1>Why wait? Try it free.</h1>
      <p class="lead" style="margin-top:18px">Carriers and operators join free. We'll reach out and get you set up.</p>
      <ul class="checks" style="color:#fff">
        <li>Carriers: free for your first 30 dispatch hauls</li>
        <li>Operators: free for your first 10 job orders</li>
        <li>No contract. No payments run through Basin Powered Dispatch.</li>
      </ul>
    </div>
    <form class="form-card" name="join" method="POST" action="join-thanks.html" data-netlify="true" netlify-honeypot="company-url">
      <input type="hidden" name="form-name" value="join">
      <p class="hidden"><label>Leave blank <input name="company-url"></label></p>
      <h3>Join the network</h3>
      <p class="sub">Takes 30 seconds.</p>
      <div class="field"><label for="jtype">I'm a&hellip;</label>
        <select id="jtype" name="type" required><option value="">Choose one</option><option value="Carrier">Carrier / trucking company</option><option value="Operator">Operator</option></select></div>
      <div class="row2">
        <div class="field"><label for="jname">Name</label><input id="jname" name="name" required autocomplete="name"></div>
        <div class="field"><label for="jcompany">Company</label><input id="jcompany" name="company" required autocomplete="organization"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="jphone">Phone</label><input id="jphone" name="phone" type="tel" required autocomplete="tel"></div>
        <div class="field"><label for="jemail">Email</label><input id="jemail" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="jtrucks">Trucks (carriers)</label><input id="jtrucks" name="trucks" inputmode="numeric"></div>
        <div class="field"><label for="jbasin">Basin</label><select id="jbasin" name="basin"><option>Permian</option><option>Bakken</option><option>Other</option></select></div>
      </div>
      <button class="btn btn-primary" type="submit">Try it free &rarr;</button>
      <p class="fine">We'll only use this to get you set up on Basin Powered Dispatch.</p>
    </form>
  </div>
</section>
<script>
(function(){var t=new URLSearchParams(location.search).get('type');var s=document.getElementById('jtype');
if(t==='carrier')s.value='Carrier';if(t==='operator')s.value='Operator';})();
</script>""")

PAGES["contact.html"] = ("Contact · Basin Powered Dispatch",
"Get in touch with Basin Powered Dispatch.", """
<section class="hero">
  <div class="wrap grid">
    <div>
      <div class="eyebrow">Contact</div>
      <h1>Talk to us.</h1>
      <p class="lead" style="margin-top:18px">Questions, setup help or want a walkthrough? Send us a note and we'll get back to you quickly.</p>
    </div>
    <form class="form-card" name="contact" method="POST" action="contact-thanks.html" data-netlify="true" netlify-honeypot="company-url">
      <input type="hidden" name="form-name" value="contact">
      <p class="hidden"><label>Leave blank <input name="company-url"></label></p>
      <h3>Send us a message</h3>
      <p class="sub">We usually reply the same day.</p>
      <div class="row2">
        <div class="field"><label for="cfirst">First name</label><input id="cfirst" name="first-name" required autocomplete="given-name"></div>
        <div class="field"><label for="clast">Last name</label><input id="clast" name="last-name" required autocomplete="family-name"></div>
      </div>
      <div class="field"><label for="ccompany">Company</label><input id="ccompany" name="company" autocomplete="organization"></div>
      <div class="row2">
        <div class="field"><label for="cphone">Phone</label><input id="cphone" name="phone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="cemail">Email</label><input id="cemail" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="field"><label for="cmsg">Message</label><textarea id="cmsg" name="message" rows="4" required></textarea></div>
      <button class="btn btn-primary" type="submit">Send message &rarr;</button>
    </form>
  </div>
</section>""")

PAGES["contact-thanks.html"] = ("Message sent · Basin Powered Dispatch",
"Thanks for reaching out to Basin Powered Dispatch.", """
<section class="hero">
  <div class="wrap center">
    <div class="eyebrow">Message sent</div>
    <h1>Thanks. We'll be in touch.</h1>
    <p class="lead" style="margin:18px auto 0">In the meantime, take a look around.</p>
    <div class="btns" style="justify-content:center"><a class="btn btn-primary" href="demo.html">Try the demo</a><a class="btn btn-ghost" href="index.html">Back to home</a></div>
  </div>
</section>""")

PAGES["join-thanks.html"] = ("You're on the list · Basin Powered Dispatch",
"Thanks for joining Basin Powered Dispatch.", """
<section class="hero">
  <div class="wrap center">
    <div class="eyebrow">You're in</div>
    <h1>Thanks. We'll be in touch.</h1>
    <p class="lead" style="margin:18px auto 0">We'll call or text you shortly to get you set up. Want a look in the meantime?</p>
    <div class="btns" style="justify-content:center"><a class="btn btn-primary" href="demo.html">Try the demo</a></div>
  </div>
</section>""")

PAGES["demo-ready.html"] = ("You're in · Basin Powered Dispatch",
"Opening the Basin Powered Dispatch demo.", f"""
<section class="hero">
  <div class="wrap center">
    <div class="eyebrow">You're in</div>
    <h1>Opening the demo&hellip;</h1>
    <p class="lead" style="margin:18px auto 0">If it doesn't open in a few seconds, tap below.</p>
    <div class="btns" style="justify-content:center"><a class="btn btn-primary" href="{APP}/demo/">Open the demo</a></div>
  </div>
</section>
<script>setTimeout(function(){{location.href="{APP}/demo/"}},2500)</script>""")

PAGES.pop("faq.html", None)  # FAQ hidden for now
out = Path(__file__).parent
for fname, (title, desc, body) in PAGES.items():
    active = fname
    (out / fname).write_text(head(title, desc) + header(active) + body + FOOTER, encoding="utf-8")
    print("wrote", fname)
