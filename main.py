import api
import extract


def process_commands(commands, message):
    for command in commands:
        if command == "/start":
            chat_id = extract.chat_id(message)
            api.send_message(chat_id, "Купи слона!")


def process_message(message):
    text = extract.text(message)
    if text:
        reply = f"Все говорят \"{text}\", а ты купи слона!"
        api.send_message(extract.chat_id(message), reply)


def run_event_loop():
    print("The bot is running...")
    offset = 0
    polling_interval = 3  # seconds

    while True:
        try:
            updates = api.get_updates(offset, polling_interval)
            offset = extract.last_offset(updates) + 1
            for update in updates:
                message = extract.message(update)
                commands = extract.commands(message)
                if commands:
                    process_commands(commands, message)
                else:
                    process_message(message)
        except Exception as e:
            print("ERROR:", e)


if __name__ == "__main__":
    run_event_loop()
