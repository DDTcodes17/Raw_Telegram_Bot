import os
from dotenv import load_dotenv
from telegram.ext import Application, MessageHandler, filters
from agents import gemini_agent

load_dotenv()

async def reply(update, context):
    result = await gemini_agent.ainvoke(
        {"messages": [{"role": "user", "content": update.message.text}]},
        config = {"configurable":{"thread_id":str(update.effective_chat.id)}}
    )

    await update.message.reply_text(result["messages"][-1].content[0]['text'])

app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()