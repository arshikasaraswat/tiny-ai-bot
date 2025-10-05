print("Running Wikipedia Q&A Bot")

import wikipedia

def ask_question(question):
    try:
        return wikipedia.summary(question, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=2)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("🤖 Wikipedia Q&A Bot")
    print("Type 'exit' anytime to quit.\n")

    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break
        answer = ask_question(question)
        print("Bot:", answer, "\n")