from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    #All the tkinter layout code must be put in the __init__ function
    # the attribute quizbrain takes input of data type Quizbrain 
    def __init__(self, quizbrain: QuizBrain ):
        #Creating the tknter interface 
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizdom")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(
            150,
            125, 
            #to help the text wrap in the canvas to fit we use a slightly smaller width than the that of the canvas
            width=280,
            text="some questions", 
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(0,20))

        
        #Labels
        self.score_label = Label(text="Score: 0", font=("Arial", 10, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=10)

        #Buttons
        self.true_img = PhotoImage(file="Quizzler\images\\true.png")
        self.true_btn = Button(image=self.true_img, command=self.check_true, highlightthickness=0, )
        self.true_btn.grid(column=0, row=2)

        self.false_img = PhotoImage(file="Quizzler\images\\false.png")
        self.false_btn = Button(image=self.false_img, command=self.check_false, highlightthickness=0, )
        self.false_btn.grid(column=1, row=2)
        
        #Since everything that appears in the interface has to come before the mainloop(), we call the method next_question here
        self.get_next_question()
        

        self.window.mainloop()
    
    def get_next_question(self):
        #On next question the canvas bg must change to white
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            #Chnage the score
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # q_text get hold of the next queston method from the quiz that contain the Quizbrain class
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="The quiz has reached it's end.")
            #When the quiz reaches it's end the buttons are disabled from working 
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")    

    def check_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)
    #the feedback from the function will be a color change

    def check_false(self):
        #Store the returned answer in the variable is_right the call the feedback method to give feed back to user
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
        #the feedback from the function will be a color change

    def give_feedback(self, is_correct):
        """This checked for the answer and gives feedback to the user"""
        #When buttons are clicked true=green, false=red, new_question=white
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)