#!/usr/bin/env python3
"""Generates the inner pages (about, projects, blogs, contact, 3 case studies)
re-using the header / FAQ / contact / footer blocks from index.html.
Run: python3 build.py
"""
import re

home = open('index.html').read()
HEAD = home[:home.index('<body>') + 6]
grab = lambda a, b: home[home.index(a):home.index(b, home.index(a)) + len(b)]
NAV = grab('<header class="nav">', '</header>')
FAQ = grab('<section class="faq">', '</section>')
CONTACT = grab('<section class="contact" id="contact">', '</section>')
FOOT = grab('<footer class="footer">', '</footer>')
TAIL = '\n<script src="script.js"></script>\n</body>\n</html>\n'
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def page(name, title, body, active=''):
    head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', HEAD)
    nav = NAV
    if active:
        nav = nav.replace(f'href="{active}"', f'href="{active}" class="on"')
    open(name, 'w').write(head + '\n' + nav + '\n' + body + '\n' + FOOT + TAIL)


def phead(chip, line1, line2, p=''):
    return f'''<section class="phero">
  <span class="chip">{chip}</span>
  <h1 class="h2"><em>{line1}</em> <span class="grad">{line2}</span></h1>
  {f'<p class="muted">{p}</p>' if p else ''}
</section>'''


# ---------------- projects ----------------
cards = re.findall(r'<article class="project reveal">.*?</article>', home, re.S)
projects = phead('Featured', 'Our', 'Projects') + '<section class="projects projects--page">' + '\n'.join(cards) + '</section>'
page('projects.html', 'Projects – Agenciy', projects + FAQ + CONTACT, 'projects.html')

# ---------------- blogs ----------------
posts = [
    ('blog-1', 'UI Trends in Design', 'Design principles are the...', 'June 2025'),
    ('blog-2', 'Designing Trends', 'What’s in, what’s out and...', 'March 2025'),
    ('blog-3', 'Sketch to Screen', 'How raw ideas evolve into...', 'April 2024'),
    ('blog-4', 'Minimal is not Empty', 'Crafting impact with less...', 'May 2025'),
    ('blog-5', 'The Art of Visual', 'How to design narratives...', 'June 2024'),
]
cards_html = ''.join(f'''<a href="#" class="post reveal"><div class="post__img"><img src="img/{i}.png" alt="{t}"></div>
  <div class="post__meta"><h3>{t}</h3><p>{d}</p></div><div class="post__date"><small>Date</small><span>{dt}</span></div></a>''' for i, t, d, dt in posts)
page('blogs.html', 'Blog – Agenciy', phead('Blog', 'Our Featured', 'Blog Insights') + f'<section class="posts">{cards_html}</section>', 'blogs.html')

# ---------------- contact ----------------
form = '''<section class="cpage">
  <div class="phero phero--tight"><span class="chip">Contact</span><h1 class="h2"><em>Let's Create</em><br><span class="grad">Together</span></h1></div>
  <form class="cform" onsubmit="event.preventDefault();this.querySelector('button').textContent='Message Sent ✓'">
    <div class="cform__row"><label>First Name<input type="text" placeholder="First name" required></label><label>Last Name<input type="text" placeholder="Last name" required></label></div>
    <label>Your Email ID<input type="email" placeholder="Enter the e-mail" required></label>
    <label>What's the type of your company?<select required><option value="" disabled selected>Select the type of your company</option><option>SAAS</option><option>Agency</option><option>Business</option><option>Banking</option><option>Other</option></select></label>
    <label>What you need from us?<select required><option value="" disabled selected>Select the Services Needed</option><option>App Design</option><option>Web Design</option><option>Branding</option><option>Development</option><option>Others</option></select></label>
    <label>More About The Project<textarea rows="4"></textarea></label>
    <button class="btn btn--light" type="submit">Send Message</button>
  </form>
</section>'''
page('contact.html', 'Contact – Agenciy', form + FAQ, 'contact.html')

# ---------------- about ----------------
svc = [
    ('/01', 'UI/UX Design', 'Focus on user-first interfaces that are both beautiful and intuitive. We create intuitive, user-first designs that guide and engage. Our UI/UX approach blends strategy and visual clarity. From wireframes to final polish, every detail serves a purpose. Custom, in depth design systems for scalable products.', 'Starts at $1200'),
    ('/02', 'Brand Identity', 'Create visual identities that align with your voice and make lasting impressions.', ''),
    ('/03', 'Web Development', 'Develop high-performance websites and apps built to grow with you.', ''),
    ('/04', 'Digital Marketing', 'Craft data-driven campaigns that attract, engage, and convert — across channels.', ''),
]
acc = ''.join(f'''<details class="acc"{' open' if k == 0 else ''}><summary><span>{n}</span><b>{t}</b><i></i></summary>
  <div><p>{d}</p>{f'<em class="price-tag">{pr}</em>' if pr else ''}</div></details>''' for k, (n, t, d, pr) in enumerate(svc))
jobs = [
    ('Optivus Digital', 'Senior UX Designer', '2021-Present', 'Optivus Digital inspired to spark creativity and its lightweight build slips effortlessly into best.'),
    ('Pixelnest Studio', 'UI/UX Designer', '2016 - 2020', 'Collaborated with senior designers to create wireframes, UI mockups, and prototypes.'),
    ('Aura & Co.', 'Visual Designer', '2010-2015', 'In Aura Designed brand identity kits including, social media creatives, and visual templates.'),
]
jobs_html = ''.join(f'<article class="job reveal"><div><h3>{c}</h3><small>{r}</small></div><span>{y}</span><p>{d}</p></article>' for c, r, y, d in jobs)
about = f'''<section class="phero"><span class="chip">Who We Are</span><h1 class="agency-word"><img src="img/logo-big.png" alt="Agenciy"></h1></section>
<section class="about about--page">
  <span class="chip">About Us</span>
  <p class="about__text" data-words>We help ambitious brands and startups build digital products that stand out and scale. We believe in working smart, building fast, and designing with purpose. We craft digital solutions that not only look good but perform exceptionally. Our team thrives on innovation and turning bold ideas into meaningful impact.</p>
  <div class="stats">
    <div><small>Projects Launced</small><b data-count="140">140+</b></div>
    <div><small>Years Of Experience</small><b data-count="10">10+</b></div>
    <div><small>Happy Clients</small><b data-count="50">50+</b></div>
  </div>
</section>
<section class="section mission">
  <div class="mission__l"><span class="chip">Built With Passion</span><h2 class="h2"><em>Your Growth,</em><br><span class="grad">Our Mission</span></h2><a href="contact.html" class="btn btn--light">Let's Connect {ARROW}</a></div>
  <div class="mission__r">{acc}</div>
</section>
<section class="section expertise">
  <div class="head head--split head--bottom"><div><span class="chip chip--abs">Our Expertise</span><h2 class="h2">Our Expertise That<br><em>Creatively Evolves</em></h2></div>
  <p class="muted head__p">We’ve grown through every challenge and collaboration. Each step has sharpened our skills and broadened our impact.</p></div>
  <div class="jobs">{jobs_html}</div>
</section>'''
page('about.html', 'About – Agenciy', about + FAQ + CONTACT, 'about.html')

# ---------------- case studies ----------------
cases = [
    dict(slug='the-news', name='The News', h1a='The', h1b='News', sub='A mobile app designed to help users get the stories that matter most.',
         hero='news-hero', img2='news-2', tags=['Web & App Design', 'Responsive Frontends'],
         o1='This project centered on reinventing the brand’s digital identity across both web and mobile platforms. The goal was to create a cohesive, user-first experience that would elevate their online presence and support their growth across digital channels. Working closely with stakeholders, we defined key objectives around usability, aesthetics and performance. From the earliest wireframes to final delivery, every step was driven by strategy and storytelling. Our role was to bridge this gap by building a design system that seamlessly aligned with the brand voice while prioritizing usability. We began by conducting workshops and discovery sessions to align with stakeholder goals, define the user journey, and map key actions that drive conversions. This formed the backbone of our strategy moving forward.',
         o2='In a fast-moving digital landscape, the brand approached us with a clear mission — to reimagine their presence across both web and mobile platforms in a way that not only captured their identity but also supported future scalability. Their existing digital experience was fragmented, slow, and lacked visual consistency, making it difficult to convert users or retain engagement.',
         h2t='Design & Frontend Approach',
         p2='Once the strategy was locked in, we shifted into design and development. Our UX process began with low-fidelity wireframes and prototypes to map interaction, hierarchy and information flow. Once validated, we transitioned into high-fidelity UI design in Figma, crafting components that would later form the basis of a unified design system.',
         bullets=['Fully responsive UI', 'Pixel-perfect frontend', 'Scalable design system'], h3t='Responsive Experience',
         p3='Creating a responsive, device-agnostic interface was a central priority throughout the project. With users accessing the platform from a wide range of screen sizes — from desktop monitors to tablets and mobile phones — we adopted a mobile-first design philosophy. All components were developed with fluid grids, flexible containers, and dynamic breakpoints to ensure seamless rendering on every device. Extensive testing was done across modern browsers, OS types and real-world devices to validate the performance, layout integrity, and user experience. We also optimized page speed and UI responsiveness using techniques like lazy loading, minified assets and prefetching. The result: a smooth, accessible experience no matter how or where the user engages.'),
    dict(slug='theo-agency-re-branding', name='Theo Agency', h1a='Theo', h1b='Agency', sub='Reimagining a creative brand for the next era of digital storytelling.',
         hero='theo-hero', img2='theo-2', tags=['Brand Identity', 'SEO'],
         o1='This project focused on redefining the brand’s identity to create a fresh, compelling presence that resonates across all touchpoints. The aim was to develop a cohesive and memorable visual language that reflects the brand’s values while positioning it for future growth. Collaborating closely with stakeholders, we established clear objectives around brand messaging, visual consistency, and audience engagement. From initial concept exploration to the final rollout, every phase was guided by strategic insight and creative storytelling. Our role was to translate the brand’s essence into a unified design system that could be applied seamlessly across marketing materials, digital platforms, and product experiences. We started with discovery workshops and stakeholder interviews to align on vision, define core narratives, and identify opportunities for differentiation. This foundation became the driving force behind a bold and authentic rebrand.',
         o2='In a rapidly evolving market, the brand came to us with a focused goal — to reinvent their identity in a way that authentically reflected their core values while positioning them for long-term growth. Their previous branding felt outdated, inconsistent, and disconnected across channels, which hindered recognition and customer loyalty. The challenge was to create a unified, flexible brand system that could adapt seamlessly across all touchpoints and resonate deeply with both existing and new audiences.',
         h2t='Immersive Experience Design',
         p2='Once the strategy was finalized, we moved into the creative and implementation phases. Our design process began with mood boards and initial brand concepts to explore visual direction, tone, and style. After stakeholder approval, we developed comprehensive brand guidelines and refined assets, including logos, typography, and color palettes. These elements formed the foundation of a cohesive brand system, ensuring consistency across all future applications and touchpoints.',
         bullets=['Flexible Layouts', 'Adaptive Brand Assets', 'Fluid Layouts'], h3t='Brand Engagement',
         p3='Ensuring a flexible, device-agnostic brand presence was a key focus throughout the rebranding process. With audiences interacting across a variety of platforms—ranging from large desktops to smartphones—we embraced a mobile-first approach to design. All visual elements and layouts were crafted using scalable grids, adaptable containers, and responsive breakpoints to maintain brand integrity and clarity on any screen. Rigorous testing was conducted across multiple browsers, operating systems, and real-world devices to confirm consistent appearance and performance. Additionally, we optimized asset delivery and loading speeds through techniques like lazy loading and asset compression. The outcome: a cohesive, engaging brand experience that resonates seamlessly wherever users connect.'),
    dict(slug='virtual-reality-encounter', name='Virtual Reality Encounter', h1a='Virtual', h1b='Reality', sub='Futuristic tech meets fearless design — branding for the next-gen AR headset.',
         hero='vr-hero', img2='vr-2', tags=['Brand Identity', 'Web Development'],
         o1='This project focused on redefining the virtual reality encounter to deliver a more immersive, emotionally engaging, and intuitive user experience. The objective was to craft a seamless blend of storytelling and interaction that would resonate deeply with users and push the boundaries of digital engagement. Collaborating closely with stakeholders, we identified key goals around immersion, accessibility, and performance optimization. From early concept sketches to high-fidelity prototypes, every phase was guided by a commitment to user-centric design and narrative cohesion. Our role was to bridge the gap between technology and emotion by designing a VR experience that was not only visually compelling but also intuitive and impactful. We initiated the process with in-depth discovery sessions and user flow mapping to define key interactions, understand user motivations, and ensure alignment with strategic objectives. This foundation shaped a compelling and cohesive experience from start to finish.',
         o2='In an evolving landscape of immersive technology, the brand came to us with a clear vision — to reimagine their virtual reality encounter in a way that not only reflected their core identity but also laid the groundwork for future innovation. Their existing VR experience felt disjointed, lacked narrative cohesion, and struggled to fully engage users on an emotional or interactive level. The challenge was to transform this fragmented environment into a seamless, intuitive journey that could captivate audiences and scale with advancing technology.',
         h2t='Visual Identity & Component Architecture',
         p2='Once the strategy was finalized, we moved into the design and development of the virtual reality experience. Our UX process began with low-fidelity spatial sketches and interaction flows to define user movement, engagement points, and environmental hierarchy. After validating core interactions, we advanced to high-fidelity 3D prototypes, focusing on immersive UI elements and tactile feedback. These designs laid the foundation for a cohesive VR design system that seamlessly blended visual storytelling with intuitive user interaction.',
         bullets=['Precision-Perfect', '3D Interface', 'VR Compatibility'], h3t='Real-Time Environmental Feedback',
         p3='Ensuring real-time environmental feedback was a core focus throughout the development of the virtual reality experience. In immersive spaces, users expect their actions—whether through gaze, gesture, or motion—to instantly influence their surroundings. To meet this expectation, we engineered responsive interaction loops that delivered immediate visual, auditory, and haptic feedback. Dynamic environmental cues—like lighting changes, object animations, and spatial audio—were triggered based on real-time input to reinforce user presence and immersion. We conducted extensive testing across multiple VR platforms and hardware configurations to validate latency, synchronization accuracy, and the consistency of user feedback. Performance optimizations such as lightweight shaders, level-of-detail adjustments, and input prediction algorithms helped maintain fluid responsiveness.'),
]
for c in cases:
    tags = ''.join(f'<span>{t}</span>' for t in c['tags'])
    bl = ''.join(f'<li>{b}</li>' for b in c['bullets'])
    body = f'''<article class="case">
  <header class="case__top"><div class="tags tags--row">{tags}</div><h1 class="h2"><em>{c['h1a']}</em> <span class="grad">{c['h1b']}</span></h1><p class="muted">{c['sub']}</p></header>
  <img class="case__hero" src="img/{c['hero']}.png" alt="{c['name']}">
  <section class="case__sec"><h2>Project Overview</h2><div><p>{c['o1']}</p><p>{c['o2']}</p></div></section>
  <section class="case__sec"><h2>{c['h2t']}</h2><div><p>{c['p2']}</p><ul class="pills">{bl}</ul></div></section>
  <img class="case__img" src="img/{c['img2']}.png" alt="">
  <section class="case__sec"><h2>{c['h3t']}</h2><div><p>{c['p3']}</p></div></section>
  <a href="index.html" class="btn btn--light case__back">Back to Home {ARROW}</a>
</article>'''
    page(f"project-{c['slug']}.html", f"{c['name']} – Agenciy", body + FAQ + CONTACT, 'projects.html')
print('built')
