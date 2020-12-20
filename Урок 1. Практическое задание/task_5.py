"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class Stack:
    def __init__(self, max):
        self.el = [[]]
        self.max = max

    def __str__(self):
        return str(self.el)

    def is_empty(self):
        return self.el == [[]]

    def push_in(self, el):
        if len(self.el[len(self.el) - 1]) < self.max:
            self.el[len(self.el) - 1].append(el)
        else:
            self.el.append([])
            self.el[len(self.el) - 1].append(el)

    def pop_out(self):
        result = self.el[len(self.el) - 1].pop()
        if len(self.el[len(self.el) - 1]) == 0:
            self.el.pop()
        return result

    def get_val(self):
        return self.el[len(self.el) - 1][len(self.el[len(self.el) - 1]) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.el:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.el)


if __name__ == '__main__':
    st = Stack(5)
    st.push_in('st1')
    st.push_in('st')
    st.push_in('st3')
    st.push_in('st4')
    st.push_in('st5')
    print(st)
    print(st.pop_out())
    print(st.get_val())
    print(st.stack_size())
    print(st.stack_count())
    print(st)