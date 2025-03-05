import tkinter as tk
import random

# Thai consonants dictionary: {Thai character: Romanized pronunciation}
thai_consonants = {
    "ก": "ko kai", "ข": "kho khai", "ฃ": "kho khuad", "ค": "kho khwai", "ฅ": "kho khon",
    "ฆ": "kho rakhang", "ง": "ngo ngu", "จ": "cho chan", "ฉ": "cho ching", "ช": "cho chang",
    "ซ": "so so", "ฌ": "cho choe", "ญ": "yo ying", "ฎ": "do cha-da", "ฏ": "to pa-tak",
    "ฐ": "tho than", "ฑ": "tho montho", "ฒ": "tho phu-thao", "ณ": "no nen", "ด": "do dek",
    "ต": "to tao", "ถ": "tho thung", "ท": "tho thahan", "ธ": "tho thong", "น": "no nu",
    "บ": "bo baimai", "ป": "po pla", "ผ": "pho phueng", "ฝ": "fo fa", "พ": "pho phan",
    "ฟ": "fo fan", "ภ": "pho sam-phao", "ม": "mo ma", "ย": "yo yak", "ร": "ro rua",
    "ล": "lo ling", "ว": "wo waen", "ศ": "so sala", "ษ": "so rue-si", "ส": "so suea",
    "ห": "ho hip", "ฬ": "lo chu-la", "อ": "o ang", "ฮ": "ho nok-huk"
}

class ThaiFlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcard Game")
        self.root.geometry("400x300")

        self.current_char = None
        self.current_answer = None

        # Thai character label
        self.label = tk.Label(root, text="", font=("Arial", 48), fg="black")
        self.label.pack(pady=20)

        # Input field
        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack()
        self.entry.bind("<Return>", self.check_answer)  # Press Enter to check

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 14))
        self.feedback_label.pack()

        # Check Answer Button
        self.check_button = tk.Button(root, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

        # Next Button
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)

        # Start game with first flashcard
        self.next_card()

    def next_card(self):
        """Show a new random Thai consonant."""
        self.current_char, self.current_answer = random.choice(list(thai_consonants.items()))
        self.label.config(text=self.current_char)
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self, event=None):
        """Check if the user input is correct."""
        user_input = self.entry.get().strip().lower()
        if user_input == self.current_answer.lower():
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(text="❌ Try again!", fg="red")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = ThaiFlashcardGame(root)
    root.mainloop()