# SheltrX Instagram strategy

Account: @sheltrx (Instagram Professional), posted through the Windsor.ai connector.
Audience: everyone, Zomato-style. Relate everyday life to where people live: PG, hostel, flat, housing society, gate, guard, neighbours, deliveries, visitors. Brand page, not an information page.
Approval: nothing is posted without Dhiraj's explicit "approve" in the Claude app.

## Content: the character (LOCKED)

Every post stars **Shel** (working name), the purple character drawn by `tools/shel.py`. Do not redesign him; reference sheet: `brand/shel_character_sheet.jpg`.

- He is 24, an office guy with a daily 9-to-5 and everyday problems.
- Each post: something happening in the world (trend, big news, geopolitics, viral story, a wild fact) shown through how it hits HIS ordinary life.
- The SheltrX product is never shown or pitched. Only the small "sheltrx" name on each post. The page should make people curious about what SheltrX is.
- Language: Hinglish.

Guardrails (proposed, pending Dhiraj's confirmation):
- No taking sides on parties, politicians or religion; only the effect of news on his life.
- No jokes about tragedies, deaths or disasters.
- Every news item and fact is verified against a source before posting; the source link goes to Dhiraj with the approval request.
- On trend days, the 4 PM run offers 2-3 options; Dhiraj picks one.

## Schedule (all times IST)

| What | When | Approval request sent |
| --- | --- | --- |
| Feed post (carousel or single image, no reels for now) | Mon, Wed, Fri, Sun at 7:00 PM | Same day, 4:00 PM |
| Story of that post (9:16 cover + "Naya post feed par") | Right after the post goes live | Together with the post |
| Festival / special-day story from SheltrX | 7:00 AM on the day | 12:00 AM (midnight) the night before |
| Monthly list of festivals and special days | Start of every month | Dhiraj approves the list |

## Rules

- If a post is not approved by 7:00 PM, it is not posted that day.
- 4 posts a week. Reels later, when a social media person joins.
- Story via the API cannot share the feed post or carry link/mention stickers; it is an image only.
- Images: JPEG, 1080x1350 for posts, 1080x1920 for stories, hosted in this repo under `posts/YYYY-MM-DD/`.
- Slides are built with `tools/make_slides.py`.
