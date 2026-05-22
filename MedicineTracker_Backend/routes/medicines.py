FROM medicines m
JOIN familymembers f ON m.member_id = f.member_id
JOIN categories c ON m.category_id = c.category_id