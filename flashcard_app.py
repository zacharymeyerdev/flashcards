import tkinter as tk
from tkinter import messagebox
import random

class Flashcard:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        self.learned = False

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard App")
        self.flashcards = []
        self.current_card = None
        self.flipped = False

        self.prompt_label = tk.Label(master, text="", font=("Arial", 24))
        self.prompt_label.pack(pady=50)

        self.flip_button = tk.Button(master, text="Flip", command=self.flip_card)
        self.flip_button.pack(side=tk.LEFT, padx=10)

        self.learned_button = tk.Button(master, text="Mark as Learned", command=self.mark_learned)
        self.learned_button.pack(side=tk.RIGHT, padx=10)

        self.next_card_button = tk.Button(master, text="Next Card", command=self.next_card)
        self.next_card_button.pack(pady=10)

        self.load_flashcards()
        self.next_card()

    def load_flashcards(self):
        # Sample flashcards, you can extend this or load from a file
        self.flashcards.append(Flashcard("What is the capital of France?", "Paris"))
        self.flashcards.append(Flashcard("What is 2 + 2?", "4"))
        self.flashcards.append(Flashcard("What is the largest ocean?", "Pacific Ocean"))

    def next_card(self):
        self.flipped = False
        if self.flashcards:
            remaining_cards = [card for card in self.flashcards if not card.learned]
            if remaining_cards:
                self.current_card = random.choice(remaining_cards)
                self.prompt_label.config(text=self.current_card.prompt)
            else:
                messagebox.showinfo("No more cards", "You have learned all the flashcards!")
        else:
            messagebox.showinfo("No more cards", "You have learned all the flashcards!")

    def flip_card(self):
        if self.current_card:
            if self.flipped:
                self.prompt_label.config(text=self.current_card.prompt)
            else:
                self.prompt_label.config(text=self.current_card.answer)
            self.flipped = not self.flipped

    def mark_learned(self):
        if self.current_card:
            self.current_card.learned = True
            self.next_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
