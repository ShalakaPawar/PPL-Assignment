#Name: Shalaka Pawar
#MIS: 111903095
#Division: 2
# Calculator app using Gtk

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CalculatorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Calculator")

        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Calculator"
        self.set_titlebar(headerBar)

        grid = Gtk.Grid()
        self.add(grid)

        self.expression = Gtk.Entry()
        self.expression.set_editable(False)

        grid.attach(self.expression, 0, 0, 10, 1)

        self.result = Gtk.Entry()
        self.result.set_editable(False)

        grid.attach_next_to(self.result, self.expression, Gtk.PositionType.BOTTOM, 10, 1)

        clear = Gtk.Button(label = "C")
        clear.connect("clicked", self.onClearClicked)
        grid.attach_next_to(clear, self.result, Gtk.PositionType.BOTTOM, 1, 1)

        delete = Gtk.Button(label = "<=")
        delete.connect("clicked", self.onDeleteClicked)
        grid.attach_next_to(delete, clear, Gtk.PositionType.RIGHT, 1, 1)

        expo = Gtk.Button(label = "**")
        expo.connect("clicked", self.onExpoClicked)
        grid.attach_next_to(expo, delete, Gtk.PositionType.RIGHT, 1, 1)

        modulo = Gtk.Button(label = "%")
        modulo.connect("clicked", self.onModuloClicked)
        grid.attach_next_to(modulo, expo, Gtk.PositionType.RIGHT, 1, 1)

        reciprocal = Gtk.Button(label = "1/x")
        reciprocal.connect("clicked", self.onReciprocalClicked)
        grid.attach_next_to(reciprocal, clear, Gtk.PositionType.BOTTOM, 1, 1)

        square = Gtk.Button(label = "x**2")
        square.connect("clicked", self.onSquareClicked)
        grid.attach_next_to(square, reciprocal, Gtk.PositionType.RIGHT, 1, 1)

        squareRoot = Gtk.Button(label = "x**(0.5)")
        squareRoot.connect("clicked", self.onSquareRootClicked)
        grid.attach_next_to(squareRoot, square, Gtk.PositionType.RIGHT, 1, 1)

        division = Gtk.Button(label = "/")
        division.connect("clicked", self.onDivisionClicked)
        grid.attach_next_to(division, squareRoot, Gtk.PositionType.RIGHT, 1, 1)

        multiplication = Gtk.Button(label = "*")
        multiplication.connect("clicked", self.onMultiplicationClicked)
        grid.attach_next_to(multiplication, division, Gtk.PositionType.BOTTOM, 1, 1)

        subtraction = Gtk.Button(label = "-")
        subtraction.connect("clicked", self.onSubtractionClicked)
        grid.attach_next_to(subtraction, multiplication, Gtk.PositionType.BOTTOM, 1, 1)

        addition = Gtk.Button(label = "+")
        addition.connect("clicked", self.onAdditionClicked)
        grid.attach_next_to(addition, subtraction, Gtk.PositionType.BOTTOM, 1, 1)

        equalTo = Gtk.Button(label = "=")
        equalTo.connect("clicked", self.onEqualClicked)
        grid.attach_next_to(equalTo, addition, Gtk.PositionType.BOTTOM, 1, 1)

        one = Gtk.Button(label = "1")
        one.connect("clicked", self.onOneClicked)
        grid.attach_next_to(one, reciprocal, Gtk.PositionType.BOTTOM, 1, 1)

        two = Gtk.Button(label = "2")
        two.connect("clicked", self.onTwoClicked)
        grid.attach_next_to(two, one, Gtk.PositionType.RIGHT, 1, 1)

        three = Gtk.Button(label = "3")
        three.connect("clicked", self.onThreeClicked)
        grid.attach_next_to(three, two, Gtk.PositionType.RIGHT, 1, 1)

        four = Gtk.Button(label = "4")
        four.connect("clicked", self.onFourClicked)
        grid.attach_next_to(four, one, Gtk.PositionType.BOTTOM, 1, 1)

        five = Gtk.Button(label = "5")
        five.connect("clicked", self.onFiveClicked)
        grid.attach_next_to(five, four, Gtk.PositionType.RIGHT, 1, 1)

        six = Gtk.Button(label = "6")
        six.connect("clicked", self.onSixClicked)
        grid.attach_next_to(six, five, Gtk.PositionType.RIGHT, 1, 1)

        seven = Gtk.Button(label = "7")
        seven.connect("clicked", self.onSevenClicked)
        grid.attach_next_to(seven, four, Gtk.PositionType.BOTTOM, 1, 1)

        eight = Gtk.Button(label = "8")
        eight.connect("clicked", self.onEightClicked)
        grid.attach_next_to(eight, seven, Gtk.PositionType.RIGHT, 1, 1)

        nine = Gtk.Button(label = "9")
        nine.connect("clicked", self.onNineClicked)
        grid.attach_next_to(nine, eight, Gtk.PositionType.RIGHT, 1, 1)

        dot = Gtk.Button(label = ".")
        dot.connect("clicked", self.onDotClicked)
        grid.attach_next_to(dot, nine, Gtk.PositionType.BOTTOM, 1, 1)

        zero = Gtk.Button(label = "0")
        zero.connect("clicked", self.onZeroClicked)
        grid.attach_next_to(zero, dot, Gtk.PositionType.LEFT, 1, 1)

        plusMinus = Gtk.Button(label = "+/-")
        plusMinus.connect("clicked", self.onPlusMinusClicked)
        grid.attach_next_to(plusMinus, zero, Gtk.PositionType.LEFT, 1, 1)

        return

    def onZeroClicked(self, widget):
        self.setExpression("0")
        return

    def onOneClicked(self, widget):
        self.setExpression("1")
        return

    def onTwoClicked(self, widget):
        self.setExpression("2")
        return

    def onThreeClicked(self, widget):
        self.setExpression("3")
        return

    def onFourClicked(self, widget):
        self.setExpression("4")
        return

    def onFiveClicked(self, widget):
        self.setExpression("5")
        return

    def onSixClicked(self, widget):
        self.setExpression("6")
        return

    def onSevenClicked(self, widget):
        self.setExpression("7")
        return

    def onEightClicked(self, widget):
        self.setExpression("8")
        return 

    def onNineClicked(self, widget):
        self.setExpression("9")
        return

    def onDotClicked(self, widget):
        self.setExpression(".")
        return

    def onExpoClicked(self, widget):
        self.setExpression(" ** ")
        return

    def onModuloClicked(self, widget):
        self.setExpression(" % ")
        return

    def onReciprocalClicked(self, widget):
        self.setExpression("1 / ")
        return

    def onSquareClicked(self, widget):
        self.setExpression(" ** 2 ")
        return

    def onSquareRootClicked(self, widget):
        self.setExpression(" ** (0.5) ")
        return

    def onDivisionClicked(self, widget):
        self.setExpression(" / ")
        return

    def onMultiplicationClicked(self, widget):
        self.setExpression(" * ")
        return

    def onSubtractionClicked(self, widget):
        self.setExpression(" - ")
        return

    def onAdditionClicked(self, widget):
        self.setExpression(" + ")
        return

    def onClearClicked(self, widget):
        self.expression.set_text("")
        self.result.set_text("")
        return

    def onDeleteClicked(self, widget):
        string = self.expression.get_text()
        self.expression.set_text(string[:len(string) - 1])
        return
    
    def setExpression(self, character):
        string = self.expression.get_text() + character
        self.expression.set_text(string)
        return

    def onEqualClicked(self, widget):
        try:
            self.result.set_text(str(eval(self.expression.get_text())))
        except:
            self.result.set_text("Invalid")
        return

    def onPlusMinusClicked(self, widget):
        num = int(self.result.get_text())
        num = -num
        self.result.set_text(str(num))
        return
    
window = CalculatorWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
