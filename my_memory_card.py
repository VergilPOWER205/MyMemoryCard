#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint



class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Французкий', 'Испанский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Национальная хижина Якутов?', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

RadioGroupBox = QGroupBox('Варианты ответов')



line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()


line2.addWidget(rbtn1)
line2.addWidget(rbtn2)
line3.addWidget(rbtn3)
line3.addWidget(rbtn4)
line1.addLayout(line2)
line1.addLayout(line3)

RadioGroupBox.setLayout(line1)
AnswerGroupBox = QGroupBox('Результат теста')
LBResult = QLabel('прав ты или нет?')
LBCorrect = QLabel('ответ будет тут!')

answer_line_1 = QVBoxLayout()

AnswerGroupBox.setLayout(answer_line_1)


answer_line_1.addWidget(LBResult)
answer_line_1.addWidget(LBCorrect)

line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()

line4.addWidget(lb_Question)
line5.addWidget(RadioGroupBox)
line5.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()

line4.addWidget(lb_Question)
line5.addWidget(RadioGroupBox)
line6.addWidget(btn_OK)
line7 = QVBoxLayout() 
line7.addLayout(line4)
line7.addLayout(line5)
line7.addLayout(line6)

main_win.setLayout(line7)

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    btn_OK.setText('Следующий вопрос')


answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    
    lb_Question.setText(q.question)
    LBCorrect.setText(q.right_answer)
    show_question()

def show_correct(res):
    LBResult.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика \n-Вопросов', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%') 
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%') 



main_win.cur_question = -1
def next_question():
    main_win.total += 1
    print('')
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    main_win.cur_question + 1
    
    ask(q)

def click_on():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


btn_OK.clicked.connect(click_on)
main_win.score = 0
main_win.total = 0
next_question()


main_win.resize(352, 352)
main_win.show()
app.exec_()
