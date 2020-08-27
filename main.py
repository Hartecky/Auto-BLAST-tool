from appJar import gui
from auto_blast import auto_blast

"""
Main simple GUI to paste or type a sequence with an organism, and then to submit search to Auto-Blast.
"""



# Setting GUI parametres | labels | widgets | buttons etc.
def main():
    def press(name):
        """
        Chooses between Quit and Clear button to run proper function

        :param name: Button name
        """
        if name == "Quit":
            app.stop()

        elif name == "Clear":
            app.clearEntry("Sequence")
            app.clearEntry("Organism")

            app.setFocus("Sequence")


    def submit(name):
        """
        Button responsible for submitting entries to run Auto-Blast

        :param name: Button name
        """
        if name == "Submit Auto-Blast":
            seq = app.getEntry("Sequence")
            org = app.getEntry("Organism")

            auto_blast(seq,org)

    app = gui("Auto-Blast Tool", "450x450")

    app.setBg("green")
    app.setFont(16)
    app.setResizable(False)

    app.addLabel("title", "Auto Blast Tool")


    app.addLabelEntry("Sequence")
    app.addLabelEntry("Organism")

    app.addButton("Submit Auto-Blast", submit)
    app.addButtons(["Clear", "Quit"], press)

    app.go()



if __name__ == '__main__':
    main()
