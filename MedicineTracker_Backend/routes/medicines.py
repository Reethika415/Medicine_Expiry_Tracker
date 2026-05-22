FROM Medicines m
JOIN FamilyMembers f ON m.member_id = f.member_id
JOIN Categories c ON m.category_id = c.category_id