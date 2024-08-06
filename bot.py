from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot's API token
TOKEN = '7153969610:AAEJL8OImaL2A75BrW2JLoPh3lJcME_fKXg'
# Replace with your channel and group chat IDs
CHANNEL_ID = '@GODxBGMI_HACKS'
GROUP_CHAT_ID = '@GODxBGMI_CHATGROUP'

# To store user IDs
user_ids = set()

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    
    # Check if user is a member of the channel
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            user_ids.add(user_id)
            await update.message.reply_text(f"Hello, {user_name}! You have access to the group chat.")
        else:
            await update.message.reply_text("You need to join the channel to access the group chat.")
    except Exception as e:
        await update.message.reply_text("An error occurred while checking membership.")
        print(e)

async def forward_to_all(update: Update, context: CallbackContext) -> None:
    # Only allow the command for admin users (optional)
    if update.effective_user.id not in [1132426169]:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    # Get the message to forward
    if context.args:
        message_text = ' '.join(context.args)
        for user_id in user_ids:
            try:
                await context.bot.send_message(chat_id=user_id, text=message_text)
            except Exception as e:
                print(f"Failed to send message to {user_id}: {e}")
        await update.message.reply_text("Message forwarded to all users.")
    else:
        await update.message.reply_text("Please provide a message to forward.")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("forward", forward_to_all))

    application.run_polling()

if __name__ == '__main__':
    main()
