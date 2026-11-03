#!/usr/bin/env python3
"""Generates one page per project (project-<slug>.html), reusing the header,
contact block and footer from index.html. Run: python3 build_projects.py

Everything written here comes from what each live site actually says.
Edit the PROJECTS list below to change a page, then re-run this script.
"""
import re

home = open('index.html').read()
HEAD = home[:home.index('<body>') + 6]
grab = lambda a, b: home[home.index(a):home.index(b, home.index(a)) + len(b)]
fix = lambda s: re.sub(r'href="#', 'href="./#', s).replace('href="#top"', 'href="#top"')
NAV = fix(grab('<header class="nav">', '</header>')).replace('href="./#top"', 'href="./"')
CONTACT = grab('<section class="contact" id="contact">', '</section>')
FOOT = fix(grab('<footer class="footer">', '</footer>')).replace('href="./#top"', 'href="#top"')
TAIL = '\n<script src="script.js"></script>\n</body>\n</html>\n'
ARROW = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
EXT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 17L17 7M8 7h9v9"/></svg>'

PROJECTS = [
 dict(slug='estateguard', img='work-estateguard.jpg', url='https://estateguard-azure.vercel.app/',
  name='EstateGuard', descriptor='Government Housing & Rent Payment Platform', chip='Platform Landing Page',
  summary='A landing page for EstateGuard, a platform where verified government employees find approved homes and pay rent by approving a prompt on their phone.',
  facts=[('Industry', 'Housing & rent payments'), ('Project type', 'Platform landing page'), ('Audience', 'Verified government employees')],
  brief=['EstateGuard offers a new way to rent a home, and it is aimed at one specific audience: verified government employees.',
         'The site has to explain the offer in seconds, show how rent is paid, and build trust in a service that involves both housing and money.'],
  scope=['Landing page design and development', 'Messaging and page structure', 'Calls to action for visitors at different stages', 'Responsive build for phones and desktops'],
  execution=[
   ('One-line message', ['The headline, "Earn your salary. Pay your home directly.", states the offer at once. A sentence below says who it is for and how it works: find approved homes and pay rent by approving a prompt on your phone.']),
   ('Trust signals', ['The page puts its safeguards where visitors can see them:'],
     ['Identity-verified tenants and landlords', 'Inspected properties', 'Digital tenancy agreements', 'Mobile-money or bank approval', 'Digital receipts and daily payment checks', 'A tamper-evident audit trail']),
   ('Two ways in', ['Two calls to action match two levels of readiness: "Request a briefing" for visitors who want to learn more, and "Get started" for those ready to begin.'])],
  outcomes=[('What visitors can do', ['Understand the offer from the headline alone', 'See how rent is paid and what protects both sides', 'Request a briefing or get started straight away'])],
  shows='Taking a service that involves trust, money and housing and turning it into a page that explains itself in seconds.'),

 dict(slug='checin', img='work-checin.jpg', url='https://checin-6982.vercel.app/',
  name='ChecIN', descriptor='Attendance Platform Website', chip='Product Website',
  summary='A product website for ChecIN, an attendance tool where a QR code on an entrance tablet changes every 15 seconds and employees scan it with their phones.',
  facts=[('Industry', 'Workforce & HR technology'), ('Project type', 'Product website'), ('Status', 'Pilot teams being onboarded')],
  brief=['Most attendance tools trust the employee\'s phone. ChecIN trusts the door. That difference is the whole product, so the site has to make it clear very quickly.',
         'It also has to speak to everyone who touches attendance, from employees to finance, and move interested teams toward a free trial.'],
  scope=['Product website design and development', 'Product messaging and feature explanation', 'Pricing section with three plans', 'FAQ and calls to action', 'Responsive build'],
  execution=[
   ('Making the idea obvious', ['The headline, "Attendance that proves people were actually there.", leads straight into how it works: a code on an entrance tablet changes every 15 seconds, so there is no GPS to spoof, no screenshot to pass around and no timesheets to chase.']),
   ('Features and benefits', ['The page explains the product in plain benefits, such as "Less chasing. More clarity.", and lists four core capabilities:'],
     ['Real-time attendance with a live team view', 'Leave and absence management', 'Announcements and team updates', 'Tamper-resistant records']),
   ('One platform for everyone', ['A section speaks to the roles behind attendance: owners and HR, team managers, employees, operations, finance and leadership.']),
   ('Pricing and questions', ['Three plans are laid out clearly: a free Starter plan for small teams, a per-user Growth plan with a monthly and yearly toggle, and a custom Enterprise plan. A FAQ answers the questions buyers ask first, such as whether a screenshot can be used to check in for someone else.'])],
  outcomes=[('What visitors can do', ['Start a free trial or open the live kiosk', 'Compare the three plans', 'Get answers on hardware, apps and data separation', 'Ask to join the launch program'])],
  shows='Explaining a product with a clear single idea, and guiding different kinds of buyers to the right next step.'),

 dict(slug='samuel-adanuvo', img='work-sammy.jpg', url='https://sammy-drab.vercel.app/',
  name='Samuel Adanuvo', descriptor='Personal Brand & Speaking Website', chip='Personal Brand Site',
  summary='A personal brand website for a business growth consultant, author and keynote speaker, built to bring in consulting clients and speaking invitations.',
  facts=[('Industry', 'Consulting, speaking & education'), ('Project type', 'Personal brand website'), ('Main actions', 'Book a call, book a talk')],
  brief=['Samuel Adanuvo is a consultant, author, speaker and event host. His website has to present all of that clearly, without leaving a visitor unsure where to start.',
         'Two actions matter most: booking a free strategy call, and booking him to speak.'],
  scope=['Website design and development', 'Content structure for consulting, speaking, events and a book', 'Enquiry form with enquiry types', 'Video, testimonial and FAQ sections', 'Responsive build'],
  execution=[
   ('A confident first screen', ['The headline, "The literal cheat code for business growth.", sits beside a one-line description of his roles and two buttons: "Book a free strategy call" and "Book Samuel to speak".']),
   ('Proof early on', ['Three numbers appear near the top: 120+ young leaders at a summit, 2000+ young entrepreneurs reached, and 5+ years convening events.']),
   ('Clear offers', ['Consulting is presented as "The Growth Engine", with six pillars: clarity, visibility, conversion, acceleration, loyalty and handover. Speaking has its own section with topics and booking.']),
   ('Events, video and the book', ['Past and upcoming events, a set of video insights, client testimonials, and a waitlist for his book keep the site active and give visitors reasons to return.']),
   ('Easy enquiries', ['The contact form lets visitors choose why they are writing (consulting, speaking, events or other), and the page states how quickly the team replies.'])],
  outcomes=[('What visitors can do', ['Book a free strategy call', 'Book Samuel to speak', 'See past events and what is coming next', 'Watch video insights and read client testimonials', 'Join the waitlist for his book'])],
  shows='Presenting one person with several roles as a single, clear brand, and sending each type of visitor to the right action.'),

 dict(slug='solara-residence', img='work-solara.jpg', url='https://solara-three-gamma.vercel.app/',
  name='Solara Residence', descriptor='Luxury Apartment Development Website', chip='Concept Build',
  summary='A website for a luxury apartment development in East Legon Hills, Accra, covering available homes, floors, amenities, the investment case and build progress.',
  facts=[('Industry', 'Real estate development'), ('Project type', 'Property development website'), ('Status', 'Concept build')],
  brief=['A property development has to do several jobs at once: show what is for sale, make a case for buying, and prove the building is really going up.',
         'The site was built to let a buyer or investor explore all of that in one place and end with an enquiry.'],
  scope=['Website design and development', 'Interactive floor finder', 'Investment simulator', 'Construction progress tracker', 'Developer comparison and enquiry form', 'Responsive build'],
  execution=[
   ('Finding a home', ['A unit inventory shows each apartment type with its price, how many are left and a booking button. An interactive floor finder lets visitors select a floor on the building facade to see what is there.']),
   ('Making the case', ['An investment section explains why the area is attractive and includes a simulator: choose a unit type and a timeframe, and see an estimated value and return.']),
   ('Building trust', ['A construction tracker shows overall completion and each stage from groundbreaking to finishing. A comparison table sets the project beside two other developments from the same developer.']),
   ('Turning interest into an enquiry', ['A registration form captures the details and the unit of interest, and a booking preview explains how a deposit locks a unit.'])],
  outcomes=[('What visitors can do', ['Compare unit types and prices', 'Explore the building floor by floor', 'Estimate a return on investment', 'Follow construction progress', 'Register interest in a unit'])],
  shows='Turning a large, detailed property offer into something a buyer can explore step by step, with proof at every stage.'),

 dict(slug='sena-academy', img='work-sena.jpg', url='https://sena-academy-lms-ten.vercel.app/',
  name='Sena Academy', descriptor='AI Design Course Platform', chip='In Development',
  summary='A platform for selling and delivering a course on creating websites with AI design tools, currently in development.',
  facts=[('Industry', 'Online education'), ('Project type', 'Course and learning platform'), ('Status', 'In development')],
  brief=['Sena Academy teaches people to design websites using AI tools, aimed at founders, designers and marketers.',
         'The site needs to explain what the course covers, show the templates that come with it, and let people choose a plan.'],
  scope=['Course platform website', 'Curriculum and templates presentation', 'Pricing plans', 'FAQ and calls to action'],
  execution=[
   ('Selling the skill', ['The page leads with a clear promise: learn to build AI-designed websites in a few days, with no coding required.']),
   ('Showing what is inside', ['A curriculum lists the lessons from first AI website to full projects, alongside page blueprints, launch checklists and a set of ready-made templates.']),
   ('Choosing a plan', ['Two plans are shown side by side, one for the course and one that adds unlimited templates and motion videos.'])],
  outcomes=[('What visitors will be able to do', ['See what the course covers', 'Browse the included templates', 'Choose a plan and get started'])],
  shows='Presenting an education product so that visitors can see what they would learn and what they would get.'),
]


def li(items):
    return '<ul class="pp__list">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


for n, p in enumerate(PROJECTS):
    prev_p, next_p = PROJECTS[n - 1], PROJECTS[(n + 1) % len(PROJECTS)]
    facts = ''.join(f'<div><small>{k}</small><b>{v}</b></div>' for k, v in p['facts'])
    brief = ''.join(f'<p>{t}</p>' for t in p['brief'])
    exe = ''
    for blk in p['execution']:
        h, paras = blk[0], blk[1]
        exe += f'<h3>{h}</h3>' + ''.join(f'<p>{t}</p>' for t in paras) + (li(blk[2]) if len(blk) > 2 else '')
    out = ''.join(f'<h3>{h}</h3>{li(items)}' for h, items in p['outcomes'])
    body = f'''<main class="pp" id="top">
  <a class="pp__back" href="./#projects"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>All projects</a>
  <header class="pp__head in-load">
    <span class="chip">{p['chip']}</span>
    <h1 class="h2">{p['name']} <span class="grad">— {p['descriptor']}</span></h1>
    <p>{p['summary']}</p>
    <div class="pp__actions"><a class="btn btn--light" href="{p['url']}" target="_blank" rel="noopener"><span>Visit the live site</span>{EXT}</a><a class="btn btn--dark" href="./#contact"><span>Start your project</span>{ARROW}</a></div>
  </header>
  <img class="pp__shot" src="img/{p['img']}" alt="{p['name']} website">
  <div class="pp__facts" data-reveal>{facts}</div>
  <section class="pp__sec" data-reveal><h2>Brief</h2><div>{brief}</div></section>
  <section class="pp__sec" data-reveal><h2>Scope of Work</h2><div>{li(p['scope'])}</div></section>
  <section class="pp__sec" data-reveal><h2>Execution</h2><div>{exe}</div></section>
  <section class="pp__sec" data-reveal><h2>Outcomes</h2><div>{out}</div></section>
  <section class="pp__sec" data-reveal><h2>What This Project Shows</h2><div><p>{p['shows']}</p></div></section>
  <nav class="pp__nav" aria-label="More projects">
    <a href="project-{prev_p['slug']}.html"><small>Previous</small><b>{prev_p['name']}</b></a>
    <a href="project-{next_p['slug']}.html"><small>Next</small><b>{next_p['name']}</b></a>
  </nav>
</main>'''
    head = re.sub(r'<title>.*?</title>', f"<title>{p['name']} – TrueCraft</title>", HEAD)
    head = re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{p["summary"]}">', head)
    head = re.sub(r'<meta property="og:title"[^>]*>', f'<meta property="og:title" content="{p["name"]} – {p["descriptor"]}">', head)
    open(f"project-{p['slug']}.html", 'w').write(head + '\n' + NAV + '\n' + body + '\n' + CONTACT + '\n' + FOOT + TAIL)
print('built', len(PROJECTS), 'project pages')
