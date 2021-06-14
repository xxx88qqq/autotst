#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDebug>
#include <QFile>
#include <QCheckBox>
#include <QPushButton>
#include <QMenu>
#include "subwidget.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    void load_style_sheet(const QString &sheetname);
    void gen_case_config(void);
    ~MainWindow();

private slots:
    void gen_subwidget_clicked();

    void on_pb_sel_all_clicked();

    void on_pb_reset_clicked();

    void on_pb_apply_clicked();

private:
    Ui::MainWindow *ui;
    subwidget subwgt;
    QList<QString> cases {"发射功率", "RE动态范围", "总功率动态", "发射关断", "开关时间", "频率误差", "EVM", "定时误差", "带宽", \
                         "ACLR", "无用发射", "杂散", "发射互调"};
    QList<QCheckBox *> check_boxes;
    QList<QPushButton *> pb_cases;
    QList<QMenu *> menu_cases;
};
#endif // MAINWINDOW_H
