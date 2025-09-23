import xml.etree.ElementTree as ET
import json

xml_file = "delhizones.WordPress.2025-09-23.xml"
output_json = "database/posts.json"

def extract_posts(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    channel = root.find("channel")
    posts = []
    for item in channel.findall("item"):
        title = item.findtext("title")
        author = item.findtext("{http://purl.org/dc/elements/1.1/}creator")
        date = item.findtext("{http://wordpress.org/export/1.2/}post_date")
        content_raw = item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded")
        if not content_raw:
            continue
        # Split content into lines, wrap each in <div>
        content_lines = [f"<div>{line.strip()}</div>" for line in content_raw.splitlines() if line.strip()]
        post = {
            "title": title,
            "author": author,
            "date": date,
            "content": content_lines
        }
        posts.append(post)
    return posts

if __name__ == "__main__":
    posts = extract_posts(xml_file)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(posts)} posts to {output_json}")