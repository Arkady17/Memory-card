from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton,QRadioButton, QGroupBox,QGroupBox, QButtonGroup
from random import*

class Question():
    def __init__(
        self,question,right_answer,
        wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии','Португальский','Английский','Испаниский','Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
questions_list.append(Question('Национальяная хижина якутов','Ураса','Юрта','Иглу','Хата'))
questions_list.append(Question('Какой первый без алкогольный напиток был взят в космос?','кока-кола','фанта','пепси','миринда'))
questions_list.append(Question('Какое национальное животное в Австралии','кенгуру','коала','крокодил','каёт'))
questions_list.append(Question('Какой национальный цветок в Япониии','Сакура','Космея','Гортензия','Ликорис'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
question = QLabel ("Какой национальности не существует?")
btn_OK = QPushButton("Ответить")
RadioGroupBox = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton ("Энцы")
btn_answer2 = QRadioButton ("Чулымцы")
btn_answer3 = QRadioButton ("Смурфы")
btn_answer4 = QRadioButton ("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

laoyt_ans1 =QHBoxLayout()
laoyt_ans2 = QVBoxLayout()
laoyt_ans3 = QVBoxLayout() 
laoyt_ans2.addWidget(btn_answer1)
laoyt_ans2.addWidget(btn_answer2)
laoyt_ans3.addWidget(btn_answer3)
laoyt_ans3.addWidget(btn_answer4)
laoyt_ans1.addLayout(laoyt_ans2)
laoyt_ans1.addLayout(laoyt_ans3)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("прав ты или нет?")
lb_Correct = QLabel("ответ будет тут!")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter , stretch=2)
AnsGroupBox.setLayout(layout_res)

RadioGroupBox.setLayout(laoyt_ans1)
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат тес
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(4)
layout_line3.addWidget(btn_OK,stretch= 2)
layout_line2.addWidget(AnsGroupBox)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

main_win.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)#сняли ограничения
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True) #вернули ограничения

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def next_question():
    main_win.total +=1
    print('Статистика\n-Всего вопросов:',main_win.total,'\n-Правильных ответов:',main_win.score)
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:',main_win.total,'\n-Правильных ответов:',main_win.score)
        print('Рейтинг:',(main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:',(main_win.score/main_win.total*100), '%')

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.total = 0

main_win.score = 0

next_question()

btn_OK.clicked.connect(click_OK) 

next_question()

main_win.show()
app.exec()