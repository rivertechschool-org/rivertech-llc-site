from html import escape

OPPORTUNITIES = [{'id': 'property',
  'tab': 'Property',
  'group': 'Provide the foundation',
  'title': 'Provide a home.',
  'intro': 'Help provide a home for a River Tech school, Tink Town, or both. We are looking for practical '
           'space in North Idaho that can be approved for the activities it will actually host.',
  'how': 'A zoning designation and an occupancy approval answer different questions. Planning must allow the '
         'use; building and fire officials must approve the building for it. An office, retail unit or '
         'church building is not automatically ready for a school or a café and workshop.',
  'bring': ['Address, floor plan, room dimensions and the intended use: school, Tink Town or both.',
            'Existing zoning, certificate of occupancy, sprinkler and alarm information, and any prior '
            'approvals.',
            'Availability, rent expectations, parking, utilities and willingness to make necessary '
            'improvements.'],
  'agree': ['Written confirmation of permitted uses and the route to building, fire and health approvals.',
            'A viable classroom layout or café/workshop plan, including costs of any conversion.',
            'Rent, lease length, responsibility for improvements and the conditions that must be met before '
            'occupancy.'],
  'step': 'Send the address and floor plan first. We can screen the fit, then discuss the property with the '
          'relevant officials before agreeing to a lease.',
  'cta': 'Tell us about your property',
  'blocks': [{'title': 'For a River Tech school',
              'body': 'Our planning target is an average of about 15 students per teaching classroom. Some '
                      'rooms may accommodate 12 if larger rooms keep the school-wide classroom average near '
                      '15. This is our operating requirement, not a legal occupancy formula.',
              'items': ['School use must be permitted by the zoning district or approved through the '
                        'required land-use process. There is not one universal “school zoning” label.',
                        'Classroom layouts must fit students, a teacher, furniture and clear circulation. '
                        'The building official determines permitted occupant loads; room dimensions and '
                        'exits matter.',
                        'Confirm educational occupancy approval, including any change-of-use permit and '
                        'certificate of occupancy required for the premises.',
                        'Check compliant exits and travel paths, emergency lighting and signs, alarms, '
                        'extinguishers, fire separations, and sprinklers where required.',
                        'Check accessible entry and circulation, suitable toilets, ventilation, lighting, '
                        'and safe arrival and pickup arrangements.']},
             {'title': 'For Tink Town',
              'body': 'Tink Town can begin without a dedicated venue, then grow into a small public hub and eventually a fuller café and workshop. The requirements below describe that fuller facility, not a day-one lease. See the three-phase launch plan on the Tink Town page.',
              'items': ['Front of house: café counter and seating, a place to discuss projects and display finished work, and flexible space for workshops and events.',
                        'Work areas: desks for design, AI and marketing work; a clean print-production and finishing area; and a dedicated 3D-printing area.',
                        'Fabrication: enclosed space for laser cutters, a waterjet, CNC routers and mills, metal bending, assembly and finishing. Separate noise, dust, fumes and production traffic from customers and food.',
                        'Support space: sheet and stock storage, paper and consumables, loading and receiving, finished orders, toilets and staff facilities.',
                        'Our working allocation is 1,500 sq ft for fabrication, marketing printing and 3D printing combined, with materials storage allocated separately. Confirm the selected machines and their operating and service clearances against a floor plan.',
                        'Assess electrical service, floor loading, delivery-door sizes, ventilation and dust extraction, compressed air, and water and drainage requirements for the chosen equipment.',
                        'Confirm permission for the full mix of café, retail, classes, events and fabrication. A commercial or flex-industrial property with an approved public-facing area may be a better fit than a conventional storefront.',
                        'In Post Falls, Community Commercial Services is a starting point to investigate for restaurant, retail and education uses; the actual fabrication processes need a separate use determination.',
                        'Obtain the applicable building, fire and food-service approvals. A café requires health review; cooking and fabrication equipment may require dedicated ventilation or fire protection.']},
             {'title': 'Fire protection: check the building, not just its listing',
              'body': 'Sprinkler requirements depend on the occupancy, fire area, occupant load, floor level '
                      'and local amendments. The 2018 model code includes Group E school triggers such as a '
                      'fire area over 12,000 square feet and certain spaces below the exit-discharge level. '
                      'Mixed café, event and workshop uses can trigger different requirements. A small '
                      'school is not automatically exempt. Obtain a property-specific determination from the '
                      'building and fire officials.',
              'items': []}],
  'sources': [('Post Falls zoning summary',
               'https://www.postfalls.gov/DocumentCenter/View/638/Zoning-Codes-PDF'),
              ('Post Falls Building Division', 'https://www.postfalls.gov/175/Building'),
              ('Idaho adopted building codes',
               'https://dopl.idaho.gov/wp-content/uploads/2025/06/2025-Updated-Idaho-Adopted-Codes.pdf'),
              ('Idaho State Fire Marshal codes',
               'https://doi.idaho.gov/state-fire-marshal/statutes-rules-codes-and-standards/'),
              ('ICC fire-protection guidance, including Group E',
               'https://www.iccsafe.org/wp-content/uploads/Session-363-2018-IFC-and-IBC-Fire-Protection-Systems.pdf'),
              ('Panhandle Health District food establishments',
               'https://panhandlehealthdistrict.org/licensing-and-permitting/food-establishments/'),
              ('NIOSH safe 3D printing guide',
               'https://www.cdc.gov/niosh/publications/numbered/2024-103.html')]},
 {'id': 'equipment',
  'tab': 'Equipment',
  'group': 'Provide the foundation',
  'title': 'Equip the work.',
  'intro': 'Help equip a place where a sketch can become a part, an idea can become a prototype, and a '
           'business can get useful work done.',
  'how': 'We are building toward a complete path from idea to finished work: design it, fabricate it, print it and put it to use. Start with software, creative work and modest print equipment; add 3D printing and fabrication as demand supports them. The list below describes the wider capability we can grow toward, not a day-one shopping list.',
  'bring': ['Equipment you own or would consider funding, including model, condition and specifications.',
            'What it can make or enable, purchase cost and availability.',
            'Power, ventilation, space, maintenance and operator-training requirements.'],
  'agree': ['Ownership, lease payments, duration and any purchase or return option.',
            'Installation, safe operation, training and consumables.',
            'Maintenance, insurance, damage and any proposed use by participating schools.'],
  'step': 'Tell us what capability you could help provide. We will match it to likely projects and operating '
          'needs before committing to equipment.',
  'cta': 'Discuss an equipment idea',
  'blocks': [{'title': 'Digital fabrication',
              'body': 'SendCutSend shows the kind of capability we want to bring within reach locally. Our equipment plan includes:',
              'items': ['Fiber laser cutters for precision metal parts, signs, brackets and panels.',
                        'CO₂ laser cutters for suitable materials such as acrylic and wood.',
                        'Abrasive waterjet cutters for composites and other materials that need a different cutting process.',
                        'CNC routers for wood, plastics and composite panels; CNC mills for three-dimensional parts machined from solid stock.',
                        'CNC press brakes for bending sheet metal, plus deburring, tapping, countersinking, hardware insertion and finishing tools.',
                        'Documented SendCutSend examples include AMADA ENSIS 3015 AJ and VENTIS 3015 AJ fiber lasers, an AMADA EGB 6020 press brake and OMAX waterjet equipment. These are reference examples, not a final purchasing list.']},
             {'title': 'Marketing print production',
              'body': 'The everyday usefulness of a print shop: help a business design its message, then produce the materials that carry it.',
              'items': ['A production color printer or digital press for flyers, brochures, business cards, menus and booklets.',
                        'Wide-format printing for posters, banners, signs and displays; vinyl cutting for lettering and decals.',
                        'Trimming, folding, creasing, binding, laminating and mounting equipment for a professional finished result.',
                        'Design workstations, color-management tools, paper and media storage, and clean space for finishing and packing.']},
             {'title': '3D printing and prototyping',
              'body': 'Filament and resin 3D printers for prototypes, models, replacement parts and custom products, matched to the material and performance each job needs. Include washing and curing equipment where needed, material storage, measuring tools and finishing benches.'},
             {'title': 'AI, robotics and creative work',
              'body': 'Computers and software for design, automation and AI-assisted work; robotics and electronics equipment for projects; cameras, sound, lighting and editing tools for marketing content, courses and events.'}]},
 {'id': 'lending',
  'tab': 'Lending',
  'group': 'Provide the foundation',
  'title': 'Finance the next step.',
  'intro': 'Help finance a defined stage of development through a business loan. The idea is a clear '
           'interest arrangement and a visible local purpose, without requiring you to buy ownership.',
  'how': 'Our working proposal is 6% annual interest, subject to a credible repayment plan, agreed terms and '
         'appropriate review. The goal is interest income alongside local impact, rather than '
         'stock-market-style ownership upside.',
  'bring': ['The approximate amount and lending period you would consider.',
            'Your preferred payment timing and whether you would need access to the money early.',
            'The information you would need to assess the purpose, repayment plan and risks.'],
  'agree': ['The borrower, permitted use of funds and conditions before release.',
            'The final interest rate, interest calculation, payment schedule, maturity and early repayment '
            'terms.',
            'Any security or guarantees, reporting, missed-payment provisions and the applicable legal '
            'requirements.'],
  'step': 'Discuss the proposed rate and purpose with us. No money should change hands until the repayment '
          'plan, risks and final loan documents are agreed.',
  'cta': 'Discuss a potential loan',
  'blocks': [{'title': 'Working proposal: 6% a year',
              'body': 'For illustration, $10,000 outstanding for a full year at 6% simple annual interest '
                      'would accrue $600 before tax. This illustrates the proposed rate; it does not set '
                      'payment frequency, fees, compounding or a commitment to lend or borrow.'},
             {'title': 'A business loan, not a savings account',
              'body': 'Savings rates vary, so we do not promise to match or beat them. A loan to our '
                      'business would not have bank-deposit insurance. Repayment depends on the business, '
                      'and some or all of the capital could be lost.'}]},
 {'id': 'projects',
  'tab': 'Projects',
  'group': 'Put talent to work',
  'title': 'Bring it in. Let’s make it happen.',
  'intro': 'A part you need made. A business that needs a fresh look. Hours lost to repetitive work. Bring '
           'us something concrete to improve.',
  'how': 'We start with a design, a sketch, a sample or a walkthrough of how your business works. Then we '
         'identify a useful first result, quote the work we can deliver and agree how to judge it. These '
         'services form our intended starting offer as Tink Town develops.',
  'bring': ['A file, sketch, sample, existing website or example of a task that wastes time.',
            'The result you need, quantities or scope, deadline and budget range.',
            'Material or quality requirements, and any systems the work would need to connect to.'],
  'agree': ['A specific deliverable or pilot, with price, timing and acceptance criteria.',
            'Materials, manufacturing limits, revisions and ownership of the resulting work.',
            'Permission to use necessary information, privacy and human checks for automated work.'],
  'step': 'Send one example: the part, the page, the process or the problem. We will begin with what would '
          'make a useful difference, then scope a practical first project.',
  'cta': 'Tell us about your challenge',
  'blocks': [{'title': 'Design it. Print it. Make it.',
              'body': 'Bring your own 3D model, a broken part, a sketch or an idea. We can explore design '
                      'assistance, prototypes, custom fixtures, display pieces and replacement parts. '
                      'Materials, tolerances and suitability must be checked; cutting or machining may be '
                      'sourced from a specialist.'},
             {'title': 'Bring your business’s image forward',
              'body': 'Videos, websites, advertising creative, product photography and a refreshed visual '
                      'identity. The aim is to help customers understand your business and see the quality '
                      'of what you do.'},
             {'title': 'Find the work that should not take so long',
              'body': 'Review intake, quoting, scheduling, customer follow-up, data entry and document '
                      'handling. Identify waste, test AI or automation where it fits, and use robotics where '
                      'physical tasks justify it. Compare time, cost and quality before and after; keep '
                      'human review where judgment matters.'}]},
 {'id': 'hiring',
  'tab': 'Hiring',
  'group': 'Put talent to work',
  'title': 'Hire emerging talent.',
  'intro': 'Find people who can think, communicate, build and use emerging technology. We are exploring an '
           'employer-paid placement service alongside our education and project work.',
  'how': 'A business describes a real role. With the candidate’s permission, we identify a potential fit '
         'using skills, work samples and relevant experience. The employer interviews and makes the hiring '
         'decision.',
  'bring': ['The role, work involved, skills, location and expected start date.',
            'Hours, compensation range and supervision or training available.',
            'Your hiring process and the evidence you need to evaluate a candidate.'],
  'agree': ['The employer’s written placement terms, fee trigger and any replacement or refund arrangement.',
            'Candidate consent and appropriate handling of applications and work samples.',
            'Employment conditions and any age, safety or supervision requirements.'],
  'step': 'Share a role description. We can explore the fit and a fair employer-paid fee before arranging '
          'introductions.',
  'cta': 'Tell us about a role',
  'blocks': [{'title': 'A placement fee, paid by the employer',
              'body': 'Our proposed model is a fixed success fee agreed before an introduction and payable '
                      'when a qualifying hire starts. The candidate would not pay the placement fee. Fee '
                      'amounts, qualifying introductions and any replacement or refund terms remain to be '
                      'defined.'},
             {'title': 'See what people can actually do',
              'body': 'Projects can provide evidence of practical ability: a working prototype, an '
                      'automation, a video, a website or a record of reliable teamwork. School participation '
                      'alone is not a guarantee of readiness for a particular job.'}]},
 {'id': 'training',
  'tab': 'Training',
  'group': 'Build capability together',
  'title': 'Multiply what your team can do.',
  'intro': 'Teach your people to use AI and automation on the work they actually do. Less time copying, '
           'chasing and formatting; more time thinking, serving customers and moving the business forward.',
  'how': 'Begin with a short workflow review, choose a repetitive task, measure the current effort, then '
         'teach and implement a better way. The goal is a working improvement, not a presentation everyone '
         'forgets. Tenfold gains are an ambition for suitable tasks, not a promised result for every '
         'employee or business.',
  'bring': ['One task or workflow that is slow, repetitive or difficult to manage.',
            'Who performs it, their experience and the tools they already use.',
            'Group size, preferred format, timing, budget and the result you want to measure.'],
  'agree': ['The chosen workflow, learning outcomes and any implementation deliverables.',
            'The venue, instructor, approved tools and rules for company or customer data.',
            'Price, follow-up support and how the improvement will be measured.'],
  'step': 'Tell us what your administrator or team spends too much time doing. We will explore a workshop or '
          'pilot built around that task.',
  'cta': 'Discuss training for your team',
  'blocks': [{'title': 'AI for the everyday administrator',
              'body': 'Turn meeting notes into actions, draft replies for review, summarize documents, '
                      'prepare reports and organize repeatable office work. Staff leave with workflows they '
                      'can use, plus rules for checking accuracy and protecting information.'},
             {'title': 'Agentic Mindset',
              'body': 'A proposed core course: break work into clear tasks, decide what to automate or '
                      'delegate to an AI agent, set boundaries, check the result and improve the process. '
                      'Learn to direct technology with judgment rather than simply ask it questions.'},
             {'title': 'A business improvement sprint',
              'body': 'Map intake, quoting, scheduling or customer follow-up. Identify a bottleneck, build a '
                      'small pilot and train the people who will use it. Measure time saved, errors, quality '
                      'and the amount of human oversight required.'}]},
 {'id': 'events',
  'tab': 'Events',
  'group': 'Build capability together',
  'title': 'Bring your team into what’s next.',
  'intro': 'Give your people an evening worth talking about: good food, emerging technology, useful ideas '
           'and a practical challenge to take back to work.',
  'how': 'We are developing a recurring Tink Town gathering for local businesses: part dinner, part keynote '
         'and demonstration, part team exercise. The aim is to make learning about the future a normal, '
         'enjoyable part of business life.',
  'bring': ['Your team or audience, likely group size and the theme that would matter to them.',
            'Whether you want a private company session, a public event or recurring participation.',
            'Timing, budget and anything you could contribute, such as a speaker, demonstration or '
            'catering.'],
  'agree': ['The date, venue, food, agenda and learning or relationship goal.',
            'Hosting responsibilities, ticketing or sponsorship price, promotion and attendee information.',
            'Equipment, accessibility, safety, cancellation terms and any follow-up session.'],
  'step': 'Tell us who you would bring and what they should leave ready to do. We can shape a pilot evening '
          'before setting a recurring schedule.',
  'cta': 'Suggest an event or workshop',
  'blocks': [{'title': 'Proposed series: Agentic Mindset evenings',
              'body': 'A monthly or quarterly format to explore: dinner and conversation, a focused keynote '
                      'with a live demonstration, then a guided group exercise. Each team leaves with one '
                      'practical experiment to try before the next session.'},
             {'title': 'A place to be part of the future',
              'body': 'Meet other local builders, try emerging tools and see what businesses are making '
                      'possible. Your company can host clients, bring its staff, sponsor an evening or '
                      'co-create a workshop with us.'},
             {'title': 'From interesting evening to useful habit',
              'body': 'Possible themes include AI for office work, better customer follow-up, '
                      'design-to-prototype, and deciding when an agent or robot is the right tool. Recurring '
                      'sessions can revisit what teams tried and what actually improved.'}]}]

def property_space_plan():
    schedules = [
        ('School: about 90 students', 'Six teaching rooms averaging 15 students, with staggered lunches and no dedicated gym or auditorium.', [
            ('Six classrooms, about 500 sq ft each', 3000), ('Lunch / multipurpose room', 900),
            ('Indoor recess / student hangout', 600), ('Principal, staff and board / conference room', 600),
            ('Storage and utility space', 400), ('Restrooms', 300), ('Hallways, walls and circulation', 1500)
        ]),
        ('Tink Town: café, shop and production', 'A compact operation with a small performance stage, modest café kitchen and a selected mix of fabrication and printing equipment.', [
            ('Café seating and small stage', 1000), ('Kitchen, counter and preparation', 500),
            ('Robotics, components and maker-supply retail', 500), ('Fabrication, marketing printing and 3D printing combined', 1500),
            ('Design workstations and collaborative work', 800), ('Materials, receiving and order storage', 700),
            ('Restrooms and utility space', 400), ('Additional circulation and walls', 1300)
        ])
    ]
    detail = ''
    for title, description, rows in schedules:
        body = ''.join(f'<tr><th scope="row">{escape(label)}</th><td>{area:,}</td></tr>' for label, area in rows)
        detail += f'<details class="space-schedule"><summary>{escape(title)} — room-by-room plan</summary><p>{escape(description)}</p><table><thead><tr><th scope="col">Space</th><th scope="col">Sq ft</th></tr></thead><tbody>{body}</tbody><tfoot><tr><th scope="row">Illustrative total</th><td>{sum(area for _, area in rows):,}</td></tr></tfoot></table></details>'
    return f'''<section class="property-space-plan" aria-labelledby="space-plan-title">
<span class="eyebrow">A practical starting point</span><h3 id="space-plan-title">The space to make it work.</h3>
<p>Three ways to give the vision a home. The Tink Town and combined-site figures describe the fuller facility—not the space needed to launch. These working estimates include indoor support space and circulation; parking and outdoor recreation space are additional.</p><p><a href="tink-town.html#growth">See how Tink Town can start small and grow through three phases ↗</a></p>
<div class="space-table-wrap"><table class="space-overview"><thead><tr><th scope="col">Location</th><th scope="col">Compact planning range</th><th scope="col">Preferred search range</th></tr></thead><tbody>
<tr><th scope="row">River Tech school</th><td>7,000 sq ft</td><td>8,000–9,000 sq ft</td></tr>
<tr><th scope="row">Tink Town · fuller hub</th><td>6,500–7,000 sq ft</td><td>7,500–9,000 sq ft</td></tr>
<tr><th scope="row">School + Tink Town</th><td>12,000–13,000 sq ft</td><td>14,000–17,000 sq ft</td></tr>
</tbody></table></div>
{detail}
<details class="space-schedule"><summary>Combined location — how sharing saves space</summary><p>The two illustrative plans total 14,000 sq ft. Sharing about 1,500 sq ft through a kitchen, lunch / performance room, conference space and selected support areas gives a compact example of <strong>12,500 sq ft</strong>. Around <strong>14,000 sq ft</strong> is our starting search target, with more room where the layout or growth plans call for it.</p><p>Shared rooms need compatible schedules. The school needs controlled access, and fabrication must be separated from students, customers and food service.</p></details>
<p class="space-plan-note">These are planning estimates, not approved building plans or legal occupancy limits. The 1,500 sq ft production allowance must be checked against selected equipment, safe working clearances and material flow. Final capacity depends on the property layout and required approvals.</p>
</section>'''

def build_opportunity_hub(link):
    tabs=[]
    panels=[]
    for i,o in enumerate(OPPORTUNITIES):
        key=o['id']; selected='true' if i==0 else 'false'
        tabs.append(f'<button class="opportunity-tab" id="tab-{key}" role="tab" aria-controls="panel-{key}" aria-selected="{selected}" tabindex="{0 if i==0 else -1}" type="button" data-path="{key}"><span class="tab-number">0{i+1}</span>{o["tab"]}</button>')
        items=lambda xs: ''.join(f'<li>{escape(x)}</li>' for x in xs)
        blocks=''.join(f'<article class="opportunity-focus"><h3>{escape(b["title"])}</h3><p>{escape(b["body"])}</p>'+ (f'<ul>{items(b["items"])}</ul>' if b.get('items') else '')+'</article>' for b in o.get('blocks',[]))
        sources=''
        if o.get('sources'):
            links=''.join(f'<li><a href="{escape(url,quote=True)}" target="_blank" rel="noopener">{escape(label)} ↗</a></li>' for label,url in o['sources'])
            sources=f'<details class="property-sources"><summary>Property guidance and sources</summary><p>Screening guidance for North Idaho, researched October 2026. Requirements depend on the address, jurisdiction, existing approvals and proposed activities. Confirm the property with planning, building, fire and health officials before committing.</p><ul>{links}</ul></details>'
        panels.append(f'''<section class="opportunity-panel" id="panel-{key}" role="tabpanel" aria-labelledby="tab-{key}"{'' if i==0 else ' hidden'}>
<div class="opportunity-head"><span class="eyebrow">0{i+1} / {escape(o['group'])}</span><h2>{escape(o['title'])}</h2><p class="lead">{escape(o['intro'])}</p></div>
<div class="opportunity-how"><h3>How this could work</h3><p>{escape(o['how'])}</p></div>
{property_space_plan() if key == "property" else ""}
<div class="opportunity-focus-list">{blocks}</div>
<div class="opportunity-details"><div><h3>Bring to the first conversation</h3><ul>{items(o['bring'])}</ul></div><div><h3>Agree before starting</h3><ul>{items(o['agree'])}</ul></div></div>
{sources}
<div class="opportunity-next"><div><span class="eyebrow">Your first step</span><p>{escape(o['step'])}</p></div>{link(o['cta'],f'contact.html?topic={key}','button')}</div>
</section>''')
    return '<section class="section opportunity-section" id="opportunities"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Seven ways to build with us</span><h2>Find your place.<br>Take the first step.</h2></div><p>Choose an opportunity to see the practical details. These are starting points for discussion; Tink Town remains in development.</p></div><div data-opportunity-hub><div class="opportunity-tabs" role="tablist" aria-label="Ways to build with us">'+''.join(tabs)+'</div>'+''.join(panels)+'</div></div></section>'
