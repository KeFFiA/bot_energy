from bot.logging_settings import logger
from database import DB


async def create_user(user_id: str, user_name: str, user_surname: str = None, username: str = None):
    db = DB()
    if await user_exists(user_id):
        db.insert(table='users', objects='user_id, user_name, username, user_surname',
                  value=f'"{user_id}", "{user_name}", "{username}", "{user_surname}"')
        logger.info(f"New User: {user_name} with ID: {user_id}")
    else:
        logger.info(f"User: {user_name} with ID: {user_id} is already registered")


async def user_exists(user_id: str) -> bool:
    db = DB()
    try:
        check_user_id = db.view(table='users', objects='user_id', where='user_id', value=f'{str(user_id)}')[0]
    except:
        logger.error('Error in the area of adding a user to the database', exc_info=True)
        return True
    for i in check_user_id:
        try:
            if user_id in i:
                return False
            else:
                return True
        except:
            logger.error('Error in the area of adding a user to the database', exc_info=True)
            return True
