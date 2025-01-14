from firebase_admin import auth

def get_user_by_id(user_id):
 try:
    user=auth.get_user(user_id)
    return {
        "uid":user.uid,
        "email":user.email
    }
 except auth.UserNotFoundError:
   return None
def list_all_users():
    users = []
    page = auth.list_users()  # Get the first page of users
    while page:
        for user in page.users:
            users.append({
                "uid": user.uid,
                "email": user.email,
            })
        # Get the next page
        page = page.get_next_page()
    return users
def create_user(validated_data):
    user = auth.create_user(
        email=validated_data.email,
        password=validated_data.password
    )
    return {
        "uid": user.uid,
        "email": user.email
    }
