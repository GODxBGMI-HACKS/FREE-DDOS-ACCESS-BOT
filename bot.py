from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your bot's API token
TOKEN = 'YOUR_BOT_API_TOKEN'
# Replace with your channel and group chat IDs
CHANNEL_ID = '@GODxBGMI_HACKS'
GROUP_CHAT_ID = '@GODxBGMI_CHATGROUP'

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    
    # Check if user is a member of the channel
    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            # User is a member of the channel
            update.message.reply_text(f"Hello, {user_name}! You have access to the group chat.")
            # Optionally add user to the group chat here
            # context.bot.add_chat_members(GROUP_CHAT_ID, user_id)
        else:
            # User is not a member of the channel
            update.message.reply_text("You need to join the channel to access the group chat.")
    except Exception as e:
        update.message.reply_text("An error occurred while checking membership.")
        print(e)

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
