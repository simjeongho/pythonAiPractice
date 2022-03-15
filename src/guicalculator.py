
from tkinter import *
def add(x,y):
    result = x+y
    return result;
def input_value(val):
    entry_value.insert("end", val);
def clear_all(val):
    entry_value.delete(0, "end");
def get_result():
    # arr = entry_value.get().split("+")
    # #print arr
    # return_value = add(int(arr[0]), int(arr[1]))
    # entry_value.delete(0, "end")
    return_value = eval(entry_value.get()) #eval 함수 중요 
    entry_value.delete(0, "end")
    entry_value.insert(0, return_value)

#main
main = Tk()
main.title("Simple Calculator")
main.geometry() # geometry window 에서는 위치가 필요하다. 
entry_value = Entry(main, width=40, justify = RIGHT) #Entry란 input text box
entry_value.grid(row=0, column=0, columnspan=4)
entry_value.focus_set() #Sets focus on the input text area

#Generating Button
Button(main, text = "=", width = 30, command = lambda:get_result()).grid(row=5, column= 0, columnspan = 3)#lambda 는 무기명의 함수 command에서 함수를 부를 수는 있지만 매개변수를 집어넣을 수는 없다. 
Button(main, text="AC", width=10, command = lambda:clear_all()).grid(row=4, column=0) # 따라서 lambda를 사용한다. 
Button(main, text="+", width=10, command= lambda:input_value('+')).grid(row=4, column=2)
Button(main, text="7", width=10, command=lambda:input_value(7)).grid(row=1, column=0)
Button(main, text="8", width=10, command=lambda:input_value(8)).grid(row=1, column=1)
Button(main, text="9", width=10, command=lambda:input_value(9)).grid(row=1, column=2)
Button(main, text="4", width=10, command=lambda:input_value(4)).grid(row=2, column=0)
Button(main, text="5", width=10, command=lambda:input_value(5)).grid(row=2, column=1)
Button(main, text="6", width=10, command=lambda:input_value(6)).grid(row=2, column=2)
Button(main, text="3", width=10, command=lambda:input_value(3)).grid(row=3, column=0)
Button(main, text="2", width=10, command=lambda:input_value(2)).grid(row=3, column=1)
Button(main, text="1", width=10, command=lambda:input_value(1)).grid(row=3, column=2)
main.mainloop()
