from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# --- 🔑 BOT TOKEN ---
TOKEN = "7964725870:AAEVll5kzeWiu5IOb0Z58W4UbKq8blug5FU"

# --- 🌐 COMPANY PROFILE LINK ---
CANVA_PROFILE_LINK = (
    "https://www.canva.com/design/DAGy386fHMM/kqcp5Ph9XErZ4QQ4Obm9aw/edit?"
    "utm_content=DAGy386fHMM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
)

# --- 🧭 MAIN MENU BUTTONS ---
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📘 Company Profile", url=CANVA_PROFILE_LINK)],
        [InlineKeyboardButton("🎓 Training & Courses", callback_data="courses")],
        [InlineKeyboardButton("📞 Contact Us", callback_data="contact")],
    ]
    return InlineKeyboardMarkup(keyboard)

# --- 🏠 START COMMAND ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the welcome menu."""
    welcome_text = (
        "👋 *Welcome to Lead Forward Academy!*\n\n"
        "Driving Leadership & Business Growth 🚀\n\n"
        "Please choose an option below:"
    )
    await update.message.reply_text(
        welcome_text, parse_mode="Markdown", reply_markup=main_menu()
    )

# --- 🔘 BUTTON ACTIONS ---
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "courses":
        await query.edit_message_text(
            "🎓 *Our Training & Courses:*\n\n"
            "• Leadership Development\n"
            "• Business & Entrepreneurship\n"
            "• HR & People Management\n"
            "• Digital Transformation\n\n"
            "Learn more at [Lead Forward Academy](https://www.leadforward.academy)",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

    elif query.data == "contact":
        await query.edit_message_text(
            "📞 *Contact Lead Forward*\n\n"
            "📧 info@leadforward.academy\n"
            "📍 Koh Pich, Phnom Penh, Cambodia\n"
            "☎️ +855 96 555 9988",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

# --- 💬 HANDLE MESSAGES (Group / Private) ---
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle every text message in group or private chat."""
    if not update.message:
        return

    user = update.message.from_user
    text = update.message.text or ""
    chat_type = update.message.chat.type

    print(f"{user.first_name} said: {text} (in {chat_type})")

    # Example: reply when boss posts something in a group
    if chat_type in ["group", "supergroup"] and user.username == "BossUsername":
        await update.message.reply_text("✅ Message received from the boss!")

# --- 🚀 MAIN FUNCTION ---
def main():
    app = Application.builder().token(TOKEN).build()

    # command and callback handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    # message listener (group + private)
    app.add_handler(MessageHandler(filters.TEXT, handle_messages))

    print("🤖 Lead Forward Bot is running...")
    print("✅ Open Telegram and type /start or send messages in group to test.")

    app.run_polling()

if __name__ == "__main__":
    main()
