from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

active_tasks = {}

@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📍 Update Channel", url="https://t.me/xuxlatex"),
            ],
            [
                InlineKeyboardButton("👥 Support Group", url="https://t.me/xuxlatex"),
                InlineKeyboardButton("👩‍💻 Developer", url="https://t.me/xuxlatex"),
            ]
        ]
    )

    start_message = (
        "Hello!\n\n"
        "Send me a ZIP file, and I'll extract it for you. "
        "I also support .RAR, .7z, .tar, and more."
    )

    await message.reply(start_message, reply_markup=reply_markup)


@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = (
        "Here are the commands you can use:\n\n"
        "/start - Start the bot and get the welcome message\n"
        "/help - Get help on how to use the bot\n\n"
        "To unzip a file, simply send me a ZIP file and I will extract its contents and send them back to you.\n\n"
        "©️ Channel : @xuxlatex"
    )

    await message.reply(help_message)


@Client.on_callback_query(filters.regex("cancel_unzip"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer(
            "⛔ Unzipping has been cancelled.",
            show_alert=True
        )
    else:
        await callback_query.answer(
            "⚠️ No ongoing unzip operation.",
            show_alert=True
        )
