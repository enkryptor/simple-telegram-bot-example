def last_offset(updates: list[dict]) -> int:
    """ Extract last update id """
    if not updates:
        return 0
    last_update = updates[-1]
    return last_update["update_id"]


def chat_id(message: dict) -> int:
    """ Extract chat id from message """
    return message["chat"]["id"]


def commands(message: dict) -> list:
    """ Extract commands from message """

    def get_command(entity, text):
        offset = entity["offset"]
        length = entity["length"]
        return text[offset:offset + length]

    if not "entities" in message:
        return []

    entities = [x for x in message["entities"] if x["type"] == "bot_command"]
    return [get_command(entity, message["text"]) for entity in entities]


def message(update: dict) -> dict:
    """ Extract message from update """
    return update["message"]


def text(message: dict) -> str:
    """ Extract text from message """
    return message.get("text")
