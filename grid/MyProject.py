from guizero import App, Box, Text, Picture

app = App(title="tạp chí", bg="lightblue", width=900, height=750)
text = Text(app,"Cuốn tạp chí", size=30, align="bottom")
box = Box(app, width=650, height=900, layout="grid")
pic1 = Picture(box,image="tapchi1.png",width=300, height=350, grid=[0,0,1,2])
pic2 = Picture(box,image="tapchi2.jpg",width=300, height=350, grid=[1,0])
pic3 = Picture(box,image="tapchi3.png",width=300, height=350, grid=[1,1])

app.display()