from turtle import *
class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        setup(width=600, height=600)
        setworldcoordinates(-(columnsInMaze - 1) / 2 - 0.5,   #自定义坐标系
                            -(rowsInMaze - 1) / 2 - 0.5,
                            (columnsInMaze - 1) / 2 + 0.5,
                            (rowsInMaze - 1) / 2 + 0.5)


    def drawMaze(self):
        self.t.speed(10)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate, -y+self.yTranslate,'tan')
            self.t.color('black', 'blue')

    def drawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate, -y+self.yTranslate))
        self.t.goto(x+self.xTranslate, -y+self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(color)#此函数用于绘制具有特定大小和某种颜色的圆点

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val
            self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1)

    def __getitem__(self, idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    # 2.遇到已经走过的格子
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3.找到出口
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # 否则，依次尝试向4个方向移动
    found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


PART_OF_PATH = 'O'            #部分路径
TRIED = '.'                    #尝试
OBSTACLE = '+'                #障碍
DEAD_END = '-'                #死胡同
myMaze = Maze('mazeExample.txt')#实例化迷宫类，maze文件是使用“+”字符作为墙壁围出空心正方形空间，并用字母“S”来表示起始位置的迷宫文本文件。
myMaze.drawMaze()            #在屏幕上绘制迷宫。
searchFrom(myMaze, myMaze.startRow, myMaze.startCol)    #探索迷宫






        

