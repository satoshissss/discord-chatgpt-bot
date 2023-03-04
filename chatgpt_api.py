import openai


def completion(
    new_message_text: str, settings_text: str = "", past_messages: list = []
):
    """
    This function generates a response message using OpenAI's GPT-3 model by taking in a new message text,
    optional settings text and a list of past messages as inputs.

    Args:
    new_message_text (str): The new message text which the model will use to generate a response message.
    settings_text (str, optional): The optional settings text that will be added as a system message to the past_messages list. Defaults to ''.
    past_messages (list, optional): The optional list of past messages that the model will use to generate a response message. Defaults to [].

    Returns:
    tuple: A tuple containing the response message text and the updated list of past messages after appending the new and response messages.
    """
    if len(past_messages) == 0 and len(settings_text) != 0:
        system = {"role": "system", "content": settings_text}
        past_messages.append(system)
    new_message = {"role": "user", "content": new_message_text}
    past_messages.append(new_message)

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=past_messages,
        top_p=1,
        n=1,
        max_tokens=1024,
        temperature=0,
        presence_penalty=0,
        frequency_penalty=0,
    )
    response_message = {
        "role": "assistant",
        "content": result.choices[0].message.content,
    }
    past_messages.append(response_message)
    response_message_text = result.choices[0].message.content
    total_tokens = result.usage.total_tokens
    tokenlog = result.usage
    return (response_message_text, past_messages, total_tokens, tokenlog)
