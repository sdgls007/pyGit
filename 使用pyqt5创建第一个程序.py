import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #创建QApplications类的实例
    app = QApplication(sys.argv)#获取命令行参数，注：GUI程序本质也是命令行程序，只是他访问了与GUI相关的API，通过对窗口API的调用，使用户看到期望的界面
    #创建一个窗口
    w = QWidget()

    w.resize(300,300)#窗口的初始大小
    
    w.move(300,300)#窗口的位置

    w.setWindowTitle('这是一个标题')

    w.show()

    #进入程序的主循环，这是运行GUI程序的机制，主循环用来循环扫描响应在窗口上的事件，并且让整个app不会退出，通过exit确保主循环安全的结束

    sys.exit(app.exec_())