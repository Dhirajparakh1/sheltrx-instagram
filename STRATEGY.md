# SheltrX Instagram strategy

Account: @sheltrx (Instagram Professional), posted through the Windsor.ai connector.
Audience: everyone, Zomato-style. Relate everyday life to where people live: PG, hostel, flat, housing society, gate, guard, neighbours, deliveries, visitors. Brand page, not an information page.
Approval: nothing is posted without Dhiraj's explicit "approve" in the Claude app.

## Content: the character (LOCKED)

Every post stars **Shelu**, the purple character drawn by `tools/shel.py`. Do not redesign him; reference sheet: `brand/shel_character_sheet.jpg`.

- He is 24, an office guy with a daily 9-to-5 and everyday problems.
- Each post: something happening in the world (trend, big news, geopolitics, viral story, a wild fact) shown through how it hits HIS ordinary life.
- The SheltrX product is never shown or pitched. Only the small "sheltrx" name on each post. The page should make people curious about what SheltrX is.
- Language: Hinglish.

### What Shelu reacts to
Anything that touches everyday India: cricket and other sport, festivals and pooja, office life, mehngai and money, politics and geopolitics (effect on his life only), tech outages, viral stories, wild facts. Posts and stories are rendered with `tools/make_post.py`.

### Hard rule: no generic memes
Every post must hang on a REAL event from the last 1-3 days (news, outage, match, launch, festival, viral story). A line that could be posted any week ("Monday blues", "Sunday scaries") is rejected. Research must cover world news too (tech outages, aviation, markets, geopolitics), India news, sport, and what is trending on X; pick the biggest story people are already talking about and show its effect on Shelu's life. Verify with 2 sources; drop viral claims that turn out false.

### Who Shelu is
- Name on his office ID: Shailesh. Everyone calls him Shelu (boss says "Shailesh", mummy says "Shelu").
- 24, first job, 9-to-5 in an office, lives away from home in a city, salary gone by the 20th.
- Personality: hopeful every Monday, defeated by Wednesday; overthinks at 2 AM; never mean, never preachy; the joke is always on him, never on a group of people.
- His world (people are heard or implied, never drawn in detail): Boss, Mummy (on phone), flatmate, landlord, the office chai.
- Voice: short spoken Hinglish, one line per post where possible. He reacts; he does not explain the news.
- Signature: every post carries the small lowercase "sheltrx" wordmark. Colours: purple #6856E6, navy #18293D, off-white #F4F2FF.
- Never: product pitch, taking political or religious sides, jokes on tragedies, punching down.

Guardrails (confirmed by Dhiraj):
- No taking sides on parties, politicians or religion; only the effect of news on his life.
- No jokes about tragedies, deaths or disasters.
- Every news item and fact is verified against a source before posting; the source link goes to Dhiraj with the approval request.
- On trend days, the 4 PM run offers 2-3 options; Dhiraj picks one.

## Schedule (all times IST)

| What | When | Approval request sent |
| --- | --- | --- |
| Feed post (carousel or single image, no reels for now) | Mon, Wed, Fri, Sun at 7:00 PM | Same day, by 12:00 noon |
| Story of that post (9:16 cover + "Naya post feed par") | Right after the post goes live | Together with the post |
| Festival / special-day story from SheltrX | 7:00 AM on the day | 12:00 AM (midnight) the night before |
| Monthly list of festivals and special days | Start of every month | Dhiraj approves the list |

## Rules

- If a post is not approved by 7:00 PM, it is not posted that day.
- 4 posts a week. Reels later, when a social media person joins.
- Story via the API cannot share the feed post or carry link/mention stickers; it is an image only.
- Images: JPEG, 1080x1350 for posts, 1080x1920 for stories, hosted in this repo under `posts/YYYY-MM-DD/`.
- Slides are built with `tools/make_slides.py`.
