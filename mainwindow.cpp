#include <iostream>
#include <QtConcurrent>
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    gen_case_config();
    add_graphics_view();
    setWindowTitle("ATE");
//    this->load_style_sheet("myStyle.qss");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::load_style_sheet(const QString &sheetname) {
    QFile file(sheetname);
    file.open(QFile::ReadOnly);
    if (file.isOpen()) {
        QString styleSheet = this->styleSheet();
        styleSheet += QLatin1String(file.readAll());
        this->setStyleSheet(styleSheet);
    }
}
void MainWindow::gen_case_config(void) {
    int i;
    QVBoxLayout *vbox = new QVBoxLayout;
    for (i = 0; i < cases.size(); i++) {
//        QCheckBox *cb = new QCheckBox(cases[i], this);
//        ui->gridLayout_2->addWidget(cb, 0, i);
//        cb->show();
//        check_boxes.append(cb);

        QPushButton *pb = new QPushButton(cases[i], this);
        pb->setFixedSize(85, 40);
        pb->setStyleSheet("color: white; background-color: #27a9e3; border-width: 0px; border-radius: 3px;");
//        QMenu *s_menu = new QMenu(this);
//        s_menu->addAction("测试项配置", this, &MainWindow::gen_subwidget_clicked);
//        pb->setMenu(s_menu);
        vbox->addWidget(pb);
        pb_cases.append(pb);
//        menu_cases.append(s_menu);
    }
    ui->groupBox->setLayout(vbox);
}
void MainWindow::add_graphics_view(void) {
    scene1.setBackgroundBrush(Qt::blue);
    scene1.addText("Hellow Graphics!");
    view1.setScene(&scene1);
    ui->graphics_grid->addWidget(&view1, 0, 0);

    scene2.setBackgroundBrush(Qt::red);
    const QRect rect(50, 50, 100, 100);
    const QRectF rectf(rect);
    scene2.addRect(rectf);
    view2.setScene(&scene2);
    ui->graphics_grid->addWidget(&view2, 0, 1);

    scene3.setBackgroundBrush(Qt::yellow);
    const QLineF linef(50, 50, 70, 70);
    scene3.addLine(linef);
    view3.setScene(&scene3);
    ui->graphics_grid->addWidget(&view3, 1, 0);

    scene4.setBackgroundBrush(Qt::green);
    const QRectF ellipse(50, 50, 100, 100);
    scene4.addEllipse(ellipse);
    view4.setScene(&scene4);
    ui->graphics_grid->addWidget(&view4, 1, 1);
}
void MainWindow::on_pb_sel_all_clicked()
{
    int i;
    for (i = 0; i < cases.size(); i++) {
        check_boxes[i]->setCheckState(Qt::Checked);
    }
}

void MainWindow::on_pb_reset_clicked()
{
    int i;
    for (i = 0; i < cases.size(); i++) {
        check_boxes[i]->setCheckState(Qt::Unchecked);
    }
}

void MainWindow::on_pb_apply_clicked()
{
    int i;
    for (i = 0; i < cases.size(); i++) {
        if (check_boxes[i]->checkState() == Qt::Checked) {
            pb_cases[i]->setStyleSheet("color: white; background-color: #27a9e3; \
               border-width: 0px; border-radius: 3px;");
            pb_cases[i]->setEnabled(true);
        } else {
            pb_cases[i]->setStyleSheet("background-color: #cfcfcf; border-width: 0px; border-radius: 3px;");
            pb_cases[i]->setEnabled(false);
        }
    }
}
void MainWindow::run(void)
{
    int i;
    for (i = 0; i < cases.size(); i++) {
        if (pb_cases[i]->isEnabled()) {
            QString msg = "Test item " + QString::number(i);
            printMessage(msg);
        }
    }
}
void MainWindow::printMessage(QString message) {
    ui->textBrowser->append(message);
}
void MainWindow::gen_subwidget_clicked() {
    subwidget *sub = new subwidget;
    sub->setFocus(Qt::ActiveWindowFocusReason);
    sub->show();
}

void MainWindow::on_pb_start_clicked()
{
    QFuture<void> future = QtConcurrent::run(&MainWindow::run, this);
}

void MainWindow::on_toolButton_clicked()
{
    intpath = QFileDialog::getOpenFileName(this, "指令文件", "./", "Txt files(*.txt)");
    if (intpath == "")
        return;
    else
        printMessage("Instruction file: " + intpath);
}

void MainWindow::on_toolButton_2_clicked()
{
    wavpath = QFileDialog::getOpenFileName(this, "波形文件", "./", "Wav files(*.wv)");
    if (wavpath == "")
        return;
    else
        printMessage("Test wave file: " + wavpath);
}
