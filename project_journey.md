
## 📝 Project Documentation / Development Journey

### Step 1: Setting up the Environment
- Installed Python 3.12 on my system.
- Installed VS Code and set it up for Python development.
- Created a new project folder named `tiny-ai-bot`.

### Step 2: Exploring Options
- Initially tried to use the **OpenAI API** with `openai` library.
- Faced API key setup issues and switched to **Hugging Face** models.
- Encountered multiple `403 Forbidden` errors from Hugging Face API.

### Step 3: Debugging
- Tried changing from `distilbert-base-uncased-distilled-squad` to `roberta-base-squad2`.
- Generated a new Hugging Face token but still received 403 errors.
- Identified that the API access was restricted for free-tier accounts.

### Step 4: Final Approach
- Decided to use the **Wikipedia library** for direct question answering.
- Implemented the Q&A bot successfully using Python and `wikipedia` module.
- Added exception handling for ambiguous queries.
- Verified that the program works for multiple questions.

### Step 5: Documentation and Submission
- Created a detailed `README.md` with setup steps and examples.
- Added an `output.png` screenshot showing successful run.
- Uploaded everything to GitHub.

---

## ✅ Outcome
- Successfully built a working AI-powered Q&A bot using Python.
- Learned about API handling, debugging, and fallback solutions.
- Demonstrated creativity, persistence, and problem-solving.
