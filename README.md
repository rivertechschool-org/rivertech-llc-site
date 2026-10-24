# River Tech LLC website

Public website: https://rivertech.llc

River Tech LLC presents its two sister brands, River Tech and Tink Town, and opportunities for schools, businesses, community partners and investors.

## Build

- `python3 build_site.py` builds an unindexed local preview.
- `python3 build_site.py --publish` builds the public HTML, canonical URLs, robots.txt and sitemap.

Content is maintained in `build_site.py`, `experience.py`, `opportunity_content.py`, `concept_story.py`, `tink_growth.py` and `phase_budgets.py`. Styles and interactions are in `assets/css/redesign.css` and `assets/js/redesign.js`.

## Pages

Home; River Tech; Tink Town; Investing; Partnerships; Church & Community; Dream Big; Our Story; Contact; Policies.

The earlier concept, licensing and flagship addresses redirect to the relevant River Tech page sections.

## Publication

GitHub Pages serves the repository root from `main`, using the custom domain in `CNAME`. Build with `--publish` before committing generated files. Keep the accepted content intact and check the actual live site after deployment, including mobile layouts and interactions.

Contact forms prepare an email draft in the visitor's own mail application; they do not submit to a form backend. Do not commit credentials, private records or local review files.

## Tink Town

The Tink Town website is independently hosted at https://tink.town/ from `rivertechschool-org/tink-town-site`. Both sites link to each other. The `tink-town/` folder here contains only redirects for old links; do not restore the former subsite or its assets.
