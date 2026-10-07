# Project rules

## Development website

Before opening or starting the development website, read [docs/DEV_WEBSITE.md](docs/DEV_WEBSITE.md). It identifies the active worktree, Tailscale access restrictions, and an isolated localhost preview for agents.

## Search indexing and privacy

Only the public marketing/landing page may be indexed by search engines. Optimize that page so users can find the website by the names `DuckProject` and `duckproject.in.th`.

Do not allow search engines to index, cache, archive, or show snippets for any other page or resource, including user profiles, names, email addresses, student IDs, IP addresses, login history, admin pages, SCQuizz sessions and submissions, API responses, uploaded media, or private application data.

- Keep sensitive content behind authentication and authorization. `robots.txt`, `noindex`, and `X-Robots-Tag` are additional safeguards, not access control.
- Apply `index, follow` only to the canonical public landing URL. Apply `noindex, nofollow, noarchive, nosnippet` to every other route and response.
- Redirect `www.duckproject.in.th` to the canonical `https://duckproject.in.th/` URL and do not create duplicate indexed pages.
- Never add personal data to metadata, structured data, sitemaps, page titles, public HTML, public logs, or crawlable URLs.
- When adding a new route, file upload, page, API, sitemap entry, or SEO feature, verify that it cannot expose personal data to Google or another search engine before considering the work complete.
