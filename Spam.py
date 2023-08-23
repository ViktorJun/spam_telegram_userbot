from pyrogram import filters, Client
from pyrogram.errors import MessageEmpty
from time import sleep

api_id = your_api_id
api_hash = "your_api_hash"

app = Client("my_acc", api_id, api_hash)

# spam
@app.on_message(filters.command("spam", prefixes=""))
def spam(_, msg):
    msg.delete(msg)
    msg.text = msg.text.lower()
    text = msg.text.split('spam ', maxsplit=1)[1]
    text = text.split()
    try:
        number = int(text[-1])
        spam_text = (" ".join(text[:-1]))
        if number <= 0 or number > 15:
            msg.reply_text("Enter a number between 1 and 15.")
        else:
            a = 0
            while a != number:
                a += 1
                sleep(0.1)
                msg.reply_text(spam_text)
        return
    except ValueError:
        msg.reply_text("Enter an integer.")
        return
    except MessageEmpty:
        msg.reply_text("Enter the text to be spammed.")
        return


app.run()