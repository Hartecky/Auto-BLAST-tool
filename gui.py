from appJar import gui

# FUNCTIONS FOR BUTTONS
def press(name):
    if name == "Cancel":
        app.stop()
    elif name == "Clear":
        app.clearEntry("Sequence")
        app.clearEntry("Organism")
        app.setFocus("Sequence")


def submit(name):
    if name == "Submit Auto-Blast":
        seq = app.getEntry("Sequence")
        org = app.getEntry("Organism")

        '''
        TODO:
        - connect this button with a main function
        - set interface to make app more eye-friendly
        - add to gui option with max target sequence
        '''

# GUI
app = gui("Auto-Blast Tool", "400x600")
app.setBg("green")
app.setFont(16)
app.setResizable(False)
app.addLabel("title", "Auto Blast Tool")


app.addLabelEntry("Sequence")
app.addLabelEntry("Organism")

app.addButton("Submit Auto-Blast", submit)
app.addButtons(["Clear", "Cancel"], press)
app.go()
