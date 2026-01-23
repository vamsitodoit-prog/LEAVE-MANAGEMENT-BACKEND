def is_admin(user):
    return user.role in ['ADMIN', 'MANAGER']
