def process_data(data):
    processed_users = []

    for user in data:
        processed_user = {
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]
        }

        processed_users.append(processed_user)

    return {
        "total_users": len(processed_users),
        "users": processed_users
    }