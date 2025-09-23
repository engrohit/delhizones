import json

with open("database/posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

def is_site_post(post):
    content = " ".join(post.get("content", []))
    # Check for required site fields
    return (
        "Site ID" in content and
        "Lat,Long" in content and
        "Site Name" in content
    )

site_posts = [post for post in posts if is_site_post(post)]

with open("database/posts.json", "w", encoding="utf-8") as f:
    json.dump(site_posts, f, ensure_ascii=False, indent=2)

print(f"Kept {len(site_posts)} site posts.")