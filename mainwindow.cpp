#include <iostream>
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->gen_case_config();
    this->setWindowTitle("ATE");
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
    for (i = 0; i < this->cases.size(); i++) {
        QCheckBox *cb = new QCheckBox(this->cases[i], this);
        ui->gridLayout_2->addWidget(cb, 0, i);
        cb->show();
        this->check_boxes.append(cb);

        QPushButton *pb = new QPushButton(this->cases[i], this);
        pb->setFixedSize(85, 50);
        QMenu *s_menu = new QMenu(this);
        s_menu->addAction("配置", this, &MainWindow::gen_subwidget_clicked);
        s_menu->addAction("测试");
        pb->setMenu(s_menu);
        vbox->addWidget(pb);
        this->pb_cases.append(pb);
        this->menu_cases.append(s_menu);
    }
    ui->groupBox->setLayout(vbox);
}

void MainWindow::on_pb_sel_all_clicked()
{
    int i;
    for (i = 0; i < this->cases.size(); i++) {
        this->check_boxes[i]->setCheckState(Qt::Checked);
    }
}

void MainWindow::on_pb_reset_clicked()
{
    int i;
    for (i = 0; i < this->cases.size(); i++) {
        this->check_boxes[i]->setCheckState(Qt::Unchecked);
    }
}

void MainWindow::on_pb_apply_clicked()
{
    int i;
    for (i = 0; i < this->cases.size(); i++) {
        if (this->check_boxes[i]->checkState() == Qt::Checked) {
            this->pb_cases[i]->setEnabled(true);
        } else {
            this->pb_cases[i]->setEnabled(false);
        }
    }
}
void MainWindow::gen_subwidget_clicked() {
    subwidget *sub = new subwidget;
    sub->setFocus(Qt::ActiveWindowFocusReason);
    sub->show();
}
